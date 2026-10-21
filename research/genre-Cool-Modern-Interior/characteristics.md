# Cool Modern Interior Lightroom Preset — Characteristics

## Use Case
The Cool Modern Interior Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Modern/minimalist architecture and commercial real estate. Clean lines, cool tones, glass/steel/concrete materials.

## Key Techniques
Cool shadow split (H225 S5) + cool highlight (H210 S3) create crisp, contemporary feel. Clarity +8 sharpens architectural edges. Whites pushed to +15 for bright white walls without clipping. Saturation slightly negative (-5) for sophisticated, desaturated look. Aqua Lum +15 for glass reflection glow. |Vibrance−Saturation|=2. 18 attributes.

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
- **Defining traits checked:** Ex +0.3, Contrast +15, Highlights -30, Shadows +20, Whites +15, Clarity +8, Vibrance -3, Saturation -5; OrangeSat -5, GreenSat -15, BlueSat -5, AquaLum +15; shadow H225/S5, highlight H210/S3, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Deliberate cool identity: shadow H225/S5 + highlight H210/S3 is a 3-5% cast, the stated look, not a WB error; Highlights -30/Whites +15 keep glazing and white walls clean; Clarity +8 for steel/glass edges.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; Imagen AI real-estate guide (neutral base, stylised grade is acceptable on modern architecture).
- **Preset adjustments:** none
