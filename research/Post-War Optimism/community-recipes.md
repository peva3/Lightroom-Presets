# Community Lightroom Recipes — Post-War Optimism

Notes for adapting the **Post-War Optimism** preset. This is a *daylight, high-key* decade look: 1950s consumer colour as sold by Kodak — Colorama transparencies, catalogue spreads, family snapshots on Kodacolor prints.

## Reference Looks

- **Kodak Colorama, Grand Central, 1950–1990** — backlit 18×60 ft transparencies; sunlit lawns, bright whites, warm skin, saturated but not garish colour.
- **Levittown / suburban snapshot, mid-1950s** — slightly over-exposed, open shadows, lawn green held back, chrome and pastel paint the loudest colours.
- **Department-store and appliance catalogue colour** — clean, evenly lit, ruddiness removed, no deep black anywhere.
- **Life magazine colour photo-essay, late 1950s** — the higher-contrast end of the same palette.

## Slider Starting Points

| Panel | Range | Contributes |
|---|---|---|
| Exposure | +0.15 to +0.45 | The high-key bias; anything below 0 stops reading as "period" |
| Contrast | +5 to +15 | Print snap without closing the shadows |
| Highlights | -25 to -45 | Protects sunlit whites and chrome |
| Shadows | +15 to +35 | Open shade — the defining tonal move |
| Whites | +5 to +20 | Bright, clean whites |
| Blacks | -10 to 0 | No true black; never below -10 |
| Temperature | 5400 to 5900 | Daylight anchor only — this is not the warmth control |
| Saturation / Vibrance | +5…+12 each, gap ≤ 5 | Confident consumer colour |
| HSL Red / Orange | +5 to +12 sat | Produce, chrome, clothing |
| HSL Orange luminance | +6 to +14 | Clean, slightly pale skin |
| HSL Green | -5 to -15 sat | Holds the lawn back |
| HSL Blue | 0 to +8 sat | Sky present, not electric |
| Color Grade highlight | 35–45 hue / 6–12 sat | Warm sun |
| Color Grade shadow | 30–40 hue / 3–8 sat | Warm bounce, never teal |
| Grain | 12–22 amount / 20–28 size | Fine 35mm texture (Sharpness must be 10) |
| Vignette | -5 to -10 | Barely-there wide-lens falloff |

## Common Mistakes

- **Cooling the shadows.** The moment the shadow grade passes ~180° the image becomes 1980s rather than 1955. Keep both grading ends on the warm side of 30°.
- **Using Vibrance to "lift" the colour.** Vibrance 25 against Saturation 10 produces the repo's selective-colour bug; keep the gap at 5 or below.
- **Crushing blacks for "richness".** Consumer colour prints of the period have no true black; -20 turns a bright decade into a moody one.
- **Adding Temperature for warmth.** 5700 K is an anchor. Warmth belongs in Color Grading; a 6500 K push yellows the whites.
- **Adding Calibration.** Never in this repo, and especially not here — it shifts every primary under a preset that already relies on HSL.
- **Heavy grain.** Grain 30+ reads as 1970s high-speed film, not 10 ASA Kodachrome.

## See Also

- [Characteristics](./characteristics.md)
- [Diner Americana](../Diner%20Americana/community-recipes.md) — the same decade at night
- [Kodachrome Mid-Century](../Kodachrome%20Mid-Century/community-recipes.md) — the slide version of 1950s colour
