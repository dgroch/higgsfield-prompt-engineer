"""The eval loop: generate → render → judge → critique → repeat."""

from __future__ import annotations

import json
import logging
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

import anthropic

from . import frames as frames_mod
from . import generator, judge, mcp_client

logger = logging.getLogger(__name__)


@dataclass
class IterationRecord:
    iteration: int
    prompt: str
    video_url: str | None = None
    video_path: str | None = None
    frame_paths: list[str] = field(default_factory=list)
    score: float | None = None
    critique: str | None = None
    breakdown: dict | None = None
    error: str | None = None
    elapsed_seconds: float | None = None


@dataclass
class RunResult:
    success: bool
    best_iteration: int
    iterations: list[IterationRecord]
    skill: str
    brief: str
    rubric_name: str
    threshold: float
    output_dir: str


def run(
    *,
    skill_path: Path | str,
    brief: str,
    rubric_path: Path | str,
    output_dir: Path | str,
    max_iterations: int = 3,
    threshold: float = 0.8,
    duration_seconds: int = 8,
    aspect_ratio: str = "16:9",
    n_frames: int = 4,
    client: anthropic.Anthropic | None = None,
) -> RunResult:
    """Run the eval loop. Returns when threshold is met or iterations exhausted."""
    client = client or anthropic.Anthropic()
    skill_path = Path(skill_path)
    rubric_path = Path(rubric_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    rubric = judge.load_rubric(rubric_path)
    iterations: list[IterationRecord] = []

    history_for_generator: list[generator.IterationResult] = []

    for i in range(1, max_iterations + 1):
        iter_dir = output_dir / f"iteration_{i:02d}"
        iter_dir.mkdir(exist_ok=True)
        record = IterationRecord(iteration=i, prompt="")
        started = time.monotonic()

        try:
            logger.info("Iteration %d: generating prompt", i)
            prompt = generator.generate(
                skill_path, brief, history_for_generator, client=client
            )
            record.prompt = prompt
            (iter_dir / "prompt.txt").write_text(prompt, encoding="utf-8")

            logger.info("Iteration %d: rendering via MCP", i)
            render_result = mcp_client.render(
                prompt,
                duration_seconds=duration_seconds,
                aspect_ratio=aspect_ratio,
                client=client,
            )
            record.video_url = render_result.video_url

            logger.info("Iteration %d: downloading + extracting frames", i)
            video_path = frames_mod.download_video(
                render_result.video_url, iter_dir
            )
            record.video_path = str(video_path)
            frame_paths = frames_mod.extract_keyframes(
                video_path, iter_dir / "frames", n=n_frames
            )
            record.frame_paths = [str(p) for p in frame_paths]

            logger.info("Iteration %d: judging", i)
            jr = judge.evaluate(
                prompt,
                frame_paths,
                rubric,
                brief=brief,
                client=client,
            )
            record.score = jr.score
            record.critique = jr.critique
            record.breakdown = jr.breakdown
            (iter_dir / "score.json").write_text(
                json.dumps(
                    {"score": jr.score, "breakdown": jr.breakdown},
                    indent=2,
                ),
                encoding="utf-8",
            )
            (iter_dir / "critique.md").write_text(jr.critique, encoding="utf-8")

            history_for_generator.append(
                generator.IterationResult(
                    iteration=i,
                    prompt=prompt,
                    score=jr.score,
                    critique=jr.critique,
                    breakdown=jr.breakdown,
                    video_path=str(video_path),
                )
            )

        except Exception as exc:
            record.error = f"{type(exc).__name__}: {exc}"
            logger.exception("Iteration %d failed", i)

        record.elapsed_seconds = time.monotonic() - started
        iterations.append(record)
        _write_iteration(iter_dir, record)

        if record.score is not None and record.score >= threshold:
            logger.info(
                "Iteration %d met threshold (%.2f >= %.2f). Stopping.",
                i,
                record.score,
                threshold,
            )
            break

    best = _pick_best(iterations)
    success = (
        best.score is not None
        and best.score >= threshold
        and best.error is None
    )

    result = RunResult(
        success=success,
        best_iteration=best.iteration,
        iterations=iterations,
        skill=str(skill_path),
        brief=brief,
        rubric_name=rubric.get("name", "unnamed"),
        threshold=threshold,
        output_dir=str(output_dir),
    )
    _write_summary(output_dir, result)
    return result


def _pick_best(iterations: list[IterationRecord]) -> IterationRecord:
    scored = [it for it in iterations if it.score is not None]
    if not scored:
        return iterations[-1]
    return max(scored, key=lambda it: it.score)


def _write_iteration(iter_dir: Path, record: IterationRecord) -> None:
    (iter_dir / "iteration.json").write_text(
        json.dumps(asdict(record), indent=2),
        encoding="utf-8",
    )


def _write_summary(output_dir: Path, result: RunResult) -> None:
    (output_dir / "summary.json").write_text(
        json.dumps(asdict(result), indent=2),
        encoding="utf-8",
    )
    lines = [
        "# Eval run summary",
        "",
        f"- skill: `{result.skill}`",
        f"- brief: {result.brief}",
        f"- rubric: {result.rubric_name}",
        f"- threshold: {result.threshold}",
        f"- success: **{result.success}**",
        f"- best iteration: {result.best_iteration}",
        "",
        "## Iterations",
        "",
    ]
    for it in result.iterations:
        score = f"{it.score:.3f}" if it.score is not None else "—"
        err = f" (error: {it.error})" if it.error else ""
        lines.append(
            f"- **#{it.iteration}** — score {score}, "
            f"{it.elapsed_seconds:.1f}s{err}"
        )
    (output_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")
