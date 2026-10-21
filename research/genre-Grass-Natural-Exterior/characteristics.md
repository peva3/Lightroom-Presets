# Grass Natural Exterior Lightroom Preset — Characteristics

## Use Case
The Grass Natural Exterior Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Exterior real estate and landscape architecture. Naturalizing grass and foliage while keeping structure crisp.

## Key Techniques
Green Hue +15 shifts neon-green grass toward natural olive. Green Sat -20 calms digital oversaturation of lawns. Yellow Hue -10 shifts yellows toward orange for golden-hour warmth on exteriors. Yellow Sat +10 boosts golden tones in dry grass and fall landscaping. Gentle shadow cool (H210 S5) adds depth. 18 attributes — clean and natural.

## Safety Check
- ProcessVersion: 15.4
- Treatment: Color
- Look Profile: Adobe Color
- Curve: Cinematic (0,20 / 64,55 / 128,128 / 192,196 / 255,235)
- ColorGradeBlending: 75
- Calibration: None (as required)
- Temperature/Tint: None (as required)
- Vibrance−Saturation gap: N/A (no Vibrance)
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
- **Defining traits checked:** Ex +0.1, Contrast +10, Highlights -35, Shadows +15, Whites +5, Blacks -5; YellowHue -10, GreenHue -10, YellowSat +10, GreenSat -20, BlueSat -5; shadow H210/S5, highlight H43/S3, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Exterior curb appeal: GreenHue -10 + YellowHue -10 push neon lawn toward olive/warm, GreenSat -20 tames digital lawns, YellowSat +10 keeps dry grass golden, Highlights -35 protects sky. Docs drift: characteristics.md still says GreenHue +15; the file's -10 is the direction that actually warms grass.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VI; real-estate exterior recipes.
- **Preset adjustments:** none
