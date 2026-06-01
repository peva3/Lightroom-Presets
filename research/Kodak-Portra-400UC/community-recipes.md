# Kodak Portra 400UC / 400VC — Community Recipes

> "Ultra Color" / "Vivid Color" — Portra 400 with elevated saturation. Sourced from t3mujinpack.

---

## 1. t3mujinpack Darktable Presets

Source: `github.com/t3mujinpack/t3mujinpack`

Both Portra 400 UC (6 modules) and Portra 400 VC (1 module) Darktable presets exist. 400UC uses Lab tone curves for color emulation; 400VC is simpler. The combined UC/VC approach provides Portra's skin handling with elevated saturation.

---

## 2. Comparison with Standard Portra 400

The project's existing Portra 400 preset is the baseline. Portra 400UC differs by:
- **Higher saturation** — the "Ultra Color" differentiator
- **Similar contrast** — same Portra characteristic curve
- **Warmer, more saturated color** across all channels
- **Less HSL desaturation** — greens/blues keep more color
- **More saturated ColorGrade** — highlights and shadows have more presence

| Attribute | Standard P400 | P400UC (derived) | Delta |
|---|---|---|---|
| Saturation | 0 | +10 | +10 |
| Green Sat | -22.5 | -15 | +7.5 |
| Blue Sat | -15 | -8 | +7 |
| Red Sat | 0 | +8 | +8 |
| Highlight Sat | 12.5 | 10 | -2.5 |
| Shadow Sat | 8 | 8 | 0 |
| Contrast | -7.5 | -5 | +2.5 |

---

## 3. Derived LR Values

| Attribute | Value | Rationale |
|---|---|---|
| Exposure | +0.50 | Standard Portra overexposure |
| Contrast | -5 | Slightly more than standard |
| Highlights | -55 | Legendary Portra latitude |
| Shadows | +30 | Open, warm |
| Whites | -5 | Conservative |
| Blacks | +10 | Lifted but with more density |
| Saturation | +10 | Ultra Color = elevated Sat |
| Vibrance | +8 | Gap=2 ✓ |
| Orange Hue | -3 | Slightly warmer skin |
| Orange Lum | +15 | Creamy skin |
| Green Hue | +15 | Olive shift |
| Green Sat | -15 | Less desaturation = retained color |
| Blue Sat | -8 | Retained blue richness |
| Red Sat | +8 | Richer reds |
| Yellow Sat | -5 | Gentle desaturation |
| ColorGrade Shadow | H200/S8 | Warm, saturated shadows |
| ColorGrade Highlight | H45/S10 | Warm, saturated highlights |
| Grain Amount | 25 | Standard Portra grain |
| Grain Size | 25 | Standard |
| Grain Frequency | 45 | Smooth |

---

## STYLEGUIDE Compliance

- No Calibration ✓
- No WB ✓
- Grain → Sharpness=10, Clarity=0, Texture=0, Dehaze=0 ✓
- |Vibrance−Saturation|=2 ≤ 5 ✓
- HSL Sat ≤ ±60 ✓
- All ColorGrade Sat ≤ 30 (for stills) ✓

---

## Sources

- t3mujinpack GitHub — Kodak Portra 400 UC + 400 VC Darktable presets
- Kodak Professional — E-4046 PORTRA Films technical data
- Project's existing Kodak Portra 400 preset (baseline reference)
