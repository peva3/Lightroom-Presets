# Agfa Scala 200 — Lightroom Preset Settings & Recipes

## Primary Source: Fuji X Weekly (Ritchie Roesch, August 2018)

Ritchie Roesch accidentally created an Agfa Scala simulation while experimenting with his Fujifilm X100F. He noticed the results resembled Scala after shooting with it for several weeks.

### Recipe
- **Film Simulation**: Acros (+Y, +R, +G)
- **Dynamic Range**: DR100
- **Highlight**: +4
- **Shadow**: 0
- **Noise Reduction**: -3
- **Sharpening**: 0
- **Grain Effect**: Weak
- **ISO**: Auto up to ISO 6400
- **Exposure Compensation**: -1/3 to +1/3 (typically)

Source: https://fujixweekly.com/2018/08/12/

### Compatibility
- Originally for X-Trans III (X100F)
- For X-Trans IV: add Color Chrome Effect Off, Color Chrome FX Blue Off

### Key Observations
- Uses Acros as the base film simulation, which Ritchie considers "the closest thing to actual film" in a digital camera
- Only subtly different from his standard Acros recipe, mirroring how real Acros and Scala produce similar results
- The +4 Highlight setting pushes highlights bright for the reversal film punch
- Shadow at 0 preserves shadow detail — reversal film has inherently deep blacks without needing shadow push

### LR Preset Design Notes
- Reversal film character: deep blacks (Blacks=-30), punchy contrast (+35)
- Minimal grain (GrainAmount=20) — reversal film has inherently fine grain
- Clean highlight rolloff with modest Whites boost
- Acros-based tonal signature informs the GrayMixer channels
- All STYLEGUIDE rules applied: Sharpness=10, Clarity/Texture/Dehaze=0, no Calibration, no WB
- The +4 Highlight in Fuji terms translates to slightly pushed Highlights in our XMP for the bright slide-film character

---

## See Also

- [Agfa Scala 200 — Film Characteristics](../Agfa-Scala-200/characteristics.md)
- [Agfa APX 100 Lightroom Preset](../Agfa-APX-100/community-recipes.md)
- [XMP Preset: Agfa Scala 200](../../Presets/Black-White/Agfa Scala 200.xmp)
