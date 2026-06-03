# Agfa APX 100 — Lightroom Preset Settings & Recipes

## Primary Source: t3mujinpack (Darktable Styles)

The t3mujinpack project includes an Agfa APX 100 emulation using Channel Mixer and Lab Tone Curves.

### t3mujinpack Approach
- Channel Mixer (RGB) for B&W conversion — slightly different ratios from APX 25
- Lab Tone Curve tailored to APX 100's moderate contrast response
- Base style that assumes prior exposure/white balance correction

Source: https://github.com/t3mujinpack/t3mujinpack

### Community Notes (from forums)
- Agfa APX 100 @ EI 200 in Rodinal 1+25 was a common push combination — increased grain and contrast with good results
- Noted for its pleasing, natural skin tone rendering in B&W portraiture
- Many photographers used it as their everyday film before going digital
- Highly regarded as a "sleeper" film — not as famous as Tri-X or HP5+ but beloved by those who used it

### LR Preset Design Notes
- Fine but visible grain — GrainAmount=25, moderate Size and Roughness
- Moderate contrast (+25) reflecting APX 100's character
- Higher Whites and deeper Blacks than APX 25 for more tonal punch
- GrayMixer favors slightly brighter oranges (skin tones) and neutral-cool background separation
- All STYLEGUIDE rules: Sharpness=10 with grain, Clarity/Texture/Dehaze=0, no Calibration, no WB
- Channels represent Agfa's ortho-panchromatic sensitivity — slightly reduced red response

---

## See Also

- [Agfa APX 100 — Film Characteristics](../Agfa-APX-100/characteristics.md)
- [Agfa APX 25 Lightroom Preset](../Agfa-APX-25/community-recipes.md)
- [Agfa APX 400 Lightroom Preset](../Agfa-APX-400/community-recipes.md)
- [Kodak Tri X 400 Lightroom Preset](../Kodak-Tri-X-400/community-recipes.md)
- [XMP Preset: Agfa APX 100](../../Presets/Black-White/Agfa APX 100.xmp)
