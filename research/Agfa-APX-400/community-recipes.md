# Agfa APX 400 — Lightroom Preset Settings & Recipes

## Primary Source: Fuji X Weekly (Ritchie Roesch, April 2019)
Ritchie Roesch created a Fujifilm Acros-based recipe that approximates the Agfa APX 400 look. Not a direct emulation, but inspired by the film's character.

### Fuji X Weekly Recipe (Fujifilm X-Trans IV)
- **Film Simulation**: Acros (Acros+Y, Acros+R, Acros+G)
- **Dynamic Range**: DR400
- **Highlight**: -2
- **Shadow**: +4
- **Noise Reduction**: -4
- **Sharpening**: +4
- **Grain Effect**: Weak
- **Color Chrome Effect**: Strong
- **Toning**: +1 (warm)
- **ISO**: Auto up to ISO 12800
- **Exposure Compensation**: +2/3 to +1-1/3

Source: https://fujixweekly.com/2019/04/18/

### Community Notes (from forums)
- The original APX 400 (Agfa-Gevaert) was beloved for its balance of speed, grain, and price
- Rodinal 1+25 was the classic developer combination — produced pronounced but organic grain
- Pushed to EI 800 in Rodinal: grain becomes prominent but structured, contrast increases
- Pushed to EI 1600 in XTOL: usable with heavy grain, good for dramatic street photography
- Current AgfaPhoto APX 400 (post-2013) is reportedly Kentmere Pan 400 — different film entirely
- The original was compared to Ilford HP5+ but with slightly more grain and character

### LR Preset Design Notes
- Moderate grain: GrainAmount=40, Size=35, Roughness=55 (between APX 100 and Kentmere 400)
- Moderate contrast (+25) — more punch than APX 100
- Agfa panchromatic signature: GrayMixer Red +20, Blue -25
- Good highlight retention (-15) and modest shadow lift (+15)
- Deeper blacks than APX 100 (-25 vs -20) — the faster Agfa had richer blacks
- All STYLEGUIDE rules: Sharpness=10 with grain, Clarity/Texture/Dehaze=0, no Calibration, no WB
- The film family consistency with APX 25/100 is important — same panchromatic GrayMixer ratios

---

## See Also

- [Agfa APX 400 — Film Characteristics](../Agfa-APX-400/characteristics.md)
- [Agfa APX 25 Lightroom Preset](../Agfa-APX-25/community-recipes.md)
- [Agfa APX 100 Lightroom Preset](../Agfa-APX-100/community-recipes.md)
- [Kodak Tri X 400 Lightroom Preset](../Kodak-Tri-X-400/community-recipes.md)
- [XMP Preset: Agfa APX 400](../../Presets/Black-White/Agfa APX 400.xmp)
