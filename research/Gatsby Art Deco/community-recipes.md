# Gatsby Art Deco Lightroom Preset — Community Recipes & Settings

Ranges for a jazz-age gold-on-black look, calibrated against Deco material palettes and against Autochrome scans rather than against any single film stock.

## Reference Looks

Three references pull in different directions. Autochrome plates from 1907–1930 (Albert Kahn's *Archives de la Planète*, the Science Museum and Library of Congress collections) show the period's real colour: warm, soft, slightly pink, with muted blues and visible starch grain. Art Deco graphic work — posters, cinema foyers, the 1925 Paris exposition — supplies a harder palette of brass, black lacquer, ivory and jewel tones. Modern period films, above all Luhrmann's *The Great Gatsby* (2013), supply the contemporary shorthand everyone recognises: hot gold highlights, saturated skin, and a glossy, high-contrast finish. The preset sits between the archive and the film; lean toward the archive if the goal is plausibility, toward the film if the goal is impact.

## Slider Starting Points

| Panel | Range | Contribution |
|---|---|---|
| Exposure | −0.2 to +0.1 | Slight density so highlights read as specular |
| Contrast | +20 to +40 | Gloss; the core of the look |
| Highlights | −60 to −30 | Holds the gold shoulder instead of clipping it |
| Shadows | +10 to +25 | Keeps tuxedos and lacquer readable |
| Whites | 0 to +10 | Specular sparkle |
| Blacks | −20 to −5 | Dense but anchored; never below −30 |
| Clarity | −5 to +5 | Keep near zero — Deco is glossy, not crunchy |
| Texture | 0 | No micro-contrast on skin |
| Dehaze | 0 to +5 | Only to clear a hazy capture; not part of the look |
| Saturation | 0 to +10 | The colour is carried by HSL and grading, not globally |
| Vibrance | 0 to +5 | Keep within ±5 of Saturation |
| HSL saturation | Orange +10 to +20, Yellow +10 to +15, Green −25 to −10, Blue −25 to −10 | Gold forward, emerald/sapphire held back |
| HSL luminance | Orange +5 to +15, Yellow 0 to +10 | Skin and brass lift |
| Color Grade — highlights | Hue 38–45°, Sat 10–20 | Gilt |
| Color Grade — shadows | Hue 20–35°, Sat 8–15 | Warm black lacquer, not teal |
| Grain | Amount 25–40, Size 25–32, Rough 50–65 | Period negative plus Autochrome texture |
| Vignette | −25 to −10 | Ballroom falloff; keep it soft |

## Common Mistakes

- **Teal shadows.** The most common failure: pairing gold highlights with cyan shadows because that is the modern teal-and-orange reflex. Deco is gold on *black*.
- **Saturating orange to neon.** Skin turns to brass. Keep orange saturation in the low twenties and compensate with luminance, not saturation.
- **Positive Clarity.** Deco is polished; micro-contrast makes it look like an HDR real-estate photo.
- **Heavy vignette.** A hard corner burn reads as 2010s Instagram, not 1920s studio printing.
- **Global Saturation boost.** Better to leave saturation alone and let HSL target gold, or every colour in the frame inflates at once.
- **Forgetting that most 1920s photographs are monochrome.** If the goal is documentary plausibility rather than a stylised look, cut `Saturation` hard and use the grading wheels only.

## See Also

- [Gatsby Art Deco characteristics](characteristics.md)
- [Autochrome](../alt-autochrome/) — the period's actual colour process.
- [Hollywood Glamour](../Hollywood%20Glamour/) — monochrome glamour of the same years.
