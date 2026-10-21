# Reset Tone Curve

Sets all four tone curves (RGB, Red, Green, Blue) to linear neutral (0,0 to 255,255). Does not affect other panels.

## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** ParametricShadows/Darks/Lights/Highlights all 0 with splits at the 25/50/75 defaults, and all four ToneCurvePV2012 sequences (RGB/R/G/B) at 0,0 -> 255,255.
- **Sources:** Reference §3 (curves are elements; parametric defaults 25/50/75).
- **Preset adjustments:** none
