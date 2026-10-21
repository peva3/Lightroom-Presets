# Bright Neutral Interior Lightroom Preset — Characteristics

## Use Case
The Bright Neutral Interior Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Real estate interiors with mixed natural/artificial light. White walls, neutral decor. Accurate color rendering essential.

## Key Techniques
Bright exposure (+0.40) to fill shadow corners. Shadow lift (+30) reveals detail in darker rooms. Clarity +5 gives subtle edge definition for architectural lines without HDR look. Aqua Lum +15 brightens windows/skylight glow. Orange Sat -5 prevents warm wood from dominating. Minimal Color Grading for neutrality. 16 attributes — real estate agents want truth, not art.

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
- **Defining traits checked:** Ex +0.4, Contrast +10, Highlights -35, Shadows +30, Whites +10, Clarity +5; OrangeSat -5, BlueSat -10, AquaLum +15; shadow H220/S3, highlight H43/S3, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Real-estate core: +0.40Ex, Highlights -35 protects window detail, Shadows +30 opens corners, Whites +10 without clipping; OrangeSat -5 keeps oak floors honest; toning at 3% sat only, so no cast. No WB override (correct: mixed lighting must be solved per frame).
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; Imagen AI real-estate preset guide; Imagtor exposure-balancing guide.
- **Preset adjustments:** none
