# Full Reset

Resets all Basic panel, Tone Curve, HSL, Color Grading, Detail, Effects, and Lens Corrections to default/neutral values. Use to strip all adjustments from an image and start fresh.

## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** All Basic sliders, HSL (24 attrs), ColorGrade (15 attrs), grain, vignette, sharpening and NR are explicitly written to defaults, with Sharpness=40, ColorNoiseReduction=25 and WhiteBalance=As Shot -- no stray creative values survive. Gaps versus the stated scope: no ParametricShadows/Darks/Lights/Highlights or split zeros (so a previous parametric curve survives) and no LensProfileEnable/AutoLateralCA despite the doc claiming Lens Corrections is reset.
- **Sources:** Reference §2/§5/§6/§7 default columns; Lightroom detail defaults (Amount 40, Radius 1.0, Detail 25).
- **Preset adjustments:** none (gap recorded, not changed)

## Reset completeness fix (2026-10-21)

The preset now actually covers everything its description claims. Added:

- **Parametric curve** — `ParametricShadows` / `ParametricDarks` / `ParametricLights` / `ParametricHighlights` = 0, splits at 25 / 50 / 75. Previously a parametric curve from an earlier edit survived a "full" reset.
- **Black & White mixer** — all eight `GrayMixer*` channels = 0. The Color Mixer panel stores HSL and GrayMixer separately, so resetting only HSL left stale B&W mix values behind.
- **Lens Corrections / Transform** — `LensProfileEnable` 0, `LensProfileSetup` LensDefaults, `LensManualDistortionAmount` 0, `VignetteAmount` 0, `AutoLateralCA` 1, `DefringePurpleAmount` / `DefringeGreenAmount` 0, defringe hues 30 / 60, `PerspectiveUpright` 0.

`AutoLateralCA="1"` is Lightroom's own default (Remove Chromatic Aberration enabled), so it is part of returning to defaults rather than a lens correction being applied. The file now carries 108 attributes; that is deliberate — a reset preset has to name every value it clears, otherwise the previous edit persists.
