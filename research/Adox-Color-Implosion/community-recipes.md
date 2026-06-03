# Community Lightroom Recipes — Adox Color Implosion

---

## Recipe Availability

**No dedicated recipes exist for Adox Color Implosion — from any source (Fuji X Weekly, t3mujinpack, forums, etc.).**

This is the most niche film in this collection. Adox Color Implosion was a deliberately experimental film with intentionally "broken" color science. By its nature, it's hard to recipe-ize — the whole point was that every frame looks different.

## Derived Values (from Film Philosophy + Character Analysis)

### Approach
Emulating Adox Color Implosion requires embracing its anti-perfect philosophy:
- **Selective desaturation**: Most channels are muted, but 1-2 channels "survive" the implosion
- **Low contrast + heavy grain**: The "degraded film" foundation
- **Negative Clarity**: Creates the soft, dreamy bloom of degraded emulsion
- **Unpredictable color pops**: Magenta and yellow tend to survive the implosion more than blue/green
- **The "found footage" aesthetic**: Colors that look like they've been aging for 40 years in an attic

### Key Derivation Rules
1. **Clarity**: -15 (negative — the soft bloom of degraded emulsion)
2. **Dehaze**: -10 (atmospheric haze/fog, adding to the degraded feel)
3. **Contrast**: -20 (compressed tonal range of degraded film)
4. **Selective desaturation**: Blue -40, Green -35, Aqua -30 (channels that "implode")
5. **Color survivors**: Magenta Sat +15, Yellow Sat +10 (colors that survive implosion)
6. **Grain**: Heavy, clustered — Amount 50, Size 40, Roughness 70 
7. **ColorGrade**: Green-brown shadow cast + fading highlights

### Preset Values
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Exposure | -0.10 | Slight underexposure for density |
| Contrast | -20 | Compressed tonal range (degraded film) |
| Highlights | -30 | Soft highlight compression |
| Shadows | +25 | Lift shadow detail |
| Whites | -10 | No bright whites (degraded) |
| Blacks | -10 | Mild black anchor |
| Clarity | -15 | Negative clarity for emulsion bloom |
| Dehaze | -10 | Atmospheric haze (degraded look) |
| Saturation | -25 | Heavy global desaturation |
| Vibrance | -22 | Within 5 of Saturation (diff=3) |
| HSL Red Sat | -10 | Muted reds |
| HSL Orange Sat | -5 | Mild orange |
| HSL Yellow Sat | +10 | Yellow survives implosion |
| HSL Green Sat | -35 | Green implodes heavily |
| HSL Aqua Sat | -30 | Aqua implodes |
| HSL Blue Sat | -40 | Blue is most destroyed |
| HSL Purple Sat | +5 | Purple tends to survive |
| HSL Magenta Sat | +15 | Magenta survives implosion |
| HSL Blue Lum | +10 | Faded blue channel |
| HSL Green Lum | +5 | Faded greens |
| ColorGrade Shadow Hue | 80 | Green-brown shadow cast |
| ColorGrade Shadow Sat | 12 | Present shadow color |
| ColorGrade Highlight Hue | 330 | Faded magenta highlight |
| ColorGrade Highlight Sat | 8 | Subtle highlight cast |
| ColorGrade Blending | 55 | Moderate blending |
| Grain Amount | 50 | Heavy "implosion" grain |
| Grain Size | 40 | Large grain clusters |
| Grain Roughness | 70 | Highly irregular texture |
| Sharpness | 10 | Grain protection mandatory |
| Texture | 0 | Grain protection |
| LuminanceSmoothing | 0 | Grain protection |

## Unique Rule Violations (Intentional)

This preset deliberately violates several STYLEGUIDE norms **by design**, because the film it emulates is intentionally "wrong":

1. **Negative Clarity (-15)**: Normally, grain → Clarity=0. But Color Implosion's defining characteristic is the soft emulsion bloom, which requires negative Clarity. The grain here is not trying to look "authentic" — it's part of the degradation effect.
2. **Negative Dehaze (-10)**: Adds atmospheric fog for the degraded print effect.
3. **Extreme channel desaturation**: Blue -40, Green -35 — these are below the recommended cap for normal presets, but are the defining characteristic of the "implosion" effect.

These violations are **documented exceptions** necessary for the film's artistic intent.

## References
- Adox/Fotoimpex Color Implosion product description
- r/analog: Adox Color Implosion scan examples and reviews
- The "expired film" degradation patterns as reference
- `Presets/Color-Negative/Kodak Gold 200 Expired 30yr.xmp` — expired film as degradation model
- STYLEGUIDE §V: Negative Clarity for bloom effect
- STYLEGUIDE §XI: Negative Dehaze for atmospheric softness

## Community Data Validation

### Validity Assessment: POOR (No Sources Available) — DERIVED

**Overall Status**: Zero community recipes exist. This film is intentionally "broken" and extremely niche. Values are entirely derived from the film's documented philosophy ("deliberately flawed") and visual references from scanned examples. The negative Clarity and Dehaze usage is documented as intentional rule violations in service of the film's anti-perfect aesthetic.

### Slider Range Check
| Check | Value | Limit | Pass |
|-------|-------|-------|------|
| HSL Blue Sat | -40 | ±60 cap | ✓ |
| HSL Green Sat | -35 | ±60 cap | ✓ |
| Clarity | -15 | ±30 safe | ✓ |
| Dehaze | -10 | ±30 safe | ✓ |
| Blacks | -10 | -30 floor | ✓ |
| All other | within range | — | ✓ |

### Self-Consistency Check
| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (-22 vs -25, diff=3) |
| GrainAmount > 0 → Sharpness=10 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ (max -40) |
| Blacks ≥ -30 | ✓ (-10) |
| Color-Negative neutral curve | ✓ |

### Film Stock Behavior Check
| Behavior | Expected | XMP Implementation | Verdict |
|----------|---------|-------------------|---------|
| Intentionally flawed color | Yes | Sat -25 global, selective -40/-35 | ✓ |
| Color survivors (magenta/yellow) | Yes | Magenta +15, Yellow +10 | ✓ |
| Low contrast | Yes | Contrast -20 | ✓ |
| Soft bloom | Yes | Clarity -15 | ✓ |
| Heavy clustered grain | Yes | Grain 50, Size 40, Roughness 70 | ✓ |
| Degraded/atmospheric feel | Yes | Dehaze -10 | ✓ |
| Green-brown shadow cast | Yes | CG Shadow H80, Sat 12 | ✓ |
