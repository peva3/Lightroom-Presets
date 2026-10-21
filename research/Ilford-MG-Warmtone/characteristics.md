# Ilford MG Warmtone — Look Characteristics

## Overview
Ilford MG Warmtone is **not a film**. It models a print on ILFORD MULTIGRADE WARM TONE FB
(fibre-base, variable-contrast) paper — one of the reference warmtone papers for B&W darkroom work.
Where the film presets describe a negative, this preset describes the *paper* the negative was
printed on: warm brown-black image tone, a cream/warm-white base, and a response to toners
(selenium pushes it cooler-brown to plum, sepia much warmer).

## Key Characteristics
- **Tonal range**: long, with grade-dependent contrast; at grade 2–3 the paper prints a full scale
  with deep neutral-warm blacks and a slight cream in the highlights
- **Image tone**: warm brown-black, not yellow — the warmth lives mostly in the mid-tones and
  highlights, with shadows staying dark brown rather than going orange
- **Base tint**: the paper base is warm/cream, which lifts the highlights very slightly and gives the
  print its characteristic "old paper" feel
- **Grain**: none from the emulsion; what reads as texture is paper surface (FB gloss/air-dried) plus
  the negative's grain. Any preset grain here is decorative, not physical
- **Contrast control**: variable by grade, so the preset should stay in the moderate band rather than
  hard-crushing

## Visual Signature
- Full-range print with a subtle warm cast sitting over the whole scale
- Highlights creamy rather than paper-white, shadows warm-black rather than inky neutral
- Distinct from Sepia Tone: no strong yellow-orange tint, just a warm bias in a nearly neutral print

## Modeling Notes
- Model the warmth with a small ColorGrade pair (highlight hue ~35–45°, shadow hue ~30–40°, sat
  10–15, mild positive balance for the base/print highlight bias) rather than a global hue shift
- Keep Contrast in the +10 to +20 band (grade 2–3), do not crush blacks — the paper holds shadow
  detail well
- Any `GrainAmount` must be paired with Sharpness ≤ 10 and LuminanceSmoothing 0 (repo grain rule)

## Sources
- ILFORD MULTIGRADE WARM TONE FB product literature (warm image tone, variable contrast, fibre base)
- Darkroom printing references on warmtone papers and their response to selenium/sepia toning

## Validation Sweep 2026-10-21
- **Verdict:** accurate (no prior research file existed — folder created during the sweep)
- **Defining traits checked:** warmtone paper = warm brown-black image over a cream base, moderate grade-2/3 contrast, no hard crush. Preset: Contrast +15, Highlights −10, Shadows +10, Whites +5, Blacks −15 (gentle, consistent with a print rather than a pushed film); warmth via ColorGrade Highlight hue 40 / sat 15 and Shadow hue 35 / sat 12 with Balance +20 — i.e. a warm cast over the whole scale, not a sepia tint (Sepia Tone uses 35/25 with sat 18/12). GrainAmount 25 / GrainSize 20 / Roughness 45 stands in for FB paper texture; Sharpness 10, LuminanceSmoothing 0, Clarity/Texture/Dehaze 0 keep it from turning gritty.
- **Sources:** ILFORD MULTIGRADE WARM TONE FB technical/product data; comparison against Sepia Tone, Selenium Tone and Gold Tone presets in this repo for cast separation.
- **Preset adjustments:** none

## Gap
Folder created during the sweep; no community-recipes.md. There is no film datasheet basis for this
preset — validation is against paper characteristics and the repo's other toning presets.
