# Color Grading Reference

Cinematic color grades with prompt phrasing. Use these to lock the visual
identity of a clip. The grade is the last 10% of the look but does 50% of the
emotional work.

| Grade                          | Visual Signature                                       | Mood                                | Prompt Phrasing |
| ------------------------------ | ------------------------------------------------------ | ----------------------------------- | ---------------- |
| **Teal & Orange**              | Cyan shadows, orange highlights, high saturation       | Modern action, blockbuster          | "Color grade: teal-orange. Shadows biased to cyan-teal (~200° hue), highlights to orange-gold (~30° hue). Midtones neutral. Saturation ~110%." |
| **Desaturated + Accent**       | 30% overall saturation; one color at 100%              | Symbolic focus, emotional intensity | "Reduce overall saturation to 30%. Maintain 100% saturation only on [accent color]. Viewer drawn to saturated element." |
| **Warm Nostalgia**             | 3200 K, warm highlights, warm shadows, soft saturation | Nostalgic, romantic                 | "Color temperature 3200 K. Highlights warm orange-gold; shadows warm orange-brown (not blue). Saturation +15% on warm tones." |
| **Cool Isolation**             | 6500 K+, blue shadows, slight desat                    | Loneliness, mystery, sci-fi         | "Color temperature 6500 K. Shadows biased blue-cyan; highlights retain mild warmth. Overall saturation 85%." |
| **Bleach Bypass**              | Lifted blacks, compressed range, heavy grain           | Vintage, gritty, tough              | "Bleach bypass: lift black point to ~10%. Greys elevated, contrast range compressed. Grain at 150% visibility. Analog film-stock feel." |
| **Vintage Film Stock**         | 70% saturation, lifted shadows, +200 K shift           | Nostalgia, classic, timeless        | "Vintage grade: saturation 70%. Lifted shadows; +200 K warm shift. Visible 35 mm grain. Faded, aged-photograph feel." |
| **High Contrast B&W**          | 0% saturation, crushed blacks, lifted whites           | Stark, dramatic, timeless           | "Pure B&W: 0% saturation. Crush blacks to true 0%, lift whites near max. S-curve gamma. Minimal mid-tones." |
| **Cyberpunk Neon**             | 140%+ saturation, split-toning, glow                   | Futuristic, dangerous, intense      | "Cyberpunk neon: saturation 140%. Vibrance +20%. Split-tone shadows cyan, highlights magenta-pink. Bloom on light sources." |
| **Monochromatic Single-Color** | 0% saturation except one hue at 100%                   | Symbolic, artistic, meditative      | "Monochromatic: convert to B&W; reintroduce only [hue] at 100% saturation in matching tonal areas." |
| **Warm/Cool Split**            | Foreground warm, background cool, extreme separation   | Conflict, duality, dreamlike        | "Split-temp grade: foreground 2700 K (orange spill), background 6500 K (blue-cyan). 4000 K separation creates striking contrast." |
| **Pixar / 3D Hero**            | Vivid, slightly stylised, lifted blacks                | Family, optimistic, playful         | "Pixar hero grade: lifted blacks (no true black), saturation +25%, slight magenta-tint highlights, hero-light wraparound on subject." |
| **Anime Cel Look**             | High saturation, hard edges, flat shading              | Stylised, animated, vibrant         | "Anime cel grade: saturation +30%. Hard cel-shading transitions (no soft gradients). Flat color blocks. Slight outline emphasis." |

## Pairing grades with lighting

| Lighting setup       | Strongest grade pairings                              |
| -------------------- | ------------------------------------------------------ |
| Three-Point Classic  | Teal & Orange, Vintage Film, Warm Nostalgia            |
| Chiaroscuro          | Bleach Bypass, High Contrast B&W                       |
| Golden Hour          | Warm Nostalgia, Vintage Film                           |
| Cool Moonlit         | Cool Isolation, Cyberpunk Neon                         |
| Practical Neon       | Cyberpunk Neon, Warm/Cool Split                        |
| Volumetric           | Teal & Orange, Warm Nostalgia                          |
| Soft Overcast        | Vintage Film, Cool Isolation, Monochromatic            |
| Firelight            | Warm Nostalgia, Bleach Bypass                          |

## Common mistakes

- **Stacking too many grades.** Pick one and commit; a "vintage cyberpunk
  noir" reads as muddy, not stylised.
- **Saturation over 150%** on skin tones — looks unnatural and dates fast.
- **True black + true white in the same grade** without intermediate values
  produces a "video" look, not a "film" look.
- **Forgetting to grade reference materials.** If you supply `@image1` as a
  style ref, its grade leaks into output. Pick references whose grade you
  want.
