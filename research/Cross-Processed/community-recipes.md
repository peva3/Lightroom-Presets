# Cross-Processed — Community Recipes

Ranges for building an E-6-in-C-41 crossover in Lightroom. Two rules govern everything below: the shadows go cool, the highlights go warm, and the *transition* must stay hard. The shipped `Cross-Processed.xmp` is the restrained editorial version of every number here.

## Reference Looks

- **Velvia 100 xpro** — "very red + some magenta or yellow" ([The Darkroom cast table](https://thedarkroom.com/cross-processing-film/)): the source of the magenta highlight this preset uses.
- **Ektachrome xpro** — "very green": the opposite bias, useful when you want a heavier shadow cast and a cleaner highlight.
- **Provia 400 xpro** — green + yellow: the closest match to a three-way crossover with a visible yellow midtone.
- **1990s snowboard and skate editorial** — hard flash, blown white, skin visibly yellow-green ([Wikipedia](https://en.wikipedia.org/wiki/Cross_processing) on the process's 1990s rise).

## Slider Starting Points

| Panel | Range | Notes |
|---|---|---|
| Exposure | -0.40 to 0.00 | Slide film xpro over-exposes; underexpose a stop |
| Contrast | +25 to +45 | Below +25 the crossover looks like a split-tone |
| Highlights | -65 to -30 | Slide highlights clip fast |
| Shadows | +5 to +30 | Keeps the shadow cast visible |
| Whites | 0 to +20 | |
| Blacks | -25 to -5 | The C41→E6 direction lifts blacks; this one does not |
| Saturation | -15 to 0 | Muting the global image is what makes two casts read |
| Vibrance | 0 to +5 | Keep within 5 points of Saturation |
| HSL Sat | Green -45…-15, Blue -30…0, Orange -20…0, Magenta +5…+25 | Green and blue are already carrying the cast |
| Color Grading | Shadow 150-175 / 18-30, Midtone 60-80 / 10-20 (optional), Highlight 305-330 / 15-25, Blend 30-45 | Hard blend; a midtone wheel only if you want the full crossover |
| Grain | 20-30 / size 25-40 / rough 45-65 | Keep Clarity/Texture/Dehaze at 0 |
| Vignette | -30 to -8 | -30 for 35mm/Lomo, -12 for editorial |

## Common Mistakes

- **Flipping the direction.** Shadow-cyan plus highlight-yellow is E6→C41. If you find yourself with *lifted* blacks, low contrast and warmth everywhere, you have built C41→E6 — a different, flatter look.
- **Blending at 70-80.** High blending softens the zone boundary into a wash; xpro's signature is an abrupt, visible crossover. 30-45 is correct.
- **Correcting the cast with White Balance.** The whole point is that the cast is un-correctable: moving Tint toward magenta fixes the shadows and poisons the highlights. Grade instead.
- **Adding Clarity or Texture.** Every xpro preset that ships with Clarity +15 looks like an HDR landscape, not film.
- **Saturating green.** The green channel is already carrying the shadow cast; +30 there collapses the separation into a green photograph.
- **Forgetting the midtone when you want "Velvia xpro".** Without a 70/15 midtone wheel the image is a two-zone split; the yellow-green bridge is what makes it read as chemistry rather than a gradient map.

## See Also

- [Cross-Processed characteristics](characteristics.md)
- [Cross-Processed E6→C41 dossier](../Cross-Processed-E6-C41/community-recipes.md) — per-stock casts
- [Lomography Cross-Processed](../Lomography%20Cross-Processed/community-recipes.md) — the maximalist variant
- [Decade presets](../../docs/decade.md)
