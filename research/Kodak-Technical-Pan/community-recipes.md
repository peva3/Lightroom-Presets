# Kodak Technical Pan — Lightroom Preset Settings & Recipes

## Primary Source: t3mujinpack (Darktable Styles)
The t3mujinpack project does not include a dedicated Technical Pan emulation, but the channel mixer approach used for other B&W films can be adapted — Technical Pan requires extended red weighting to simulate its super-panchromatic sensitivity.

Source: https://github.com/t3mujinpack/t3mujinpack

## Community Notes (from forums)
- Technidol developer was the key to pictorial contrast — without it, the film is essentially lithographic
- POTA developer (1,4-Phenylenediamine + sulfite) was the DIY alternative to Technidol
- Some photographers developed Technical Pan in highly dilute Rodinal (1:300) for pictorial contrast
- C-41 development (color negative chemistry) produced surprisingly good low-contrast results
- The film's resolution exceeded most lenses — the lens was the limiting factor, not the film
- NASA used Technical Pan for the Apollo Lunar Orbiter mapping and Skylab solar observations
- Rollei ATP 1.1 (Advanced Technical Pan) is the current spiritual successor, made by Agfa-Gevaert for Maco

## LR Preset Design Notes
- Essentially grainless: GrainAmount=5, Size=10, Roughness=30 (bare minimum grain values)
- Extended red sensitivity: GrayMixer Red +20, Blue -35 (dramatic sky darkening without filters)
- Higher contrast (+35) reflecting Technical Pan's inherent contrast, even with low-contrast development
- Deep blacks (-25) from the extended red sensitivity and high Dmax
- Moderate highlight reduction (-20) to protect the compressed highlight range
- All STYLEGUIDE rules: Sharpness=10 with grain, Clarity/Texture/Dehaze=0, no Calibration, no WB
- The super-panchromatic GrayMixer is the defining characteristic — brighter reds, dramatically darker blues

---

## See Also

- [Kodak Technical Pan — Film Characteristics](../Kodak-Technical-Pan/characteristics.md)
- [Kodak Panatomic X 32 Lightroom Preset](../Kodak-Panatomic-X-32/community-recipes.md)
- [Kodak T Max 100 Lightroom Preset](../Kodak-T-Max-100/community-recipes.md)
- [XMP Preset: Kodak Technical Pan](../../Presets/Black-White/Kodak Technical Pan.xmp)
