# Neon Synthwave — Community Recipes

Community starting points for building a 1980s outrun/neon grade in Lightroom. Ranges below are what circulated presets, tutorial series and colourist breakdowns converge on; they are deliberately wider than the shipped `Neon Synthwave.xmp`, which sits at the restrained end of each range.

## Reference Looks

- **Blade Runner (1982), street level** — saturated neon practicals against near-black architecture, hard backlight and smoke. The reference for *separation*: the neon must be brighter than everything around it ([ASC](https://theasc.com/article/blade-runner-cronenweths-photography/)).
- **Drive (2011) / Hotline Miami (2012) title art** — the post-2000 codification: magenta-to-cyan gradients, chrome italic type, a flat poster tonal curve ([vocab.design](https://vocab.design/synthwave)).
- **IBM CGA four-colour art** — white, black, cyan, pink. The reason the palette is two hues plus darkness rather than a full spectrum ([Aesthetics of Design](https://www.aesdes.org/2024/01/24/aesthetics-exploration-synthwave/)).
- **Airbrushed 1980s album sleeves and arcade cabinet art** — clean gradients, no grain. This is the register the Decade preset targets.

## Slider Starting Points

| Panel | Range | Notes |
|---|---|---|
| Exposure | -0.40 to 0.00 | Under-expose; neon needs darkness to read as light |
| Contrast | +20 to +45 | Above +45 the midtones posterise |
| Highlights | -75 to -40 | Tames practicals so they glow instead of clipping to white |
| Shadows | +15 to +40 | Opens the architecture without lifting the blacks |
| Whites | +5 to +25 | Emissive whites |
| Blacks | -30 to -12 | Stay at or above -30 |
| Dehaze | 0 to +15 | Adds gloss; keep Clarity near 0 so it stays a poster |
| Saturation / Vibrance | 0 / 0 | Let the wheels do the colour; global saturation muddies magenta |
| HSL Sat | Magenta +20…+45, Blue +10…+25, Green -60…-30 | Green is the enemy hue |
| Color Grading | Shadow 195-220 / 15-30, Highlight 305-325 / 15-30, Blend 60-80 | Blend below 40 mixes the zones into brown |
| Grain | 0 | Tape grain belongs to the VHS variant |
| Vignette | -25 to -10 | Seals the frame |

## Common Mistakes

- **Using Vibrance to "bring the neon back".** Vibrance lifts muted midtones, which here means the greens and skin you just suppressed. Push the magenta/cyan saturation sliders instead.
- **Leaving greens alive.** A magenta highlight grade over full greens produces a muddy purple-brown image. Greens need -30 or more, or the frame never resolves into two colours.
- **Blending at 50.** The default mixes shadow cyan and highlight magenta through the midtones and the result reads brown. This look wants 65-80 for hard, printed separation.
- **Adding grain for "authenticity".** Grain is a VHS/CRT artefact. Poster and vector references are clean; grain plus Dehaze also fights itself.
- **Applying it to flat daylight.** With no emissive source the grade just looks like a cold colour cast with a violet sky. The preset needs night, rain or practical light.
- **Splitting the grade across three zones.** A midtone wheel at 20-30 saturation is what turns a clean neon poster into a video-game filter; keep midtones at 0.

## See Also

- [Neon Synthwave characteristics](characteristics.md)
- [VHS / Synthwave 1980s](../VHS-Synthwave-1980s/community-recipes.md) — the tape-artefact variant
- [Miami Vice](../Miami%20Vice/characteristics.md) — pastel daylight 1980s
- [Decade presets](../../docs/decade.md)
