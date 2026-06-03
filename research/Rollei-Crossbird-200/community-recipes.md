# Community Lightroom Recipes — Rollei Crossbird 200

---

## Recipe Availability

**No dedicated Fuji X Weekly or t3mujinpack recipes exist for Rollei Crossbird 200.**

This is a niche experimental film. However, the cross-process (E6→C41) look is well-characterized in the STYLEGUIDE and has established community recipes for the general cross-process aesthetic. Fuji X Weekly has published "Cross Process" recipes for multiple sensor generations as a general cross-process look.

## Derived Values (from Cross-Process Formula + Film Characteristics)

### Approach
The STYLEGUIDE §VI provides the canonical cross-process ColorGrade formula:
```
Shadows:  Hue 160° (green-cyan),  Sat 20-30
Midtones: Hue 70° (yellow-green), Sat 15-20
Highlights: Hue 320° (magenta),   Sat 15-25
Blending: 40 (sharper transitions)
```

Crossbird 200 amplifies this with:
- Even higher contrast (designed-for-xpro)
- Exaggerated green saturation
- More pronounced grain
- Lower dynamic range

### Key Derivation Rules
1. **Contrast**: Extreme for cross-process → +65
2. **Green saturation**: The defining Crossbird characteristic → Green Sat +50 (hyper)
3. **Blue shift**: Strong cyan/teal → Blue Hue -30
4. **ColorGrade**: STYLEGUIDE formula + amplified saturation
5. **Grain**: Prominent → Amount 40, Size 35, Roughness 60
6. **Blacks**: Crushed → -30 (at floor)

### Preset Values
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Contrast | +65 | Extreme cross-process contrast |
| Highlights | -70 | Protect from aggressive blowout |
| Shadows | -25 | Crushed shadow look |
| Whites | +10 | Bright specular highlights |
| Blacks | -30 | Dense crushed blacks (at floor) |
| Saturation | +5 | Slight global boost |
| Vibrance | +8 | Within 5 of Saturation (diff=3)? NO — check: +8-5=3 ≤ 5 ✓ |
| HSL Red Hue | -10 | Toward orange |
| HSL Orange Sat | +15 | Warm highlight saturation |
| HSL Yellow Hue | -10 | Toward green-yellow |
| HSL Yellow Sat | +20 | Boost yellows |
| HSL Green Hue | -25 | Toward yellow-green |
| HSL Green Sat | +50 | Hyper-saturated greens (X-Pro signature) |
| HSL Green Lum | +10 | Brighten greens |
| HSL Aqua Sat | +20 | Cyan saturation |
| HSL Blue Hue | -30 | Toward cyan (dramatic shift) |
| HSL Blue Sat | +15 | Blue saturation |
| HSL Purple Sat | +15 | Magenta spectrum |
| HSL Magenta Sat | +25 | Magenta highlight boost |
| ColorGrade Shadow Hue | 160 | Green-cyan shadows (STYLEGUIDE formula) |
| ColorGrade Shadow Sat | 25 | Strong green shadow cast |
| ColorGrade Midtone Hue | 70 | Yellow-green midtone |
| ColorGrade Midtone Sat | 18 | Present midtone color |
| ColorGrade Highlight Hue | 320 | Magenta highlights (STYLEGUIDE formula) |
| ColorGrade Highlight Sat | 20 | Strong magenta highlight |
| ColorGrade Blending | 40 | Sharp transitions for X-Pro look |
| Grain Amount | 40 | Prominent X-Pro grain |
| Grain Size | 35 | Medium-large grain |
| Grain Roughness | 60 | Rough, textured |
| Sharpness | 10 | Grain protection |

**Vibrance check**: +8 vs +5, diff=3 ≤ 5 ✓

## References
- `Presets/Creative/` — Cross-Processed presets in Creative category
- STYLEGUIDE §VI: Cross-Processed ColorGrade formula
- Fuji X Weekly: "Cross Process" recipes (multiple sensor versions)
- Maco/Rollei Crossbird 200 product info
- r/analog: Cross-processed film examples
- Lomography: Cross-process guides and community examples

## Community Data Validation

### Validity Assessment: FAIR (Derived from Established Formulas)

**Overall Status**: While no Crossbird-specific recipes exist, the cross-process (E6→C41) look is well-characterized. The STYLEGUIDE provides a canonical ColorGrade formula. Values are derived by amplifying that formula for Crossbird's "designed-for-xpro" intensity. The green saturation boost (+50) is the single most important slider — this is the defining visual characteristic of cross-processed color.

### Slider Range Check
| Check | Value | Limit | Pass |
|-------|-------|-------|------|
| HSL Green Sat | +50 | ±60 cap | ✓ |
| All other HSL Sat | ≤ ±30 | ±60 cap | ✓ |
| Blacks | -30 | -30 floor | ✓ |
| Contrast | +65 | 0..100 range | ✓ |

### Self-Consistency Check
| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (+8 vs +5, diff=3) |
| GrainAmount > 0 → Sharpness=10 | ✓ |
| GrainAmount > 0 → Clarity=0, Texture=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ (max +50) |
| Blacks ≥ -30 | ✓ (at floor) |
| Color-Negative neutral curve with Blending=40 | ✓ |

### Film Stock Behavior Check
| Behavior | Expected | XMP Implementation | Verdict |
|----------|---------|-------------------|---------|
| Extreme contrast | Yes | Contrast +65, Highlights -70 | ✓ |
| Hyper green saturation | Yes | Green Sat +50, CG Midtone H70 | ✓ |
| Green-cyan shadows | Yes | CG Shadow H160, Sat 25 | ✓ |
| Magenta highlights | Yes | CG Highlight H320, Sat 20 | ✓ |
| Crushed blacks | Yes | Blacks -30 | ✓ |
| Prominent grain | Yes | Grain 40, Sharpness 10 | ✓ |
| Lo-fi experimental | Yes | Sharp separation (Blending 40) | ✓ |
