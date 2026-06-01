# Adox Silvermax 21 — Community Recipes

## Community Notes (from forums)
- No dedicated Fuji X Weekly recipe exists for Adox Silvermax 21
- Photrio discussions note the exceptional silver content and resulting deep blacks
- Silvermax developer is specifically formulated for this film — using other developers changes the character
- The film can be reversal-processed using Adox Scala kit to produce B&W slides (marketed as "Adox Scala 160")
- Emulsive reviews emphasize the "wet print look without wet printing"
- 35mmc: compared to Kodak Technical Pan and CMS 20 — Silvermax has more "soul" (more tonality, less clinical)
- Forums note that Silvermax requires precise exposure — the high silver content is unforgiving of errors

## Adox Product Information
- Highest silver content of any commercially available B&W film
- Designed for both negative processing (Silvermax) and reversal processing (Scala)
- The silver content produces Dmax values exceeding standard B&W films
- Anti-halation layer between emulsion and base for clean highlight transitions
- Clear PET base for maximum transparency in scanning/projection

## Massive Dev Chart Data
- Silvermax developer: 10 min at 20°C (ISO 21)
- Rodinal 1+50: 9 min at 20°C
- HC-110 Dilution G: 15 min at 20°C
- D-76 stock: 8 min at 20°C

## LR Preset Design Notes
- Virtually grainless: GrainAmount=8, Size=12, Roughness=35
  - Even less grain than Panatomic-X (8 vs 10)
- High contrast (+40) — the high silver content naturally creates deep blacks and contrast
  - This is the defining tonal characteristic
- Near-orthopanchromatic GrayMixer: Red +10 (slightly reduced), Blue -30 (dramatic sky darkening)
  - The reduced red sensitivity darkens skin slightly, lightens blue skies
- Deepest blacks (-30) — the maximum allowed by STYLEGUIDE
  - The high silver Dmax is the signature feature
- Bright whites (+20) — clean highlights from excellent anti-halation
- Moderate highlight reduction (-15) to protect the compressed highlights
- Minimal shadow lift (+8) — shadows go dark naturally, that's the point
- All STYLEGUIDE rules: Sharpness=10 with grain, Clarity/Texture/Dehaze=0, no Calibration, no WB
- The deep blacks + high contrast + virtual grainlessness create the distinctive "silver gelatin" look
- This is the most "demanding" B&W preset — requires well-exposed source images
