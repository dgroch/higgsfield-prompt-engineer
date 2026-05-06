---
name: higgsfield-cinematic
description: Generate cinematic film-style video prompts for Higgsfield Seedance 2.0. Use whenever the user wants cinematic, film-look, movie-quality, Hollywood-style, dramatic, or professional film-quality AI video. Triggers on cinematic, film look, movie scene, dramatic lighting, depth of field, lens flare, anamorphic, letterbox, noir, epic, Steadicam, dolly, crane shot, or any cinematic video request. Use even if the user describes a film-like aesthetic without saying "cinematic."
---

# Cinematic — Higgsfield Seedance 2.0

Generates film-quality prompts: dramatic lighting, intentional camera
language, controlled depth of field, considered grading. The opposite of
"AI video stock."

## When to use

- "Make it look like a movie."
- "Cinematic shot of ___."
- Any reference to Blade Runner, Dune, Fincher, Villeneuve, Deakins, A24,
  Christopher Doyle, Roger Deakins, or specific film titles.
- Drama, noir, period, prestige TV aesthetic.
- When the user asks for *quality* without a more specific genre.

If the user wants action choreography → `05-fight-scenes`. If they want
3D-rendered Pixar/Unreal look → `02-3d-cgi`. If they want viral/TikTok hook
specifically → `11-social-hook`.

## What's unique to cinematic

1. **Camera moves with intent.** Every move communicates emotion: dolly
   forward = intimacy; pull-back = revelation; handheld = urgency. Never
   move "just because."
2. **Lighting motivates the shot.** Sources are visible or implied
   (windows, lamps, fire). Naked three-point lighting reads as TV.
3. **Composition before action.** Establish frame; *then* let action move
   through it. The frame is a stage.
4. **Sound is half the cinema.** Specify ambient + score + foley + silence
   pattern. Silent moments before sound earn the impact.
5. **Grade is identity.** Bleach bypass, teal-orange, monochromatic, vintage
   film stock — pick one and commit.

## Cinematic-specific hooks

Beyond the [generic 12](../../shared/hook-framework.md), cinematic openers:

| Hook                   | Phrasing |
| ---------------------- | -------- |
| **Long unbroken pre-roll** | "12 s of slow handheld through fog before any subject appears. Builds dread before the reveal." |
| **In medias res action** | "Open mid-action: subject already running / falling / fighting. Context comes after." |
| **Single source flicker** | "Fire/lamp flicker the only light source. Frame breathes with light intensity." |
| **Reflection-only reveal** | "Subject visible only as reflection (water, glass, mirror) for first 2 s, then camera tilts to real subject." |
| **Sound-led entrance** | "Diegetic sound (radio, voice, footstep) precedes the visual subject by 1–2 s." |

## References

- Camera language: [shared/camera-movements.md](../../shared/camera-movements.md)
- Lighting setups (favour Three-Point, Chiaroscuro, Golden Hour, Volumetric):
  [shared/lighting-library.md](../../shared/lighting-library.md)
- Grading (favour Teal & Orange, Bleach Bypass, Vintage Film Stock):
  [shared/color-grading.md](../../shared/color-grading.md)
- Sound design: [shared/sound-design.md](../../shared/sound-design.md)
- Timing: [shared/timeline-structures.md](../../shared/timeline-structures.md)
- Skeleton: [shared/prompt-template.md](../../shared/prompt-template.md)

## Worked example — Noir detective, 10 s

```
[HOOK 0–2 s]
Pure black, complete silence. At 0.8 s explosive cool-blue 5000 K light
burst from frame-left. Hard-edged shadow stripes the centre of frame.
Sub-bass rumble enters −20 → −6 dB.

[ESTABLISH 2–4.5 s]
1940s warehouse interior, cool grey concrete, exposed metal beams
overhead. Camera 40 ft back, 15° low angle, 35 mm equivalent. Chiaroscuro:
hard 3000 K key at 60° upper-left; fill 15%; rim 40%. 35 mm film grain.

[ACTION 4.5–8 s]
Camera dollies forward at 1.5 ft/s, low angle held. Detective silhouette
materialises in shadow-pool centre-frame. At 5.5 s detective's face
catches edge of overhead light — eye glint visible. At 6 s pulls cigarette
from pocket (silhouette).

[CLIMAX 8–10 s]
Detective lights cigarette; small flame momentarily lights weathered face
— grim, weary. At 8.3 s practical desk lamp flicks on frame-right; second
warm 2700 K source creates conflicting shadows. Detective turns
camera-left. Fade to black at 9.5 s.

[CAMERA] f/2.0 shallow. Focus locked on face during dolly. Constant 1.5
ft/s, no acceleration.

[GRADE] Bleach bypass: blacks at 10% (not 0), greys elevated, saturation
0%. Grain at 150% on shadow areas.

[AUDIO] 0–1 s silence. 1–4 s low jazz trumpet enters at −6 dB. 4–7 s foley
— footsteps on concrete, cloth rustle. 8–8.3 s sharp lighter scratch
synced to flame. 8.5–10 s music swells to −2 dB.

[OUTPUT] 10 s, 16:9, 720p.
```

## Worked example — Golden hour landscape, 8 s

```
[HOOK 0–2 s]
Extreme macro of a single dust mote drifting across a sunbeam. Shallow
f/1.4. At 1.5 s rack focus pulls back; mote becomes one of thousands in a
volumetric beam through forest canopy.

[ESTABLISH 2–4.5 s]
Pine forest, late golden hour. Volumetric god rays through canopy, warm
3200 K directional. Camera at ground level, 24 mm equivalent. Color
grade: warm nostalgia, +15% saturation on warm tones.

[ACTION 4.5–7 s]
Slow crane up at 3 ft/s over 2.5 s, tilting down to maintain forest floor
visibility. Reveals a single deer standing in the beam, frozen, looking
toward camera.

[CLIMAX 7–8 s]
Camera locks. Deer holds still. Wind moves leaves. Single bird call.
Frame breathes.

[AUDIO] Forest ambient bed throughout at −5 dB. Sparse foley: leaf
rustle, distant crow at 4 s. Solo cello note at 7 s, sustained.

[OUTPUT] 8 s, 16:9, 720p.
```

## Common pitfalls

- **Over-specifying every parameter.** If your prompt is 50 lines, you've
  almost certainly contradicted yourself somewhere. Prefer 20 strong lines.
- **Naming film references without translating them.** "Like Blade Runner
  2049" tells the model little; "neon practical lights, deep blue
  shadows, atmospheric haze, slow handheld" tells it a lot.
- **Static + handheld.** Pick one. Locked-off and handheld in the same clip
  reads as a mistake.
- **Forgetting silence.** Cinematic is as much about what isn't on the
  soundtrack as what is.


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
