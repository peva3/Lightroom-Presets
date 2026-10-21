---
title: Decade Presets (25 era presets)
tags: [presets, decade, category]
sourceRefs: [Presets/Decade/, docs/decade.md, research/Summer of Love/, research/Earth Tones/, research/Disco Warm/, research/Punk Rock/, research/New Wave/, research/Miami Vice/]
lastReviewed: 2026-10-21
---

# Decade Presets

25 presets in `Presets/Decade/`, spanning 1840s daguerreotype to 2000s digicam. All follow the repo's structural boilerplate (ProcessVersion 15.4, `crs:Look`, neutral `ToneCurvePV2012`).

## The historical block (full dossiers)

Thirteen presets now carry a full research dossier (`characteristics.md` + `community-recipes.md`) and a declared tonal register.

### Pre-1945 processes

| Preset | Process / source | Register | Grain |
|---|---|---|---|
| Civil War Era | wet collodion → albumen print, 1861–65 | sepia-toned (mid-contrast) | 20 / 25 / 50 |
| Victorian Daguerreotype | silvered copper plate, 1839–1850s | sepia-toned (low-key) | 18 / 38 / 70 |
| Edwardian Pictorialist | platinum / gum / photogravure, 1900s | neutral (soft, high-key) | 0 |
| Prohibition Sepia | 4×5 press camera, flash powder, rotogravure | sepia-toned | 40 / 32 / 65 |
| Gatsby Art Deco | Deco palette + Autochrome colour, 1920s | warm-golden | 35 / 30 / 60 |
| Dust Bowl Documentary | FSA/OWI file prints, 1935–43 | warm-golden (muted) | 45 / 32 / 65 |
| WWII Newsreel | 35mm nitrate newsreel release print | cool-overcast | 50 / 35 / 70 |

### Post-1945 colour and print

| Preset | Process / source | Register | Grain |
|---|---|---|---|
| Summer of Love | 1967 Kodachrome / Ektachrome slide printed hot | warm-golden, high-key end | 0 (plus `Temperature 5800`) |
| Earth Tones | 1970s C-41 consumer negative, aged print | warm-golden, low-saturation | 25 / 28 / 55 |
| Disco Warm | direct flash + pushed 400 colour negative, tungsten | low-key amber | 20 / 26 / 50 |
| Punk Rock | pushed Tri-X 400 + xeroxed zine reproduction | low-key, high-contrast, cool shadow | 50 / 40 / 68 |
| New Wave | 1980s style-press colour, web-offset misregistration | high-key, cool (cyan/magenta) | 0 |
| Miami Vice | 1984–89 broadcast 35mm, pastel production design | high-key pastel | 0 |

Structural notes:

- None of the thirteen uses the Calibration panel, and none carries a `Tint`.
- All keep `Blacks ≥ −25` and HSL saturation within ±60.
- Only Edwardian Pictorialist overrides the grain/Clarity-Dehaze guard, deliberately: soft-focus diffusion is its defining trait and it has no grain.
- **Punk Rock changed on 2026-10-21**: `GrainAmount 0 → 50`, `GrainSize 0 → 40`, `GrainRoughness 0 → 68`, and `Clarity +20 / Texture +10 / Dehaze +15 → 0`. The dossier records the trade (pushed Tri-X signature versus xerox crunch) and the reason the photographic claim won.
- `docs/decade.md` describes WWII Newsreel as 16mm; theatrical newsreels were 35mm (16mm was the military field format). The doc line is uncorrected as of 2026-10-21.
- `docs/decade.md` also describes Punk Rock and New Wave as black-and-white presets, but both XMPs are `Treatment="Color"`. The colour reading is defensible for both eras (drained punk colour; cyan/magenta style press), so the doc lines are the stale element. Uncorrected as of 2026-10-21.

## Rules that govern the category

See [[wiki/concepts/era-authenticity-rules]] for the grain, Dehaze, Vibrance, white-balance and look-vs-emulation decisions that recur here.
