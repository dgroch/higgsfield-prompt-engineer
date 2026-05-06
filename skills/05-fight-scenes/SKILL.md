---
name: higgsfield-fight-scenes
description: Generate intense fight scene and action sequence video prompts for Higgsfield Seedance 2.0. Use whenever the user wants fight scenes, combat, martial arts, battles, action choreography, sword fights, hand-to-hand combat, chase scenes, or superhero action. Triggers on fight, combat, battle, martial arts, action scene, choreography, duel, sword fight, kung fu, chase, brawl, punch, kick, weapon combat, superhero fight, parkour, or any action/fight request. Use even for "intense action video" or "epic battle."
---

# Fight Scenes — Higgsfield Seedance 2.0

For action choreography: martial arts, sword fights, gunplay, chase
sequences, superhero combat, parkour. Demands tight rhythmic structure
between strikes, camera, and audio.

## When to use

- Any combat scenario: martial arts, sword, gun, magic.
- Chase sequences (foot, vehicle, parkour).
- Superhero clashes.
- Sport-adjacent: boxing, MMA, wrestling.

For animated anime fights specifically → `08-anime-action`. For
choreographed dance → use `10-music-video`.

## What's unique to fight choreography

1. **Beats, not seconds.** A fight is structured in *strikes*: anticipation
   → impact → recovery. Each strike takes 0.4–0.8 s. Specify per strike.
2. **The 180° rule (or break it deliberately).** Camera stays on one side
   of the action axis or chaos breaks. Most amateur action prompts have
   the model crossing the line accidentally.
3. **Stillness amplifies impact.** A frozen beat *before* a strike makes
   the strike land. A frozen beat *after* lets the audience feel the
   damage.
4. **Hits sync to audio.** Every contact = audio impact (+2 dB). Without
   this, fights read as flailing.
5. **Camera shake on impact.** Subtle (3–5 px) for hits, heavy
   (10–15 px) for explosions. Don't over-shake or it reads as a phone
   video.

## Fight-specific hooks

| Hook                       | Phrasing |
| -------------------------- | -------- |
| **Pre-strike stillness**   | "Two combatants frozen mid-stance, eyes locked, 0–1.5 s. At 1.5 s simultaneous explosive movement; both lunge." |
| **Weapon draw**            | "Macro on weapon at hip / sheath. At 1 s draw begins; blade emerges in slow-mo. Audio: scrape of steel." |
| **Match-cut on impact**    | "Cut from one fight to another on the moment of impact; same body position, different opponents." |
| **Slow-mo into real-time** | "First strike at 0.25× speed (0–1.5 s). Snap to 1× speed at moment of impact at 1.5 s." |
| **POV strike incoming**    | "Subjective camera. Opponent's fist swings into lens; impact frame at 1.8 s with hit-flash." |

## References

- Camera (use **Whip Pan**, **Handheld**, **Push-In + Zoom**, **Tracking**):
  [shared/camera-movements.md](../../shared/camera-movements.md)
- Lighting (favour Low-Key Dramatic, Practical Neon, Volumetric):
  [shared/lighting-library.md](../../shared/lighting-library.md)
- Sound (impacts on every contact!): [shared/sound-design.md](../../shared/sound-design.md)
- Pacing: [shared/timeline-structures.md](../../shared/timeline-structures.md)

## Worked example — Sword duel, 8 s

```
[HOOK 0–2 s]
Two samurai frozen mid-stance, blades raised, in foggy bamboo grove.
Cool 6500 K rim light from behind both. Complete silence except wind
through bamboo. At 1.8 s simultaneous lunge — both step forward.

[ACTION 2–7 s]
Strike beats, 0.6 s each:
- 2.0–2.6 s: blades clash centre-frame; sparks. Camera shakes 5 px.
  Audio: steel-on-steel impact +2 dB.
- 2.6–3.2 s: parry left; blade slides off blade. Both step right.
- 3.2–3.8 s: counter-strike; samurai-A blocks high. Sparks.
- 3.8–5 s: locked blades, 1.2 s slow push-in to faces eye-to-eye.
- 5–5.6 s: samurai-B feints, breaks lock, strikes low.
- 5.6–6.2 s: samurai-A leaps back; lands at frame-edge.
- 6.2–7 s: final stillness. Both panting, breath visible in cold air.

Camera throughout: handheld 1 mm jitter, follows action with whip-pans
between strikes. 35 mm equivalent. Stays on the right side of the
180° axis.

[CLIMAX 7–8 s]
Slow push-in on samurai-A's eyes — narrowed, focused. Cuts to black.

[LIGHTING] Low-key dramatic: cool 6500 K rim from above-back; minimal
fill. Volumetric god rays through bamboo. 70% frame in shadow.

[GRADE] Bleach bypass: lifted blacks, compressed range, 35 mm grain.
Cool blue tint.

[AUDIO] Wind-through-bamboo ambient at −5 dB throughout. Silence
0–1.8 s. Steel impacts +2 dB at every clash. Breath foley at 6.5 s.
Single drum hit at 7 s under the push-in.

[OUTPUT] 8 s, 16:9, 720p.
```

## Worked example — Hand-to-hand POV, 6 s

```
[HOOK 0–2 s]
First-person POV, eye-level. Opponent steps into frame from far right,
fast. At 1.5 s opponent throws first punch — fist swings toward camera.
Impact frame at 1.8 s with white hit-flash + heavy bass thud. Camera
jolts 12 px right.

[ACTION 2–5 s]
Camera stabilises, recovers. 2.5 s: subjective return punch — fist
extends from bottom-right of frame into opponent's jaw. Hit-flash, bass
thud. Camera shakes 8 px.
3 s: opponent staggers back. POV pans left.
3.5 s: opponent lunges with kick toward camera. Camera ducks (frame
drops 30%) at 4 s.
4–5 s: rising counter — POV fist arcs upward into opponent's chin.

[CLIMAX 5–6 s]
Opponent falls back into slow motion (0.25× speed). Camera holds.

[LIGHTING] Practical neon: cyan + magenta from off-frame sources.
Multiple conflicting shadows. Hard.

[CAMERA] Handheld POV, 35 mm wide. Heavy on impacts (8–12 px shake);
recovers between hits.

[AUDIO] Urban night ambient. Heavy bass thud on every impact +3 dB.
Breath foley throughout (own panting). Crowd murmur at −10 dB. Sub-bass
sweep on the slow-mo finale.

[OUTPUT] 6 s, 16:9, 720p.
```

## Common pitfalls

- **Crossing the 180° line.** Specify "camera stays on right side of action
  axis throughout" or expect spatial confusion.
- **Continuous motion.** Real fights have stillness beats; AI-generated
  fights without them feel like flailing.
- **No impact audio.** Without synced impact sound, every strike feels
  weightless.
- **Over-shaking the camera.** Reads as amateur. Calibrate shake to hit
  intensity, don't apply it constantly.
- **Forgetting injury / recovery.** Combatants who never react to hits
  read as video-game NPCs.


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
