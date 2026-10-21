# Eterna Summer — Characteristics

## Base Profile
Eterna is Fujifilm's cinema film simulation, modeled after their Eterna motion picture film stock. It provides:
- Lower contrast than Classic Chrome or PRO Neg.
- Smooth, cinematic tonal transitions
- Natural skin tone rendering
- Moderate saturation with subtle color separation

## Key Aesthetic
- Warm, golden cinematic look
- Moderate contrast with amber highlights
- Slightly cool shadow split for depth
- Summer daylight cinema aesthetic
- Negative clarity for atmospheric bloom
- Fine grain (Strong/Small → textured but not overwhelming)

## XMP Translation Notes
- WB Daylight + warm shift → Temperature 5800, Tint -10 (defining)
- H+2.5 → Highlights +25 (unusual positive value, defining for the bright summer look)
- Eterna → moderate contrast, cinematic tonality
- Color +4 → Saturation +18
- Clarity -3 → Clarity -12 (bloom)
- Grain Strong/Small → Amount 30, Size 15

## STYLEGUIDE Compliance
- No Calibration ✓
- WB is defining (warm Daylight balance) ✓
- |Vibrance - Saturation| = 3 ≤ 5 ✓
- HSL ≤ ±60 ✓
- Grain → Sharpness=10, LuminanceSmoothing=0 ✓
- Tone Curve: Cinematic Creative ✓
- ColorGradeBlending: 75 ✓

## Validation Sweep 2026-10-21
- **Verdict:** minor drift (hybrid, deliberately documented)
- **Defining traits checked:** (1) Eterna's smooth, low-contrast transition — Contrast +10 only, Clarity -12, Dehaze -5; (2) summer daylight cinema warmth — Temperature 5800 / Tint -10, Highlight H42/S12, Midtone H38/S6, Balance +10; (3) fine film grain — Grain 30/15/50.
- **Drift:** the preset is far more saturated than Eterna itself (Saturation +18, Vibrance +15, Highlights +25 — an unusual positive highlight value). That is the documented "Summer" reinterpretation, not a stock emulation, so it was left intact; the name and research both describe it as a warm summer riff rather than Eterna fidelity.
- **Sources:** research/characteristics (Fujifilm Eterna simulation: low contrast, natural skin, moderate saturation; XMP translation notes map Highlights +25 as defining); Fuji X Weekly Eterna references.
- **Preset adjustments:** none.
