# Kodak Panatomic-X 32 — Community Recipes

## Primary Source: t3mujinpack (Darktable Styles)
The t3mujinpack project includes a Panatomic-X emulation using Channel Mixer and Lab Tone Curves. The approach uses slightly reduced red channel weight to simulate Panatomic-X's ortho-panchromatic sensitivity.

Source: https://github.com/t3mujinpack/t3mujinpack

## Community Notes (from forums)
- Ansel Adams frequently shot Panatomic-X at EI 25 and developed in dilute HC-110
- Noted for exceptionally long tonal scale — 10+ zones possible
- EKCo (Eastman Kodak Company) discontinued it in 1987 due to declining sales, not quality
- T-Max 100 was the official replacement but has different spectral sensitivity and tonality
- Highly sought after on expired market — well-stored frozen rolls still produce excellent results

## Fuji X Weekly Reference
- No dedicated Fuji X Weekly recipe exists for Panatomic-X
- The film was referenced in the "XPan III" article where Tony Andersen simulated a "Kodak Panatomic-X ISO 32" look using Phase One P65+ CCD + Velvia base (unusual but noteworthy reference)

## LR Preset Design Notes
- Ultra-fine grain is the defining characteristic: GrainAmount=10, Size=15, Roughness=40
- Low contrast (+12) with wide tonal range — these two define Panatomic-X
- Moderate highlights reduction (-10) for the smooth shoulder
- Modest shadow lift (+12) to preserve detail without looking flat
- GrayMixer reflects ortho-panchromatic sensitivity: slightly reduced red (+15), darker blue (-25)
- All STYLEGUIDE rules: Sharpness=10 with grain, Clarity/Texture/Dehaze=0, no Calibration, no WB
- The absence of grain is what makes this preset special — smoothness is the point
