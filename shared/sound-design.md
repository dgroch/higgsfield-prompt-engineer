# Sound Design Reference

Seedance 2.0 outputs include synchronised audio (≤ 15 s, mp3/wav). A clip
with thoughtful audio reads as twice the production budget of a silent clip.

## The six layers

| Layer        | Purpose                                | Volume vs dialogue | Examples |
| ------------ | -------------------------------------- | ------------------ | -------- |
| **Ambient**  | Establishes location reality           | −4 to −6 dB        | Room tone, wind, traffic, ocean, forest |
| **Foley**    | Adds physical reality to actions       | −1 to +1 dB        | Footsteps, cloth rustle, impacts, breaths |
| **Music**    | Emotional architecture                 | −2 to −4 dB        | Score, song, ambient pad |
| **Dialogue** | Narrative information                  | 0 dB (reference)   | On-screen speech, voiceover |
| **SFX**      | Punctuates key moments                 | +1 to +3 dB        | Gunshots, whooshes, impacts, transitions |
| **Silence**  | Negative space, tension                | —                  | 1.5–2.5 s gaps before re-entry |

## Mixing principles

- **Dialogue is reference (0 dB).** Everything else sits relative to it.
- **Ambient never disappears.** Even at −6 dB it gives the scene a "room."
- **Use silence as a hook.** A 1.5 s silent hold immediately before a sound
  drop is more attention-grabbing than the loudest possible opener.
- **Sync foley to frame.** Specify the timecode for impacts: "Footstep on
  concrete at 2.4 s." Vague foley reads as unsynced.
- **Reverb communicates space.** Long tails (1+ s) = cathedral / warehouse.
  Short tails (0.3 s) = small room. Dry = outdoors / open air.

## Hooking with sound

| Technique                  | How it works                                              |
| -------------------------- | --------------------------------------------------------- |
| Silent → drop              | 1.5 s of silence, then full mix arrives at 1.5 s mark     |
| Subliminal low rumble      | 30 Hz sub builds 0–2 s, brain registers tension before mind |
| Foley first                | Open with single foley (footstep, breath) before music    |
| Diegetic→non-diegetic       | In-world sound (radio, fire) bridges into score           |
| Hard cut on impact         | Sharp SFX hit synchronised to visual cut                  |

## Reference syntax

Higgsfield supports up to 3 audio files per generation, each ≤ 15 MB and
collectively ≤ 15 s. Reference uploaded audio with `@audio1`, `@audio2`,
`@audio3` inline in the prompt.

```
@audio1 establishes ambient bed throughout. @audio2 enters at 4 s as
musical layer. Dialogue is generated; sync foley to visual beats at 2.4 s
and 6.8 s.
```

## Genre cheat sheet

| Genre              | Audio priority                                              |
| ------------------ | ----------------------------------------------------------- |
| Cinematic          | Ambient + score; silence before climax; rich reverb         |
| Action / fight     | SFX punches + percussive score; impacts on every hit        |
| Horror             | Sub-bass rumble + sparse foley; long silences               |
| Comedy             | Tight foley sync; clean dialogue; minimal score             |
| Music video        | Music drives everything; foley/SFX punctuate beats          |
| E-commerce / ad    | Clean dialogue / VO; bright music; clear product foley      |
| Real estate        | Soft ambient + warm score; minimal foley                    |
| Food               | Foley-forward (sizzle, pour, crunch); subtle warm score     |
| Social hook        | Front-load: SFX + music drop in first 0.5 s                 |
| Brand story        | Score-led; sparse but emotional foley; minimal SFX          |
