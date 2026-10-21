# Haze Removal Lightroom Preset — Characteristics

## Use Case
The Haze Removal Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Drone and aerial photography in hazy conditions. Distance shots, urban skylines, horizon landscapes. Atmospheric haze removal.

## Key Techniques
Dehaze +25 is the defining slider — maximum safe value for haze removal. Clarity +20 + Contrast +30 support long-distance detail recovery. Blue Sat +10 restores sky color lost in haze. Green Sat -15 calms vegetation that Dehaze over-saturates as a side effect. |Vibrance−Saturation|=0. 17 attributes — clean and surgical.

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
- **Defining traits checked:** Ex +0.1, Contrast +30, Highlights -45, Shadows +20, Whites +10, Blacks -10, Clarity +20, Dehaze +25, Vibrance +5, Saturation +5; YellowSat +5, GreenSat -15, BlueSat +10; shadow H225/S5, highlight H43/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Dehaze +25 is the hero, +30C/Clarity +20 support distance recovery, BlueSat +10 restores washed sky, GreenSat -15 counters Dehaze's vegetation over-saturation. No grain, Vibrance 5/Saturation 5.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. V (Dehaze destructive-interaction note).
- **Preset adjustments:** none
