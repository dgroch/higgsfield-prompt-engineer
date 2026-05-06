---
name: higgsfield-fashion-lookbook
description: Generate fashion lookbook, model showcase, and style video prompts for Higgsfield Seedance 2.0. Use whenever the user wants fashion video content, lookbook videos, model walks, outfit showcases, style guides, fashion campaigns, runway clips, streetwear content, or any fashion/clothing video. Triggers on fashion video, lookbook, model showcase, outfit, style guide, fashion campaign, runway, streetwear, collection launch, fashion ad, clothing video, OOTD, fashion film, or any fashion/model video request. Use even for "show off this outfit" or "fashion content for my brand."
---

# Fashion Lookbook — Higgsfield Seedance 2.0

For fashion video: lookbooks, runway, model walks, outfit showcases,
campaigns, streetwear. The garment is the protagonist; everything else —
location, lighting, music, model — frames it.

## When to use

- Lookbook reveals, OOTD content, outfit showcases.
- Runway / catwalk style.
- Streetwear campaigns.
- Editorial fashion film.
- Collection launch teasers.

For pure product shots → `09-product-360`. For e-commerce conversion →
`07-ecommerce-ad`. For brand-led storytelling → `12-brand-story`.

## What's unique to fashion

1. **Fabric movement is the star.** Wind in hair, billow in coat, sway in
   dress. Without this, fashion video reads as catalogue stills.
2. **Walk pace defines the brand.** Streetwear = casual handheld follow.
   Luxury = slow, deliberate, locked. High fashion = stylised, exaggerated.
3. **Three-quarter angles for outfits.** Pure profile or pure front
   undersells. 3/4 turns let viewer see silhouette, fabric, fit.
4. **Location is wardrobe.** Backdrop should harmonise with palette and
   mood: brutalist concrete for streetwear, marble for luxury, forest for
   romantic.
5. **Light from behind for hero.** Backlit / rim-lit silhouettes
   exaggerate fabric texture and form.
6. **Detail shots matter.** Macro on stitch, button, lacing, belt,
   accessory. The story is in the detail.

## Fashion-specific hooks

| Hook                       | Phrasing |
| -------------------------- | -------- |
| **Hair flick / fabric snap** | "Macro on hair / fabric edge frozen mid-flick. At 1 s motion resumes in slow-mo. Camera locks." |
| **Walk-in entrance**       | "Empty location 0–1 s. At 1 s model strides into frame from off-screen edge; camera tracks." |
| **Detail-then-wide**       | "Macro on a single garment detail (button, stitch, pattern). At 1.5 s rack out to full outfit." |
| **Mirror / reflection**    | "Frame on mirror / glass. Reflection shows model first; camera tilts/pans to real model at 2 s." |
| **Wind-flag pose**         | "Model in dramatic pose; cape / dress / hair caught mid-blow by off-frame wind. Held still." |

## References

- Camera (favour **Tracking**, **Steadicam**, **360 Orbit**, **Rack Focus**):
  [shared/camera-movements.md](../../shared/camera-movements.md)
- Lighting (**Golden Hour**, **High-Key Beauty**, **Three-Point**,
  **Practical Neon** for streetwear):
  [shared/lighting-library.md](../../shared/lighting-library.md)
- Grading (often **Warm Nostalgia**, **Vintage Film**, **Bleach Bypass**
  for high-fashion editorial):
  [shared/color-grading.md](../../shared/color-grading.md)
- Sound (often track-driven; minimal foley):
  [shared/sound-design.md](../../shared/sound-design.md)

## Worked example — Streetwear walk, 8 s

```
[HOOK 0–2 s]
Brutalist concrete underpass, midday. Wide locked shot. Empty for 0–1 s
except for distant city ambient. At 1 s model strides into frame from
right edge — confident, mid-pace, hood up. Camera holds locked.

[ACTION 2–6 s]
Camera tracks left at model's walking speed (~3 ft/s) over 4 s,
matching pace. Side profile maintained. Outfit visible:
- 2–3 s: full outfit silhouette against concrete; texture of fabric
  visible against rough wall.
- 3–4 s: rack focus to detail — graphic on hoodie, then back to wide.
- 4–5 s: model glances at camera; subtle nod.
- 5–6 s: camera pulls slightly ahead, framing 3/4 angle as model
  approaches.

[CLIMAX 6–8 s]
Camera locks; model walks past lens at 7 s in 3/4 angle. Pauses for one
beat just past camera; turns head back to camera at 7.5 s. Brand
wordmark appears bottom-third at 7.8 s.

[STYLE] Streetwear documentary feel. Casual handheld energy with
locked-off framings.

[LIGHTING] Harsh midday sun reflecting off concrete. Hard-edge shadows,
high contrast. No fill.

[GRADE] Bleach bypass: lifted blacks, compressed range, grain at 100%.
Cool blue tint on shadows.

[CAMERA] Tracking dolly + locked. 35 mm equivalent. f/2.8.

[AUDIO] Urban ambient. Footstep foley sync to walk cadence. Trap-flavoured
beat enters at 2 s, mid-tempo. Audio mix lean.

[OUTPUT] 8 s, 9:16, 720p.
```

## Worked example — Editorial fashion film, 10 s

```
[HOOK 0–2 s]
Macro on flowing silk fabric — extreme close-up of fabric in slow-motion
ripple. Soft golden light tracks across surface. At 1.5 s rack out 50%
to reveal hem of dress on marble floor.

[ACTION 2–7 s]
Camera continues slow rack-out to reveal full model, standing centre-
frame in vast marble-floored gallery. Golden hour streams through tall
windows behind her — strong rim light haloes silhouette and dress.

3 s: model takes a single slow step forward. Dress flows in slow-motion
behind. Camera does subtle 5% push-in.

4–5 s: she turns slowly toward camera, hand brushing dress; rack focus
to her face.

5–7 s: full body reveal in 3/4 angle. Camera dollies right at 1 ft/s
around her in a 90° arc.

[CLIMAX 7–10 s]
Camera locks 3/4 hero framing. Model holds gaze on lens. Light
intensifies briefly (cloud passing). Dress drifts. Logo / collection
title fades in beside her at 8.5 s. Holds.

[STYLE] Editorial vogue feel. Sumptuous, slow.

[LIGHTING] Backlit golden hour + soft fill from front (white reflector
suggested). Rim haloes silhouette.

[GRADE] Warm nostalgia: 3200 K, lifted shadows, slight grain. Skin tone
priority.

[CAMERA] Slow rack-focus + 90° dolly arc + push-in. f/2.0. 50 mm portrait
lens equivalent.

[AUDIO] Soft string pad ambient. Subtle fabric foley. Single piano note
at 2 s, sustained. Mid-tempo cinematic strings build from 4 s. Resolves
on final beat.

[OUTPUT] 10 s, 16:9, 720p.
```

## Common pitfalls

- **Static garment + static model.** Always specify movement: wind, walk,
  turn, fabric flow.
- **Front-only angles.** A 3/4 angle reads as styled; pure front reads as
  catalogue.
- **Backdrop competing with outfit.** Pattern + pattern is busy. Pick
  contrast.
- **Generic music.** A great fashion clip with the wrong track is
  unwatchable. Either pair with a strong reference track or go silent +
  foley.
- **Overlit.** Fashion looks best in directional, often low-key lighting.
  Flat overhead = catalogue.


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
