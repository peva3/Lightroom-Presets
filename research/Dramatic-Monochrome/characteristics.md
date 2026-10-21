# Dramatic Monochrome — Look Characteristics

## Overview
Dramatic Monochrome is a creative B&W look inspired by the high-contrast photography of the 1930s-1950s master photographers (Ansel Adams, Andre Kertesz, Robert Doisneau, Weegee, Paul Strand, Elliott Erwitt). It is NOT a specific film emulation but rather a stylistic recipe designed to create dramatic, punchy black-and-white images in-camera.

## Key Characteristics
- **Contrast**: Very high — the defining characteristic
- **Blacks**: Deep, dramatic — shadows that go to black intentionally
- **Highlights**: Bright, luminous — strong tonal separation
- **Grain**: Strong and pronounced — adds to the vintage, dramatic feel
- **Clarity**: High (in Fuji terms) — contributes to edge definition
- **Development Inspiration**: Push-processing and high-contrast paper grades

## Historical Inspiration
- **Ansel Adams**: Zone System mastery — deliberate placement of shadows and highlights
- **Weegee (Arthur Fellig)**: Hard flash, stark contrast, gritty urban scenes
- **Andre Kertesz**: Strong geometric compositions with dramatic tonal separation
- **Robert Doisneau**: French humanist with contrast-rich street photography
- **Paul Strand**: Sharp formal compositions with deep blacks
- **Elliott Erwitt**: Witty observations rendered in rich B&W

## Visual Signature
- Punchy, high-impact contrast
- Deep, dramatic blacks that crush deliberately
- Bright, clean highlights with midtone separation
- Strong grain texture adds vintage character
- Ideal for street photography, photojournalism, and dramatic landscapes

## Sources
- Fuji X Weekly (Ritchie Roesch recipe, February 2020)
- Study of mid-century B&W master photographers

---

## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** not a film emulation — a 1930s–50s high-contrast darkroom look. Defining traits per this folder: very high contrast, deliberate black crush, luminous highlights, strong grain. Preset: Contrast +40, Blacks −30, Whites +25, Highlights −10, GrainAmount 55 / GrainSize 40 / GrainRoughness 70 — all consistent. Note the folder's "Clarity: high" bullet is intentionally *not* implemented (Clarity/Texture/Dehaze all 0): repo rule 9 forbids local-contrast sliders on grain-heavy presets (`GrainAmount > 0` needs Sharpness ≤ 10 and LuminanceSmoothing 0, both satisfied), so the grain and curve carry the drama.
- **Sources:** This folder's characteristics and community-recipes notes (Fuji X Weekly Feb 2020 recipe, mid-century masters); repo STYLEGUIDE.md grain/sharpness safeguards.
- **Preset adjustments:** none
