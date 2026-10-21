# Punk Rock Lightroom Preset — Characteristics

**Category**: Decade

The Punk Rock Lightroom preset renders the 1976–79 punk scene as a hard, low-key, near-monochrome colour image: blocked blacks, blown flash highlights, cool shadow cast, desaturated greens and blues, and — since the 2026 research pass — heavy pushed-Tri-X grain. It is a low-key, high-contrast preset for flash-lit portraits, club reportage and photocopied-print artefacts, not a clean digital black-and-white conversion.

## Historical Context

CBGB opened at 315 Bowery in 1973 and by 1975 was the room where the Ramones, Television, Blondie, Patti Smith and Talking Heads played to a few dozen people ([CBGB — Wikipedia](https://en.wikipedia.org/wiki/CBGB)). In Britain the Sex Pistols formed in 1975; *Sniffin' Glue* (Mark Perry, 1976–77) and New York's *Punk* magazine (1976) turned the scene into printed matter almost immediately. The defining artefacts are not gallery prints but fanzines, flyers and sleeves — cheap, fast, and reproduced badly on purpose.

That print layer matters to the grade. Punk graphics were cut from newspapers and run through an office photocopier, so images arrived already high-contrast, half-toned and darkened by toner smears ([JSTOR Daily](https://daily.jstor.org/xerox-and-roll-the-corporate-machine-and-the-making-of-punk/)). The V&A's *Punk to Pop* treats that output as the movement's primary visual record ([V&A](https://www.vam.ac.uk/exhibitions/punk-to-pop)).

## Photographic Technology

- **Tri-X 400, pushed to 1600.** The standard punk film, exposed two stops under and over-developed, which raises contrast, blocks shadows and produces the signature coarse "salt and pepper" grain ([Tri-X — Wikipedia](https://en.wikipedia.org/wiki/Kodak_Tri-X)). HP5 was the British equivalent.
- **Two lighting schools.** Available light at CBGB — David Godlis shot the room on slow shutter and wide aperture, letting motion smear — and direct on-camera flash, as on Roberta Bayley's Ramones cover (1976), which flattens the face and drops the background to black.
- **Cheap reproduction.** Photocopiers screened photographs into halftone dots, clipped highlights to paper white and filled shadows with toner; a second-generation copy was darker still. Zines were stapled, not bound ([Zine — Wikipedia](https://en.wikipedia.org/wiki/Zine)).

## Visual Signature

Contrast +40 and Blacks −25 do most of the work: the image is genuinely dark, with Highlights −55 protecting flash-burnt skin from turning into a flat white shape. Saturation is only −10, so this is a *drained colour* image rather than black-and-white — a distinction the category index currently blurs. Greens lose 35 points and blues 20, which removes park and denim colour; orange luminance is lifted +8 to keep faces readable against the black. The shadow grade sits at hue 225 (cool blue) at 8, the colour of cold light in a Bowery club, and a −18 vignette seals the frame.

Grain is now the texture carrier: Amount 50, Size 40, Roughness 68 — the classic Tri-X pushed band, coarse enough to read as silver rather than sensor noise.

## Tonal Register

**Register**: low-key, high-contrast, cool-shadowed

Exposure −0.25 with Shadows −15 and Blacks −25 places the image firmly below middle grey; the only bright values are flash-lit skin and paper-white highlights. The register assumes a dark surround — a club wall, a stage edge, a xeroxed page. On a bright daylight frame the preset crushes the subject into the background, because there is no highlight recovery left after −55. It is a night/flash look, and should be labelled as one.

## Lighting & Subject Matter

Direct flash against a black wall, bathroom-mirror selfies, stage edge at eye level, sweat and safety pins, ripped shirts, cheap sunglasses, cramped back rooms. Available-light frames with motion smear also fit; flat overcast daylight does not.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure −0.25, Contrast +40 | Underexposed, over-developed look |
| Basic | Highlights −55, Shadows −15 | Holds flash-burnt skin; lets shadows block up |
| Basic | Whites +10, Blacks −25 | Paper-white speculars over a near-black floor |
| Presence | Saturation −10 | Drained colour, not monochrome |
| HSL | Green −35, Blue −20 | Kills park and denim colour |
| HSL | Orange Lum +8, Red Sat +5 | Keeps faces readable against black |
| Color Grading | Highlight 40/5, Shadow 225/8, blend 70 | Cool club shadow, faint warm highlight |
| Detail | Sharpness 10, Grain 50 / 40 / 68 | Pushed Tri-X; sharpening suppressed so grain stays organic |
| Effects | Clarity 0, Texture 0, Dehaze 0 | Texture budget spent on grain alone |
| Effects | Post-Crop Vignette −18 | Sealed, claustrophobic frame |

## Verification

**Structural**: Color, PV 15.4, `Adobe Color` Look, neutral curves, no Calibration, no Temperature or Tint. HSL saturation peaks at −35 / +5; Blacks −25, inside the −30 floor. Vibrance is absent while Saturation is −10: the cut is global and there is no vibrance boost, so no midtone-vs-global split — the failure the ±5 rule targets — can arise. (This matches the existing convention in Grunge and Dust Bowl, where an absent Vibrance accompanies a negative Saturation.)

**XMP change 2026-10-21**: `GrainAmount 0 → 50`, `GrainSize 0 → 40`, `GrainRoughness 0 → 68`, `Clarity2012 +20 → 0`, `Texture +10 → 0`, `Dehaze +15 → 0`. Sharpness stayed at 10, LuminanceSmoothing at 0. Strict XML parse passed; no unescaped ampersands.

Rationale: pushed Tri-X grain is the most cited property of punk photography, and its absence was a genuine miss rather than a stylistic choice. The preset could not keep the xerox-crunch trio *and* grain under the repo's grain rule, so the trade went in favour of the photographic signature: Contrast +40, Blacks −25, Highlights −55 and the −18 vignette still deliver the hard, cheap-print look, and grain now supplies the texture the local-contrast sliders were faking. The cost is a softer read in small exports; the alternative — crunch without grain — read as digital HDR rather than 1977.

One documentation mismatch is recorded, not fixed: `docs/decade.md` describes this preset as "high-contrast B&W" while the XMP has always been `Treatment="Color"`. The colour reading is defensible for the scene (colour punk photographs exist and the preset is only −10 saturated), so the doc line is the stale element and should be corrected in a docs pass.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 1977 zine register: Contrast +40, Clarity +20 / Texture +10 / Dehaze +15 (xerox crunch rather than digital sharpening), Saturation -10, cool shadow cast (225deg/8), crushed blacks -25.
- **Sources:** 1970s punk fanzine/xerox print references
- **Preset adjustments:** none at sweep time - gap flagged: GrainAmount 0 on an era of pushed Tri-X (corrected in the research pass below).

**Review 2026-10-21 (research pass).** The sweep's flagged gap was real and has been corrected: grain added, local-contrast trio zeroed, per the note above. The rest of the grade — cool 225° shadow, −10 saturation, −25 blacks — matches both the flash and available-light photographic record and the photocopied print record.

## Sources

- [Xerox and Roll — JSTOR Daily](https://daily.jstor.org/xerox-and-roll-the-corporate-machine-and-the-making-of-punk/) — toner smears, halftone, dark second-generation copies.
- [Punk to Pop — V&A](https://www.vam.ac.uk/exhibitions/punk-to-pop) — punk and post-punk graphic output as primary record.
- [Kodak Tri-X — Wikipedia](https://en.wikipedia.org/wiki/Kodak_Tri-X) — 400 ASA film, push processing, photojournalism.
- [CBGB — Wikipedia](https://en.wikipedia.org/wiki/CBGB) — 1973 opening, the Bowery room, the 1975–77 bands.
- [Zine — Wikipedia](https://en.wikipedia.org/wiki/Zine) — photocopied, non-commercial circulation.

## See Also

- [Decade presets](../../docs/decade.md)
- [Grunge](../Grunge/characteristics.md) — the 1990s descendant: distressed, desaturated, dirty
- [Indie Sleaze](../Indie%20Sleaze/characteristics.md) — flash-lit DIY 25 years later
- [Kodak-Tri-X-400](../Kodak-Tri-X-400/characteristics.md) — the stock as its own emulation
