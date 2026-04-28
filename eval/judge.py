"""Claude as judge — score (prompt, frames) against a rubric."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

import anthropic
import yaml

from . import frames as frames_mod

MODEL = "claude-opus-4-7"


@dataclass
class JudgeResult:
    score: float  # 0.0–1.0 (weighted average of criterion scores normalized)
    breakdown: dict  # {criterion_id: {"score": int, "reason": str}}
    critique: str  # actionable feedback for the next iteration
    raw: dict


def load_rubric(path: Path | str) -> dict:
    """Load a YAML rubric file."""
    with Path(path).open("r", encoding="utf-8") as f:
        rubric = yaml.safe_load(f)
    _validate_rubric(rubric)
    return rubric


def _validate_rubric(rubric: dict) -> None:
    if "criteria" not in rubric:
        raise ValueError("Rubric must have a 'criteria' list.")
    weights = sum(c.get("weight", 0) for c in rubric["criteria"])
    if abs(weights - 1.0) > 0.01:
        raise ValueError(
            f"Rubric weights must sum to 1.0; got {weights:.3f}."
        )
    for c in rubric["criteria"]:
        for field in ("id", "weight", "description"):
            if field not in c:
                raise ValueError(f"Rubric criterion missing '{field}': {c}")


def _build_schema(rubric: dict) -> dict:
    """JSON schema enforcing structured output for the judge."""
    criterion_props = {
        c["id"]: {
            "type": "object",
            "properties": {
                "score": {"type": "integer", "minimum": 1, "maximum": 5},
                "reason": {"type": "string"},
            },
            "required": ["score", "reason"],
            "additionalProperties": False,
        }
        for c in rubric["criteria"]
    }
    return {
        "type": "object",
        "properties": {
            "scores": {
                "type": "object",
                "properties": criterion_props,
                "required": list(criterion_props.keys()),
                "additionalProperties": False,
            },
            "critique": {
                "type": "string",
                "description": (
                    "Actionable feedback the prompt engineer can use to "
                    "improve the next iteration. Bullet list. Each bullet "
                    "names a specific change."
                ),
            },
        },
        "required": ["scores", "critique"],
        "additionalProperties": False,
    }


def _system_prompt(rubric: dict) -> str:
    criteria_block = "\n\n".join(
        f"## {c['id']} (weight {c['weight']})\n{c['description']}"
        for c in rubric["criteria"]
    )
    return (
        f"You are a strict but fair video-prompt evaluator. You score "
        f"prompts and rendered output against the rubric below.\n\n"
        f"# Rubric: {rubric.get('name', 'unnamed')}\n\n"
        f"{criteria_block}\n\n"
        "# Scoring rules\n"
        "- Each criterion: integer 1–5. 1=fails, 3=acceptable, 5=excellent.\n"
        "- Score the rendered frames, not just the prompt text.\n"
        "- Your `reason` field cites specific evidence (frame N shows X; "
        "prompt line Y).\n"
        "- The `critique` is the most useful section. It should be a short "
        "list of concrete edits the next iteration should make. Avoid "
        "vague praise. Avoid generic suggestions like 'add more detail'.\n"
        "- If the rendered frames don't match the prompt, that's a "
        "visual_coherence problem — call it out explicitly.\n\n"
        "Return only the JSON object matching the schema."
    )


def evaluate(
    prompt: str,
    frame_paths: list[Path],
    rubric: dict,
    *,
    brief: str | None = None,
    client: anthropic.Anthropic | None = None,
) -> JudgeResult:
    """Score a prompt + its rendered frames against the rubric."""
    client = client or anthropic.Anthropic()

    user_content: list[dict] = []
    if brief:
        user_content.append(
            {"type": "text", "text": f"USER BRIEF:\n{brief}"}
        )
    user_content.append({"type": "text", "text": f"PROMPT:\n{prompt}"})
    user_content.append(
        {"type": "text", "text": f"RENDERED FRAMES ({len(frame_paths)}):"}
    )
    for i, path in enumerate(frame_paths, 1):
        user_content.append({"type": "text", "text": f"Frame {i}:"})
        user_content.append(frames_mod.frame_to_image_block(path))
    user_content.append(
        {
            "type": "text",
            "text": (
                "Score this against the rubric. Return JSON matching the "
                "schema."
            ),
        }
    )

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        thinking={"type": "adaptive"},
        output_config={
            "effort": "high",
            "format": {"type": "json_schema", "schema": _build_schema(rubric)},
        },
        system=_system_prompt(rubric),
        messages=[{"role": "user", "content": user_content}],
    )

    text = next((b.text for b in response.content if b.type == "text"), None)
    if not text:
        raise RuntimeError(
            f"Judge returned no text. stop_reason={response.stop_reason!r}"
        )

    raw = json.loads(text)

    weighted = 0.0
    breakdown: dict = {}
    for c in rubric["criteria"]:
        s = raw["scores"][c["id"]]
        breakdown[c["id"]] = s
        # Normalise 1–5 to 0–1: (score - 1) / 4
        weighted += c["weight"] * ((s["score"] - 1) / 4)

    if os.environ.get("EVAL_DEBUG"):
        print(
            f"[judge] usage: input={response.usage.input_tokens} "
            f"output={response.usage.output_tokens} "
            f"score={weighted:.3f}"
        )

    return JudgeResult(
        score=weighted,
        breakdown=breakdown,
        critique=raw["critique"],
        raw=raw,
    )
