# Moody Editorial Wedding Lightroom Preset — Characteristics

## Use Case
The Moody Editorial Wedding Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Dramatic editorial wedding — receptions, night portraits, industrial venues. Dark, rich, cinematic mood with film-like grain.

## Key Techniques
Underexposure (-0.30) + strong Contrast (+30) create dramatic tonality. Highlights crushed (-50) for cinematic shoulder rolloff. Teal shadows (H225 S15) + warm highlights (H40 S10) = Hollywood teal/orange split. Greens desaturated (-40) and pushed brown (+30) to remove distracting foliage. Grain (Amount 20, Size 25) for filmic texture. Sharpness=10 required by grain rule. |Vibrance−Saturation| = 2 (safe).

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
- Grain protection: Sharpness=10, Clarity=0, Texture=0, Dehaze=0

## See Also

- [Genre Presets](../../docs/genre.md)
- [Mobile Presets](../../docs/mobile.md)
- [Seasonal Presets](../../docs/seasonal.md)
- [All Lightroom Preset Categories](../../docs/index.md)


## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** Ex -0.3, Contrast +30, Highlights -50, Shadows +25, Whites +10, Blacks -15, Vibrance -8, Saturation -10, Sharpness +10, Grain +20; GreenHue +30, YellowSat -15, GreenSat -40, OrangeLum +10; shadow H225/S15, midtone H35/S5, highlight H40/S10, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. -0.30Ex, +30C, Highlights -50 shoulder, teal H225/S15 vs warm H40/S10 split, Greens pushed brown (+30 hue, -40 sat), OrangeLum +10 with no orange sat push, Grain 20 with Sharpness 10/Clarity 0.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VI/VII; wedding editorial recipes.
- **Preset adjustments:** none
