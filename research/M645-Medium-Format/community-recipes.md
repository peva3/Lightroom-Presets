# M645 Medium Format — Community Recipes

## Primary Source: Archive-663/lightroomPresets (GitHub)

The Archive-663/lightroomPresets repository includes a color XMP preset called M645 that emulates the Mamiya 645 film aesthetic. Our B&W version is derived from the same tonal philosophy but adapted for monochrome.

### Original M645 XMP (Color) — Key Slider Values
- **Exposure**: +0.70
- **Contrast**: 0
- **Highlights**: -67 (heavy compression for the highlight rolloff)
- **Shadows**: +46 (significant shadow lift)
- **Whites**: +23
- **Blacks**: -39
- **Vibrance**: +32, Saturation: -16 (selective-color issue per STYLEGUIDE — not used in our B&W version)
- **Dehaze**: +11
- **Grain**: Amount 45, Size 25, Frequency 50
- **Custom Tone Curve**: 0,26 / 34,38 / 255,243 (lifted blacks + compressed highlights)
- **Calibration**: RedHue +19/RedSat -14, GreenHue -21/GreenSat -14, BlueHue -23/BlueSat -32, ShadowTint -11

Source: https://github.com/Archive-663/lightroomPresets/blob/main/M645.xmp

### STYLEGUIDE Compliance Notes
- The original M645.xmp contains Calibration panel adjustments — these violate STYLEGUIDE rules and are NOT included in our B&W version
- The original has Vibrance=+32 and Saturation=-16 — a 48-point gap that triggers the selective-color bug per STYLEGUIDE. This is omitted.
- The custom tone curve is replaced with our neutral B&W curve (0,0 → 255,255)
- The original's Exposure offset, Dehaze, and HSL values apply only to color rendering
- Our B&W version extracts the tonal philosophy: smooth transitions, gentle contrast, lifted shadows, compressed highlights

### LR Preset Design Notes
- Medium format character: smooth tonal transitions, gentle contrast (+15)
- Lifted Shadows (+20) and compressed Highlights (-20) simulate larger-negative tonality
- Modest contrast — medium format doesn't need aggressive contrast for dimensionality
- Fine, elegant grain (GrainAmount=25) — larger format = less apparent grain
- Clean, even GrayMixer distribution for natural-tonality B&W
- All STYLEGUIDE rules: Sharpness=10, Clarity/Texture/Dehaze=0, no Calibration, no WB
- The "medium format magic" is in the tonal smoothness, not in aggressive slider values
