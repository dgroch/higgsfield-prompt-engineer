# The 2-Second Hook Framework

The first two seconds determine whether a viewer keeps watching or scrolls
past. Every prompt should specify what happens in those two seconds with the
same precision as the rest of the clip.

## Why 2 seconds

Short-form platforms (TikTok, Reels, Shorts) measure completion rate from
frame zero. Drop-off in the first 2 s tanks algorithmic reach. Theatrical
cinema treats the same window differently — but even there, openings like
*Blade Runner 2049*'s neon eye, *Dunkirk*'s leaflet drop, or *1917*'s
sleeping soldiers earn attention in the same brief window.

Human pre-attentive processing operates around 200–500 ms. By 2 s, the
viewer has consciously decided whether to commit. Win that decision.

## Twelve generic hook patterns

Use these as a starting kit. Vertical-specific hooks (e.g. drone-swoop for
real estate) live in the matching skill.

| #   | Hook                              | Mechanism                              | Phrasing fragment |
| --- | --------------------------------- | -------------------------------------- | ----------------- |
| 1   | **Macro → wide reveal**           | Scale dissonance, then context         | "Open extreme macro of [detail]; at 0.5 s, whip cut to wide reveal of [landscape]." |
| 2   | **Black → light burst**           | Tension release                        | "Pure black 0–0.8 s. At 0.8 s explosive light burst from [direction]; lens flare blooms." |
| 3   | **Reverse motion**                | Unnatural = attention-grabbing         | "Action moves backward in first 2 s: [object] slides in reverse, smoke swirls counter-clockwise." |
| 4   | **Unexpected scale on familiar**  | Cognitive dissonance, lean-in          | "Macro of mundane object (fabric weave, raindrop, leaf vein); reads as vast landscape; viewer can't place scale." |
| 5   | **Silent → explosive sound**      | Audio contrast                         | "Complete silence 0–1.2 s. At 1.3 s sudden [gunshot/drop/slam] synced to visual cut." |
| 6   | **Color shift**                   | Palette punch                          | "Frame opens cool desaturated blue-grey. At 0.6 s sudden shift to saturated amber/neon." |
| 7   | **High-velocity entrance**        | Motion grabs peripheral vision         | "Subject enters from [edge] at high speed. Leading lines, motion blur, ~25 mph implied." |
| 8   | **Rack focus reveal**             | Focus pull = professional attention    | "Two planes sharp at 0 s. At 1 s rack to dramatic foreground, blurring background. f/1.4 equivalent." |
| 9   | **Geometric contrast**            | Compositional power                    | "Sharp horizontal vs vertical lines, or circles vs straight edges. High contrast lighting on geometry." |
| 10  | **Eyes open / lock-on**           | Primal attention trigger               | "Close shot of eyes in low-light. At 0.8 s eyes snap open / lock on camera. Pupil dilation optional." |
| 11  | **Rotation / vertigo**            | Sensory disorientation                 | "Camera tilts/rolls 45–180° in first 1.5 s. Tilted horizon. Stabilises level by 2 s." |
| 12  | **Scale impossibility**           | Awe or claustrophobia                  | "Tiny figure in vast landscape, OR giant object in confined space. Leading lines emphasise proportion." |

## Stacking hooks

For maximum impact, layer 2–3 techniques inside the same 2-second window.

- **Audio + visual + cognitive**: silent black (1) + sudden light burst with
  audio drop (2 + 5) = triple sensory engagement.
- **Primal + compositional**: eyes lock-on (10) + geometric contrast (9) +
  shallow depth of field.
- **Motion + scale**: high-velocity entrance (7) + scale impossibility (12).

## Specifying a hook in a prompt

Be precise about timing, intensity, and resolution:

```
[HOOK — 0 to 2 seconds]
Technique: black-to-burst, stacked with audio drop.
0–0.8 s:    pure black, complete silence. Sub-bass rumble building from
            −20 dB to −6 dB.
0.8 s:      explosive 5000 K light burst from frame-left corner; full mix
            arrives (music + SFX hit). Lens flare blooms.
0.8–2 s:    light settles into key position; viewer sees [first
            establishing detail]. Reverb tail of impact decays.
```

## Genre tendencies

| Vertical          | Strongest hooks (typical)              |
| ----------------- | --------------------------------------- |
| Cinematic         | 2 (black→light), 5 (silent→sound), 8 (rack focus) |
| 3D CGI            | 1 (macro→wide), 6 (color shift)        |
| Cartoon / anime   | 6 (color), 7 (velocity), 11 (rotation) |
| Comic-to-video    | 4 (scale), 6 (color), 11 (rotation)    |
| Fight scenes      | 5 (silent→sound), 7 (velocity), 10 (eyes) |
| Motion design ad  | 6 (color), 9 (geometric), 11 (rotation) |
| E-commerce        | 1 (macro→wide), 8 (rack focus)         |
| Anime action      | 5 (silent→sound), 7 (velocity), 10 (eyes) |
| Product 360       | 8 (rack focus), 9 (geometric)          |
| Music video       | 5 (silent→drop), 6 (color), 11 (rotation) |
| Social hook       | All 12 — this is its native habitat    |
| Brand story       | 4 (scale), 8 (rack focus), 10 (eyes)   |
| Fashion           | 6 (color), 7 (velocity), 8 (rack focus) |
| Food              | 4 (scale macro), 8 (rack focus)        |
| Real estate       | 1 (macro→wide), 12 (scale)             |
