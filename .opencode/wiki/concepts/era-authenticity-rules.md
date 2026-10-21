---
title: Era Authenticity Rules (Decade presets)
tags: [presets, decade, grain, dehaze, vibrance, white-balance, research]
sourceRefs: [STYLEGUIDE.md, AGENTS.md, research/Civil War Era/characteristics.md, research/Dust Bowl Documentary/characteristics.md, research/Punk Rock/characteristics.md]
lastReviewed: 2026-10-21
---

# Era Authenticity Rules

Recurring judgement calls that come up when a preset is validated against photographic history rather than against a look. Distilled from the Decade dossier pass of 2026-10-21.

## 1. Grain belongs to the process, not the era

The strongest predictor of a wrong "vintage" preset is grain applied to a grain-free process. Glass-plate processes (daguerreotype, wet collodion) and contact prints (platinum, albumen) have no silver grain; what texture exists is plate mottle, paper tooth or print dirt.

- Daguerreotype: grain-free → `GrainAmount` ≤ 20, best read as surface mottle at high `GrainSize`.
- Wet collodion / albumen: grain-free in the negative and the contact print → fine-grain band or none. `GrainAmount 60` is the pushed-Tri-X band and is never period-correct here.
- Film-era presets (1920s press, FSA, newsreel) may legitimately carry 35–55, because the working object is an enlargement or a dupe print.

See [[wiki/entities/decade-presets]].

## 2. Dehaze is a physical claim

Negative `Dehaze` models atmospheric scattering (dust, mist, smoke in the air). Positive `Dehaze` removes it.

- Dust-storm imagery (Dust Bowl) genuinely needs a small negative value — this is a documented override of the "grain presets keep Clarity/Texture/Dehaze at 0" guard, kept at the minimum effective value (−5) with Clarity/Texture still at 0.
- Flash-lit interiors (Prohibition) do **not**: flash at a few metres defeats veiling, so Dehaze stays 0.
- Pictorialist soft focus uses negative `Clarity` + `Dehaze` as the defining trait, with `GrainAmount 0`, so the grain guard does not bind.

## 3. The Vibrance clause has an escape hatch

STYLEGUIDE §VIII.5: keep `|Vibrance − Saturation| ≤ 5`, **or remove Vibrance entirely**. Almost every sepia preset in the repo needs `Saturation` around −45 to −50 for a global mute and writes no `Vibrance` attribute at all. That is compliance with the second clause, not a violation of the first — but it must be stated in the dossier, because the numeric gap looks alarming on inspection.

## 4. Absolute Temperature is a portability risk, not a period claim

`Temperature` is an absolute Kelvin value, so its effect depends on the raw's as-shot balance. The sepia presets keep it (5800–6000) because the brown axis assumes a warm neutral; Gatsby is the only Decade preset without it, and it produces its warmth entirely downstream in HSL and Color Grading.

## 5. Look vs emulation

A preset that only survives one tonal register is a *look*. The Gatsby Art Deco palette is a Deco material palette plus Autochrome warmth, not a film stock; 1940s newsreel release prints were neutral-to-warm, so the cool blue-grey is a modern war-film convention. Both are declared as looks in their Verification sections rather than sold as accuracy.

## 6. One texture budget per preset

Grain and the local-contrast trio draw on the same budget. Punk Rock (2026-10-21) is the worked example: the preset had `Clarity +20 / Texture +10 / Dehaze +15` and no grain, which reproduced a photocopy but not a photograph. Adding pushed Tri-X grain forced the trio to zero, and the hard look had to be carried by `Contrast +40`, `Blacks −25`, `Highlights −55` and a −18 vignette instead. The lesson: decide which *object* the preset describes — a negative, or a reproduction of a negative — because it can only describe one convincingly.

A related distinction from the same pass: a photocopier is not a grade. Zine pages are halftone dots and toner smears, not local contrast, which is why the reprographic variant belongs in `community-recipes.md` as an alternative build rather than in the preset.

## 7. Sources that actually check out

Library of Congress collection pages block automated fetches (403) but their search snippets and article URLs are reliable to cite. Wikipedia photography-process articles, Met/AIC/ Getty essays, NEDCC leaflets, NARA and BFI preservation pages are all fetchable or citable. Avoid citing Reddit threads for process facts; they are useful for *recipes*, not for history.
