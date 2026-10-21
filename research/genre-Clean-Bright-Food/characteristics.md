# Clean Bright Food Lightroom Preset — Characteristics

## Use Case
The Clean Bright Food Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Clean white-background food photography. Overhead flat lays, bright salads, beverages, desserts. Fresh, clean, editorial.

## Key Techniques
High Exposure (+0.40) + Whites (+15) for clean white backgrounds. Low Contrast (+5) preserves subtle food detail. Clarity +5 for gentle edge definition on food surfaces. Orange Lum +10 brightens. Red Sat -5 calms overly red food. Minimal Color Grading — barely perceptible warmth. |Vibrance−Saturation|=3. 16 attributes.

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
- **Verdict:** minor drift
- **Defining traits checked:** Ex +0.4, Contrast +5, Highlights -35, Shadows +20, Whites +15, Clarity +5, Vibrance +3; RedSat -5, GreenSat -10, OrangeLum +10; shadow H210/S3, highlight H43/S3, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Bright/clean brief is met (+0.40Ex, Whites +15, Reds calmed), but warmth is carried only by a 3% H43 highlight tint - midtones are effectively neutral. Food reads 'clean' rather than 'appetising'. Advisory: nudge CG highlight sat to 6-8 or add +300K if a warmer plate is wanted; left unchanged to preserve the 'clean' brief.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VI warm-highlight recipe (H40-45, Sat 5-10); research food community recipes.
- **Preset adjustments:** none
