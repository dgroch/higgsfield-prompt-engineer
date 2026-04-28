# Eval Harness

Iteratively refines Higgsfield Seedance 2.0 prompts. Generates a prompt
from a skill, renders via the Higgsfield MCP, scores the result against a
rubric, and loops with critique until the threshold is hit or iterations
are exhausted.

## What it does

```
        ┌───────────────────────────────────────────────────────┐
        │ for i in 1..max_iterations:                           │
        │                                                       │
        │   1. generator.generate(skill, brief, history)        │
        │      └─ Claude (Opus 4.7) + skill + shared library    │
        │         + previous critiques  →  prompt               │
        │                                                       │
        │   2. mcp_client.render(prompt)                        │
        │      └─ Anthropic MCP connector → Higgsfield MCP      │
        │         submits prompt, polls until rendered          │
        │         → video_url                                   │
        │                                                       │
        │   3. frames.extract(video, n=4)                       │
        │      └─ ffmpeg → 4 keyframes                          │
        │                                                       │
        │   4. judge.evaluate(prompt, frames, rubric)           │
        │      └─ Claude (Opus 4.7) + rubric + frames           │
        │         → score (0–1) + per-criterion breakdown       │
        │           + critique                                  │
        │                                                       │
        │   if score >= threshold: stop                         │
        │   else: feed critique into next iteration             │
        └───────────────────────────────────────────────────────┘
```

## Setup

```bash
pip install -r requirements.txt
brew install ffmpeg  # or apt-get install ffmpeg

cp .env.example .env
# fill in ANTHROPIC_API_KEY, HIGGSFIELD_MCP_URL, HIGGSFIELD_OAUTH_TOKEN
source .env
```

See [`mcp/README.md`](../mcp/README.md) for Higgsfield MCP options.

Verify the MCP connection before running an eval:

```bash
python -m eval.cli check-mcp
```

This sends a list-tools request through the connector and prints the
exposed tool surface. If it errors, fix the MCP wiring before continuing.

## Run an eval

```bash
python -m eval.cli run \
  --skill skills/01-cinematic/SKILL.md \
  --brief "lone samurai walking through bamboo grove at dawn, mist, 8 seconds" \
  --rubric eval/rubrics/cinematic.yaml \
  --max-iterations 3 \
  --threshold 0.85 \
  --output runs/samurai_v1
```

Each iteration writes to `runs/samurai_v1/iteration_NN/`:

```
runs/samurai_v1/
├── summary.json          # full machine-readable result
├── summary.md            # human-readable summary
├── iteration_01/
│   ├── prompt.txt        # generated prompt
│   ├── video.mp4         # rendered output
│   ├── frames/           # 4 extracted JPGs
│   ├── score.json        # weighted score + per-criterion breakdown
│   ├── critique.md       # actionable feedback for the next iteration
│   └── iteration.json    # full record (timing, video URL, etc.)
├── iteration_02/
└── iteration_03/
```

The harness exits 0 on success (threshold met), 2 if all iterations ran
but no iteration met the threshold.

## Rubrics

A rubric is a YAML file with weighted criteria. Each criterion is scored
1–5 by the judge; the composite is the weighted mean of `(score - 1) / 4`.

```yaml
name: my-rubric
threshold: 0.8                      # composite to beat (default: 0.8)

criteria:
  - id: hook_strength               # used as the JSON schema key
    weight: 0.25                    # weights must sum to 1.0
    description: |
      What the judge is looking for.

      1 = ... 3 = ... 5 = ...        # anchor the scale explicitly
```

Three rubrics ship by default:

- `default.yaml` — applies to any vertical
- `cinematic.yaml` — for skill 01; heavier weight on visual coherence and
  motivated lighting
- `social-hook.yaml` — for skill 11; 40% of the score is the hook itself

Add more in `eval/rubrics/` for the other 13 skills as you validate them.

## What you can configure

| Flag                  | Default      | Notes                                 |
| --------------------- | ------------ | ------------------------------------- |
| `--skill`             | required     | Path to a `SKILL.md`                  |
| `--brief`             | required     | What the user wants                   |
| `--rubric`            | `default.yaml` | Path to rubric YAML                  |
| `--max-iterations`    | 3            | Loop cap                              |
| `--threshold`         | 0.8          | Composite score to beat (0.0–1.0)     |
| `--duration`          | 8            | Output video length, 4–15s            |
| `--aspect-ratio`      | 16:9         | 16:9 / 9:16 / 1:1                     |
| `--frames`            | 4            | Keyframes extracted for the judge     |
| `--output`            | `runs/run_<ts>` | Output directory                   |
| `--debug`             | off          | Verbose logging + token usage prints  |

## Cost shape

Per iteration:
- 1 generator call: Opus 4.7, adaptive thinking, ~5–15K input + ~1K output
- 1 MCP orchestrator call: Opus 4.7, MCP connector (Higgsfield) + polling
- 1 judge call: Opus 4.7, adaptive thinking, ~5K input + 4 images + ~1K output

The skill + shared library are cached on the system prompt; the second and
third iteration in a single run pay cache-read prices on those blocks.

`--debug` prints `usage` for each call so you can tally costs.

## Extending

- **More rubrics.** Copy `default.yaml`, tune weights for the vertical, drop
  in `eval/rubrics/`. Then run with `--rubric eval/rubrics/yourname.yaml`.
- **Different MCP tool surface.** Edit `eval/mcp_client.py` —
  `PREFERRED_RENDER_TOOLS` and `PREFERRED_STATUS_TOOLS` are at the top.
- **Different judge model.** Change `MODEL` in `eval/judge.py`. The judge
  benefits from Opus-tier reasoning; downgrading to Sonnet costs ~30% of
  the rubric agreement on internal tests.
- **Audio judging.** The current judge scores audio from prompt evidence
  only. To judge actual rendered audio, extract the audio track via
  ffmpeg, transcribe with whisper, and pass the transcript to the judge.

## Known limits

- The judge cannot watch video, only frames. Motion quality (smoothness,
  motion blur, easing) is judged from prompt evidence + the frame
  sequence. For motion-heavy verticals (action, music video), consider
  bumping `--frames` to 8.
- Cost grows linearly with iterations. For unattended runs, set
  `--max-iterations 2` and a `--threshold` you trust, or you'll burn
  budget chasing the last 5%.
- The harness assumes the MCP returns a downloadable URL. If your MCP
  returns a file ID requiring a separate download endpoint, edit
  `mcp_client.render` to follow that pattern.
