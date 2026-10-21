# Reset Effects + Detail

Resets all Detail panel (Sharpening, Noise Reduction) and Effects panel (Grain, Vignette, Clarity, Texture, Dehaze) to defaults. Does not affect Basic panel, Tone Curve, or HSL.

## Validation Sweep 2026-10-21
- **Verdict:** minor drift (fixed)
- **Defining traits checked:** Detail defaults are Sharpness 40 / Radius +1.0 / Detail 25 / Masking 0 and NR 0/25/50; Effects defaults are grain 0/25/50, vignette 0 with midpoint/feather 50, style 1. The file had Sharpness=0 -- the only non-default value in an otherwise default-restoring preset -- which left images unsharpened instead of reset.
- **Sources:** blog.jholko.com Adobe capture-sharpening presets (Amount 40, Radius 1, Detail 25); kevinlisota.photography and bcgforums.com (LR Detail defaults Amount 40 / Radius 1.0 / Detail 25 / Masking 0).
- **Preset adjustments:** Sharpness 0 -> 40 (restores the Lightroom default, matching the rest of the file)

## Reset completeness fix (2026-10-21)

Added the Lens Corrections / Transform defaults the description claimed but the file did not set: `LensProfileEnable` 0, `LensProfileSetup` LensDefaults, `LensManualDistortionAmount` 0, `VignetteAmount` 0, `AutoLateralCA` 1, `DefringePurpleAmount` / `DefringeGreenAmount` 0, defringe hues 30 / 60, `PerspectiveUpright` 0.

Grain, sharpening, noise reduction and post-crop vignette were already reset to Lightroom defaults (GrainAmount 0 with Size 25 / Roughness 50, Sharpness 40, SharpenRadius 1.0, SharpenDetail 25, ColorNoiseReduction 25). `AutoLateralCA="1"` matches Lightroom's default state.
