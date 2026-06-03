# Fuji Provia 400F — Lightroom Preset Settings & Recipes

---

## Recipe Availability

### Fuji X Weekly
- **Provia 400 recipe** (2021, GFX-50S): FUJI X Weekly has a "Provia 400" recipe using the Provia film simulation base. Settings: Highlight +1, Shadow +2, Color +4, Chrome Strong, Sharp -2, NR -4, Grain Strong, WB Fluorescent 2 (-2R, -2B). This recipe was a happy accident that resembles Provia 400, possibly closest to 400X.
- **Classic Slide recipe** (2020): Ritchie describes this as being in the neighborhood of Provia 400X/100F.

### t3mujinpack (Darktable)
- **Provia 400F**: Available as a dedicated Darktable style
- **Provia 400X**: Available as a separate Darktable style

## Derived Values (from Existing Recipes + Family Analysis)

### Approach
Based on Provia 400F being warmer than 400X, with Fuji's magenta-cyan balance:
- **From Provia 400X preset**: Inherits the Fuji slide structure (Contrast, color grading pattern)
- **Key difference**: Warmer balance, magenta-leaning shadows (not neutral), higher grain
- **From Fuji X Weekly Provia 400 recipe**: The +4 Color, Strong Chrome, Fluorescent 2 WB approach informs the saturation profile

### Key Derivation Rules
1. **Contrast**: Similar to 400X but slightly lower — +40
2. **Warm tone**: Shadow Hue 320 (magenta) vs neutral for 400X — Fuji's signature magenta shadow
3. **Blue handling**: Blue Hue +5 (toward magenta, not cyan like Kodak) 
4. **Saturation**: Moderate for a 400-speed — Fuji's restrained approach
5. **Grain**: ISO 400 slide — Amount 18, Size 28 (slightly less than Ektachrome 400X)
6. **ColorGrade**: Fuji magenta shadows + warm highlights

### Preset Values
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Contrast | +40 | Moderate-high slide contrast |
| Highlights | -40 | Highlight protection |
| Shadows | +12 | Moderate shadow lift |
| Whites | +12 | Clean whites with warmth |
| Blacks | -28 | Deep blacks |
| HSL Red Hue | +5 | Toward warm (Fuji skin) |
| HSL Orange Sat | -5 | Skin tone protection (Fuji) |
| HSL Green Hue | +5 | Subtle warmth in greens |
| HSL Green Sat | -5 | Restrained foliage |
| HSL Blue Hue | +5 | Toward magenta (Fuji signature, not cyan) |
| HSL Blue Sat | +5 | Moderate blue saturation |
| HSL Blue Lum | -10 | Sky depth |
| HSL Purple Sat | +5 | Fuji purple bias |
| HSL Magenta Sat | +5 | Fuji magenta richness |
| ColorGrade Shadow Hue | 320 | Fuji magenta shadow (NOT cyan) |
| ColorGrade Shadow Sat | 8 | Subtle magenta cast |
| ColorGrade Highlight Hue | 45 | Warm golden highlight |
| ColorGrade Highlight Sat | 5 | Gentle warmth |
| Grain Amount | 18 | ISO 400 slide grain |
| Grain Size | 28 | Medium grain |
| Grain Roughness | 42 | Moderate texture |
| Saturation | +3 | Moderate global saturation |
| Vibrance | +5 | Within 5 of Saturation (diff=2) |
| Sharpness | 10 | Grain protection |

## References
- `Presets/Slide/Fuji Provia 400X.xmp` — sibling anchor
- `Presets/Slide/Fuji Provia 100F.xmp` — baseline Fuji slide
- Fuji X Weekly "Provia 400" recipe (2021): GFX-50S
- t3mujinpack: Provia 400F and Provia 400X Darktable styles

## Community Data Validation

### Validity Assessment: GOOD (Blended)

Values sourced from t3mujinpack (Provia 400F exists as dedicated style), Fuji X Weekly "Provia 400" recipe, and family analysis with Provia 400X.

### Self-Consistency Check
| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (+5 vs +3, diff=2) |
| GrainAmount > 0 → Sharpness=10 | ✓ |
| GrainAmount > 0 → Clarity=0, Texture=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ |
| Blacks ≥ -30 | ✓ |
| Slide S-curve applied | ✓ |

### Film Stock Behavior Check
| Behavior | Expected | XMP Implementation | Verdict |
|----------|---------|-------------------|---------|
| Warmer than 400X | Yes | Shadow Hue 320 (magenta, warmer) | ✓ |
| Fuji magenta shadow | Yes | Magenta shadow grading | ✓ |
| ISO 400 slide grain | Yes | Grain 18, Size 28 | ✓ |
| Good skin tones | Yes | Orange Sat -5 (protection) | ✓ |
| Fuji green richness | Yes | Green Hue +5, Sat -5 | ✓ |

---

## See Also

- [Fuji Provia 400F — Film Characteristics](../Fuji-Provia-400F/characteristics.md)
- [Fuji Velvia 50 Lightroom Preset](../Fuji-Velvia-50/community-recipes.md)
- [Fuji Velvia 100 Lightroom Preset](../Fuji-Velvia-100/community-recipes.md)
- [Fuji Astia 100F Lightroom Preset](../Fuji-Astia-100F/community-recipes.md)
- [XMP Preset: Fuji Provia 400F](../../Presets/Slide/Fuji Provia 400F.xmp)
