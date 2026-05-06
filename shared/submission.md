# Submitting Seedance 2.0 prompts

All 15 skills in this repo produce a Seedance 2.0 prompt. The canonical
way to submit it is the **Higgsfield CLI** — not the Higgsfield MCP
server, not the REST API.

## One-shot command

```bash
higgsfield generate create seedance_2_0 \
  --prompt "$(cat <<'EOF'
[HOOK 0–2 s]
... your assembled prompt ...
EOF
)" \
  --duration 8 \
  --aspect_ratio 16:9 \
  --resolution 720p \
  --wait
```

`--wait` blocks until the job reaches a terminal state and prints the
result URL on stdout. No polling, no second command.

## Flags worth setting

| Flag | Choices | When to change |
|---|---|---|
| `--duration` | `4` / `6` / `8` / `10` / `12` / `15` (seconds) | Match the `[OUTPUT]` block in the prompt |
| `--aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `9:16` for social, `16:9` for cinematic, `1:1` for square ads |
| `--resolution` | `480p` / `720p` | `720p` is the Seedance default; `480p` only for fast iteration |
| `--wait-timeout` | duration string, default `10m` | Bump to `20m`+ for 12–15 s clips during peak load |

For the full schema run `higgsfield model get seedance_2_0 --json`.

## Reference media

If the prompt references uploaded materials (`@image1`, `@start_image`,
`@audio1`), pass them as flags. Local paths auto-upload; UUIDs from a
prior `higgsfield upload create` or a previous job id also work.

```bash
... --start-image ./first-frame.png \
    --end-image ./last-frame.png \
    --audio ./score.mp3
```

Seedance 2.0 accepts `image`, `start_image`, `end_image`, `video`, and
`audio` roles. Use `--audio` for music / voiceover / lipsync — do NOT
use `--generate-audio` on Seedance (that flag belongs to Marketing
Studio).

## Bootstrap

If `higgsfield` isn't on `$PATH`:

```bash
curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
```

If `higgsfield account status` reports `Session expired` or
`Not authenticated`, ask the user to run `higgsfield auth login`
(opens a browser) and confirm before retrying.

## Why CLI, not MCP

- Streams progress and blocks on `--wait` — one command, one URL.
- Auto-uploads local file paths; no separate `media_upload` step.
- Schema-flexible: any param the model accepts can be passed as a flag.
- Survives MCP server outages and works in non-interactive contexts.

The `mcp__claude_ai_Higgsfield_AI__*` tools are a fallback when the CLI
isn't installed. They are not the default.
