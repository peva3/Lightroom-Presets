# Kodak Portra 160NC — Lightroom Preset Settings & Recipes

> "Natural Color" variant — lower contrast, more neutral than standard Portra 160. Sourced from t3mujinpack and film characteristics.

---

## 1. t3mujinpack Darktable Preset

Source: `github.com/t3mujinpack/t3mujinpack`

The Portra 160 NC preset uses 10 modules including Lab tone curves. Designed as a post-WB/exposure starting point for further editing.

---

## 2. Comparison with Standard Portra 160

The project's existing Portra 160 preset provides the baseline. Portra 160NC differs by:
- **Lower contrast** — NC was specifically designed flatter for commercial reproduction
- **Less saturation** — "Natural Color" = less color bias than standard
- **More neutral color balance** — less warm/golden than standard Portra 160
- **Even more lifted blacks** — maximum shadow detail for reproduction work

| Attribute | Standard P160 | P160NC (derived) | Delta |
|---|---|---|---|
| Contrast | -15 | -20 | -5 |
| Exposure | +0.50 | +0.40 | -0.10 |
| Shadows | +30 | +35 | +5 |
| Blacks | +20 | +25 | +5 |
| Saturation | -10 | -15 | -5 |
| Green Sat | -15 | -20 | -5 |
| Blue Sat | -10 | -15 | -5 |
| Grain Amount | 20 | 18 | -2 |

---

## 3. Derived LR Values

| Attribute | Value | Rationale |
|---|---|---|
| Exposure | +0.40 | Slight overexposure sweet spot |
| Contrast | -20 | Lowest contrast in Portra line |
| Highlights | -30 | Standard Portra highlight protection |
| Shadows | +35 | Maximum shadow openness |
| Whites | -5 | Conservative white point |
| Blacks | +25 | Lifted black point, maximum detail |
| Saturation | -15 | Desaturated "Natural Color" |
| Vibrance | -12 | Within 5 of Sat (gap=3) |
| Orange Lum | +15 | Creamy skin |
| Green Hue | +8 | Toward olive |
| Green Sat | -20 | Signature Portra green |
| Blue Sat | -15 | Muted sky |
| ColorGrade Shadow | H210/S5 | Neutral-cool shadow |
| ColorGrade Highlight | H50/S3 | Subtle warmth |
| Grain Amount | 18 | Very fine, NC had finest grain |
| Grain Size | 20 | Fine grain |
| Grain Frequency | 40 | Smooth |

---

## STYLEGUIDE Compliance

- No Calibration ✓
- No WB ✓
- Grain → Sharpness=10, Clarity=0, Texture=0, Dehaze=0 ✓
- |Vibrance−Saturation|=3 ≤ 5 ✓
- HSL Sat ≤ ±60 ✓

---

## Sources

- t3mujinpack GitHub — Kodak Portra 160 NC Darktable preset
- Kodak Professional — E-4046 PORTRA Films technical data
- Project's existing Kodak Portra 160 preset (baseline reference)

---

## See Also

- [Kodak Portra 160NC — Film Characteristics](../Kodak-Portra-160NC/characteristics.md)
- [Kodak Portra 400VC Lightroom Preset](../Kodak-Portra-400VC/community-recipes.md)
- [Kodak Portra 400 Lightroom Preset](../Kodak-Portra-400/community-recipes.md)
- [Kodak Portra 400NC Lightroom Preset](../Kodak-Portra-400NC/community-recipes.md)
- [XMP Preset: Kodak Portra 160NC](../../Presets/Color-Negative/Kodak Portra 160NC.xmp)
