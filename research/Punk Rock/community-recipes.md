# Punk Rock — Community Lightroom Recipes

Community settings for a 1976–79 punk look, gathered from r/AnalogCommunity threads on pushing Tri-X, darkroom notes on printing punk negatives, and the Lightroom recipes people post with CBGB-era scans. The consistent finding: the era is made of **grain, contrast and cheap reproduction**, not of digital micro-contrast.

## Reference Looks

- **David Godlis, *History is Made at Night* (1976–79)** — available light, slow shutter, deep blacks, motion smear.
- **Roberta Bayley's Ramones cover (1976)** — direct flash, flat face, black background.
- ***Sniffin' Glue* / *Punk* magazine pages** — halftone dots, toner streaks, blown paper-white highlights.
- **Jamie Reid's Sex Pistols sleeves** — ransom typography and high-contrast cut-outs; a graphic reference for contrast, not for colour.

## Slider Starting Points

| Panel | Range | Notes |
|---|---|---|
| Exposure | −0.40 to −0.10 | Underexpose; the print is dark |
| Contrast | +30 to +50 | The primary lever |
| Highlights | −65 to −40 | Hold flash-burnt skin |
| Shadows | −25 to 0 | Let shadows block up |
| Whites | +5 to +20 | Paper-white speculars |
| Blacks | −30 to −15 | Hard floor, never past −30 |
| Saturation | −20 to 0 | Drained colour, not monochrome |
| HSL Green | Sat −45 to −25 | Parks and foliage out of the palette |
| HSL Blue | Sat −30 to −10 | Denim and cold light muted |
| HSL Orange | Lum +5 to +12 | Faces readable against black |
| Color Grading | Highlight 35–45 / 3–8; Shadow 215–235 / 5–12 | Cool shadow |
| Grain | 45–60 / 35–45 / 60–75 | Pushed Tri-X |
| Sharpness | 10, Luminance Smoothing 0 | Required with grain |
| Clarity / Texture / Dehaze | 0 | Non-negotiable once grain is on |
| Vignette | −20 to −10 | Claustrophobic frame |

## The Grain-versus-Crunch Trade

There are two defensible builds of this look:

1. **Photographic (current preset)** — grain 50/40/68 with Clarity, Texture and Dehaze at zero. Reads as a pushed Tri-X print. Correct for portraits and club frames.
2. **Reprographic variant** — no grain, Clarity +20 / Texture +10 / Dehaze +15. Reads as a photocopy of a photograph: hard edges, flattened midtones, no silver. Correct only for flat-lay or zine-mockup work, and it is the wrong build for skin, where the trio looks like HDR.

Do not combine them. The styleguide's rule exists because Lightroom's sharpening pass treats grain as detail and amplifies it into jagged noise.

## Common Mistakes

- **Adding grain on top of Clarity.** The single most common failure: digital noise, not film grain.
- **Converting to pure monochrome.** The era's photographs are often colour, just drained; −10 saturation with a cool shadow reads more 1977 than a B&W conversion.
- **Lifting shadows to "recover detail".** Punk prints have blocked shadows. Raising Shadows past 0 undoes the look.
- **Crushing Blacks below −30.** On an uncalibrated display the subject merges with the background.
- **Using Dehaze to add grit.** It also adds saturation and moves the black point; it is the least controllable of the three.
- **Ignoring output size.** Heavy grain at full resolution disappears in a 1080 px export and can read as compression artefacts on some panels.

## See Also

- [Punk Rock — Characteristics](characteristics.md)
- [Grunge](../Grunge/characteristics.md)
- [Kodak-Tri-X-400](../Kodak-Tri-X-400/characteristics.md)
- [Decade presets](../../docs/decade.md)
