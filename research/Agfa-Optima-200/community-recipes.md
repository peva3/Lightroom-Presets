# Agfa Optima 200 — Lightroom Preset Settings & Recipes

---

## Recipe Availability

### Fuji X Weekly (Dedicated Recipe)
- **Agfa Optima 200** (X-Trans III/IV, 2021-11-03): Pro 400H base. This was the "Recipe of the Month" for November 2021 and featured in SOOC Episode 05.
- **Agfa Optima** (X-Trans II, 2020-03-22): Provia base — the earlier version

### Key Community Observations
- "This recipe isn't usually my first choice for colorful landscapes, but trying recipes in various situations is a part of the fun" — Ritchie Roesch
- The recipe was featured across multiple FJW articles as a top indoor/natural-light recommendation
- Community consensus: warm, gently golden, versatile for snapshots and portraits

## Derived Values (from Fuji X Weekly Agfa Optima 200)

### Approach
Based on the Agfa Optima 200 recipe and its relationship to Optima 100:
- **From Optima 100 preset**: Shares the golden warmth DNA
- **Key differences**: Slightly more contrast, marginally more saturation, visible ISO 200 grain
- **ColorGrade**: Similar golden pattern but slightly more prominent

### Key Derivation Rules
1. **Contrast**: Slightly more than Optima 100 (-5) → 0 (neutral, subtle lift)
2. **Golden glow**: Stronger than Optima 100 — Highlight Sat 10 (vs 8)
3. **Saturation**: Slightly higher than Optima 100 — Sat -5 (vs -10)
4. **Grain**: ISO 200 consumer neg — Amount 25, Size 25
5. **Warmth**: More prominent — Midtone Sat 8 (vs 5)
6. **Green handling**: Same European forest green pattern

### Preset Values
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Contrast | 0 | Neutral (slightly more than Optima 100) |
| Highlights | -18 | Slightly more compression than ISO 100 |
| Shadows | +18 | Slight shadow lift |
| Whites | +8 | Gentle brightness |
| Blacks | -18 | Softer blacks than Optima 100 |
| Saturation | -5 | Less desaturated than Optima 100 |
| Vibrance | -2 | Within 5 of Saturation (diff=3) |
| HSL Red Hue | +5 | Warm red |
| HSL Orange Sat | -3 | Skin tone restraint |
| HSL Yellow Hue | -5 | Toward golden |
| HSL Green Hue | +10 | Yellow-green (European forest) |
| HSL Green Sat | -8 | Subdued foliage |
| HSL Blue Sat | -3 | Muted skies |
| ColorGrade Shadow Hue | 40 | Warm shadow |
| ColorGrade Shadow Sat | 6 | Slightly warmer shadows |
| ColorGrade Midtone Hue | 45 | Golden midtone |
| ColorGrade Midtone Sat | 8 | Noticeable golden glow |
| ColorGrade Highlight Hue | 45 | Golden highlight |
| ColorGrade Highlight Sat | 10 | Prominent golden warmth |
| Grain Amount | 25 | ISO 200 consumer grain |
| Grain Size | 25 | Medium consumer grain |
| Grain Roughness | 50 | Moderate texture |
| Sharpness | 10 | Grain protection |

## References
- Fuji X Weekly: "Recipe of the Month: Agfa Optima 200" (2021-11-03)
- Fuji X Weekly: "SOOC – SE01E05 – Agfa Optima 200" (2021-11-19)
- FJW SOOC Episode 05 Viewer Images (2021-12-07)
- Multiple FJW articles recommending Agfa Optima 200 for indoor/natural light
- r/analog: Agfa Optima 200 user experiences

## Community Data Validation

### Validity Assessment: GOOD

**Overall Status**: The most well-documented of the Agfa Optima family. Fuji X Weekly dedicated an entire SOOC episode and "Recipe of the Month" feature to Agfa Optima 200. Multiple appearances in "Which Recipe When" guides confirm its community adoption.

### Self-Consistency Check
| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (-2 vs -5, diff=3) |
| GrainAmount > 0 → Sharpness=10 | ✓ |
| GrainAmount > 0 → Clarity=0, Texture=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ |
| Blacks ≥ -30 | ✓ (-18) |
| Color-Negative neutral curve | ✓ |

### Film Stock Behavior Check
| Behavior | Expected | XMP Implementation | Verdict |
|----------|---------|-------------------|---------|
| Golden warmth | Yes | ColorGrade Midtone H45, Highlight H45 | ✓ |
| More saturated than ISO 100 | Yes | Sat -5 vs -10 for Optima 100 | ✓ |
| ISO 200 grain | Yes | Grain 25, Size 25 | ✓ |
| European color | Yes | Green Hue +10, muted blues | ✓ |
| Warm neutral cast | Yes | Shadow Hue 40, Sat 6 | ✓ |

---

## See Also

- [Agfa Optima 200 — Film Characteristics](../Agfa-Optima-200/characteristics.md)
- [Agfa Optima 100 Lightroom Preset](../Agfa-Optima-100/community-recipes.md)
- [Agfa Vista 200 Lightroom Preset](../Agfa-Vista-200/community-recipes.md)
- [Kodak Portra 400 Lightroom Preset](../Kodak-Portra-400/community-recipes.md)
- [XMP Preset: Agfa Optima 200](../../Presets/Color-Negative/Agfa Optima 200.xmp)
