---
name: higgsfield-3d-cgi
description: Generate 3D CGI and rendered video prompts for Higgsfield Seedance 2.0. Use whenever the user wants 3D rendered, CGI, Pixar-style, Unreal Engine, photorealistic 3D, computer-generated, or digitally rendered video. Triggers on 3D animation, CGI, rendered, Blender, Unreal Engine, octane, ray tracing, volumetric, subsurface scattering, PBR, isometric, low-poly, Pixar, DreamWorks, or any 3D/CG video request. Use even when the user says "make it look 3D" or describes a rendered aesthetic.
---

# 3D CGI — Higgsfield Seedance 2.0

For prompts that should read as 3D-rendered output: Pixar/DreamWorks
character animation, Unreal-Engine cinematic, Octane/Blender architectural
renders, low-poly stylised, isometric, photoreal CGI.

## When to use

- "Pixar-style", "Unreal Engine cinematic", "Octane render", "Blender render."
- "Photoreal but obviously 3D" — product visualisations, architectural fly-throughs.
- "Low-poly", "isometric", "voxel", "claymation."
- VFX-heavy concepts (physics simulations, particle systems, fluid dynamics).

If the user wants flat/cel-shaded 2D animation → `03-cartoon`. Anime →
`08-anime-action`. Live-action film look → `01-cinematic`.

## What's unique to 3D CGI

1. **Render pedigree matters.** Naming a renderer (Octane, Redshift, Unreal,
   Arnold) anchors the look. Naming a studio (Pixar, ILM, Weta) anchors
   character / story sensibility.
2. **Materials carry the realism.** PBR (physically based rendering),
   subsurface scattering on skin, refraction through glass, anisotropic
   highlights on metal — these are the cues that separate "video that
   looks 3D" from "amateur render."
3. **Lighting is global.** HDRi-style ambient + key + bounce. Hard direct
   shadows give it away as render; physically plausible bounce light gives
   it polish.
4. **Camera moves can be impossible.** Use moves that real cameras can't
   do: through-walls, inside objects, micro-scale, atomic-scale.
5. **Frame rate / motion blur.** 24 fps with motion blur reads cinematic;
   60 fps no-blur reads game engine.

## CGI-specific hooks

| Hook                       | Phrasing |
| -------------------------- | -------- |
| **Material macro reveal**  | "Open extreme macro on a single PBR surface (brushed metal, woven fabric). Light moves across, revealing micro-scale detail. Rack out at 1.5 s." |
| **Impossible camera**      | "Camera passes through solid wall / inside object / through keyhole in 0–2 s." |
| **Rig-style spin reveal**  | "Subject rotates 360° in studio void on invisible turntable. Three-point CGI lighting. At 2 s background fades in around it." |
| **Particle storm**         | "Frame fills with simulated particles (sparks, snow, leaves). Camera pushes through; particles part to reveal subject at 2 s." |
| **Wireframe → render**     | "Open in wireframe / clay shading. At 1 s materials and lighting cascade in shot-by-shot until full render at 2 s." |

## References

- Camera language (use **Push-In + Zoom**, **Spiral**, **360 Orbit**):
  [shared/camera-movements.md](../../shared/camera-movements.md)
- Lighting (favour Three-Point, High-Key Beauty, Volumetric):
  [shared/lighting-library.md](../../shared/lighting-library.md)
- Grading (favour Teal & Orange, Pixar Hero):
  [shared/color-grading.md](../../shared/color-grading.md)

## Worked example — Photoreal product render, 6 s

```
[HOOK 0–2 s]
Black void. At 0.6 s spotlight punches in from above; reveals a single
chrome smartwatch suspended mid-air. Hard specular highlight tracks
across brushed-titanium case. Sub-bass swell.

[ACTION 2–5 s]
Camera orbits 270° clockwise at 8 ft constant distance over 3 s. Watch
rotates counter-orbit, so the face stays toward camera. Sapphire crystal
catches anisotropic flare at 3 s. Subsurface translucency on rubber
strap visible against backlight.

[CLIMAX 5–6 s]
Camera locks centre-front. Display lights up: clean UI animates in.

[LIGHTING] Studio three-point: 5500 K key 100% at 45° upper-left, fill
30% from below (kicker), back rim 80% at 6500 K. HDRi-style soft ambient
bounce.

[GRADE] Teal & Orange, restrained: highlights warm 30°, shadows cool
200°. Saturation 105%.

[CAMERA] f/2.8. Constant orbit speed 90°/s. Locked focus on watch face.

[OUTPUT] 6 s, 16:9, 720p.
```

## Worked example — Pixar-style character moment, 10 s

```
[HOOK 0–2 s]
Macro on a tiny robot's eye iris (cel-style aperture mechanism inside).
At 1 s iris dilates; pulls back to reveal full robot character standing
in a sunlit kitchen.

[ESTABLISH 2–4 s]
Pixar-style stylised kitchen, golden hour streaming through window.
Bright high-key lighting, soft wraparound on character. Saturated but
not gaudy.

[ACTION 4–8 s]
Robot lifts a comically oversized teacup with both hands. Camera dollies
forward 2 ft at 1.5 ft/s, slight low angle for hero feel. Robot's
expression shifts: focused → surprised → delighted as steam rises.

[CLIMAX 8–10 s]
Robot sips. Eye-shapes squint into a smile. Camera pulls back into wide
hero shot.

[GRADE] Pixar hero: lifted blacks (no true black), saturation +25%, soft
magenta highlights, hero-light wraparound.

[AUDIO] Soft kitchen ambient. Foley: ceramic clink at 5.5 s, sip slurp
at 8.5 s. Light orchestral cue swells from 6 s, peaks at 9 s.

[OUTPUT] 10 s, 16:9, 720p.
```

## Common pitfalls

- **Mixing renderers.** "Octane meets Pixar meets Unreal" produces
  incoherent output. Pick one renderer aesthetic.
- **Static character poses.** 3D characters need micro-motion (breath,
  blink, weight shift) or they read as mannequins.
- **No bounce light.** Single-source CGI looks like a 1998 video game.
- **Forgetting subsurface scattering** on skin / wax / fabric / fruit —
  the most common "tell" of weak CGI.


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
