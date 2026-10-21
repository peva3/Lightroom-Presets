# Beige Cream — Characteristics

## Key Aesthetic
- Creamy, warm aesthetic base
- Golden-warm highlights with cool shadow depth
- Positive texture for fine detail enhancement
- Balanced contrast with gentle highlight recovery
- Warm/cool interplay via split toning

## Usage
Best for: Lifestyle photography, Instagram aesthetics, fashion, product photography, and content creation.

## STYLEGUIDE Compliance
- No Calibration ✓
- No WB ✓
- |Vibrance - Saturation| = 2 ≤ 5 ✓
- No grain → Texture/Clarity kept as defining ✓
- Tone Curve: Cinematic Creative ✓
- ColorGradeBlending: 75 ✓

## Validation Sweep 2026-10-21
- **Verdict:** minor drift (palette control missing) — fixed
- **Defining traits checked:** (1) creamy warm-neutral base — warm highlight grade H42/S9, cool shadow H220/S7, Temperature left As Shot; (2) soft, slightly lifted tone — Highlight -19, Shadows +19, Contrast +14, no crushed blacks; (3) beige palette = warm neutrals with competing hues muted.
- **Problem:** trait 3 was unimplemented — the preset had zero HSL, so foliage and signage rendered at full digital saturation and the frame read "warm lifestyle", not beige/cream. Added Green Sat -20 and Yellow Sat -10 to hold the palette in beige territory without touching skin (Orange untouched).
- **Sources:** research/characteristics; STYLEGUIDE §XI-C foliage naturalization; beige/cream aesthetic guides (muted greens, warm highlights, no colour punch).
- **Preset adjustments:** added `SaturationAdjustmentGreen=-20`, `SaturationAdjustmentYellow=-10`.
