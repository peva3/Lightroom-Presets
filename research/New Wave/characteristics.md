# New Wave Lightroom Preset — Characteristics

**Category**: Decade

The New Wave Lightroom preset reproduces the colour of early-1980s music-press photography: cold cyan-blue shadows, magenta-pink highlights, bright punchy midtones and a slightly hard flash-lit finish. It is a high-key, cool-toned colour preset with no grain, built for portraits and club frames shot under direct flash rather than for landscape or available light.

## Historical Context

The scene condensed in a Covent Garden basement. The Blitz club ran Tuesday nights in 1979–80, with Steve Strange on the door and Rusty Egan DJing, and the regulars — the Blitz Kids — are credited with launching the New Romantic movement ([Blitz Kids — Wikipedia](https://en.wikipedia.org/wiki/Blitz_Kids_(New_Romantics))). The look moved from club to shop floor within two years, a pipeline the V&A documented in *Club to Catwalk: London Fashion in the 1980s* ([V&A](https://www.vam.ac.uk/exhibitions/club-to-catwalk)).

Its photographic record is the style press. *The Face* launched in 1980 under Nick Logan and *i-D* in the same year under Terry Jones; both treated street and club photography as fashion editorial and gave a generation of photographers a printed home ([The Face — Wikipedia](https://en.wikipedia.org/wiki/The_Face_(magazine)); [i-D — Wikipedia](https://en.wikipedia.org/wiki/I-D)). The colour in those pages is not cinematic: it is bright, cold, slightly misregistered, and printed on paper that was never meant to hold a fine gradation.

## Photographic Technology

- **400 ASA colour negative, mostly.** Fast enough for flash-at-f/8 club work, and cheap enough for a magazine with a small budget. Kodachrome appeared on covers where budget allowed.
- **Direct flash plus gel.** On-camera or bracket flash, often gelled, against a seamless or a painted wall; slow-shutter drag pulled club ambient and moving lights into the frame. The result is a hard shadow edge and a bright, flattened subject.
- **Cheap web-offset.** Colour separations on newsprint stock drift: cyan and magenta misregister, shadows go cold and slightly blue-green, blacks fill in, and saturated areas lose gradation. That misregistration is a large part of what "early 80s colour" looks like.
- **Cross-processing.** Developing E-6 slide film in C-41 chemistry — an intentional accident of the period — produced cyan shadows and yellow-green highlights; the palette overlaps this preset at the cool end.

## Visual Signature

Cold shadows at hue 205 (cyan-blue) at saturation 15, magenta highlights at 310 at 12 — the two hues that define the era, sitting almost opposite each other on the wheel. Blue and magenta saturations are pushed +15 each, yellow +10, while green is cut −25 so foliage and fluorescent spill stay out of the palette. Contrast is firm (+25), whites are high (+15), and the exposure sits at +0.15 with shadows +25 — a bright image with cold holes in it. Dehaze +5 restores the slightly brittle clarity of a flash frame printed small.

## Tonal Register

**Register**: high-key, cool

Exposure +0.15, Whites +15 and Shadows +25 lift the image above middle grey; the *cold* shadow grade is what keeps that lift from reading as pastel or airy. This is the opposite structure to a warm-golden preset: brightness comes from exposure, not from amber highlights. It is stable on flash-lit portraits and club frames, but on a genuinely warm source — tungsten interiors, sunset — the cyan shadow fights the light and skin can go grey. The magenta highlight is also the first thing to clip on saturated pink clothing.

## Lighting & Subject Matter

Direct flash against a seamless, hard shadow on the wall behind, gel washes in magenta or cyan, chrome and PVC speculars, eyeliner, angular poses, shoulder pads, sculpted hair. Subject matter is studio-ish portraits made in clubs, bands on stairs, and fashion spreads shot on the street. Available light works only if the frame already has cold highlights.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure +0.15, Contrast +25 | Bright, hard flash frame |
| Basic | Highlights −40, Shadows +25 | Recovers gel hotspots; opens black clothing |
| Basic | Whites +15, Blacks −10 | Crisp edge; floor left intact |
| Presence | Saturation +12, Vibrance +10 | 2-point gap — punch without selective colour |
| HSL | Blue +15, Magenta +15 | The two era hues, both pushed |
| HSL | Yellow +10, Green −25 | Warm accents in, foliage out |
| Color Grading | Highlight 310/12, Shadow 205/15, blend 75 | Magenta above, cyan below |
| Effects | Dehaze +5 | Brittle print clarity |
| Effects | Post-Crop Vignette −10 | Slight lens/flash falloff |
| Detail | Sharpness 10, Grain 0 | Magazine reproduction is clean at page size |

## Verification

**Structural**: Color, PV 15.4, `Adobe Color` Look, neutral curves, no Calibration, no Temperature or Tint. |Vibrance − Saturation| = 2. HSL saturation peaks at +15 / −25; Blacks −10. GrainAmount 0, so no local-contrast restriction applies — Dehaze +5 is a deliberate print-clarity trait, not an accidental HDR trio.

One documentation mismatch is recorded, not fixed: `docs/decade.md` describes this preset as "stark B&W with cold blue tint", but the XMP has always been `Treatment="Color"` with magenta and blue saturation boosts. The colour reading matches the era's style press, so the doc line is the stale element.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 1980s new-wave: cyan shadow (205deg/15) and magenta highlight (310deg/12); Vibrance/Saturation +10/+12; Dehaze +5; Exposure +0.15; no grain.
- **Sources:** In-Depth Cine, Kodak 5247 analysis; Filmmakers Academy, 'Magenta: Movie Color Palettes'; Cutaway, 'A history of color in film' (1980s/90s/2000s sections)
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** The cyan/magenta split is corroborated by the Blitz-era style press and by newsprint misregistration behaviour. No XMP changes: the shadow hue is cyan rather than teal-green, the pair is close to complementary, and the Vibrance/Saturation gap stays at 2.

## Sources

- [Blitz Kids — Wikipedia](https://en.wikipedia.org/wiki/Blitz_Kids_(New_Romantics)) — 1979–80 Covent Garden club, New Romantic launch.
- [Club to Catwalk — V&A](https://www.vam.ac.uk/exhibitions/club-to-catwalk) — London club fashion into the mainstream, 1980s.
- [The Face — Wikipedia](https://en.wikipedia.org/wiki/The_Face_(magazine)) — 1980 launch under Nick Logan; style-press photography.
- [i-D — Wikipedia](https://en.wikipedia.org/wiki/I-D) — 1980 launch under Terry Jones; street and club photography.
- [Cross-processing — Wikipedia](https://en.wikipedia.org/wiki/Cross_processing) — E-6 in C-41, cyan shadows and skewed highlights.

## See Also

- [Decade presets](../../docs/decade.md)
- [Neon Synthwave](../Neon%20Synthwave/characteristics.md) — the same decade as graphic neon rather than printed colour
- [Miami Vice](Miami%20Vice/characteristics.md) — later 1980s pastel, warmer and softer
- [Cross-Processed](../Cross-Processed/characteristics.md) — the chemistry behind the cyan shadows
