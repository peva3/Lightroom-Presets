# Full Reset

Resets all Basic panel, Tone Curve, HSL, Color Grading, Detail, Effects, and Lens Corrections to default/neutral values. Use to strip all adjustments from an image and start fresh.

## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** All Basic sliders, HSL (24 attrs), ColorGrade (15 attrs), grain, vignette, sharpening and NR are explicitly written to defaults, with Sharpness=40, ColorNoiseReduction=25 and WhiteBalance=As Shot -- no stray creative values survive. Gaps versus the stated scope: no ParametricShadows/Darks/Lights/Highlights or split zeros (so a previous parametric curve survives) and no LensProfileEnable/AutoLateralCA despite the doc claiming Lens Corrections is reset.
- **Sources:** Reference §2/§5/§6/§7 default columns; Lightroom detail defaults (Amount 40, Radius 1.0, Detail 25).
- **Preset adjustments:** none (gap recorded, not changed)
