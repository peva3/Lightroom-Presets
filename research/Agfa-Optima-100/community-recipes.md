# Agfa Optima 100 — Lightroom Preset Settings & Recipes

---

## Recipe Availability

### Fuji X Weekly
- **Agfa Optima** (X-Trans II, 2020-03-22): Provia base, Highlight -1, Shadow +1, Color -2, Sharp 0, NR -2, WB Daylight (-3R, +1B)
- **Agfa Optima 200** (X-Trans III/IV, 2021-11-03): Pro 400H base — this is the X-Trans III/IV version mentioned in numerous FJW articles

### Key Community Observations
- "Agfa Optima is a color negative film that was around from the mid-1990's to the mid-2000's" — Ritchie Roesch, FJW
- The film was noted for its subtle golden warmth and European color character
- The FJW recipe uses Provia as the base, with -2 Color (desaturation) and Daylight WB shifted -3 Red, +1 Blue

## Derived Values (from Fuji X Weekly Agfa Optima Recipe)

### Approach
Translating the Fuji X Weekly Agfa Optima recipe to Lightroom XMP values:
- **Provia base → Adobe Color profile** (color negative)
- **Highlight -1 → Highlights -15** (consumer film highlight compression)
- **Shadow +1 → Shadows +15** (slight shadow lift for consumer latitude)
- **Color -2 → Saturation -10** (restrained European color)
- **WB Daylight (-3R, +1B) → ColorGrade** (warmth through grading, not WB)

### Key Derivation Rules
1. **Contrast**: Consumer film = low contrast → -5 (vs neutral 0)
2. **Golden glow**: ColorGrade Highlight Hue 45, Sat 8 (golden highlight warmth)
3. **Restrained color**: Global Saturation -10, Vibrance -5 (the "Color -2" equivalent)
4. **Warm midtones**: ColorGrade Midtone Hue 40, Sat 5 (the Optima golden signature)
5. **Green handling**: European forest greens — Green Hue +10 (toward yellow), Green Sat -10
6. **Grain**: ISO 100 consumer neg — Amount 20, Size 22

### Preset Values
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Contrast | -5 | Low consumer contrast |
| Highlights | -15 | Highlight compression |
| Shadows | +15 | Shadow lift (consumer latitude) |
| Whites | +5 | Subtle brightness |
| Blacks | -15 | Gentle blacks |
| Saturation | -10 | "Color -2" equivalent |
| Vibrance | -5 | Within 5 of Saturation (diff=5) |
| HSL Red Hue | +5 | Slightly warm red |
| HSL Orange Sat | -5 | Skin tone restraint |
| HSL Yellow Sat | -5 | Muted yellow warmth |
| HSL Green Hue | +10 | Toward yellow-green (European forest) |
| HSL Green Sat | -10 | Subdued foliage |
| HSL Blue Sat | -5 | Muted skies |
| ColorGrade Shadow Hue | 35 | Warm brown shadow |
| ColorGrade Shadow Sat | 5 | Subtle shadow warmth |
| ColorGrade Midtone Hue | 40 | Golden midtone warmth |
| ColorGrade Midtone Sat | 5 | Subtle golden glow |
| ColorGrade Highlight Hue | 45 | Golden highlight |
| ColorGrade Highlight Sat | 8 | Noticeable golden warmth |
| Grain Amount | 20 | Consumer color neg grain |
| Grain Size | 22 | Fine consumer grain |
| Grain Roughness | 45 | Moderate texture |
| Sharpness | 10 | Grain protection |

## References
- Fuji X Weekly: "Fujifilm X-T1 Agfa Optima (Provia) Film Simulation Recipe" (2020-03-22)
- Fuji X Weekly: "Recipe of the Month: Agfa Optima 200" (2021-11-03)
- FJW SOOC Episodes 04-06 (Agfa Optima 200 discussions)
- Community comments on FJW Agfa Optima recipe posts
- r/analog: Agfa Optima discussions

## Community Data Validation

### Validity Assessment: GOOD

**Overall Status**: Well-sourced from Fuji X Weekly (Ritchie Roesch), the primary authority on film simulation recipes. The X-Trans II Agfa Optima recipe is explicitly documented with slider values. Lightroom translation follows established patterns for converting Fuji JPEG settings to XMP attributes.

### Self-Consistency Check
| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (-5 vs -10, diff=5) |
| GrainAmount > 0 → Sharpness=10 | ✓ |
| GrainAmount > 0 → Clarity=0, Texture=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ (max -10) |
| Blacks ≥ -30 | ✓ (-15) |
| Color-Negative neutral curve | ✓ |

### Film Stock Behavior Check
| Behavior | Expected | XMP Implementation | Verdict |
|----------|---------|-------------------|---------|
| Golden warmth | Yes | ColorGrade: Midtone H40, Highlight H45 | ✓ |
| Restrained color | Yes | Sat -10, Vibrance -5 | ✓ |
| Low contrast | Yes | Contrast -5 | ✓ |
| European green | Yes | Green Hue +10, Sat -10 | ✓ |
| Consumer film grain | Yes | Grain 20, Size 22, Sharpness 10 | ✓ |

---

## See Also

- [Agfa Optima 100 — Film Characteristics](../Agfa-Optima-100/characteristics.md)
- [Agfa Optima 200 Lightroom Preset](../Agfa-Optima-200/community-recipes.md)
- [Agfa Vista 100 Lightroom Preset](../Agfa-Vista-100/community-recipes.md)
- [Kodak Portra 160 Lightroom Preset](../Kodak-Portra-160/community-recipes.md)
- [XMP Preset: Agfa Optima 100](../../Presets/Color-Negative/Agfa Optima 100.xmp)
