"""CLI entrypoint for the eval harness.

Usage:
    python -m eval.cli run \\
        --skill skills/01-cinematic/SKILL.md \\
        --brief "samurai walks through bamboo at dawn, 8s" \\
        --rubric eval/rubrics/cinematic.yaml \\
        --max-iterations 3 \\
        --threshold 0.8 \\
        --output runs/run_001

    python -m eval.cli check-mcp
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from pathlib import Path

from . import harness, mcp_client


def _add_run_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--skill", required=True, help="Path to a SKILL.md file")
    p.add_argument("--brief", required=True, help="What the user wants the video to be")
    p.add_argument(
        "--rubric",
        default="eval/rubrics/default.yaml",
        help="Path to rubric YAML",
    )
    p.add_argument(
        "--output",
        default=None,
        help="Output directory (default: runs/run_<timestamp>)",
    )
    p.add_argument(
        "--max-iterations",
        type=int,
        default=int(os.environ.get("EVAL_MAX_ITERATIONS", "3")),
    )
    p.add_argument(
        "--threshold",
        type=float,
        default=float(os.environ.get("EVAL_THRESHOLD", "0.8")),
    )
    p.add_argument("--duration", type=int, default=8, help="Seconds, 4–15")
    p.add_argument("--aspect-ratio", default="16:9", choices=("16:9", "9:16", "1:1"))
    p.add_argument("--frames", type=int, default=4, help="Keyframes to extract for the judge")
    p.add_argument("--debug", action="store_true")


def cmd_run(args: argparse.Namespace) -> int:
    if args.debug:
        os.environ["EVAL_DEBUG"] = "1"
        logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    else:
        logging.basicConfig(level=logging.WARNING)

    output = args.output
    if output is None:
        output = Path(os.environ.get("EVAL_OUTPUT_DIR", "runs")) / f"run_{int(time.time())}"

    result = harness.run(
        skill_path=args.skill,
        brief=args.brief,
        rubric_path=args.rubric,
        output_dir=output,
        max_iterations=args.max_iterations,
        threshold=args.threshold,
        duration_seconds=args.duration,
        aspect_ratio=args.aspect_ratio,
        n_frames=args.frames,
    )

    print(f"\nRun complete: {output}")
    print(f"  success:    {result.success}")
    print(f"  threshold:  {result.threshold}")
    print(f"  best iter:  #{result.best_iteration}")
    print(f"  iterations: {len(result.iterations)}")
    for it in result.iterations:
        score = f"{it.score:.3f}" if it.score is not None else "—"
        err = f" (error)" if it.error else ""
        print(f"    #{it.iteration}: {score}{err}")

    return 0 if result.success else 2


def cmd_check_mcp(args: argparse.Namespace) -> int:
    logging.basicConfig(level=logging.INFO)
    try:
        tools = mcp_client.list_tools()
    except Exception as exc:
        print(f"FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    if not tools:
        print("Connected, but the MCP server reported zero tools.")
        return 1

    print(f"Connected. {len(tools)} tools available:\n")
    for t in tools:
        desc = t.get("description", "")
        if len(desc) > 120:
            desc = desc[:117] + "..."
        print(f"  - {t['name']}: {desc}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="eval")
    sub = parser.add_subparsers(dest="cmd", required=True)

    run_p = sub.add_parser("run", help="Run an eval loop")
    _add_run_args(run_p)
    run_p.set_defaults(func=cmd_run)

    check_p = sub.add_parser("check-mcp", help="Verify MCP server connectivity")
    check_p.set_defaults(func=cmd_check_mcp)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
