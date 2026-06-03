# Kodak Ektachrome 400X — Lightroom Preset Settings & Recipes

---

## Recipe Availability

**No dedicated Fuji X Weekly recipe exists for Ektachrome 400X.**

Fuji X Weekly has Elite Chrome 400 (consumer variant) and the E100 family, but no 400X-specific recipe. The t3mujinpack has Kodak Elite Chrome 400 as a Darktable style.

## Derived Values (from Film Family Analysis)

### Approach
Ektachrome 400X is the high-speed, high-impact Ektachrome:
- **From E100**: Inherits the slide S-curve structure
- **Key differences**: Higher contrast, warmer balance, punchier saturation, more grain
- **ColorGrade**: Less cool shadow, more prominent warm highlights
- Grain is a defining characteristic — more than E100/E200

### Key Derivation Rules
1. **Contrast**: Higher than E100 — +45 (vs +42.5) for punchy action-slide look
2. **Warmth**: Warmer than E100 — Highlight Hue 55 (vs 45)
3. **Saturation**: Higher global saturation — +8 (vs E100's +5)
4. **Blues**: Less cyan, more deep-saturated — Blue Hue -5
5. **Reds**: Punchier than E100 — Red Sat +5
6. **Grain**: ISO 400 slide — Amount 20, Size 30, Roughness 45
7. **Curve**: Slightly more aggressive shadow crush

### Preset Values
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Contrast | +45 | High contrast for ISO 400 slide |
| Highlights | -45 | Protect highlights from the aggressive curve |
| Shadows | +10 | Low shadow lift (slide character) |
| Whites | +15 | Bright whites for projection |
| Blacks | -30 | Deep blacks (at floor) |
| HSL Blue Hue | -5 | Slight warm-blue |
| HSL Blue Sat | +10 | Deep saturated blue |
| HSL Blue Lum | -15 | Dramatic sky darkening |
| HSL Red Hue | +10 | Warm red |
| HSL Red Sat | +5 | Punchy reds for action |
| HSL Orange Sat | +5 | Warm saturation |
| HSL Green Hue | +10 | Yellow-green bias |
| HSL Green Sat | +5 | Slightly vivid greens |
| ColorGrade Shadow Hue | 200 | Neutral-cool shadow (less cyan than E100) |
| ColorGrade Shadow Sat | 8 | Present shadow color |
| ColorGrade Highlight Hue | 55 | Prominent warm highlights |
| ColorGrade Highlight Sat | 6 | Noticeable warmth |
| Grain Amount | 20 | Visible ISO 400 slide grain |
| Grain Size | 30 | Medium grain structure |
| Grain Roughness | 45 | Moderate texture |
| Saturation | +8 | Higher global saturation |
| Vibrance | +3 | Within 5 of Saturation (diff=5) |
| Sharpness | 10 | Grain protection rule |

## References
- `Presets/Slide/Kodak Ektachrome E100.xmp` — family anchor
- `Presets/Slide/Kodak Elite Chrome 400.xmp` — consumer variant
- t3mujinpack: Kodak Elite Chrome 400 Darktable style

## Community Data Validation

### Validity Assessment: FAIR (Derived)

Values derived from family analysis with E100 as anchor, scaled for ISO 400 characteristics.

### Self-Consistency Check
| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (+3 vs +8, diff=5) |
| GrainAmount > 0 → Sharpness=10 | ✓ |
| GrainAmount > 0 → Clarity=0, Texture=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ (max +10) |
| Blacks ≥ -30 | ✓ (at floor) |
| Slide S-curve applied | ✓ |

---

## See Also

- [Kodak Ektachrome 400X — Film Characteristics](../Kodak-Ektachrome-400X/characteristics.md)
- [Kodak Ektachrome E100 Lightroom Preset](../Kodak-Ektachrome-E100/community-recipes.md)
- [Kodak Ektachrome 320T Lightroom Preset](../Kodak-Ektachrome-320T/community-recipes.md)
- [Kodak Ektachrome 64 Lightroom Preset](../Kodak-Ektachrome-64/community-recipes.md)
- [XMP Preset: Kodak Ektachrome 400X](../../Presets/Slide/Kodak Ektachrome 400X.xmp)
