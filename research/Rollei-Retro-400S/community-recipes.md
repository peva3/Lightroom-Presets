# Rollei Retro 400S — Community Recipes

## Primary Source: Fuji X Weekly (Ritchie Roesch, January 2025)
Ritchie Roesch created an "Agfa 400S" recipe for the Fujifilm X-T4 ES full-spectrum camera, explicitly inspired by Rollei Retro 400S (Agfa Aviphot 400S aerial film).

### Fuji X Weekly Recipe (Full Spectrum IR, X-T4 ES)
- **Filters**: Tiffen Deep Yellow 15 + Kolari Vision IR Chrome + QB2 Blue
- **Film Simulation**: Acros+R
- **Monochromatic Color**: WC 0 MG 0 (Off)
- **Dynamic Range**: DR200
- **Grain Effect**: Strong, Small
- **Color Chrome Effect**: Off
- **Color Chrome FX Blue**: Off
- **White Balance**: 2500K, +9 Red & -2 Blue
- **Highlight**: +4
- **Shadow**: +4
- **Sharpness**: -1
- **High ISO NR**: -4
- **Clarity**: -2
- **ISO**: Auto, up to ISO 12800

Source: https://fujixweekly.com/2025/01/09/

Note: This recipe requires three specialized filters and a full-spectrum IR camera — not applicable for standard cameras. Our XMP preset derives the super-panchromatic character from the same film physics (extended red sensitivity, aerial surveillance tonality) for general use.

### Community Notes (from forums)
- Also sold as JCH StreetPan 400 (Japan Camera Hunter) — identical emulsion, different packaging
- Astrum Foto 400 and Svema Foto 400 are the same Belgian master roll in Ukraine packaging
- The film's IR capability with R72 filter is well-documented
- Photrio users note that development in Rodinal produces "gritty, dramatic" results
- The anti-halation properties are excellent despite the clear base
- Forum consensus: this film has "personality" — it's not a neutral B&W

## LR Preset Design Notes
- Super-panchromatic GrayMixer: Red +40, Blue -35 (extreme red brightening, dramatic sky darkening)
- Moderate-heavy grain: GrainAmount=45, Size=35, Roughness=55
- Moderate contrast (+22) with aerial film punch
- Highlights pulled significantly (-25) for the aerial film's compressed DR
- Shadow lift (+18) to retain ground detail
- All STYLEGUIDE rules: Sharpness=10 with grain, Clarity/Texture/Dehaze=0, no Calibration, no WB
- The extreme GrayMixer values create the defining super-panchromatic look
