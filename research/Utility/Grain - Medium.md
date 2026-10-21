# Grain - Medium

Grain preset: Amount=25, Size=30, Roughness=50.
Sharpness capped at 10 per STYLEGUIDE to prevent edge amplification of grain particles. Clarity, Texture, and Dehaze set to 0.

## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** GrainAmount 25 / GrainSize 30 / GrainRoughness 50, ascending on all three axes across Fine -> Medium -> Heavy -> Pushed. Grain rule respected: Sharpness=10 and LuminanceSmoothing=0, with no Clarity/Texture/Dehaze values written. No GrainFrequency alias anywhere.
- **Sources:** Reference §7 (GrainAmount 0-100, GrainSize default 25, GrainRoughness default 50; GrainFrequency does not exist); STYLEGUIDE rule 9.
- **Preset adjustments:** none
