# Agfa APX 25 — Lightroom Preset Settings & Recipes

## Primary Source: t3mujinpack (Darktable Styles)

The t3mujinpack project provides a dedicated Agfa APX 25 film emulation style for Darktable, using Channel Mixer for B&W conversion and Lab Tone Curves for contrast. This data informed our channel mix ratios and contrast structure.

### t3mujinpack Approach
- Uses Channel Mixer (RGB) for monochrome conversion
- Applies Lab Tone Curve for Agfa APX 25 tonal response
- Designed to work as a step in a workflow, not a one-click solution
- Assumes basic exposure and white balance are already set

Source: https://github.com/t3mujinpack/t3mujinpack

### Community Notes (from forums)
- APX 25 in Rodinal 1+50 was a legendary combination — very sharp, excellent tonal separation
- Known for its ability to hold highlight detail while maintaining deep blacks
- Often compared to Kodak Technical Pan in sharpness but with more forgiving contrast
- Ultra-fine grain made it popular for 35mm photographers wanting medium format quality

### LR Preset Design Notes
- APX 25 is ultra-fine-grain — minimal GrainAmount (15), small Size (20)
- Moderate contrast (+15) with subtle highlight compression to preserve detail
- Clean shadow character without crushing — Blacks only -20
- Neutral tonality through even-handed GrayMixer distribution
- All STYLEGUIDE rules applied: Sharpness=10, Clarity/Texture/Dehaze=0, no Calibration, no WB
- The low ISO character translates to a cleaner, more transparent film emulation

---

## See Also

- [Agfa APX 25 — Film Characteristics](../Agfa-APX-25/characteristics.md)
- [Agfa APX 100 Lightroom Preset](../Agfa-APX-100/community-recipes.md)
- [Agfa APX 400 Lightroom Preset](../Agfa-APX-400/community-recipes.md)
- [Kodak Tri X 400 Lightroom Preset](../Kodak-Tri-X-400/community-recipes.md)
- [XMP Preset: Agfa APX 25](../../Presets/Black-White/Agfa APX 25.xmp)
