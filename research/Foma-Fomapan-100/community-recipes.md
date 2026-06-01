# Foma Fomapan 100 — Community Recipes

## Community Notes (from forums)
- No dedicated Fuji X Weekly recipe exists for Fomapan 100
- Foma films are well-represented on Massive Dev Chart with extensive developer/time data
- Photrio users consistently describe Fomapan 100 as "punchier than expected" for a 100-speed film
- The Rodinal + Fomapan 100 combination is legendary in the budget film community — maximum character
- Reddit r/analog has numerous comparison posts: Fomapan 100 vs Ilford FP4+, vs Kodak T-Max 100
- Forum consensus: Fomapan 100 has more "soul" than Delta/T-Max but less refinement

## Massive Dev Chart Data
- D-76 stock: 7-8 min at 20°C
- Rodinal 1+50: 8-9 min at 20°C (dramatic grain + acutance)
- XTOL stock: 7 min at 20°C (smoother, more modern)
- HC-110 Dilution B: 6 min at 20°C
- Push to 200: add ~30% development time

## t3mujinpack Reference
The t3mujinpack project does not include Fomapan films, but their approach to other traditional-grain B&W films provides methodology for channel mixer derivation.

## LR Preset Design Notes
- Traditional cubic grain: GrainAmount=30, Size=25, Roughness=50
- Moderate contrast (+20) — slightly higher than Western 100-speed equivalents
- Standard panchromatic GrayMixer: Red +25, Orange +18, Blue -25
- Deeper blacks (-25) reflecting Fomapan's character
- Moderate highlight reduction (-15)
- Modest shadow lift (+12)
- All STYLEGUIDE rules: Sharpness=10 with grain, Clarity/Texture/Dehaze=0, no Calibration, no WB
- The higher contrast and deeper blacks distinguish this from gentler 100-speed presets
