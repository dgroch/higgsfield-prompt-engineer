# Lighting Library

Reusable lighting setups for Higgsfield Seedance 2.0 prompts. Each entry
covers mood, intensity ratio, color temperature, and prompt phrasing.

Color temperatures are given in Kelvin: lower = warmer (orange/red), higher =
cooler (blue). 2700–3200 K is incandescent / golden hour. 5500 K is daylight.
6500 K+ is overcast / moonlight / cool.

| Setup                          | Mood / Genre                                | Ratio (Key/Fill/Back) | Color Temp        | Prompt Phrasing |
| ------------------------------ | ------------------------------------------- | --------------------- | ----------------- | ---------------- |
| **Three-Point Classic**        | Universal, controlled, professional         | 100 / 33 / 60         | 3000 K key        | "Three-point: warm 3000 K key at 45° left; soft fill at 33% right; rim at 60% behind. Shadows soft, no hard edges." |
| **Chiaroscuro / Noir**         | Mystery, danger, psychological depth        | 100 / 10 / 40         | 3000 K            | "Hard 3000 K key at 45° left. Fill 10%; deep shadow occupies 85% of frame. Crushed blacks, film noir aesthetic." |
| **Silhouette Backlight**       | Mystery, power, separation                  | 0 / 0 / 100           | 5000 K back       | "Subject backlit by bright 5000 K source (window, fire, sunset). Zero fill. Subject as black shape; rim defines outline." |
| **Golden Hour**                | Romance, nostalgia, beauty, endings         | 100 / 50 / 60         | 3000–3500 K       | "Warm 3000 K directional at 15° low angle. Diffused atmospheric haze. Shadows have warm spill. Fill at 50%. Frame bathed in golden glow." |
| **Cool Moonlit**               | Isolation, mystery, dreamlike, night        | 100 cool / 20 / 30    | 6500 K            | "Directional cool 6500 K at 30° angle (moon position). Blue-tinted shadows. Fill 20%. Low overall intensity; eerie." |
| **Practical Neon / Cyberpunk** | Dystopian, sci-fi, modern danger            | Multi-source          | Mixed (cyan/pink) | "Visible neon sources in frame: hot-pink + cyan + acid-green spill. Multiple conflicting shadows. Optional flicker. Cool overall with neon accents." |
| **Soft Overcast**              | Calm, clarity, vulnerability, natural       | Flat 100 / 100        | 5500 K            | "Diffused omnidirectional daylight. Soft-edge shadows with 10 ft+ falloff. Even 5500 K across frame. No visible source." |
| **Volumetric / God Rays**      | Spirituality, magic, grandeur               | 100 directional       | 3000 K            | "3000 K directional through particle-filled atmosphere; visible light shafts. Dust motes in beams. Lens flare at source." |
| **Fluorescent / Institutional**| Clinical, dystopian, unease, soulless       | 100 flat / —          | 4500 K green-cast | "Cool slightly-green 4500 K overhead. Even, harsh. Optional 2–3 Hz flicker. No shadows; reveals everything without warmth." |
| **Firelight / Candlelit**      | Intimacy, danger, primal, vulnerability     | 100 flicker / —       | 1500–2000 K       | "Warm 1800 K from visible fire source. Flicker at 2–4 Hz. Large dancing shadows. Soft contrast, warm spill into shadows." |
| **Harsh Midday Sun**           | Heat, exposure, relentless                  | 100 / 10 / —          | 5500 K            | "Direct 5500 K at 60° angle. Contrast 10:1. Hard-edge shadows; minimal fill. Heat shimmer in air." |
| **Two-Source Split**           | Conflict, duality, sci-fi, modern drama     | 100 warm / 100 cool   | 3000 K vs 6000 K  | "Warm 3000 K key from left, cool 6000 K back from right (both 100%). Color temperature conflict on subject; opposite-color shadows." |
| **Low-Key Dramatic**           | Tension, mystery, suspense                  | 100 / 25 / 80         | 3000 K            | "Hard 3000 K key at 45° (100%). Fill 25%; most of face in shadow. Strong rim 80% separates from background. 60–70% frame shadow." |
| **High-Key Beauty**            | Optimism, safety, clarity, advertising      | 100 / 90 / 40         | 3500 K            | "Soft 3500 K key at 45° (100%). Fill 90% (1.1:1 ratio); shadows nearly absent. Rim 40%. Bright, optimistic, beautiful." |
| **Practical Tungsten Domestic**| Realism, intimacy, nostalgia                | 100 / ambient         | 2700 K            | "Visible warm 2700 K table lamp / ceiling fixture as primary source. Window ambient fill 25%. Lived-in, domestic, nostalgic." |

## Choosing by genre

| Genre                  | First-choice setups                                       |
| ---------------------- | --------------------------------------------------------- |
| Cinematic / film       | Three-point, Chiaroscuro, Golden Hour, Volumetric         |
| 3D CGI                 | Three-point, High-Key Beauty, Volumetric                  |
| Cartoon / anime        | High-Key Beauty, Two-Source Split                         |
| Action / fight         | Low-Key Dramatic, Practical Neon, Volumetric              |
| Horror / thriller      | Chiaroscuro, Cool Moonlit, Fluorescent, Firelight         |
| Product / e-commerce   | High-Key Beauty, Three-Point, Soft Overcast               |
| Fashion                | High-Key Beauty, Golden Hour, Three-Point                 |
| Food                   | Practical Tungsten Domestic, Golden Hour, Soft Overcast   |
| Real estate            | Soft Overcast, Golden Hour, Practical Tungsten            |
| Music video            | Practical Neon, Two-Source Split, Volumetric              |
| Brand story            | Golden Hour, Three-Point, Practical Tungsten              |

## Composition shorthand

- **Rule of thirds**: subject at one of four power points; horizon on top or
  bottom third line, never centre.
- **Leading lines**: roads, rails, shadows, architecture converge toward
  subject.
- **Negative space**: subject occupies 15–30% of frame; remainder is
  environment. Conveys isolation, scale.
- **Frame within frame**: doorway, window, branches form an inner border.
- **Symmetry**: balance, formality, divine. **Asymmetry**: tension, naturalism.
