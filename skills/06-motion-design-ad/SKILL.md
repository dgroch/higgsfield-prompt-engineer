---
name: higgsfield-motion-design-ad
description: Generate motion design advertisement video prompts for software, SaaS, and tech products using Higgsfield Seedance 2.0. Use whenever the user wants to create a software product ad, SaaS promo, app launch video, tech demo, UI showcase, startup video, or motion graphics for a tech company. Triggers on software ad, SaaS video, product launch, app promo, tech commercial, UI animation, motion design ad, startup video, product demo video, feature showcase, or any software/tech promotional video. Use even for "make a video for my app" or "promo for our platform."
---

# Motion Design Ad — Higgsfield Seedance 2.0

For software / SaaS / tech product videos: app launches, feature
showcases, dashboards animating, UI walkthroughs, tech-startup brand ads.
Distinct from general e-commerce (`07-ecommerce-ad`) which is for
physical products.

## When to use

- App launches, SaaS feature reveals.
- Dashboard / UI showcase videos.
- Developer tools, API demos.
- Tech-startup brand ads (Linear, Vercel, Stripe aesthetic).
- Apple-keynote-style product reveals.

For physical products → `07-ecommerce-ad`. For viral hooks specifically →
`11-social-hook`.

## What's unique to motion design

1. **Vector-friendly aesthetics.** UI, icons, geometric shapes. Avoid
   skeuomorphism unless explicitly requested.
2. **Restrained palette.** 2–4 brand colors + neutral. The brand's color
   is the visual identity.
3. **Easing functions matter.** "Ease-in-out cubic" reads pro. "Linear"
   reads cheap. Specify easing on every motion.
4. **Hierarchy through motion.** Headline animates first, supporting
   elements after. Not all at once.
5. **Show the product doing something.** A static UI screen for 5 s is
   weak. A cursor clicking, data flowing, a state-change animating — that
   sells.
6. **Negative space sells confidence.** Apple keynote, Linear, Stripe —
   they all use generous empty space. Don't fill the frame.

## Motion-design hooks

| Hook                       | Phrasing |
| -------------------------- | -------- |
| **Logo lockup reveal**     | "Logo elements assemble from off-frame; mark + wordmark click into place at 1.5 s with subtle stinger SFX." |
| **UI element drop-in**     | "Empty white frame. UI cards drop in from above with ease-out-cubic, stagger 0.1 s between each." |
| **Cursor demo entrance**   | "Cursor enters from right, hovers over CTA at 1 s, click ripple at 1.5 s, dashboard data animates in at 2 s." |
| **Data viz reveal**        | "Empty chart axes draw in 0–1 s. At 1 s data series animates from left to right with ease-out." |
| **Geometric pattern**      | "Geometric brand pattern morphs / reflows; settles into product silhouette at 2 s." |

## References

- Camera (mostly **Lock-Off** with subtle dolly):
  [shared/camera-movements.md](../../shared/camera-movements.md)
- Lighting (**High-Key Beauty**, **Three-Point**):
  [shared/lighting-library.md](../../shared/lighting-library.md)
- Grading (clean, restrained — pick one brand-aligned grade)
- Sound (clean, sparse, subtle stingers): [shared/sound-design.md](../../shared/sound-design.md)

## Worked example — SaaS dashboard reveal, 8 s

```
[HOOK 0–2 s]
Pure white frame. At 0.3 s a single cursor enters from frame-right,
travels left with ease-in-out. At 1 s cursor hovers over a CTA button
that materialises beneath it (ease-out-cubic). At 1.5 s click ripple +
soft "tick" SFX. At 2 s dashboard frame begins to assemble.

[ACTION 2–6 s]
Dashboard cards drop in with 0.15 s stagger, each ease-out-cubic from
above. Order:
- 2.0–2.4 s: top metric card (large number animates 0 → final value)
- 2.4–2.8 s: chart area (axes draw, then bars rise left-to-right)
- 2.8–3.2 s: side panel (list items slide in)
- 3.2–4 s: secondary metrics ripple in
- 4–6 s: live state — chart pulses, numbers tick up, cursor moves.

[CLIMAX 6–8 s]
Camera does subtle 5% push-in toward chart area as a peak metric ticks
upward and highlights amber. Holds. Tagline fades in below at 7 s.

[STYLE] Flat / minimal. Brand palette: deep navy (#0B1F3A), soft white,
single accent amber (#F2A341). Inter / SF Pro typography. Generous
whitespace.

[CAMERA] Locked frame, 16:9, mostly static. Subtle 5% push-in on climax.

[GRADE] Clean: high-key, slightly cool 6000 K bias, no grain.

[AUDIO] No ambient. Soft "tick" foley on each cursor click and card
drop. Single ascending two-note motif at 6 s. No music; cleanliness is
the brand.

[OUTPUT] 8 s, 16:9, 720p.
```

## Worked example — Apple-keynote product reveal, 10 s

```
[HOOK 0–2 s]
Pure black frame. At 0.5 s soft spotlight pools at frame-centre. Subtle
glint at 1 s. At 1.8 s product silhouette materialises in spotlight
(matte black device against black background; only edges + surface
highlights visible).

[ACTION 2–7 s]
Camera slow orbits 90° clockwise at 8 ft distance over 4 s. Studio
three-point lighting: hard 5500 K key from above-left, cool 6500 K back
rim, fill from below at 30%. Subsurface highlights track across
brushed-aluminium edges. At 5 s display turns on — minimal UI, brand
color glow.

[CLIMAX 7–10 s]
Camera locks frame-front. Subtle parallax background — soft gradient
shifts. Tagline types in below at 8 s. Logo wordmark fades in at 9 s.
Holds.

[STYLE] Cinematic product photography. Black-on-black with controlled
specular. Brand palette: matte black, cool white, accent only on
display.

[GRADE] Restrained teal-orange: highlights warm, shadows cool, mid
neutral. Saturation 95%. Slight bloom on display.

[AUDIO] Sub-bass swell from 0–2 s, peaks at hook reveal. Single soft
chime at 5 s when display lights. Restrained ambient bed throughout.
Tagline VO optional, calm-confident delivery.

[OUTPUT] 10 s, 16:9, 720p.
```

## Common pitfalls

- **Too many UI elements.** A keynote-grade ad shows *one* feature in 8 s.
  Trying to show five reads as TV-shopping channel.
- **Linear motion / no easing.** Specify ease curves explicitly.
- **Generic stock music.** Sparse, branded audio (one stinger + ambient)
  out-classes uplifting royalty-free score every time.
- **Forgetting the cursor / interaction.** Software is interactive; show
  it being used.
- **Skeuomorphic 3D when flat reads better.** Default to flat unless the
  brand is explicitly photoreal.
