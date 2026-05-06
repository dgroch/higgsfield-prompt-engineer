---
name: higgsfield-ecommerce-ad
description: Generate e-commerce product advertisement video prompts for Higgsfield Seedance 2.0. Use whenever the user wants product ads, e-commerce videos, product showcases, unboxing, product demos, shopping ads, fashion ads, beauty ads, food ads, or any commercial product video for online selling. Triggers on product ad, e-commerce, product showcase, Amazon video, Shopify ad, Instagram shop, TikTok shop, product commercial, fashion video, beauty ad, food ad, product demo, dropshipping video, or any product promotional request. Use even for "make a video for my product" or "product promo."
---

# E-Commerce Ad — Higgsfield Seedance 2.0

For physical-product video ads designed to convert: Amazon, Shopify,
Instagram Shop, TikTok Shop, DTC brands. The job is to make the product
desirable in 6–15 seconds, with the product unmistakeably visible.

## When to use

- Physical products: fashion, beauty, electronics, accessories, food,
  homewares.
- Hero shots, lifestyle shots, demo shots, before/after.
- Platforms: Amazon listing video, Shopify hero, Meta / TikTok ads.

For software / SaaS → `06-motion-design-ad`. For pure 360° turntable →
`09-product-360`. For viral hook focus → `11-social-hook`. For fashion
campaign → `13-fashion-lookbook`.

## What's unique to e-commerce

1. **The product is hero.** It must be on-screen, clearly identifiable,
   for at least 80% of the clip. Lifestyle context is a frame, not the
   subject.
2. **One feature per ad.** "Cushioned sole, breathable mesh, sustainable
   leather" is three ads, not one. Pick the strongest.
3. **Show benefit, not feature.** "Waterproof" is a feature; water beading
   off the surface is the benefit shown.
4. **Conversion language in the visuals.** Empty hand → product →
   satisfied user. The transaction is implied.
5. **Brand grade is non-negotiable.** Match the brand's existing visual
   identity — same palette, same lighting style.
6. **Mobile-first framing.** 9:16 vertical; product centred so it survives
   UI overlays on Reels / Shorts / TikTok.

## E-commerce hooks

| Hook                       | Phrasing |
| -------------------------- | -------- |
| **Macro reveal**           | "Extreme macro on product texture (fabric weave, leather grain, screen pixel). At 1 s rack out to full product." |
| **Pour / drop / unbox**    | "Product drops into frame from above with shallow-depth catch frame; settles at 1.5 s with subtle bounce." |
| **Hand presents**          | "Hand enters from frame-right holding product. At 1 s product is centred and lit. Hand exits at 2 s." |
| **Before / after**         | "Split frame: dull / problematic state left for 0–1 s, product solving it right from 1 s onward; wipe at 2 s." |
| **Lifestyle moment**       | "Subject mid-action with product (sip, run, type). Product is the pivot of the action." |

## References

- Camera (favour **Macro Push-In**, **360 Orbit**, **Rack Focus**):
  [shared/camera-movements.md](../../shared/camera-movements.md)
- Lighting (**High-Key Beauty**, **Soft Overcast**, **Three-Point**):
  [shared/lighting-library.md](../../shared/lighting-library.md)
- Grading (clean, brand-aligned)
- Hooks: [shared/hook-framework.md](../../shared/hook-framework.md)

## Worked example — Beauty product hero, 8 s

```
[HOOK 0–2 s]
Soft-focus pink gradient background. At 0.5 s a single drop of the
product (golden-amber serum) falls into frame from above in slow motion,
landing softly on a glass surface at 1.5 s — splash radiates outward in
slow-mo. Audio: subtle synth chime + soft impact.

[ACTION 2–6 s]
Camera slow rack-focus pulls back from the splash; product bottle
materialises in foreground (was out-of-focus). Bottle is centred, lit
with three-point high-key beauty lighting: warm 3500 K key at 45°,
strong fill at 90% (1.1:1), gentle rim at 40%. Specular highlights
travel across glass.

Camera does subtle 5% push-in over 3 s.

[CLIMAX 6–8 s]
Logo + tagline fade in beside bottle at 6.5 s. Single drop of serum
clings to dropper, catches a hero highlight. Holds. Final brand mark
appears at 7.5 s.

[STYLE] High-key beauty: bright, dreamy, 5% bloom on highlights.
Saturation 105%, restrained.

[CAMERA] f/2.0 shallow throughout. Locked rack-focus pull. 50 mm
equivalent.

[GRADE] Soft warm bias, lifted shadows, no true black. Skin-tone-safe
saturation curve.

[AUDIO] Soft pad ambient. Synth chime on hook. Subtle splash foley.
Single ascending two-note motif at 6.5 s when logo appears.

[OUTPUT] 8 s, 9:16, 720p.
```

## Worked example — Sneaker drop, 8 s

```
[HOOK 0–2 s]
Black frame. At 0.4 s sneaker drops in from above — frozen mid-air at
1 s in centre frame. Camera matches its rotation. Studio lighting comes
on at 1.5 s revealing colourway and silhouette.

[ACTION 2–6 s]
Camera orbits 270° around levitating sneaker over 4 s at constant 6 ft
distance. Sneaker slowly rotates counter-orbit so the lateral panel
stays toward camera. Highlights track across mesh, swoosh, sole. At 4 s
focus pull to sole tread; at 5 s to lacing detail; at 6 s back to full
silhouette.

[CLIMAX 6–8 s]
Sneaker descends slightly to surface, lands at 7 s with subtle bounce.
Brand wordmark types in below at 7.5 s. Drop date / CTA pulses subtly
at 8 s.

[STYLE] Studio black void with controlled spill. Sneaker is hero.

[LIGHTING] Three-point + edge kicker: 5500 K key at 45° upper-left;
fill 50% from below; cool 6500 K back rim; warm 3000 K accent kicker
on sole.

[GRADE] Slight teal-orange split: highlights warm, shadows cool 200°,
saturation 110%.

[AUDIO] Bass drop on hook landing. Sub-bass bed throughout. Sharp
"thunk" foley on landing at 7 s. Confident tagline VO optional at end
("Drop Friday").

[OUTPUT] 8 s, 9:16, 720p.
```

## Common pitfalls

- **Lifestyle-only framing.** Showing a smiling person without the
  product visible for 4 s defeats the purpose.
- **Generic music + product = stock.** Pair with brand-aligned audio or
  silence + foley.
- **Five features in 8 seconds.** Strip down. One product, one feature,
  one benefit.
- **16:9 for mobile platforms.** Default to 9:16 for IG / TikTok / Reels.
- **Cluttered hero shots.** The product should sit in 60–80% negative
  space when on-screen.


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
