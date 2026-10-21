# Night Sky Landscape Lightroom Preset — Characteristics

## Use Case
The Night Sky Landscape Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Night landscapes with foreground detail. Mountains under stars, desert night scenes. Balanced sky and land exposure.

## Key Techniques
Highest Shadow lift (+50) across all presets — foreground is as important as sky. Exposure +0.50 for overall brightness in near-total darkness. Blue Sat +10 + Aqua Sat +5 enhance sky. Green Sat -15 and Yellow Sat -10 calm foreground vegetation color casts from moonlight/light painting. Moderate Dehaze (+8) balances sky clarity with foreground softness. |Vibrance−Saturation|=5. 18 attributes.

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
- **Defining traits checked:** Ex +0.5, Contrast +25, Highlights -55, Shadows +50, Whites +15, Blacks -10, Clarity +15, Dehaze +8, Vibrance +10, Saturation +5; YellowSat -10, GreenSat -15, AquaSat +5, BlueSat +10; shadow H245/S8, highlight H38/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Highest shadow lift in the set (+50) with Blacks -10 so foreground survives without crushing; Dehaze only +8 to keep land soft; BlueSat +10/AquaSat +5 for sky, Green/Yellow sat down for moonlight casts. No grain; NR left at camera default (correct for a stackable base).
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; jonnorrisphoto.com Milky Way workflow (foreground/sky balance); photographylife.com.
- **Preset adjustments:** none
