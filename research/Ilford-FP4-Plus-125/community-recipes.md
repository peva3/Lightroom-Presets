# Community Recipes — FP4 Plus 125 Emulation in Lightroom

> Compiled from Fuji X Weekly, r/analog, r/Lightroom, and film photography forums.

---

## Fuji X Weekly Recipe (FP4 Look on Fuji Cameras)

**Source**: Fuji X Weekly community

| Setting | Value |
|---------|-------|
| Film Simulation | Monochrome |
| Dynamic Range | DR200 |
| Highlight | -0.5 |
| Shadow | -1.5 |
| Sharpness | 0 |
| Clarity | +2 |
| Grain Effect | Weak / Large |
| White Balance | Daylight, +6 Red / -8 Blue |

**Translation to Lightroom B&W:**
- Highlight -0.5 → Highlights2012 -5
- Shadow -1.5 → Shadows2012 +15 (inverted: -10 × shadow_value)
- Sharpness 0 → Sharpness 10 (capped per grain rules)
- Clarity +2 → Clarity2012 0 (overridden per STYLEGUIDE grain protection)
- Grain Weak → GrainAmount 20
- Grain Large → GrainSize 35
- WB +6R/-8B → GrayMixer Red +30, Blue -40

---

## Community Core Settings for FP4+ Look

### Basic Panel

FP4+ is medium-contrast, fine-grain, with a neutral tonal palette:

| Setting | Value | Notes |
|---------|-------|-------|
| Contrast | +15 to +25 | Moderate, clean contrast |
| Highlights | -15 to -25 | Good highlight retention |
| Shadows | +10 to +20 | Open but not flattened shadows |
| Whites | +5 to +15 | Clean whites |
| Blacks | -15 to -25 | Deep but not crushed blacks |

### B&W Mix

FP4+ has balanced panchromatic sensitivity — no strong spectral biases:

| Channel | Value | Notes |
|---------|-------|-------|
| Red | +25 to +35 | From WB +6R translation |
| Orange | +5 to +15 | Natural skin |
| Yellow | 0 to +10 | Subtle highlight warmth |
| Green | -5 to 0 | Near-neutral foliage |
| Aqua | -5 to -15 | Cool tone darkening |
| Blue | -35 to -45 | From WB -8B translation, dramatic sky |
| Purple | 0 | Neutral |
| Magenta | 0 | Neutral |

### Grain (from STYLEGUIDE FP4+ table)

| Setting | Value |
|---------|-------|
| Amount | 15-25 |
| Size | 20-30 |
| Roughness | 45-55 |

---

## Community Data Validation

### Validity Assessment: GOOD

FP4+ is well-understood in community recipes. The Fuji X Weekly recipe provides clear translation data. The film occupies a clear position: finer than HP5+, coarser than Pan F, with the most neutral spectral response of the Ilford line.

### Sources Assessment

| Source | Verifiability | Relevance |
|--------|--------------|-----------|
| Fuji X Weekly | High (active site) | High — concrete Fuji→LR translation data |
| Ilford datasheet | High (manufacturer) | High — RMS, spectral sensitivity |
| r/analog | Medium | Medium — less discussed than HP5+/Tri-X |
| Photrio | High (archive) | High — developer comparison data |
