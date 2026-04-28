---
name: higgsfield-music-video
description: Generate music video and beat-synced visual content prompts for Higgsfield Seedance 2.0. Use whenever the user wants to create a music video, lyric video, beat-synced visuals, performance video, concert visual, album art animation, or music-driven visual content. Triggers on music video, lyric video, beat sync, music visualization, performance video, concert visual, album visual, song video, music clip, beat drop visual, rhythm sync, or any music-driven video request. Use even for "make visuals for my song" or "video for this track."
---

# Music Video — Higgsfield Seedance 2.0

For visuals locked to a music track. The track (provided as `@audio1`) is
the spine; everything visual cuts and moves to its rhythm.

## When to use

- "Music video for my song" — user supplies `@audio1`.
- Lyric video, beat-sync visualiser, performance/concert content.
- Album-art animation, song teaser, social music clip.

For brand storytelling with music as accompaniment → `12-brand-story`. For
fashion with track sync → `13-fashion-lookbook`.

## What's unique to music video

1. **The track dictates structure.** Identify intro / verse / chorus /
   drop / bridge in the audio, then map visual beats onto each.
2. **Cuts on beats, holds in pockets.** A music-video cut on the snare or
   kick reads as "synced." A cut on a non-beat moment reads as random.
3. **Performance vs narrative vs abstract.** Pick one mode: artist
   performing, story unfolding, or pure abstract visual. Mixing them
   poorly reads as confused.
4. **Drop = climax.** When the track drops, the visual must escalate:
   faster cuts, brighter, denser, or absolute lock-off contrast.
5. **Loops and motifs.** Repeating visual motifs (a colour, a frame, a
   gesture) across verses build cohesion.

## Music-video hooks

| Hook                       | Phrasing |
| -------------------------- | -------- |
| **Pre-drop silence**       | "First 1.5 s use silent or sub-bass-only audio. At drop moment (1.5–2 s) full mix arrives + visual explosion." |
| **Artist eye lock-on**     | "Close-up on artist's eyes for 0–1.5 s. At first beat eyes lock to camera; whip-pan to wide on second beat." |
| **Title-card stinger**     | "Album / track title appears as bold typography on first beat; flickers / shatters / dissolves on second." |
| **Match-cut on rhythm**    | "Two locations match-cut on the kick: same composition, different scenes; toggles for first 4 beats." |
| **Visual freeze on note**  | "Visual freezes on a sustained note; resumes on next downbeat with a cut to new angle." |

## References

- Camera (use **Whip Pan**, **Push-In + Zoom**, **Dutch Angle**, **360 Orbit**):
  [shared/camera-movements.md](../../shared/camera-movements.md)
- Lighting (**Practical Neon**, **Two-Source Split**, **Volumetric**):
  [shared/lighting-library.md](../../shared/lighting-library.md)
- Grading (often **Cyberpunk Neon**, **Teal & Orange**, **Bleach Bypass**):
  [shared/color-grading.md](../../shared/color-grading.md)
- Sound: `@audio1` is the centre of gravity, see
  [shared/sound-design.md](../../shared/sound-design.md)

## Worked example — Performance, neon-lit, 10 s

```
[AUDIO REFERENCE]
@audio1 — assume 120 BPM track. Beat grid: 0.5 s per beat, 2 s per bar.
Drop at 2 s. Identify kick beats and cut to them.

[HOOK 0–2 s]
Black frame, sub-bass only from @audio1 for 0–1.5 s. Artist silhouette
appears at 1.5 s, backlit by single magenta neon. At 2 s drop hits —
full mix + practical neon lights snap on (cyan + magenta + green).
Whip-pan from silhouette to artist face.

[ACTION 2–8 s]
Artist performing centre-frame. Cuts on every kick (every 0.5 s):
- 2.0 s: medium-wide on artist
- 2.5 s: close-up on hands holding mic
- 3.0 s: low-angle hero, neon rim
- 3.5 s: dutch-angle profile
- 4.0 s: wide pull-back showing full stage
- 4.5 s: crowd silhouette POV from artist
- 5.0–5.5 s: hold on artist eyes, locked
- 5.5–7 s: rapid double-time cuts (4 cuts) — different angles of same
  performance moment
- 7.0–8.0 s: longer hold; slow push-in on artist face

Camera moves between cuts: handheld, gimbal-smooth, locked, dutch.
Variety drives energy.

[CLIMAX 8–10 s]
Slow-motion shot of artist throwing arm upward; sparks / particles fly
from gesture. Lights flicker on every beat. Final lock-off at 9.5 s
holds for two beats.

[LIGHTING] Practical neon: hot magenta, cyan, acid green from off-frame
fixtures. Multiple conflicting shadows. Volumetric haze enhances beams.

[GRADE] Cyberpunk neon: saturation 140%, split-tone shadows cyan,
highlights magenta. Bloom on light sources.

[CAMERA] f/2.0 throughout. 35 mm equivalent. Mix of handheld + gimbal +
locked. Cuts on the kick.

[AUDIO] @audio1 throughout, full mix from 2 s. Subtle reverb on artist
foley (vocal performance gestures). No additional ambient.

[OUTPUT] 10 s, 9:16, 720p.
```

## Worked example — Lyric video, 8 s

```
[AUDIO]
@audio1, mid-tempo 90 BPM track. Lyric line: "and the city never sleeps."

[HOOK 0–2 s]
Aerial drone shot of city at night, traffic light trails. At 1.5 s
camera descends sharply (drone-swoop). At 2 s lyric "and the city" types
on in bold type, kerning-locked.

[ACTION 2–7 s]
City rooftop POV. Camera drifts handheld through neon environment.
Type animates with the lyrics — each phrase appearing on its downbeat,
fading on next:
- "and the city" — 2 s
- "never" — 3.5 s, larger type
- "sleeps" — 4.5 s, with neon glow
- (lyric break) — 5–6 s, instrumental motif visualised as light pulses
- repeat lyric variation — 6–7 s

Type style: bold sans-serif, slight motion blur on entrance/exit, anchor
to beat grid.

[CLIMAX 7–8 s]
Camera locks on a single neon sign. Final lyric phrase pulses with each
remaining beat. Fade to black on final beat.

[GRADE] Cyberpunk neon: saturation 140%, magenta highlights, cyan
shadows.

[OUTPUT] 8 s, 9:16, 720p.
```

## Common pitfalls

- **Cuts on non-beats.** Identify the kick / snare / crash and cut there.
- **Visuals escalating before the drop.** Save the visual punch for the
  drop. Burning your peak in the verse loses the climax.
- **No audio reference.** Music videos need `@audio1` — without it the
  prompt is just a vibey clip, not a music video.
- **Three modes at once.** Performance + narrative + abstract in 8 s
  reads as a trailer for three different videos.
