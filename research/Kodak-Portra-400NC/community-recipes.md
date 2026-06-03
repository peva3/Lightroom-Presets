# Kodak Portra 400NC — Lightroom Preset Settings & Recipes

> "Natural Color" at 400 speed — more neutral, cooler, and lower contrast than standard Portra 400. Sourced from t3mujinpack.

---

## 1. t3mujinpack Darktable Preset

Source: `github.com/t3mujinpack/t3mujinpack`

The Portra 400 NC preset uses 11 modules including Lab tone curves. The high module count reflects the need to counterbalance 400-speed film's inherent warmth with NC's neutral palette.

---

## 2. Comparison with Standard Portra 400

The project's existing Portra 400 preset is the baseline. Portra 400NC differs by:
- **Lower contrast** — flat, accurate reproduction
- **Less saturation** — "Natural Color" neutral palette
- **No warm cast** — the defining difference from standard Portra 400
- **More shadow openness** — maximum detail

| Attribute | Standard P400 | P400NC (derived) | Delta |
|---|---|---|---|
| Contrast | -7.5 | -12 | -4.5 |
| Shadows | +32 | +35 | +3 |
| Blacks | +12 | +15 | +3 |
| Saturation | 0 | -15 | -15 |
| Green Sat | -22.5 | -22 | — |
| Blue Sat | -15 | -18 | -3 |
| Highlight Hue | 45 | 48 | +3 |
| Highlight Sat | 12.5 | 5 | -7.5 |
| Shadow Sat | 8 | 5 | -3 |

---

## 3. Derived LR Values

| Attribute | Value | Rationale |
|---|---|---|
| Exposure | +0.45 | Slight overexposure |
| Contrast | -12 | Lower than standard P400 |
| Highlights | -55 | Legendary Portra latitude |
| Shadows | +35 | Maximum openness |
| Whites | -5 | Conservative |
| Blacks | +15 | Lifted for detail |
| Saturation | -15 | NC desaturation |
| Vibrance | -12 | Gap=3 ✓ |
| Orange Lum | +15 | Creamy skin |
| Green Hue | +12 | Olive shift |
| Green Sat | -22 | Signature desaturation |
| Blue Sat | -18 | Muted |
| Red Sat | +5 | Gentle warmth |
| ColorGrade Shadow | H210/S5 | Neutral-cool |
| ColorGrade Highlight | H48/S5 | Subtle |
| Grain Amount | 22 | Fine for 400 |
| Grain Size | 25 | Standard |
| Grain Frequency | 45 | Smooth |

---

## STYLEGUIDE Compliance

- No Calibration ✓
- No WB ✓
- Grain → Sharpness=10, Clarity=0, Texture=0, Dehaze=0 ✓
- |Vibrance−Saturation|=3 ≤ 5 ✓
- HSL Sat ≤ ±60 ✓

---

## Sources

- t3mujinpack GitHub — Kodak Portra 400 NC Darktable preset
- Kodak Professional — E-4046 PORTRA Films technical data
- Project's existing Kodak Portra 400 preset (baseline reference)

---

## See Also

- [Kodak Portra 400NC — Film Characteristics](../Kodak-Portra-400NC/characteristics.md)
- [Kodak Portra 160NC Lightroom Preset](../Kodak-Portra-160NC/community-recipes.md)
- [Kodak Portra 400VC Lightroom Preset](../Kodak-Portra-400VC/community-recipes.md)
- [Kodak Portra 400 Lightroom Preset](../Kodak-Portra-400/community-recipes.md)
- [XMP Preset: Kodak Portra 400NC](../../Presets/Color-Negative/Kodak Portra 400NC.xmp)
