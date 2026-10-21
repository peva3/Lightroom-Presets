# Soft Milky Newborn Lightroom Preset — Characteristics

## Use Case
The Soft Milky Newborn Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Newborn studio and lifestyle sessions. Soft, creamy skin tones, high-key bright background. Works on fair to medium skin tones.

## Key Techniques
High Exposure (+0.65) floods sensor for clean whites. Negative Contrast (-20) + negative Clarity (-12) + negative Dehaze (-5) create triple-layer soft bloom. Orange Sat -10 calms ruddy newborn skin; Orange Lum +15 brightens. Saturation -10 global + Vibrance -8 (|diff|=2, safe). Lifted blacks (+15) for matte finish.

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
- **Defining traits checked:** Ex +0.65, Contrast -20, Highlights -50, Shadows +35, Whites +10, Blacks +15, Clarity -12, Texture -5, Dehaze -5, Vibrance -8, Saturation -10; GreenHue +15, RedSat -5, OrangeSat -10, GreenSat -25, BlueSat -20, OrangeLum +15; shadow H50/S5, highlight H43/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Newborn-safe: +0.65Ex, -20C, Clarity -12/Texture -5/Dehaze -5 for cream, Blacks +15 matte, OrangeSat -10 calms ruddy skin, OrangeLum +15 brightens, Saturation -10/Vibrance -8 (gap 2). No harsh clarity anywhere.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. V/VI; newborn workflow practice.
- **Preset adjustments:** none
