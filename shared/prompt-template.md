# Master Prompt Template

The skeleton every Higgsfield Seedance 2.0 prompt should follow. Each
section is optional, but keeping the order is what helps the model produce
consistent, high-fidelity output.

```
[OPENING HOOK — 0 to 2 seconds]
Technique:        <hook from shared/hook-framework.md>
Sensory trigger:  <what specifically the viewer sees / hears>
Transition:       <how the hook resolves into the main scene at 2 s>

[ESTABLISHING — 2 to ~4.5 seconds]
Location:         <geography, architecture, atmosphere>
Time of day:      <golden hour / midday / blue hour / night>
Weather / mood:   <fog, rain, dust, calm>
Lighting setup:   <from shared/lighting-library.md>
Color grade:      <from shared/color-grading.md>

[PRIMARY ACTION — main body]
Camera move:      <from shared/camera-movements.md, with timing>
Subject action:   <what the protagonist or focal element does>
Emotional arc:    <tension point, decision moment, reveal>
Audio integration: <ambient / score / dialogue / SFX cues>
Beats:            <beginning → middle → climax → resolution>

[DEPTH & COMPOSITION]
Foreground:       <element + role>
Mid-ground:       <element + role>
Background:       <element + role>
Depth cues:       <atmospheric perspective, focus layers, scale>

[CAMERA SPECS]
Focal length:     <14 / 24 / 35 / 50 / 85 / 135 mm equivalent>
Depth of field:   <f/1.4 / f/2.0 / f/2.8 / f/4 / f/8>
Movement speed:   <ft/s linear, or °/s rotational>
Focus behaviour:  <locked / breathing / racking>

[LIGHTING SPECS]
Key:              <intensity %, direction (clock or angle), color temp K>
Fill:             <intensity % relative to key, color temp K>
Back / rim:       <intensity %, position, color temp K>
Shadow profile:   <hard / soft / colored>

[AUDIO]
@audio1, @audio2: <if reference uploaded>
Ambient:          <bed sound, dB level>
Music:            <enters at __ s, peaks at __ s>
Dialogue:         <if any, with delivery instruction>
SFX:              <synced to visual beats, with timing>
Silence:          <gaps for tension, with timing>

[PACING]
Cuts / transitions: <where and what kind>
Velocity profile:   <slow start, fast middle, settling end>
Hold durations:     <key frames to hold longer>

[MOOD & ATMOSPHERE]
Emotional target: <what feeling viewer should leave with>
Atmosphere:       <fog, particles, dust, rain>
Texture:          <grain, sharp digital, soft, painterly>

[REFERENCES]
@image1, @image2: <what they contribute — composition / character / style>
@video1:          <motion or transition reference>

[OUTPUT]
Duration:         <4 / 6 / 8 / 10 / 12 / 15 s>
Aspect ratio:     <16:9 widescreen / 9:16 vertical / 1:1 square>
Resolution:       720p (Seedance default)
Audio:            synchronised
```

## How to use this template

1. Don't include every section if it doesn't matter for the clip. A 4 s
   product macro doesn't need a [DEPTH & COMPOSITION] block.
2. Time-stamp everything that has a timing dimension. "Camera dollies
   forward" is weaker than "0–2 s: camera dollies forward at 2 ft/s."
3. Reference uploaded materials inline (`@image1`, not "the reference image").
4. Keep numbers concrete. "Shallow depth of field" is fine; "f/2.0
   equivalent" is better. Tighten numbers as you validate against output.
5. Put the hook first in the prompt text. Models weight earlier tokens more,
   and the hook is the most failure-prone section to under-specify.

## Compact form (for 4–8 s clips)

For shorter clips, collapse the template:

```
[HOOK 0–2 s]      <technique + trigger>
[ACTION 2–end]    <camera move + subject action + lighting + color grade>
[AUDIO]           <one or two specific cues>
[OUTPUT]          <duration, aspect ratio>
```

Aim for 12–20 lines for a compact clip, 25–40 lines for a 15 s narrative.
More lines past that point usually means redundancy.
