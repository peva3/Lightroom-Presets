# Copper Tone — Look Characteristics

## Overview
Copper Tone is not a film emulation. It reproduces a **copper-toned silver gelatin print**: a
finished B&W print put through a copper toner (typically a ferrocyanide/copper sulphate bleach-redevelop
bath), which converts part of the image silver to copper ferrocyanide. The result keeps the
photograph's full tonal range but shifts the silver to a warm reddish-brown — visibly warmer and
redder than sepia, and less yellow than gold or sulphide toning.

## Key Characteristics
- **Tonal range**: unchanged from the underlying print; copper toning tints rather than fades
- **Colour**: reddish copper / rust brown, roughly a 15–30° hue on the HSL wheel, saturated in the
  upper mid-tones and highlights where silver density is being converted, weaker in deep shadows
- **Contrast**: unchanged; toners do not compress the curve (unlike bleach-bypass looks)
- **Split**: real copper toning acts most strongly on the mid-tones and highlights, so a positive
  ColorGrade balance (highlight-weighted) is the faithful way to model it
- **Grain**: whatever the source print had — this preset is not grain-defined

## Visual Signature
- Warm, metallic red-brown cast over a still-complete monochrome scale
- Reads as a darkroom print, not as a digital filter: blacks stay black, highlights go warm rather
  than cream
- Often paired with warmtone papers; the copper cast is stronger in the mid-tones than at the ends

## Modeling Notes
- Use `ColorGradeHighlightHue` / `ColorGradeShadowHue` in the 15–30° band, saturation ~10–18, with a
  positive `ColorGradeBalance` so highlights carry more of the cast
- Keep `Saturation` at 0 — the cast must come from ColorGrade, never from a global desaturation trick
- Do not add calibration or WB shifts; the underlying render stays neutral

## Sources
- Darkroom toning references (copper toner formulations, bleach-redevelop behaviour)
- Print-toning hue comparisons: sepia (~35–45°), copper (~15–25°), gold (~45–50° warm / cool-purple
  variants depending on process and paper)

## Validation Sweep 2026-10-21
- **Verdict:** accurate (no prior research file existed — folder created during the sweep)
- **Defining traits checked:** copper toner = warm reddish-brown that tints mid-tones/highlights while preserving black and white ends. Preset: ColorGrade Highlight hue 20 / sat 15, Shadow hue 15 / sat 12, Balance +20 (highlight-weighted), Sat 0 elsewhere; tone curve neutral, Contrast +20 with Highlights −15 / Shadows +15 so the print's scale survives. Hue lands in the copper band (below Sepia Tone's 35°, well below Gold Tone's 48°), and the two-stop spread between highlight (20°) and shadow (15°) hues keeps the shadows from going pink. GrainAmount 35 / GrainSize 25 is a print-texture nod, not a claim about the toner; Sharpness 10 and LuminanceSmoothing 0 satisfy the repo grain rule.
- **Sources:** standard copper-toner chemistry descriptions (ferrocyanide bleach + copper sulphate redevelop) and darkroom print-toning hue charts; comparison against the Gold Tone (48/40) and Sepia Tone (35/25) presets in this repo for hue separation.
- **Preset adjustments:** none

## Gap
This folder was missing before the sweep. No community-recipes.md exists; the preset was validated
from toning chemistry and from cross-comparison with the other toning presets rather than from a
collected recipe set.
