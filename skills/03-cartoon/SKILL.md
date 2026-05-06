---
name: higgsfield-cartoon
description: Generate cartoon and 2D animation video prompts for Higgsfield Seedance 2.0. Use whenever the user wants cartoon, 2D animation, cel-shaded, hand-drawn, illustrated, flat animation, motion graphics, vector animation, or rubber-hose style. Triggers on cartoon, animation, cel shading, hand-drawn, illustrated, flat design animation, vector animation, retro cartoon, rubber hose, motion graphics, watercolour, gouache, or any cartoon/animated style request. Use even for vague "make it look animated" or "fun colourful style."
---

# Cartoon — Higgsfield Seedance 2.0

For 2D-feeling animation: cel-shaded, hand-drawn, flat vector, watercolour,
rubber-hose retro, motion graphics. Distinct from anime (`08-anime-action`)
which has its own conventions.

## When to use

- "2D animation", "cel-shaded", "hand-drawn", "flat design".
- Children's content, explainer videos, motion-graphics ads.
- Watercolour, gouache, ink-and-wash, pastel.
- Retro: 1930s rubber-hose, 1950s mid-century, 80s Saturday morning.
- "Disney early style" (pre-CG), Cartoon Network 90s, Adventure Time, Studio
  Mir, Genndy Tartakovsky.

If anime / manga → `08-anime-action`. If 3D Pixar → `02-3d-cgi`.

## What's unique to cartoon

1. **Frame rate is a stylistic choice.** "On twos" (12 fps animated motion)
   reads as classic hand-drawn. Smooth 24 fps reads as Disney feature.
   60 fps reads wrong.
2. **Lines and fills are separate concerns.** Specify line weight, line
   color, fill style. "Black ink lines on flat watercolour fills" is a
   different look from "no lines, soft gradient fills."
3. **Squash and stretch.** Characters compress on impact, stretch on
   movement. Without it, animation reads as paper cutouts.
4. **Limited palette = identity.** 4–8 colors total beats 50 colors.
5. **Backgrounds painted, characters animated.** Classic cartoon split:
   detailed static backgrounds, simpler animated foreground characters.

## Cartoon-specific hooks

| Hook                       | Phrasing |
| -------------------------- | -------- |
| **Splash entrance**         | "Character enters frame with squash-stretch impact; animation principle 'anticipation' — pulls back before launch." |
| **Hand draws scene in**     | "Empty white frame. Animated hand draws scene with ink line in 0–2 s. Colors flood in at 2 s." |
| **Color pop on B&W**        | "Frame opens in flat B&W line art. Single accent color (red, gold) appears at 1 s and spreads at 2 s." |
| **Page turn / panel split** | "Frame opens as comic panel. At 1.5 s panel border peels away like a page turn." |
| **Bouncing logo / squash**  | "Logo / title bounces into frame with rubber-hose squash; settles by 2 s." |

## References

- Camera moves (use sparingly, favour Lock-Off, Pan, Whip Pan):
  [shared/camera-movements.md](../../shared/camera-movements.md)
- Grading: [Anime Cel Look](../../shared/color-grading.md), Vintage Film,
  Monochromatic
- Hooks: [shared/hook-framework.md](../../shared/hook-framework.md)

## Worked example — Watercolour storybook scene, 8 s

```
[HOOK 0–2 s]
Empty cream paper texture. At 0.5 s ink lines flow in from frame-edges
forming a tree silhouette. At 1.5 s watercolour wash floods in: warm
amber for autumn leaves, cool grey for sky. Settles at 2 s into still
painted scene.

[ACTION 2–6 s]
Subtle animation: leaves drift down on twos (12 fps). Camera does slow
locked-off lean (no real motion, just gentle parallax between layers:
foreground leaves, mid-tree, background sky). Watercolour bleeds remain
visible as layers.

[CLIMAX 6–8 s]
Single fox enters frame from left, hand-animated walk cycle on twos.
Stops centre-frame, looks up at falling leaves.

[STYLE] Watercolour gouache aesthetic. Visible paper texture. Soft ink
lines, varying weight. 4-color palette: amber, sage, slate-grey,
cream-white.

[AUDIO] Soft wind ambient. Sparse foley: leaf rustle. Gentle solo piano
melody from 3 s.

[OUTPUT] 8 s, 16:9, 720p.
```

## Worked example — Flat-vector explainer, 6 s

```
[HOOK 0–2 s]
Flat solid orange background. At 0.5 s a circle drops in with squash
impact (anticipation + bounce). At 1 s it's joined by a rectangle and
triangle, all primary geometric shapes. At 2 s shapes assemble into a
stylised rocket icon.

[ACTION 2–5 s]
Rocket launches: anticipation (0.3 s squash down), then upward streak
across frame with motion lines and exhaust dots. Frame transitions via
whip-pan match to scene 2 — same rocket now in space, planets as flat
circles.

[CLIMAX 5–6 s]
Title card slides in below rocket: bold sans-serif typography animates
on with letter-by-letter scale.

[STYLE] Flat vector, no gradients, hard-edged. 5-color palette: orange,
navy, white, mint, coral. Line weight 2 px where lines exist.

[AUDIO] Synth swoosh on launch. Bright two-note motif on title card
arrival. No ambient.

[OUTPUT] 6 s, 16:9, 720p.
```

## Common pitfalls

- **Smooth 60 fps motion** breaks cartoon language. Specify "on twos" /
  "12 fps stepped animation" for hand-drawn feel.
- **Photoreal lighting in cartoons.** Cel shading uses 2–3 hard shading
  steps, not gradients. Specify "no soft shading, hard-edged shadow
  transitions."
- **Too many colors.** Cartoons live or die by palette discipline.
- **Realistic camera moves.** A cinematic crane shot in a flat-vector
  cartoon looks cheap. Stick to pans, whips, lock-offs.


## Submitting

Submit via the Higgsfield CLI (not the MCP server, not the API):

```bash
higgsfield generate create seedance_2_0 \
  --prompt "<the prompt you assembled above>" \
  --duration <n> --aspect_ratio <r> --wait
```

`--wait` blocks until the job is done and prints the result URL. See
[shared/submission.md](../../shared/submission.md) for media flags,
auth bootstrap, and the full rationale for preferring CLI over MCP.
\r
