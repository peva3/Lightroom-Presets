# Miami Vice Lightroom Preset — Characteristics

**Category**: Decade

The Miami Vice Lightroom preset reproduces the look of the 1984–89 television series: high-key pastel colour, cyan-teal shadows, magenta-pink highlights, soft bloom and a deliberate absence of earth tones. It is a bright, low-contrast colour preset with negative Clarity and Dehaze and no grain, built for neon night exteriors and sunlit pastel architecture rather than for documentary realism.

## Historical Context

*Miami Vice* premiered on NBC on 16 September 1984 and ran five seasons to 1989 ([Miami Vice — Wikipedia](https://en.wikipedia.org/wiki/Miami_Vice)). Its production design drew on the Art Deco revival and, by Michael Mann's instruction, admitted no earth tones at all ([Art Deco — Wikipedia](https://en.wikipedia.org/wiki/Art_Deco)). Costume designer Jodie Tillen described the rule precisely: "no earth tones, no primary, all pastel. Every car colour, every wall that the actors walked in front of, was by design" ([Hollywood Reporter](https://www.hollywoodreporter.com/lifestyle/style/miami-vice-michael-mann-costume-designers-interview-menswear-1235961920/)).

The palette had a domestic origin: Mann has said it came out of a colour-theory session with his wife Summer, an artist, over Easter-egg paint chips, producing "that sense of vibrating pastels" and a strict three-colour scheme for the first two seasons. He also named the failure mode — "if you let it get too loud, then it was just … kind of gross" — and had rundown Miami buildings repainted so backgrounds would hold the palette ([The Rake](https://therake.com/stories/the-miami-vice-effect)).

## Photographic Technology

- **35mm colour negative**, shot for broadcast. The colour was largely *in front of the lens* — paint, wardrobe, neon — which is why the show looks designed rather than graded.
- **Diffusion and telephoto.** Net filters and long lenses compressed backgrounds and bloomed highlights; a modern preset fakes that with negative Clarity.
- **NTSC transmission.** 1980s broadcast chroma bandwidth was roughly a quarter of luma bandwidth, so saturated edges smeared and fine colour detail was lost. Pastels were partly a survival strategy: low-saturation colour survived transmission that loud primaries did not.
- **Practical neon.** Night exteriors were lit with magenta and cyan neon and gels, not corrected to white — the origin of the two-colour night.

## Visual Signature

Cyan-teal shadows at hue 190, saturation 15; magenta-pink highlights at 330 at 15. Aqua is pushed +15 and magenta +20, blue +10, while green is cut −20 — that cut is the "no earth tones" rule expressed as a grade. Orange luminance is lifted +10 so skin stays luminous against all that cyan. The image is bright (+0.30 EV, Whites +15, Shadows +30) and low in contrast (+10), with Clarity −5 and Dehaze −5 providing bloom rather than bite. There is no grain and no vignette: the frame is open and airy, not sealed.

## Tonal Register

**Register**: high-key pastel

Exposure +0.30 with Shadows +30 and Blacks −5 is the brightest setting in the Decade group, and the low Contrast +10 keeps highlights from hardening. The cold shadow grade is what stops that brightness from becoming a wash: pastel needs a temperature contrast, not a tonal one. The preset is stable on white linen, pale stucco, water and neon, but it is fragile on warm interiors and fall landscapes — the green cut removes exactly the colours those scenes depend on, and skin can go pink under the 330° highlight.

## Lighting & Subject Matter

Hard sun bounced off stucco, neon at night, pool water, chrome and glass brick, palm silhouettes, sunset gradients. Subject matter is linen suits, pastel tees, sports cars, boats, ocean horizons, Art Deco hotels and nightclub interiors. Overcast light flattens the palette; harsh midday sun and neon both work.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure +0.30, Contrast +10 | Bright, airy, low-contrast |
| Basic | Highlights −45, Shadows +30 | Recovers white linen and neon cores; opens shade |
| Basic | Whites +15, Blacks −5 | Clean white; no crushed anchor |
| Presence | No Saturation or Vibrance | Colour comes from HSL and grading |
| HSL | Aqua +15, Magenta +20 | The two signature hues |
| HSL | Blue +10, Green −20 | Water and sky supported; foliage suppressed |
| HSL | Orange Lum +10 | Skin luminous against cyan |
| Color Grading | Highlight 330/15, Shadow 190/15 | Magenta above, cyan-teal below |
| Effects | Clarity −5, Dehaze −5 | Diffusion bloom and atmospheric softness |
| Detail | Sharpness 10, Grain 0 | Broadcast-clean; grain would fight the bloom |

## Verification

**Structural**: Color, PV 15.4, `Adobe Color` Look, neutral curves, no Calibration, no Temperature or Tint. HSL saturation peaks at +20 / −20; Blacks −5. GrainAmount 0, so Clarity −5 and Dehaze −5 are free to produce bloom — this is the one preset in the set where *both* local-contrast sliders are negative, which is the correct way to emulate diffusion.

No white-balance shift is present, which matters: a Temperature push plus a 330° highlight grade would double-warm the skin and lose the pastel read. The green cut at −20 is the enforceable version of Mann's "no earth tones" rule.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 1980s teal-and-pink: shadow 190deg/15, highlight 330deg/15, low contrast (+10), magenta and aqua saturation pushed, greens cut -20; no grain (the show was shot on 35mm colour negative).
- **Sources:** In-Depth Cine, Kodak 5247 analysis; Filmmakers Academy, 'Magenta: Movie Color Palettes'; Cutaway, 'A history of color in film' (1980s/90s/2000s sections)
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** The palette is corroborated by Mann's and Tillen's own accounts (Easter-egg pastels, no earth tones, no primaries) and by the show's Art Deco production design. No XMP changes: the shadow hue at 190 is cyan-teal rather than blue, the highlight at 330 is magenta rather than red, and the green cut enforces the design rule.

## Sources

- [Miami Vice — Wikipedia](https://en.wikipedia.org/wiki/Miami_Vice) — 1984 premiere, 1984–89 run, Art Deco revival, no earth tones.
- [How Miami Vice Changed Menswear — Hollywood Reporter](https://www.hollywoodreporter.com/lifestyle/style/miami-vice-michael-mann-costume-designers-interview-menswear-1235961920/) — Tillen's "no earth tones, no primary, all pastel"; Mann on "vibrating pastels".
- [The Miami Vice Effect — The Rake](https://therake.com/stories/the-miami-vice-effect) — repainted buildings, the earth-tone ban in practice.
- [Art Deco — Wikipedia](https://en.wikipedia.org/wiki/Art_Deco) — the revival the show rode.
- [Memphis Group — Wikipedia](https://en.wikipedia.org/wiki/Memphis_Group) — the 1980s Italian design language behind the interiors.

## See Also

- [Decade presets](../../docs/decade.md)
- [New Wave](New%20Wave/characteristics.md) — the same decade, colder and printed
- [Neon Synthwave](../Neon%20Synthwave/characteristics.md) — neon as graphic grid rather than pastel architecture
- [Cinestill-800T](../Cinestill-800T/characteristics.md) — tungsten night colour with halation
