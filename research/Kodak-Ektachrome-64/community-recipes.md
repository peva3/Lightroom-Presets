# Kodak Ektachrome 64 — Lightroom Preset Settings & Recipes

This document compiles available community data for emulating Kodak Ektachrome 64.

---

## Recipe Availability

**No dedicated Fuji X Weekly or t3mujinpack recipes exist for Ektachrome 64 specifically.**

The film is a vintage emulsion that predates most digital-era recipe creation. However, its characteristics can be derived from:
1. Family relationship with Ektachrome E100 (cooler, lower contrast)
2. Relationship with Kodachrome 64 (shared ISO, similar era)
3. Known characteristics of early Ektachrome emulsions from film community sources

## Derived Values (from Film Family Analysis)

### Approach
Ektachrome 64 sits between E100 and Kodachrome 64 in character:
- **From E100**: Inherits the cool-blue shadow signature (Blue Hue shift), clean slide rendering, and ColorGrade shadow coolness
- **From Kodachrome 64**: Shares the ISO 64 gentle grain character, moderate contrast expectations
- **Unique to Ektachrome 64**: Pronounced cyan-leaning blues (stronger than E100), lower contrast, more muted reds

### Key Derivation Rules
1. **Contrast**: Lower than E100 (+42.5) — set to +35 (the vintage slide sweet spot)
2. **Blue Hue**: More cyan than E100 (-12.5) — set to -20 for the pronounced vintage cyan shift
3. **Shadow coolness**: Stronger than E100's H215 — set to H225 (deeper cyan-blue shadow)
4. **Saturation**: Lower than E100 — global Sat -5, reduced channel saturation overall
5. **Reds**: More magenta-muted than E100 — Red Hue -5, Red Sat -10
6. **Grain**: Fine grain for ISO 64 slide — Amount 12, Size 20

### Preset Values
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Contrast | +35 | Lower than E100 (+42.5); vintage slide |
| Highlights | -35 | Moderate highlight protection |
| Shadows | +15 | Slight shadow lift for older film latitude |
| Whites | +10 | Clean but not brilliant whites |
| Blacks | -28 | Deep but not crushed (vintage toe) |
| HSL Blue Hue | -20 | Pronounced cyan lean (signature) |
| HSL Blue Sat | +5 | Boost blue depth |
| HSL Blue Lum | -15 | Darken skies |
| HSL Red Hue | -5 | Toward magenta (vintage) |
| HSL Red Sat | -10 | Muted reds |
| ColorGrade Shadow Hue | 225 | Stronger cyan-blue shadow |
| ColorGrade Shadow Sat | 10 | Present but not heavy |
| ColorGrade Highlight Hue | 40 | Warm highlights for balance |
| ColorGrade Highlight Sat | 3 | Subtle warmth |
| Grain Amount | 12 | Fine slide grain |
| Grain Size | 20 | Small grain |
| Saturation | -5 | Lower global saturation |
| Vibrance | -2.5 | Within 5 of Saturation |

## References

- **Kodak Ektachrome E100 Preset** (family anchor): `Presets/Slide/Kodak Ektachrome E100.xmp`
- **Kodachrome 64**: `Presets/Slide/Kodachrome 64.xmp` — era and ISO reference
- **Photrio**: Discussions on early Ektachrome generations
- **r/analog**: Ektachrome 64 scan examples

## Community Data Validation

### Validity Assessment: FAIR (Derived)

**Overall Status**: No direct community recipes exist. Values are derived from film family analysis and cross-referenced with known Ektachrome characteristics. The derivation follows the established pattern: E100 is the family anchor, and E64 should be recognizably related but distinguished by lower contrast, cooler/cyan-leaning shadows, softer highlight handling, and more muted reds.

### Slider Range Check
All derived values within valid ranges per STYLEGUIDE §XV.

### Self-Consistency Check
| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (-2.5 vs -5, diff=2.5) |
| GrainAmount > 0 → Sharpness=10 | ✓ |
| GrainAmount > 0 → Clarity=0, Texture=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ (max +5) |
| Blacks ≥ -30 | ✓ (-28) |
| Slide S-curve applied | ✓ |

### Sources Assessment
| Source | Verifiability | Relevance |
|--------|--------------|-----------|
| E100 presets (existing) | High | High — family anchor |
| Photrio historical threads | Medium | Medium — technical analysis |
| r/analog scans | Medium | Medium — visual reference |

### Film Stock Behavior Check
| Behavior | Expected | XMP Implementation | Verdict |
|----------|---------|-------------------|---------|
| Lower contrast than E100 | Yes | Contrast +35 vs E100's +42.5 | ✓ |
| Cooler/cyan shadows | Yes | Blue Hue -20, Shadow Hue 225 | ✓ |
| Vintage reds | Yes | Red Hue -5, Red Sat -10 | ✓ |
| Fine ISO 64 grain | Yes | Grain 12, Size 20 | ✓ |
| Moderate saturation | Yes | Sat -5 global, per-channel muted | ✓ |

---

## See Also

- [Kodak Ektachrome 64 — Film Characteristics](../Kodak-Ektachrome-64/characteristics.md)
- [Kodak Ektachrome E100 Lightroom Preset](../Kodak-Ektachrome-E100/community-recipes.md)
- [Kodak Ektachrome 320T Lightroom Preset](../Kodak-Ektachrome-320T/community-recipes.md)
- [Kodak Ektachrome 400X Lightroom Preset](../Kodak-Ektachrome-400X/community-recipes.md)
- [XMP Preset: Kodak Ektachrome 64](../../Presets/Slide/Kodak Ektachrome 64.xmp)
