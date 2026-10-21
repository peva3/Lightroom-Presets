# Indie Sleaze — Community Recipes

Ranges for a 2006-2012 direct-flash party grade: blown white, cool room, muted colour, small-sensor grain. The shipped `Indie Sleaze.xmp` is a moderate version — most community recipes push the whites harder and the saturation lower.

## Reference Looks

- **The Cobrasnake, 2004-2010** — flash on skin, black behind, unedited ([Vogue](https://www.vogue.com/article/the-cobrasnake-y2ks-archive-mark-hunter-book-indie-sleaze)).
- **Terry Richardson-era editorial flash** — single hard source, no fill, shadow directly behind the subject.
- **Early Facebook and MySpace party albums** — compressed, red-shifted, no highlight recovery ([Dazed](https://www.dazeddigital.com/fashion/article/59676/1/digital-cameras-trend-indie-sleaze-miu-miu-tiktok-bella-hadid-instagram-myspace) on why the imperfections are the point).
- **Compact digicam JPEG output** — cool AWB drift, hot centres, noise in the shadows rather than film grain.

## Slider Starting Points

| Panel | Range | Notes |
|---|---|---|
| Exposure | 0.00 to +0.60 | The flash already over-exposes; go up only for underexposed compacts |
| Contrast | +10 to +30 | Past +30 the background goes to pure black |
| Highlights | -30 to 0 | Recovery only; positive values look digital |
| Shadows | -10 to +15 | Keep the room dark, but not clipped |
| Whites | +10 to +35 | The blowout lives here |
| Blacks | -30 to -12 | Never below -30 |
| Saturation | -25 to -5 | The "unedited" look is actually muted |
| Vibrance | within 5 of Saturation | Or omit it entirely |
| HSL Sat | Green -25…-5, Blue -10…0, Red 0…+10, Orange 0…+15 | Green club light is the main enemy |
| HSL Lum | Orange +5…+18 | Face rescue |
| Color Grading | Shadow 190-215 / 5-18, Highlight 30-50 / 5-15, Blend 70-80 | Cool room, warm flash |
| Grain | 12-25 / size 15-25 / rough 40-60 | Small size = sensor noise, not 35mm |
| Vignette | -25 to -8 | Flash falloff |

## Common Mistakes

- **Chasing "blown highlights" with the Highlights slider.** Highlights is a recovery control; positive values only work on already-clipped files. Blow the image with Whites and exposure, then recover a little.
- **Adding Clarity and Texture.** The reference files are soft, compressed and slightly out of focus. Crisp micro-contrast instantly reads as a modern edit.
- **Large grain size.** Grain at size 40+ looks like pushed Tri-X and dates the image to the 1990s. Keep size near 15-25 for CCD/JPEG noise.
- **Correcting the white balance.** Half the era's charm is a wrong-WB cast; a neutral frame looks like a press photo, not a blog post.
- **Vibrance above Saturation.** That combination produces near-monochrome images with one surviving colour — the repo's selective-colour bug. Keep the two within 5 points or drop Vibrance.
- **Applying it in daylight.** With no dark background there is no flash falloff, so the grade just looks over-exposed and slightly blue.

## See Also

- [Indie Sleaze characteristics](characteristics.md)
- [Y2K Flash Digicam](../Y2K-Flash-Digicam/community-recipes.md) — harder, colder flash
- [McBling Heyday](../McBling%20Heyday/community-recipes.md) — the glossy counter-look of the same years
- [Decade presets](../../docs/decade.md)
