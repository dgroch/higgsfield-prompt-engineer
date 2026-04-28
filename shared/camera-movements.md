# Camera Movement Reference

Reusable camera movement vocabulary with prompt phrasing tuned for Higgsfield
Seedance 2.0. Each entry gives the cinema purpose, typical duration, and a
copy-pasteable phrasing fragment.

Numeric specifics (feet/second, degrees/second, focal lengths) are starting
points that should be tightened against real Higgsfield generations. Items
flagged `[unverified]` have not yet been empirically tested.

| Movement              | Purpose                                                | Typical | Prompt Phrasing |
| --------------------- | ------------------------------------------------------ | ------- | ---------------- |
| **Dolly Forward**     | Build intimacy, draw viewer in                         | 1–3 s   | "Camera dollies forward at constant 2 ft/s. Subject stays centre-frame. Sharpness maintained throughout, no focus breathing." |
| **Dolly Backward**    | Reveal context, expand environment                     | 1–4 s   | "Camera pulls back 15 ft over 3 s. Subject anchored centre-frame. Background reveals progressively. Anticipatory tension." |
| **Truck Left/Right**  | Lateral move, parallax-driven environment reveal       | 2–4 s   | "Camera trucks left 10 ft at 2 ft/s. Subject holds frame-right. Foreground parallaxes faster than background." |
| **Pan**               | Horizontal rotation in place                           | 0.5–2 s | "Camera pans left across scene at 30°/s. Smooth ease-in/ease-out. Sweeps 60° total field, settles on secondary subject." |
| **Tilt Up/Down**      | Vertical rotation, scale or emotion reveal             | 1–3 s   | "Camera tilts upward from feet to face at 20°/s. Decelerates at end. Reveals vertical scale." |
| **Whip Pan**          | Energetic transition, hide a cut                       | 0.3–0.6 | "Whip pan A→B in 0.5 s at ~90°/s. Motion blur acceptable. No pause; smooth deceleration." |
| **Handheld**          | Documentary feel, urgency, human presence              | 2–6 s   | "Handheld follow with 0.5–1 mm jitter at ~2 Hz. Subtle breathing motion. Not locked-off." |
| **Steadicam / Gimbal**| Smooth flowing motion, controlled professional feel    | 3–8 s   | "Gimbal-smooth follow at 3 ft distance. Vibrations removed; motion is liquid. Optional micro-breathing." |
| **Tracking / Side**   | Subject moves through environment                      | 3–6 s   | "Camera tracks subject from 4 ft side distance. Subject frame-right, environment frame-left. Sync to walking pace." |
| **Crane Up**          | Establish scale, transition to wide                    | 3–6 s   | "Camera rises 30 ft over 4 s. Tilts down slightly to keep subject visible. Landscape reveals as crane rises." |
| **Crane Down**        | Intimate approach from overview                        | 2–4 s   | "Camera descends 20 ft over 3 s. Starts overhead, ends at eye level. Tilts up during descent." |
| **360 Orbit**         | Show subject from all angles                           | 4–8 s   | "Camera orbits 270° counterclockwise around subject over 5 s at constant 8 ft distance. Subject locked centre-frame." |
| **Spiral**            | Orbit + rise/descend, dreamlike                        | 4–8 s   | "Camera spirals up + around: rise 15 ft, orbit 180°, both over 5 s. Hypnotic, complex." |
| **Rack Focus**        | Guide attention via focus, not movement                | 0.5–2 s | "Rack focus from foreground (2 ft) to background (25 ft) over 1.5 s. Mid-field blurs during transition." |
| **Dutch Angle**       | Unease, psychological tension                          | 3–8 s   | "Frame tilted 20° counterclockwise. Diagonal horizon. Hold tilt for full clip duration." |
| **Push-In + Zoom**    | Vertigo / Hitchcock zoom, intense focus                | 2–4 s   | "Simultaneous dolly forward 5 ft and zoom to 85 mm equivalent over 3 s. Background compresses; subject magnifies." |
| **Parallax Pan**      | Depth via differential layer movement                  | 2–4 s   | "Pan left 20° over 3 s. Foreground full pan amount, midground 65%, background 35%." |
| **Push-In + Reveal**  | Forward motion uncovers hidden subject                 | 2–4 s   | "Dolly forward 10 ft at 3 ft/s. Foreground element gradually reveals (or obscures) background subject." |
| **Match Cut Whip**    | Invisible scene transition through motion blur         | 0.4–0.7 | "Whip blur transition A→B. Subject A exits left with blur, B enters right simultaneously. Cut hidden in motion." |
| **Lock-Off Static**   | Observation, allow action through frame                | 2–6 s   | "Camera locked, zero movement. Subject moves through frame. Quiet, observational." |
| **Reverse Parallax**  | Background moves faster than foreground (impossible)   | 3–5 s   | "Pan right 30°. Foreground 20% of pan amount, background 100%. Reverses normal spatial logic; dreamlike." |
| **POV / First Person**| Empathy, immersion                                     | 2–6 s   | "Eye-level camera, moves as if subject walking. Slight head-bob jitter. Frame matches their gaze direction." |
| **Bird's Eye**        | God-perspective, layout reveal                         | 2–5 s   | "Camera directly above, 15 ft up, 0° angle. Looks straight down. Reveals spatial layout." |
| **Over the Shoulder** | Spatial relationship between two subjects              | 2–4 s   | "OTS framing: camera 2 ft behind near-character. Partial shoulder/head frame-left, subject frame-right. Soft focus on near shoulder." |

## Stacking moves

Combine 2–3 moves within a single 8–15 s prompt for sophisticated sequences.

- **Reveal arc**: dolly forward (0–2 s) → whip pan (2–2.3 s) → tracking (2.3–5 s)
- **Scale arc**: lock-off (0–2 s) → crane up (2–6 s) → tilt down (6–8 s)
- **Tension arc**: handheld (0–3 s) → push-in + zoom (3–5 s) → dutch hold (5–8 s)

Specify each move with its time window so Seedance can sequence them.

## Lens / focal length cheat sheet

| Equivalent | Use                                                  |
| ---------- | ---------------------------------------------------- |
| 14–24 mm   | Ultra-wide, environmental, slight distortion         |
| 24–35 mm   | Wide establishing, documentary feel                  |
| 35–50 mm   | Standard, natural perspective                        |
| 50–85 mm   | Portrait / dialogue, mild compression                |
| 85–135 mm  | Beauty, isolation, strong compression                |
| 135 mm+    | Telephoto, extreme compression, sports / action      |

## Depth-of-field cheat sheet

| Aperture | Effect                                                |
| -------- | ----------------------------------------------------- |
| f/1.4    | Extreme shallow, dreamy, isolates subject             |
| f/2.0    | Cinematic shallow, classic look                       |
| f/2.8    | Moderate shallow, professional standard               |
| f/4–f/5.6| Balanced, environmental context visible               |
| f/8+     | Deep focus, all planes sharp, documentary             |
