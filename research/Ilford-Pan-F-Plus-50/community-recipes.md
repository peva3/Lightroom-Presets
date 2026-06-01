# Community Recipes — Pan F Plus 50 Emulation in Lightroom

> Compiled from Fuji X Weekly, r/analog, r/Lightroom, and film photography forums.

---

## Fuji X Weekly Recipe (Pan F Look on Fuji Cameras)

**Source**: Fuji X Weekly community

| Setting | Value |
|---------|-------|
| Film Simulation | Monochrome (not Acros — cleaner grain) |
| Dynamic Range | DR100 |
| Highlight | 0 |
| Shadow | +1 |
| Noise Reduction | -4 |
| Sharpness | 0 |
| Clarity | +2 |
| Grain Effect | Weak / Large |
| White Balance | Daylight, +1 Red / -6 Blue |

**Translation to Lightroom B&W:**
- Highlight 0 → Highlights2012 0
- Shadow +1 → Shadows2012 -10 (inverted linear mapping)
- Sharpness 0 → Sharpness 10 (capped per grain rules)
- Clarity +2 → Clarity2012 0 (overridden per STYLEGUIDE grain protection)
- Grain Weak → GrainAmount 20
- Grain Large → GrainSize 35
- WB +1R/-6B → GrayMixer Red +5, Blue -30

---

## Community Core Settings for Pan F Look

### Basic Panel

Pan F is high-contrast, fine-grain. Community consensus:

| Setting | Value | Notes |
|---------|-------|-------|
| Contrast | +25 to +35 | High native contrast of Pan F |
| Highlights | -20 to -30 | Protect highlight detail |
| Shadows | +10 to +20 | Moderate shadow lift |
| Whites | +5 to +15 | Clean whites |
| Blacks | -20 to -30 | Deep, rich blacks |

### B&W Mix

Pan F has slightly reduced red sensitivity (ortho-panchromatic), giving more sculpted skin tones:

| Channel | Value | Notes |
|---------|-------|-------|
| Red | 0 to +10 | Slight skin lift, not aggressive |
| Orange | 0 to +10 | Subtle skin |
| Yellow | 0 to +5 | Neutral |
| Green | 0 to -5 | Slight foliage darkening |
| Aqua | 0 to -5 | Neutral cool |
| Blue | -25 to -35 | Dramatic sky (from WB -6B translation) |
| Purple | 0 | Neutral |
| Magenta | 0 | Neutral |

### Grain (from STYLEGUIDE Pan F table)

| Setting | Value |
|---------|-------|
| Amount | 10-20 |
| Size | 15-25 |
| Roughness | 45-55 |

---

## Community Data Validation

### Validity Assessment: GOOD

Pan F Plus is less commonly emulated than Tri-X or HP5+, but the Fuji X Weekly recipe provides a solid translation foundation. The film's defining characteristics (ultra-fine grain, high contrast, ortho-panchromatic sensitivity) are well understood.

### Sources Assessment

| Source | Verifiability | Relevance |
|--------|--------------|-----------|
| Fuji X Weekly | High (active site) | High — provides concrete Fuji→LR translation data |
| Ilford datasheet | High (manufacturer) | High — RMS granularity, spectral sensitivity, contrast |
| r/analog | Medium | Medium — less Pan F discussion than HP5/Tri-X |
