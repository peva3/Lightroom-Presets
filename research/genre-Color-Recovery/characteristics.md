# Color Recovery Lightroom Preset — Characteristics

## Use Case
The Color Recovery Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Underwater photography color restoration. Water absorbs red light — this preset restores the lost warm spectrum. Snorkeling, diving, pool photography.

## Key Techniques
This is THE one preset where aggressive red/orange saturation is the defining purpose. Red Sat +30 and Orange Sat +25 restore colors at 5-15m depth (red gone by 5m, orange by 15m). Blue/Aqua desaturation removes overwhelming cyan cast. Dehaze +20 + Clarity +15 cut through water turbidity. Saturation +15 global for overall color restoration. Warm Color Grading (shadows H40 S10) reinforces red restoration. 19 attributes.

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
- **Defining traits checked:** Kelvin 7500, Tint +15, Ex +0.5, Contrast +25, Highlights -30, Shadows +25, Whites +10, Blacks -10, Clarity +15, Dehaze +20, Vibrance +15, Saturation +15; RedSat +30, OrangeSat +25, YellowSat +15, GreenSat -15, AquaSat -10, BlueSat -20; shadow H40/S10, highlight H38/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Underwater cast correction is correct in direction: Kelvin 7500 + Tint +15 magenta counter blue-green, RedSat +30/OrangeSat +25 restore the absorbed warm spectrum, BlueSat -20/AquaSat -10 remove cyan dominance, Dehaze +20 for turbidity. Structural note: Temperature/Tint are written without crs:WhiteBalance="Custom"; if a given Lightroom build ignores Kelvin in that form, add the enum. Verified as repo-wide convention (78 temperature-bearing presets, only 6 write the enum).
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; Underwater colour-restoration practice (red-channel loss vs depth); whitepaper sec. 2 (Temperature is absolute Kelvin).
- **Preset adjustments:** none
