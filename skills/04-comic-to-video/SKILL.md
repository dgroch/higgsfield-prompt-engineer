---
name: higgsfield-comic-to-video
description: Convert comic book panels, manga pages, webtoons, and illustrated storyboards into animated video using Higgsfield Seedance 2.0. Use whenever the user wants to animate comics, bring illustrations to life, convert manga to video, animate storyboards, or create motion from sequential art. Triggers on comic to video, manga animation, panel animation, storyboard to video, webtoon animation, comic book motion, sequential art, graphic novel animation, or any illustrate-to-animate request. Use even when user says "make this drawing move" or "animate this page."
---

# Comic-to-Video — Higgsfield Seedance 2.0

For animating static sequential art: comic book panels, manga pages,
webtoons, storyboards, illustrated novels. The challenge is honouring the
source illustration's style while introducing motion that feels native to
animation, not "Photoshop puppet warp."

## When to use

- User uploads comic / manga / illustration as `@image1` and asks for
  motion.
- "Animate this panel / page / storyboard."
- Webtoon scrolling content.
- Graphic novel adaptation, motion comics.
- Storyboard previz.

For pure 2D animation from scratch (no source illustration) → `03-cartoon`.
For anime aesthetics → `08-anime-action`.

## What's unique to comic-to-video

1. **Source illustration is the style anchor.** `@image1` defines line
   weight, palette, shading style. Specify "preserve original ink line",
   "preserve flat colour blocks", etc.
2. **Motion is selective.** Don't animate everything. Pick 1–3 elements:
   character eye-blink, hair movement, smoke, cape, weapon. The frozen
   parts make the motion feel alive.
3. **Camera moves on the panel.** Often the most effective animation is
   *no character motion* — just slow push-in or parallax across a static
   panel, like Ken Burns for comics.
4. **Panel transitions are dramatic.** Whip pan, page turn, ink-wipe,
   speed-line wipe. Use the comic's own visual grammar.
5. **Speech bubbles / SFX text.** Decide whether to animate them in (typed,
   bounced) or omit entirely. Don't half-include them.

## Comic-specific hooks

| Hook                          | Phrasing |
| ----------------------------- | -------- |
| **Panel iris-in**             | "Black frame with single panel iris opening at centre over 1 s. Reveals first panel of @image1." |
| **Hand turns page**           | "Frame opens with animated hand pulling page edge from frame-right; page peels back revealing @image1." |
| **Ink lines draw in**         | "Frame starts blank. Ink lines from @image1 draw themselves over 0–1.5 s. Colours flood in at 1.5 s." |
| **Speed-line burst**          | "Frame fills with manga-style speed lines radiating from centre. At 1 s lines clear to reveal @image1's hero pose." |
| **Multi-panel flash**         | "Three panels of @image1 flash in sequence (0.3 s each) before settling on the chosen panel at 2 s." |

## References

- Source: always use `@image1` (and `@image2`, `@image3` for multi-panel)
- Motion: keep it minimal — see [shared/camera-movements.md](../../shared/camera-movements.md),
  prefer **Push-In + Reveal**, **Parallax Pan**, **Lock-Off**, **Whip Pan**
- Hooks: [shared/hook-framework.md](../../shared/hook-framework.md)
- Sound: [shared/sound-design.md](../../shared/sound-design.md)

## Worked example — Manga panel come-to-life, 6 s

```
[HOOK 0–2 s]
Black frame with single white speed-burst at centre. Speed lines fill
frame at 0.5 s in classic manga ink style. At 1.5 s lines clear to
reveal @image1 (the manga panel) in full. SFX: whoosh + sharp drum hit
synced to reveal.

[ACTION 2–5 s]
Source-faithful animation of @image1: preserve all ink lines and flat
colour blocks. Animate only:
- Character's hair drifts in 2 Hz wind motion
- Cape edge ripples on twos (12 fps stepped)
- Eye blink at 3.5 s
- Sparkle particles drift across background

Camera holds locked on @image1 with slow 5% push-in over 3 s.

[CLIMAX 5–6 s]
Speed lines burst in from edges; whip-pan exit at 6 s. Last frame holds
on character's eyes.

[STYLE] Preserve @image1's exact line weight, ink density, screentone
patterns. No new shading, no gradient. Strictly cel transitions only.

[AUDIO] Wind ambient at −6 dB. Drum impact on hook reveal. Light cape
flap foley at 2.5 s. Sustained synth tone from 3 s. Whip-pan SFX at 6 s.

[OUTPUT] 6 s, 9:16 (manga reads vertical), 720p.
```

## Worked example — Webtoon scrolling reveal, 10 s

```
[HOOK 0–2 s]
@image1 starts at top of vertical 9:16 frame, only top 30% visible.
Camera scrolls down at 0.5 frames/sec — mimics finger-scroll on phone.
By 2 s the first panel boundary scrolls into view.

[ACTION 2–8 s]
Continuous downward scroll across @image1, @image2, @image3 stitched
vertically (the webtoon's natural reading flow). Speed varies:
- 2–4 s: faster scroll, exposition panels
- 4–6 s: slow at dramatic panel; lingering
- 6–8 s: speed-up into action panel

Within each panel, minimal motion: a wisp of hair, a tear forming, smoke
drifting. Foreground character elements only — backgrounds stay static.

[CLIMAX 8–10 s]
Scroll halts on final panel. 10% slow push-in. Single visual element
(eyes, weapon, tear) animates into close-up.

[STYLE] Preserve webtoon line weight and flat-color shading. No new
elements introduced.

[AUDIO] Soft ambient pad throughout. Page-flip SFX at each panel
transition. Emotional piano arrives at 6 s, peaks at 9 s.

[OUTPUT] 10 s, 9:16, 720p.
```

## Common pitfalls

- **Animating everything.** Reads as cheap puppet-warp. Pick 1–3 motion
  elements, freeze the rest.
- **Adding shading the source doesn't have.** If `@image1` is flat-color,
  don't render with new gradients. Match its rendering.
- **Aspect mismatch.** Webtoons are vertical (9:16). Manga panels are
  often square or wider. Match output ratio to source.
- **Forcing dialogue.** Sequential art has speech bubbles, not voiceover.
  Add VO only if explicitly requested.
