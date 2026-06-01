# Haze Removal — Characteristics

## Use Case
Drone and aerial photography in hazy conditions. Distance shots, urban skylines, horizon landscapes. Atmospheric haze removal.

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
