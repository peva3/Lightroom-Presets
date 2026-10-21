# Community Lightroom Recipes — Kodachrome Mid-Century

Notes for adapting the **Kodachrome Mid-Century** preset. This is the *pre-K-14, projected-and-printed* Kodachrome register — 10 ASA Kodachrome (1936–1962), Kodachrome II (25 ASA, K-12, from 1961) and Kodachrome-X (64 ASA, from 1962). It is **not** the same object as `Presets/Slide/Kodachrome 25/64/200.xmp`, which model the post-1974 K-14 emulsions.

## Reference Looks

- **1950s family slide on a projector screen** — dense reds, deep blue sky, steep highlight shoulder, warm bulb cast.
- **Kodachrome II travel and editorial work, 1961–1974** — National Geographic-era palette, saturated but natural.
- **Dye-transfer print from a Kodachrome original** — the highest-saturation, cleanest separation version of the palette.
- **Aged transparency** — cyan dye loss pushing the whole frame red; the reason so many mid-century slides look warm.

## Slider Starting Points

| Panel | Range | Contributes |
|---|---|---|
| Exposure | 0 to +0.30 | Slide density; do not overexpose, reversal film clips |
| Contrast | +15 to +25 | Transparency curve |
| Highlights | -30 to -45 | The steep shoulder, pulled back |
| Shadows | +15 to +25 | Detail in a dense slide shadow |
| Whites | +5 to +15 | Projected white |
| Blacks | -20 to -5 | Dense, not crushed |
| Saturation / Vibrance | +5…+12 each, gap ≤ 5 | Saturated but controlled |
| HSL Red sat | +15 to +25 | Kodachrome's defining red |
| HSL Red lum | 0 to +8 | Keeps red dense but not opaque |
| HSL Orange / Yellow sat | +5 to +12 | Warm earth axis |
| HSL Blue sat | +12 to +22 | Deep sky weight |
| HSL Green sat | -15 to 0 | Print-era restraint; never +20 |
| Color Grade highlight | 35–45 hue / 6–12 sat | Projector warmth |
| Color Grade shadow | 30–40 hue / 5–10 sat | Warm shadow — this is the key difference from the Slide presets |
| Grain | 8–18 amount / 15–25 size | Reproduction texture (Sharpness 10 required) |
| Vignette | -8 to -12 | Slide-mount falloff |

## Common Mistakes

- **Cooling the shadow grade to 220°.** That is the Slide/Kodachrome recipe. Doing it here produces a duplicate of `Kodachrome 64` and loses the warm projection cast.
- **Crushing Blacks to -25.** Correct for a K-14 slide, wrong for this print/projection register; -10 is the anchor.
- **Adding Calibration.** Never in this repo; it also destroys the red/blue relationship the preset depends on.
- **Making it "faded vintage".** Lifting blacks and dropping contrast is expired-film territory. Real Kodachrome is high-contrast and dense.
- **Pushing Blue and Green saturation together.** You get a cyan surge into the foliage; keep Green at or below 0.
- **Copying the Slide grain values.** 5–8 at size 15 belongs to a film emulation; this preset's 15/24 is doing print-and-scan texture.

## See Also

- [Characteristics](./characteristics.md)
- [Kodachrome 64](../Kodachrome-64/community-recipes.md) — the K-14 stock emulation, for contrast
- [Post-War Optimism](../Post-War%20Optimism/community-recipes.md) — the same palette graded for prints rather than slides
