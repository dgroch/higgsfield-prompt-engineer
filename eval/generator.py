"""Prompt generator: Claude + skill → Higgsfield Seedance prompt."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import anthropic

MODEL = "claude-opus-4-7"
SHARED_DIR = Path(__file__).resolve().parent.parent / "shared"


@dataclass
class IterationResult:
    iteration: int
    prompt: str
    score: float | None = None
    critique: str | None = None
    breakdown: dict | None = None
    video_path: str | None = None


def _system_prompt(skill_path: Path) -> list[dict]:
    """Compose the generator's system prompt: skill + shared craft library.

    Loaded as cached blocks so repeat calls in the same loop pay write cost
    once and read cost on every subsequent iteration.
    """
    skill_text = skill_path.read_text(encoding="utf-8")

    shared_files = [
        "camera-movements.md",
        "lighting-library.md",
        "color-grading.md",
        "sound-design.md",
        "hook-framework.md",
        "timeline-structures.md",
        "prompt-template.md",
    ]
    shared_blob = "\n\n".join(
        f"# shared/{name}\n\n{(SHARED_DIR / name).read_text(encoding='utf-8')}"
        for name in shared_files
    )

    instructions = (
        "You are a prompt engineer for Higgsfield Seedance 2.0. The user "
        "will give you a brief. You will produce a single, paste-ready "
        "prompt block — nothing else.\n\n"
        "Rules:\n"
        "1. Follow the skill above. Use its hook patterns, structure, "
        "vocabulary.\n"
        "2. Reference the shared craft library for camera moves, lighting, "
        "grading, sound, hooks, timeline.\n"
        "3. Specify timing precisely (every camera move, audio cue, action).\n"
        "4. Reference uploaded materials with @image1 / @video1 / @audio1 "
        "syntax when the brief mentions them.\n"
        "5. End with [OUTPUT] block: duration, aspect ratio, resolution.\n"
        "6. If a previous iteration's critique is provided, address each "
        "specific issue. Do not regress fixed problems.\n\n"
        "Output only the prompt block. No preamble, no postscript, no "
        "markdown code fences."
    )

    return [
        {
            "type": "text",
            "text": f"# Skill\n\n{skill_text}",
            "cache_control": {"type": "ephemeral"},
        },
        {
            "type": "text",
            "text": f"# Shared craft library\n\n{shared_blob}",
            "cache_control": {"type": "ephemeral"},
        },
        {
            "type": "text",
            "text": instructions,
        },
    ]


def _user_message(brief: str, history: Sequence[IterationResult]) -> str:
    parts = [f"BRIEF:\n{brief}"]
    if history:
        parts.append("\nPREVIOUS ITERATIONS:")
        for h in history:
            parts.append(
                f"\n--- Iteration {h.iteration} ---\n"
                f"PROMPT:\n{h.prompt}\n\n"
                f"SCORE: {h.score:.2f}\n"
                f"CRITIQUE:\n{h.critique}"
            )
        parts.append(
            "\nProduce a new prompt that addresses every critique above. "
            "Do not regress strengths from prior iterations."
        )
    return "\n".join(parts)


def generate(
    skill_path: Path | str,
    brief: str,
    history: Sequence[IterationResult] = (),
    *,
    client: anthropic.Anthropic | None = None,
) -> str:
    """Produce a Higgsfield Seedance prompt for the given brief."""
    client = client or anthropic.Anthropic()
    skill_path = Path(skill_path)

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        system=_system_prompt(skill_path),
        messages=[{"role": "user", "content": _user_message(brief, history)}],
    )

    text = next(
        (b.text for b in response.content if b.type == "text"), ""
    ).strip()

    if not text:
        raise RuntimeError(
            "Generator returned no text content. "
            f"stop_reason={response.stop_reason!r}"
        )

    if os.environ.get("EVAL_DEBUG"):
        print(
            f"[generator] usage: input={response.usage.input_tokens} "
            f"output={response.usage.output_tokens} "
            f"cache_read={response.usage.cache_read_input_tokens}"
        )

    return text
