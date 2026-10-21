# Cross-Processed Lightroom Preset — Characteristics

**Category**: Decade

The Cross-Processed Lightroom preset recreates slide film developed in colour-negative chemistry: cyan-green shadows, magenta highlights, hard zone transitions and a slightly muted overall saturation so the crossovers stay legible on skin. It is the "clean editorial" reading of xpro — no HSL hue warping, no calibration, a mild vignette — as distinct from the repo's three louder xpro presets. Its direction is **E-6 film in C-41 chemistry**, the common form of the process, and that direction was verified against both the colour grading values and the sibling presets.

## Historical Context

Cross-processing was discovered independently, and usually by accident, in the C-22 and E-4 era, and became a deliberate style in the 1990s ([Wikipedia](https://en.wikipedia.org/wiki/Cross_processing)). The mechanic is a chemistry mismatch: C-41 is built for dye-coupler negative film with an orange mask, E-6 for reversal film without one. Run E-6 stock through C-41 and the scanner, expecting an orange-masked negative, misinterprets the image — producing casts that cannot be corrected out, because pulling blue out of the shadows intensifies yellow in the highlights ([Photo StackExchange](https://photo.stackexchange.com/questions/7656/what-are-the-results-of-developing-slide-film-e-6-process-with-c41-chemicals)).

The two directions are not symmetrical: E-6-in-C-41 gives "increased contrast with strong color casts", C-41-in-E-6 gives "muted, pastel colors with little contrast" ([The Darkroom](https://thedarkroom.com/cross-processing-film/); [Lomography](https://www.lomography.es/about/faq/1376-what-is-cross-processing)).

## Photographic Technology

- **Slide film has a narrow latitude.** The Darkroom's guidance is to rate a 100 ISO slide film at 200 and underexpose roughly a stop, because xpro E-6 "tends to over expose" and blows its highlights.
- **The cast is stock-specific.** Their cast table is worth memorising: Sensia 100 → red; Sensia 400 → blue + green; Velvia 50 → green + blue; Provia 400 → green + yellow; Velvia 100 → "very red + some magenta or yellow"; Ektachrome → "very green" ([The Darkroom](https://thedarkroom.com/cross-processing-film/)). So a magenta highlight is a legitimate xpro outcome, but it belongs to particular stocks, not to the process in general.
- **The lab is part of the look.** Minilabs auto-corrected xpro frames back toward "normal", which is why serious xpro was scanned on dedicated film scanners with correction disabled ([Photo StackExchange](https://photo.stackexchange.com/questions/7656/what-are-the-results-of-developing-slide-film-e-6-process-with-c41-chemicals)).

## Visual Signature

Shadow hue 160 (green-cyan) at saturation 25 and highlight hue 320 (magenta) at 20, with Blending 40 so the two zones meet in a hard, visible transition rather than a soft wash. Greens are pulled -30 and blue -15 — the crossover already lives in those hues, so extra saturation there destroys the separation. Magenta is lifted +15 and orange dropped -10, which keeps skin chemically wrong rather than healthy and stops the grade reading as merely warm. Saturation -5 is a deliberate restraint: the preset mutes the *global* image so the two crossovers are the only strong colour in the frame.

## Tonal Register

**Register**: neutral, high-contrast, split-shadow

Exposure -0.15 with Contrast +30, Highlights -50 and Blacks -20 keeps the image at a normal mid-key median: unlike Grunge or Neon Synthwave, this preset is not trying to be dark or low-key. All of its character is in hue separation, not in exposure. Against a flat, evenly lit frame it will look like a strong split-tone; against hard sunlight or direct flash it looks like film, because the contrast is already in the scene.

## Lighting & Subject Matter

Hard sun, direct flash, single-source strobe — anything that produces specular highlights and deep shadows for the crossovers to occupy. 1990s editorial and fashion, snowboarding and skate photography, band portraits, nightlife. Skin is the test: it should look yellow-green in the shadows and slightly magenta in the light, never uniformly warm.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure -0.15, Contrast +30 | Underexposed slide film, hard contrast |
| Basic | Highlights -50, Shadows +15 | Recovers blown slide highlights, keeps shadow colour visible |
| Basic | Whites +5, Blacks -20 | Print-like whites, closed but not crushed blacks |
| HSL | Sat Green -30, Blue -15, Orange -10 | Stops the crossover hues from saturating into mud |
| HSL | Sat Magenta +15 | Holds the highlight cast |
| Presence | Saturation -5 | Global restraint so the two casts read |
| Color Grading | Shadow 160/25, Highlight 320/20, Blend 40 | The crossover itself, with hard zone edges |
| Detail | Sharpness 10, Luminance Smoothing 0, Grain 25/28/55 | 35mm xpro grain, grain-safe sharpening |
| Effects | Post-Crop Vignette -12 | Editorial falloff, far lighter than the Lomo preset |

## Verification

**Direction test.** E6→C41 must put the *cool* cast in the shadows and the *warm/magenta* cast in the highlights, with a contrast lift. This file does exactly that: shadow 160 / highlight 320, Contrast +30, Blacks -20. The reverse process is encoded in `Presets/Alternative-Process/Cross Process C41→E6.xmp` as the opposite signature — Contrast +8, Blacks **+15** (lifted), shadow 45 / midtone 40 / highlight 35, i.e. flat, warm and washed. **The Decade preset is therefore not inverted**, and no colour-grading change was made.

**Comparison with the three related presets** (all values read from the files):

| Preset | Direction | Grade (shadow / mid / highlight) | Blend | Distinguishing artefact |
|---|---|---|---|---|
| `Decade/Cross-Processed` | E6→C41 | 160/25 · — · 320/20 | 40 | No HSL hue warps; Saturation -5; vignette -12; grain 25 |
| `Alternative-Process/Cross Process E6→C41` | E6→C41 | 160/25 · 70/15 · 320/20 | 40 | Six hue warps; Saturation +12 / Vibrance +15; vignette -30 |
| `Creative/Cross-Processed Velvia` | E6→C41 (Velvia-specific) | 160/22 · — · 305/18, Balance -40 | 75 | Clarity +18, Dehaze +15, Contrast +50 — the crunchy variant |
| `Creative/Lomography Cross-Processed` | Purple/yellow "Lomo" reading | 270/45 · — · 55/35, Balance -20 | 75 | Vignette -50, eight hue warps, Saturation +15 — maximalist |
| `Alternative-Process/Cross Process C41→E6` | C41→E6 | 45/16 · 40/18 · 35/20 | 45 | Flat: Contrast +8, Blacks +15, Saturation -5 |

**Coverage gap (documented, not changed).** The repo's canonical xpro formula in `STYLEGUIDE.md` §VI includes a midtone wheel at hue 70 / saturation 15-20, and the Alternative-Process sibling carries it. This file leaves midtones at 0, so it reads as a two-zone split rather than a three-way crossover; the yellow-green bridge is missing. That is a simplification, not a contradiction of a defining trait, so the XMP was left untouched — add Midtone 70/15 for the full crossover.

**Structural**: Treatment Color, ProcessVersion 15.4, Adobe Color Look block, neutral curves, no Calibration, no Temperature/Tint. Grain 25 with Sharpness 10, Luminance Smoothing 0 and Clarity/Texture/Dehaze absent satisfies the grain rule. HSL saturation peaks at -30; Blacks -20 is above the floor; Vibrance is absent, so no ±5 gap.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** Generic x-pro: Contrast +30 with Highlights -50; green/cyan shadows (160deg/25) and magenta highlights (320deg/20); Saturation -5 so the shifts stay readable; grain 25; vignette -12.
- **Sources:** Kubus Photo, 'Cross Processing Film: E-6 in C-41'; Photo.net, 'Processing C-41 color negatives in E-6'; Flickr Cross Processed group
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** Direction confirmed as E6→C41 and explicitly *not* inverted; before → after: no change. The sweep's third-party sources could not be verified as live URLs and are replaced below with sources checked in this pass.

## Sources

- [Cross processing — Wikipedia](https://en.wikipedia.org/wiki/Cross_processing) — both process directions, accidental discovery in the C-22/E-4 era, 1990s popularity, the "cannot be corrected" property.
- [Cross Processing Explained — The Darkroom](https://thedarkroom.com/cross-processing-film/) — E6→C41 is the common form; contrast/cast asymmetry between directions; per-stock cast table; underexpose by a stop.
- [What is Cross-Processing? — Lomography](https://www.lomography.es/about/faq/1376-what-is-cross-processing) — the two chemistry pairs and why E-6-in-C-41 is the "Lomographic" one.
- [What are the results of developing slide film in C41? — Photo StackExchange](https://photo.stackexchange.com/questions/7656/what-are-the-results-of-developing-slide-film-e-6-process-with-c41-chemicals) — the blue-shadow/yellow-highlight crossover, and why minilab auto-correction ruins xpro.
- [Cross development, X-Pro — filmphotography.eu](https://filmphotography.eu/en/infos/development/cross-development/) — "green or pink" stock-dependent casts; grainy results in C-41.
- [Cross Processing slide film with Agfa Precisa CT — FollowTheGrain](https://followthegrain.de/cross-processing-slide-film-agfa-precisa/) — worked example: dominant green, high contrast.

## See Also

- [Decade presets](../../docs/decade.md)
- [Cross-Processed E6→C41](../Cross-Processed-E6-C41/characteristics.md) — the per-stock research dossier behind this direction
- [alt-cross-process-e6-c41](../alt-cross-process-e6-c41/characteristics.md) — the Alternative-Process sibling, with the yellow midtone this preset omits
- [alt-cross-process-c41-e6](../alt-cross-process-c41-e6/characteristics.md) — the reverse chemistry, which is flat and warm rather than split
- [Lomography Cross-Processed](../Lomography%20Cross-Processed/community-recipes.md) — the maximalist purple/yellow reading
