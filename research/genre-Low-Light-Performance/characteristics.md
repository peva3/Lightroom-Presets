# Low Light Performance Lightroom Preset — Characteristics

## Use Case
The Low Light Performance Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Low-light concerts, clubs, and small venues. High ISO shooting, minimal stage lighting. Noise management while preserving mood.

## Key Techniques
High Exposure (+0.50) + Shadow lift (+30) rescue underexposed low-light frames. LuminanceSmoothing +20 reduces high-ISO color noise without destroying detail. Muted saturation (-5) calms chroma noise artifacts. Green Sat -20 removes LED backlight pollution. Cool shadow split (H235 S10) + warm highlights (H40 S8) add depth. |Vibrance−Saturation|=2. 18 attributes.

## Safety Check
- ProcessVersion: 15.4
- Treatment: Color
- Look Profile: Adobe Color
- Curve: Cinematic (0,20 / 64,55 / 128,128 / 192,196 / 255,235)
- ColorGradeBlending: 75
- Calibration: None (as required)
- Temperature/Tint: None (as required)
- Vibrance−Saturation gap: Checked — within ±5
- HSL Sat max: Within ±60
- Blacks floor: ≥ -30
- Grain protection: N/A (no grain)

## See Also

- [Genre Presets](../../docs/genre.md)
- [Mobile Presets](../../docs/mobile.md)
- [Seasonal Presets](../../docs/seasonal.md)
- [All Lightroom Preset Categories](../../docs/index.md)


## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** Ex +0.5, Contrast +20, Highlights -40, Shadows +30, Whites +5, Blacks -10, Clarity +10, Vibrance -3, Saturation -5, LumNR +20; GreenSat -20, BlueSat -15, OrangeLum +5; shadow H235/S10, highlight H40/S8, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. +0.50Ex and Shadows +30 rescue high-ISO frames; LuminanceSmoothing +20 is the one place NR is explicitly set; Saturation -5/Vibrance -3 mute chroma noise, GreenSat -20 kills LED spill, cool/warm split for depth.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VI; low-light/concert recipes.
- **Preset adjustments:** none
