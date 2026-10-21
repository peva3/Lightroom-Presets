# Mod London Lightroom Preset — Characteristics

**Category**: Decade

The Mod London Lightroom preset recreates the colour side of mid-1960s London editorial: pale clean skin against drab olive brickwork, red and blue as graphic accents, a cool cast in the shadows and the visible grain of 35mm enlarged across a spread. It carries the contrast discipline of the era's black-and-white printing — "soot and whitewash" — into colour.

## Historical Context

Between roughly 1960 and 1966 a small group of young London photographers displaced the established fashion press. David Bailey, Terence Donovan and Brian Duffy — Beaton's "Terrible Three", Parkinson's "Black Trinity" — shot with a "fresh and informal style" that "embodied the freewheeling spirit of the swinging sixties" ([Amateur Photographer](https://amateurphotographer.com/technique/portrait_photography/a-look-back-at-terence-donovans-editorial-photography/)). Bailey joined British Vogue in 1960, known for "stark black and white backgrounds, closely cropped shots and sharp lighting" ([Google Arts & Culture](https://artsandculture.google.com/story/david-bailey-and-the-story-of-fashion-photography-british-fashion-council/JQXhztVGSo0WLw)). Donovan took menswear onto gasworks and power stations, using bomb-damaged London as backdrop ([Wikipedia](https://en.wikipedia.org/wiki/Terence_Donovan_(photographer))). Antonioni's *Blow-Up* (1966) fixed the myth.

The colour half is the press. On **4 February 1962** the *Sunday Times* launched the Colour Section, the first colour supplement attached to a British newspaper; its cover was eleven Bailey photographs of Jean Shrimpton in a Mary Quant dress ([Press Gazette](https://pressgazette.co.uk/publishers/magazines/sunday-times-magazine-60-years-gallery/)). The *Telegraph* and *Observer* followed in 1964.

## Photographic Technology

- **35mm, enlarged hard.** The new photographers worked small and fast, and art directors bled frames across double-page spreads. *Town*'s design "demanded maximum enlargement from the 35mm format", and "its loose, grainy quality became a keynote look of the 1960s" ([Eye](https://eyemagazine.com/feature/article/town-shaped-the-sixties)).
- **Reproduction contrast.** The standard was "rich blacks and clean whites — 'soot and whitewash'" — achieved in the darkroom and on press, when "colour pages were still limited"; the first double-page spread printed from part of a 35mm *colour* slide was a production milestone ([Eye](https://eyemagazine.com/feature/article/town-shaped-the-sixties)).
- **Colour film of the moment.** 35mm Kodachrome — 25 ASA Kodachrome II from 1961, 64 ASA Kodachrome-X from 1962 — and Agfacolor transparency, separation-printed for letterpress or gravure ([timeline](https://en.wikipedia.org/wiki/Kodachrome)). Ink and paper did as much to the palette as the emulsion: greens muddied toward olive, blues stayed clean, warm skin was protected.

## Visual Signature

Drab ground, graphic accents. Foliage and painted brick drift toward olive-yellow and desaturate; blues and reds stay saturated as flat poster colour — bus, postbox, mini-dress, signage. Skin is pale, clean and slightly luminous. Shadows carry a cyan-blue cast: daylight-balanced film in a grey climate, and cold press blacks.

## Tonal Register

**Register**: neutral, cool-shadowed

Exposure +0.20 with Whites +10 keeps the image open and reportorial rather than moody; Contrast +15 supplies the "soot and whitewash" separation. The grade is asymmetric — a restrained warm highlight (35/5) against a distinctly cool shadow (210/10) — which is the point: skin stays neutral-warm while brick, concrete and shadowed clothing go blue-grey, as a grey London day renders on daylight film. A golden drift turns it into nostalgia; a shadow past ~210° turns it into teal-and-orange cinema.

## Lighting & Subject Matter

Flat overcast daylight, open shade, direct on-camera flash against a white wall, and the hard contrast of studio seamless. Subject matter is fashion and portraiture: mini-skirts, sharp suits, pale models against brick, rooftops and gasworks, close-cropped pop-star headshots.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure +0.20, Contrast +15 | Open reportorial exposure with press-like separation |
| Basic | Highlights -40, Whites +10 | Holds pale skin and white seamless |
| Basic | Shadows +25, Blacks -5 | Opens coats and doorways; no ink-black floor |
| HSL | Hue Green -15 | Rotates foliage/paint toward yellow-olive (negative = toward yellow) |
| HSL | Sat Green -25 | Drains parks and painted brick — the drab ground |
| HSL | Blue +10, Red +10 | Graphic accents, not sky |
| HSL | Orange Lum +10 | Pale, clean, slightly high-key skin |
| Color Grading | Highlight 35/5, Shadow 210/10, blend 75 | Warm-neutral skin against blue-grey shadow |
| Effects / Detail | Vignette -8, Sharpness 10, Grain 15/23/45 | Tight-crop falloff; 35mm blown up across a spread |

## Verification

**Structural**: Color treatment, PV 15.4, Adobe Color Look, neutral curves, no Calibration, no WB cast. Grain present with Sharpness 10, Luminance Smoothing 0 and no Clarity/Texture/Dehaze. HSL peaks at -25; Blacks -5.

**On the category description.** `docs/decade.md` calls this "high-contrast B&W"; the XMP is `Treatment="Color"`, and correctly so — monochrome has its own category, while this preset encodes the colour-supplement half of the era and imports the B&W contrast standard.

**Hue direction.** `HueAdjustmentGreen="-15"` is the correct sign for olive greens: Lightroom's axis runs Red → Orange → Yellow → Green → Aqua → Blue, so a negative Green value moves foliage toward yellow/olive, not cyan (STYLEGUIDE §4.1).

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 1960s: Exposure +0.20 with mild grain 15; warm highlight (35deg/5) against cool shadow (210deg/10); blue +10, green -25, red +10.
- **Sources:** 1960s Kodachrome/Agfacolor print references
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** Grain 15 at size 23 would be excessive for a transparency but is right for the artefact — 35mm enlarged to a spread, where grain is "a keynote look of the 1960s" ([Eye](https://eyemagazine.com/feature/article/town-shaped-the-sixties)). No XMP changes made.

## Sources

- [Terence Donovan's editorial photography — Amateur Photographer](https://amateurphotographer.com/technique/portrait_photography/a-look-back-at-terence-donovans-editorial-photography/) — the "Terrible Three", industrial backdrops.
- [Town shaped the Sixties — Eye](https://eyemagazine.com/feature/article/town-shaped-the-sixties) — 35mm enlargement, grain, "soot and whitewash".
- [David Bailey — Google Arts & Culture](https://artsandculture.google.com/story/david-bailey-and-the-story-of-fashion-photography-british-fashion-council/JQXhztVGSo0WLw) — Vogue 1960, white backgrounds.
- [Sunday Times Magazine at 60 — Press Gazette](https://pressgazette.co.uk/publishers/magazines/sunday-times-magazine-60-years-gallery/) — the first UK newspaper colour supplement.
- [Terence Donovan — Wikipedia](https://en.wikipedia.org/wiki/Terence_Donovan_(photographer)) — "Black Trinity", bomb-damaged London.
- [Kodachrome — Wikipedia](https://en.wikipedia.org/wiki/Kodachrome) — Kodachrome II (1961) and Kodachrome-X (1962).

## See Also

- [Decade presets](../../docs/decade.md)
- [Summer of Love](../Summer%20of%20Love/characteristics.md) — 1967, warmer and softer
- [New Wave](../New%20Wave/characteristics.md) — the cold monochrome descendant
- [Kodachrome Mid-Century](../Kodachrome%20Mid-Century/characteristics.md) — the slide stock these colour pages were printed from
