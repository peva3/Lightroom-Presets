# Fuji Pro 800Z — Community Recipes

> High-speed professional portrait film. Primarily sourced from t3mujinpack Darktable presets and film characteristics.

---

## 1. t3mujinpack Darktable Preset

Source: `github.com/t3mujinpack/t3mujinpack`

The t3mujinpack Fuji Pro 800Z preset uses Lab tone curves for color emulation in Darktable. The preset is designed as a starting point — basic processing (exposure, WB) should be applied first, then the style, then further adjustments.

---

## 2. Film Characteristics Summary (Community-Consensus)

From r/AnalogCommunity and film photography forums:

### Key Traits:
- **Warm-biased** portrait film designed for low light
- **Moderate visible grain** — expected for 800 speed, structured
- **Good highlight latitude** for a high-speed film
- **Skin tones are warm and flattering** — the primary design goal
- **Natural color rendering** with moderate saturation
- **Contrast is moderate** — slightly higher than 400H, lower than consumer 800

### Recommended Shooting:
- Rate at ISO 640–800 for best results
- Overexpose by 1/3 stop for softer grain
- Excellent for indoor/event work with mixed lighting
- Pairs well with TTL flash for wedding receptions

---

## 3. Derived LR Values (from film characteristics)

Since there is no direct Fuji X Weekly recipe for Pro 800Z, values are derived from:
1. PRO 800Z film characteristics (warm bias, moderate grain, portrait skin tones)
2. Comparison with Pro 400H (same family, different speed class)
3. t3mujinpack tone curve character
4. Standard 800-speed film behavior (more grain, slightly higher contrast)

| Attribute | Value | Rationale |
|---|---|---|
| Exposure | +0.33 | Slight overexposure for grain softening |
| Contrast | -5 | Portrait-appropriate soft contrast |
| Highlights | -35 | High-speed film highlight compression |
| Shadows | +25 | Open shadows for low-light work |
| Saturation | -5 | Slight desaturation for portraits |
| Grain Amount | 35 | Moderate visible grain (800 speed) |
| Grain Size | 30 | Characteristic structure |
| Grain Frequency | 50 | Standard roughness |
| Orange Lum | +15 | Portrait skin brightness |
| Green Sat | -15 | Muted greens |
| Blue Sat | -10 | Natural sky |
| ColorGrade Shadow | H220/S5 | Cool shadow anchor |
| ColorGrade Highlight | H40/S8 | Warm portrait highlights |

---

## STYLEGUIDE Compliance

- No Calibration ✓
- No WB ✓
- Grain → Sharpness=10, Clarity=0, Texture=0, Dehaze=0 ✓
- |Vibrance−Saturation|=0 ✓
- HSL Sat ≤ ±60 ✓

---

## Sources

- t3mujinpack GitHub — Fuji Pro 800Z Darktable preset
- r/AnalogCommunity — Pro 800Z threads
- Fujifilm professional product literature (archived)
