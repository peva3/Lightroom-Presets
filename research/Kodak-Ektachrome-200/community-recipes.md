# Kodak Ektachrome 200 — Lightroom Preset Settings & Recipes

---

## Recipe Availability

**No dedicated Fuji X Weekly recipe exists for Ektachrome 200.**

The Fuji X Weekly "Retro Color" recipe (Patron Early-Access, 2025) mentions some similarity to Ektachrome 200 prints from the 1970s, but is not a dedicated emulation. The Elite Chrome 200 recipe (Fuji X Weekly) emulates the consumer-grade version.

## Derived Values (from Film Family Analysis)

### Approach
Ektachrome 200 is the middle-ground Ektachrome:
- **From E100**: Inherits the slide contrast structure and ColorGrade pattern
- **Key differences**: Warmer neutral balance, slightly lower contrast, more grain
- **ColorGrade**: Less cool shadow bias than E100 — more neutral-cool

### Key Derivation Rules
1. **Contrast**: Slightly lower than E100 — +38 (vs +42.5)
2. **Blue Hue**: Less cyan than E100 (-12.5) — set to -8 (warmer blue)
3. **Shadow coolness**: Muted compared to E100 — Shadow Hue 210 (vs 215)
4. **Warmer midtones**: Highlight Hue 50 (vs E100's 45)
5. **Grain**: ISO 200 slide — Amount 15, Size 22
6. **Red handling**: Slightly warmer reds — less muted than E100

### Preset Values
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Contrast | +38 | Slightly lower than E100 |
| Highlights | -38 | Moderate highlight protection |
| Shadows | +18 | Slight shadow visibility |
| Whites | +12 | Clean whites |
| Blacks | -28 | Deep slide blacks |
| HSL Blue Hue | -8 | Warmer blue (less cyan than E64/E100) |
| HSL Blue Sat | +5 | Moderate blue saturation |
| HSL Blue Lum | -12 | Darken skies |
| HSL Red Hue | +5 | Toward warm (portrait-friendly) |
| HSL Red Sat | 0 | Neutral red saturation |
| HSL Green Hue | +10 | Slight yellow-green bias |
| HSL Green Sat | -5 | Subdued greens |
| ColorGrade Shadow Hue | 210 | Neutral-cool shadow |
| ColorGrade Shadow Sat | 6 | Subtle shadow color |
| ColorGrade Highlight Hue | 50 | Warmer highlight |
| ColorGrade Highlight Sat | 4 | Gentle warmth |
| Grain Amount | 15 | ISO 200 slide grain |
| Grain Size | 22 | Fine-medium grain |
| Saturation | +2 | Slightly positive (warmer film) |
| Vibrance | +4 | Within 5 of Saturation |

## References
- `Presets/Slide/Kodak Ektachrome E100.xmp` — family anchor
- `Presets/Slide/Elite Chrome 200.xmp` — consumer variant
- Fuji X Weekly "Retro Color" recipe — tangential mention
- Photrio: Ektachrome 200 discussion threads

## Community Data Validation

### Validity Assessment: FAIR (Derived)

Values derived from family analysis with E100 as anchor, adjusted for warmer balance and ISO 200 characteristics.

### Self-Consistency Check
| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (+4 vs +2, diff=2) |
| GrainAmount > 0 → Sharpness=10 | ✓ |
| GrainAmount > 0 → Clarity=0, Texture=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ |
| Blacks ≥ -30 | ✓ |
| Slide S-curve applied | ✓ |

---

## See Also

- [Kodak Ektachrome 200 — Film Characteristics](../Kodak-Ektachrome-200/characteristics.md)
- [Kodak Ektachrome E100 Lightroom Preset](../Kodak-Ektachrome-E100/community-recipes.md)
- [Kodak Ektachrome 320T Lightroom Preset](../Kodak-Ektachrome-320T/community-recipes.md)
- [Kodak Ektachrome 64 Lightroom Preset](../Kodak-Ektachrome-64/community-recipes.md)
- [XMP Preset: Kodak Ektachrome 200](../../Presets/Slide/Kodak Ektachrome 200.xmp)
