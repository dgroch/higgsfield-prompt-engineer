---
name: higgsfield-anime-action
description: Generate anime-style video prompts for Higgsfield Seedance 2.0. Use whenever the user wants anime, Japanese animation style, shonen action, seinen drama, magical girl, mecha, isekai, slice-of-life anime, or any Japanese animation aesthetic. Triggers on anime, Japanese animation, shonen, seinen, manga style video, anime fight, anime opening, anime ending, sakura, chibi, kawaii, mecha, isekai, Studio Ghibli, Madhouse, MAPPA, Ufotable, or any anime-style request. Use even for "make it look like an anime" or "Japanese cartoon style."
---

# Anime — Higgsfield Seedance 2.0

For Japanese animation aesthetics: shonen action, seinen drama, magical
girl, mecha, slice-of-life, isekai, sports anime. Distinct from generic
cartoon (`03-cartoon`) — anime has its own grammar of pacing, framing,
and visual flourishes.

## When to use

- Any "anime" reference.
- Genre-specific: shonen (battle), seinen (mature), shojo (romance),
  mecha, magical girl, isekai, sports.
- Studio aesthetics: Ghibli (whimsical), Madhouse (dark), Ufotable (FX-heavy
  battle), MAPPA (modern shonen), Trigger (kinetic), Kyoto Animation
  (slice-of-life detail).
- Anime opening / ending sequences.
- Manga adaptation.

For non-anime 2D → `03-cartoon`. For source-comic animation → `04-comic-to-video`.

## What's unique to anime

1. **Limited animation principles.** Mouth flaps on twos, full-body motion
   on ones during action, holds otherwise. Selective motion is the style.
2. **Speed lines and impact frames.** Single-frame all-white or
   high-contrast hold at moment of impact. Then speed-line burst.
3. **Cel shading, not gradients.** Hard-edged shading transitions, two or
   three steps from light to shadow. Highlights are flat shapes.
4. **Big eyes, expressive faces.** Anime over-emphasises eye reflection
   and pupil dynamics. Specify "highlight in eyes," "pupil dilation."
5. **Wind, hair, cloth.** Even in still moments, hair drifts, cloth ripples,
   particles float. Stillness without these reads as mannequin.
6. **Panel-style compositions.** Inspired by manga: Dutch angles, extreme
   foreshortening, dramatic close-ups on detail (eye, weapon, hand).
7. **Pacing extremes.** Long held still frames, then rapid-cut action.
   Mid-tempo action is rare.

## Anime-specific hooks

| Hook                       | Phrasing |
| -------------------------- | -------- |
| **Eye close-up reflection**| "Extreme close-up of single eye. Reflection of antagonist / object visible in iris. Pupil dilates at 1 s." |
| **Wind-blown hair reveal** | "Camera at low angle, sky behind. Subject's hair drifts in wind. Subject rises into frame at 1.5 s, looks down." |
| **Speed-line pre-action**  | "Speed lines fill frame radiating from off-frame point. At 1.5 s subject bursts into centre with motion blur." |
| **Sakura petal drift**     | "Cherry petals drift across frame in slow motion. Subject walks through them, paused mid-step at 1.8 s." |
| **Power-up aura**          | "Subject stands centre-frame. Energy aura builds 0–2 s, hair lifts, ground cracks; flash-cut to full power form at 2 s." |

## References

- Camera (use **Whip Pan**, **Push-In + Zoom**, **Dutch Angle**, **Lock-Off**):
  [shared/camera-movements.md](../../shared/camera-movements.md)
- Grading: [Anime Cel Look](../../shared/color-grading.md), Cyberpunk Neon for
  modern shonen
- Sound (silence-then-impact pattern is core):
  [shared/sound-design.md](../../shared/sound-design.md)

## Worked example — Shonen battle moment, 8 s

```
[HOOK 0–2 s]
Extreme close-up of protagonist's eye. Iris reflects opponent silhouette.
At 1.2 s pupil dilates. At 1.5 s eyes narrow; energy aura begins. At 2 s
whip-pan to wide shot.

[ACTION 2–6 s]
Wide shot: protagonist stands on broken stone platform, hair lifting from
energy. Cherry petals + dust particles drift around. Camera 35 mm wide,
slight low angle hero framing.

3 s: protagonist takes single step forward (animated on ones during step).
Speed lines fill background.
3.5 s: clenches fist; impact frame (single all-white frame).
4 s: lunges out of frame to right with motion blur.
4.5–5.5 s: cut to opponent — same composition mirrored. Receives strike;
impact frame all-white at 5 s, then high-contrast hold for 0.15 s.
5.5–6 s: opponent flies backward into stone wall; cracks radiate.

[CLIMAX 6–8 s]
Cut to slow-motion close-up of protagonist's face — focused, breath
visible. Hair settles. Aura dims. Hold.

[STYLE] Cel-shaded; hard 2-step shading. Saturation +30%. Outline
emphasis on subject. Manga screentone in shadows.

[CAMERA] Mostly locked + whip-pans. Push-in + zoom on key reveal beats.

[AUDIO] Silence on hook. Single bass swell builds 1–2 s. Whoosh on
whip-pan at 2 s. Foley step at 3 s. Energy hum from 3.5 s. Silence pause
at 4.5 s before impact. Heavy drum hit at 5 s. Impact-debris foley
5.5–6 s. Held silence + slow piano motif from 6 s.

[OUTPUT] 8 s, 16:9, 720p.
```

## Worked example — Slice-of-life moment, 8 s

```
[HOOK 0–2 s]
Sun-dappled classroom. Curtains drift in summer breeze. Protagonist
asleep at desk, head on arms. Camera slow push-in over 0–2 s. Cicada
ambient.

[ACTION 2–6 s]
Single hair strand drifts from breeze. At 3 s student stirs — slow
inhale, eyes flutter. At 4 s wakes fully, lifts head. Hair bounces with
subtle gravity. Looks toward window. At 5 s sun catches face,
overexposes briefly (anime lens flare). At 5.5 s a single tear glistens
at corner of eye.

[CLIMAX 6–8 s]
Wide pull-back: empty classroom, sun streaming, cicada cresting on
audio. Petal drifts across frame. Title card fades in — Japanese
calligraphy + romaji translation.

[STYLE] Kyoto Animation slice-of-life: detailed backgrounds, soft cel
shading, warm summer palette. Slight bloom on highlights.

[CAMERA] Locked + slow push-in / pull-back. 35 mm equivalent.

[GRADE] Warm nostalgia: 3200 K, +15% saturation on warm tones. Slight
lifted shadows.

[AUDIO] Cicada ambient throughout. Curtain rustle foley. Solo piano
arrives at 4 s, builds to 7 s. Held quiet on title card.

[OUTPUT] 8 s, 16:9, 720p.
```

## Common pitfalls

- **Western cartoon shading on anime.** Gradients break the cel look.
  Specify hard 2–3 step shading.
- **No speed lines / impact frames** in action. They're not optional in
  shonen — they're the genre.
- **Smooth 24 fps mid-tempo motion.** Anime alternates extremes. Specify
  "limited animation; full animation only on specific beats."
- **Generic anime.** Pick a studio sensibility (Ghibli vs Trigger vs
  Ufotable) — they're radically different.


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
