# Ilford Delta 400 — Community Recipes

## Primary Source: t3mujinpack (Darktable Styles)

The t3mujinpack project includes an Ilford Delta 400 emulation for Darktable using Channel Mixer and Lab Tone Curves.

### t3mujinpack Approach
- Channel Mixer (RGB) for B&W conversion — different ratios than HP5 or FP4
- Lab Tone Curve designed for Delta 400's fine-grain, modern tonal character
- Part of the 12-film B&W t3mujinpack collection

Source: https://github.com/t3mujinpack/t3mujinpack

### Community Notes (from forums)
- Often described as "HP5+ that went to university" — smarter, cleaner, more refined
- Popular with photographers who want ISO 400 speed but fine-grain results
- Pushes well to 800 in DD-X with modest grain increase
- Some report a slightly "cooler" tonal rendering than HP5+
- Many use it as their "modern" 400-speed film while keeping HP5+ for a more classic look

### LR Preset Design Notes
- T-grain character: finer grain than traditional 400 films — GrainAmount=35
- Clean contrast structure (+25) without pushing into high-contrast territory
- Neutral GrayMixer distribution with emphasis on blue darkening for dramatic skies
- T-grain films have a distinctly modern, clean character — the preset reflects this
- All STYLEGUIDE rules: Sharpness=10, Clarity/Texture/Dehaze=0, no Calibration, no WB
- Higher blue suppression than HP5+ reflects Delta's cooler-leaning tonal character
