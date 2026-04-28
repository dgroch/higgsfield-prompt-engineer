# higgsfield-prompt-engineer

Claude Skills for generating production-grade Higgsfield video prompts. Lean,
deduplicated, and designed to compose with the Higgsfield MCP.

## Why this exists

Generic AI video prompts produce generic results. Each video vertical
(cinematic, e-commerce, anime, real estate, etc.) has its own conventions for
camera language, lighting, pacing, and audience expectation. This repo
encodes those conventions as Claude Skills, so the model produces prompts
that respect the craft of each genre rather than averaging across all of them.

## Design principles

1. **One source of truth for shared craft.** Camera moves, lighting setups,
   color grades, and sound layers live once in `shared/`. Skills reference
   them; they do not duplicate them.
2. **Skills are thin.** A skill encodes what is *unique* to its vertical —
   visual references, genre-specific hook patterns, vocabulary, two or three
   worked examples. Anything generic belongs in `shared/`.
3. **Prompts are the artifact.** The output of a skill is a paste-ready
   prompt block. The skill itself is documentation; the prompt is the
   product.
4. **Empirically validated, not assertively written.** Every numeric claim
   ("dolly at 2 ft/s", "rack focus over 1.5s") should be confirmed against
   real Higgsfield generations and tightened over time. Unverified phrasings
   are marked `[unverified]` until a tester confirms.

## Repo structure

```
higgsfield-prompt-engineer/
├── README.md
├── LICENSE
├── shared/                        # Reusable craft library
│   ├── camera-movements.md        # ~22 camera moves with prompt phrasing
│   ├── lighting-library.md        # ~15 lighting setups
│   ├── color-grading.md           # ~10 grading approaches
│   ├── sound-design.md            # 6 audio layers + spatial cues
│   ├── hook-framework.md          # 12 attention-grabbing openers
│   ├── timeline-structures.md     # 4s / 8s / 10s / 15s arcs
│   └── prompt-template.md         # Master prompt skeleton
└── skills/
    ├── 01-cinematic/SKILL.md
    ├── 02-3d-cgi/SKILL.md
    ├── 03-cartoon/SKILL.md
    ├── 04-comic-to-video/SKILL.md
    ├── 05-fight-scenes/SKILL.md
    ├── 06-motion-design-ad/SKILL.md
    ├── 07-ecommerce-ad/SKILL.md
    ├── 08-anime-action/SKILL.md
    ├── 09-product-360/SKILL.md
    ├── 10-music-video/SKILL.md
    ├── 11-social-hook/SKILL.md
    ├── 12-brand-story/SKILL.md
    ├── 13-fashion-lookbook/SKILL.md
    ├── 14-food-beverage/SKILL.md
    └── 15-real-estate/SKILL.md
```

## How a skill is structured

Every `SKILL.md` follows the same shape:

```yaml
---
name: <slug>
description: When this skill should be triggered, with explicit keyword list.
---
```

Then:

1. **When to use** — concrete examples of user intent that should activate it.
2. **What's unique to this genre** — the conventions, vocabulary, and pitfalls
   specific to this vertical.
3. **Genre-specific hooks** — 3–5 opener patterns tuned to this audience.
   Generic openers stay in `shared/hook-framework.md`.
4. **References** — pointers into `shared/` for camera, lighting, color, sound.
5. **Worked examples** — 2–3 complete prompts. Quality over quantity; each one
   gets validated against real Higgsfield output before it ships.

## Higgsfield MCP integration

Higgsfield publishes an MCP server that exposes video generation as tool
calls. The intended workflow is:

1. The user describes what they want.
2. Claude routes to the right skill (via `description` triggers).
3. The skill builds a prompt and invokes the Higgsfield MCP tool to generate.
4. Output is returned to the user with the prompt for reuse / iteration.

The MCP tool surface is documented at the Higgsfield platform. Add the server
to your Claude config; the skills here produce prompts in the format the MCP
expects, with `@image1` / `@video1` / `@audio1` reference syntax for uploaded
materials.

## Seedance 2.0 platform constraints

| Input  | Format                              | Limit                                |
| ------ | ----------------------------------- | ------------------------------------ |
| Image  | jpeg, png, webp, bmp, tiff, gif     | ≤ 9 files, < 30 MB each              |
| Video  | mp4, mov                            | ≤ 3 files, < 50 MB each, 2–15 s      |
| Audio  | mp3, wav                            | ≤ 3 files, < 15 MB each, ≤ 15 s      |
| Text   | natural language                    | —                                    |
| Total  | —                                   | ≤ 12 files combined                  |
| Output | video                               | 4–15 s, 720p, audio synchronised     |

Reference uploaded materials inline with `@image1`, `@video1`, `@audio1`.

## Status

This is a working scaffold. The 15-skill taxonomy and shared craft library
are in place. Next steps:

- [ ] Validate camera/lighting numerics against real Higgsfield generations
- [ ] Replace `[unverified]` markers with confirmed phrasings
- [ ] Add MCP tool invocation snippets once the tool surface is documented
- [ ] Build a small evaluation harness: prompt → render → rating
- [ ] Bilingual (zh-CN) once English is empirically tightened

## Contributing

PRs welcome. Rules:

1. Don't add prose for its own sake. If a sentence isn't load-bearing, cut it.
2. New craft knowledge goes in `shared/`. Skills only get genre-specific
   content.
3. Numeric claims need a source: cinematography textbook, real generation, or
   `[unverified]` tag.
4. Examples must be tested against Higgsfield output before being added.
