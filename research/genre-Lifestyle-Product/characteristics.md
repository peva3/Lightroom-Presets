# Lifestyle Product Lightroom Preset — Characteristics

## Use Case
The Lifestyle Product Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Lifestyle product photography — products in natural settings, flat lays with props, hand-model shots. Aspirational but authentic.

## Key Techniques
Warm Color Grading (shadows H45 S8, highlights H43 S5) creates aspirational golden glow. Mild positive Saturation (+5) with balanced Vibrance (+5) for subtle color pop. Red/Orange Sat +5 warm product colors. Orange Lum +10 brightens skin in hand-model shots. Green Sat -10 naturalizes backgrounds. Clarity +5 for clean product edges. |Vibrance−Saturation|=0. 18 attributes.

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
- **Defining traits checked:** Ex +0.2, Contrast +10, Highlights -30, Shadows +20, Whites +5, Clarity +5, Vibrance +5, Saturation +5; RedSat +5, OrangeSat +5, GreenSat -10, OrangeLum +10; shadow H45/S8, highlight H43/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Lifestyle (not on-white): warm H45/H43 grade at 5-8%, Red/OrangeSat +5, OrangeLum +10 for hand-model skin, GreenSat -10 for props, Clarity +5 for edges; Vibrance/Saturation 5/5 neutral overall.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VI.
- **Preset adjustments:** none
