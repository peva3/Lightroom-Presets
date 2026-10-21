# Post-War Optimism Lightroom Preset — Characteristics

**Category**: Decade

The Post-War Optimism Lightroom preset recreates the unclouded colour of late-1940s and 1950s American consumer photography — the Kodak Colorama, the new suburban lawn, the department-store catalogue. It is a high-key, warm-neutral grade with open shadows, restrained greens and light 35mm grain, built for ordinary daylight.

## Historical Context

Colour was a rounding error in Kodak's business until the war ended: when the company took the east balcony of Grand Central Terminal in 1949, colour was about **two percent** of its trade ([DART/PDN](https://www.ai-ap.com/publications/article/2564/dont-take-my-kodachrome-away.html)). The Colorama — an 18-by-60-foot backlit transparency changed every few weeks from May 1950 — was the campaign that followed, 565 of them over forty years ([George Eastman Museum](http://hdl.handle.net/1802/35061)). Its brief was explicit: Kodak wanted commuters who had "had a bad day at the office" to look up and "like their wives and children the better for it" ([The New Yorker, 1950](https://www.newyorker.com/magazine/1950/05/27/the-giant)).

This is advertising, not documentary: staged with art directors, crews, models and studio lighting ([finding aid](http://hdl.handle.net/1802/35061)).

One correction to the popular memory: the colour of 1945–1953 is largely *not* the colour we associate with the decade. Early Kodacolor prints had "very poor dye stability and severe coupler staining" and have faded brown; magenta stability improved in 1954 and cyan in 1959, and colour only overtook black-and-white in US amateur photofinishing around 1960 ([Topics in Photographic Preservation](https://resources.culturalheritage.org/pmgtopics/2009-volume-thirteen/13_13_Weaver.html)).

## Photographic Technology

- **Kodachrome** (35mm from 1936) was a 10 ASA daylight transparency processed only by Kodak; K-11 ran from 1955 ([timeline](https://en.wikipedia.org/wiki/Kodachrome)). Its thin, coupler-free emulsion gave high acutance and pure dye, but it was a *slide* medium — prints needed duplication.
- **Ektachrome** arrived in 1946 as an 8 ASA daylight sheet film, deliberately home-processable. Kodak warned of blue casts under overcast skies and recommended CC13–CC15 filters ([Photomemorabilia](https://www.photomemorabilia.co.uk/Colour_Darkroom/Early_Kodak_Ektachrome.html)): daylight balance was approximate.
- **Kodacolor** negative film (1942) was the route to the family print, and slow emulsions demanded enormous light — the Colorama team reportedly used hundreds of flashbulbs to balance foreground against sky ([DART](https://www.ai-ap.com/publications/article/2564/dont-take-my-kodachrome-away.html)). Print reproduction was the weak link: originals "could be glorious" while early magazine reproduction was "generally wretched" ([Jenkins](http://www.rupertjenkins.com/colorado-photo-history-blog/2021/6/22/mid-century-color)). Part of this look is a *printing* artefact.

## Visual Signature

Sunlit whites that read as white; shadows open and faintly warm rather than teal. Skin is clean, slightly pale and even, with ruddiness pulled back. Skies are confident but never Velvia-electric. Reds and oranges carry the loudest chroma — chrome, produce, children's clothing — while lawns sit back.

## Tonal Register

**Register**: warm-golden, high-key

At +0.30 EV with Whites +12 and Shadows +25 the histogram crowds upward: that is the Colorama register, where a correct exposure is *bright*. Warmth comes from grading both ends (highlight 40/10, shadow 35/6), not from white balance, and Blacks stop at -5 so nothing anchors to true black. The preset must never crush shadows, cool them toward cyan, or let greens dominate.

## Lighting & Subject Matter

Hard summer sun with open shade, on-camera flash fill, or flat studio light pretending to be a garden. Subject matter is aspirational domesticity: sprinklers, station wagons, chrome, picnics, new kitchens.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure +0.30, Contrast +10 | High-key density without flattening |
| Basic | Highlights -35, Shadows +25 | Recovers slide-like shoulders; keeps shade open |
| Basic | Whites +12, Blacks -5 | Bright whites, no true black |
| WB | Temperature 5700 | Daylight anchor — warmth belongs to the grade |
| Presence | Saturation +10, Vibrance +8 | Confident consumer colour (2-point gap) |
| HSL | Red +8, Orange +8, Orange Lum +10 | Chrome, produce, clean bright skin |
| HSL | Blue +5, Green -10 | Sky present, lawn held back |
| Color Grading | Highlight 40/10, Shadow 35/6, blend 75 | Warm sun and warm bounce, no cool end |
| Detail / Effects | Sharpness 10, Grain 18/24/45, Vignette -8 | Fine 35mm texture, grain-safe sharpening |

## Verification

**Structural**: Color treatment, PV 15.4, Adobe Color Look, neutral four-curve ToneCurvePV2012, no Calibration, no Tint. Grain present with Sharpness 10, Luminance Smoothing 0 and no Clarity/Texture/Dehaze. HSL peaks at ±10; Blacks -5.

Temperature 5700 is retained under the repo's "defining characteristic" exception: it is the daylight anchor that keeps warmth in the grade; without it a warm-graded preset drifts gold on auto-WB imports.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 1950s consumer colour: Temp 5700, +0.30 EV, Vibrance +8 / Saturation +10, grain 18, warm 35-40deg highlights, greens -10.
- **Sources:** 1950s Kodachrome/Ektachrome consumer print references
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** No XMP changes made.

## Sources

- [Don't Take My Kodachrome Away — DART/PDN](https://www.ai-ap.com/publications/article/2564/dont-take-my-kodachrome-away.html) — 1949 colour at 2% of Kodak's business; Colorama history.
- [Kodak Colorama archive — George Eastman Museum](http://hdl.handle.net/1802/35061) — 565 displays, staged domesticity.
- [The Giant — The New Yorker, 1950](https://www.newyorker.com/magazine/1950/05/27/the-giant) — Stuber's brief.
- [Mid-Century Color — Rupert Jenkins](http://www.rupertjenkins.com/colorado-photo-history-blog/2021/6/22/mid-century-color) — stock dates, advertising, poor reproduction.
- [Topics in Photographic Preservation](https://resources.culturalheritage.org/pmgtopics/2009-volume-thirteen/13_13_Weaver.html) — Kodacolor 1942; 1954/1959 dye fixes.
- [Early Kodak Ektachrome — Photomemorabilia](https://www.photomemorabilia.co.uk/Colour_Darkroom/Early_Kodak_Ektachrome.html) — 1946 8 ASA sheet film.

## See Also

- [Decade presets](../../docs/decade.md)
- [Diner Americana](../Diner%20Americana/characteristics.md) — the same decade after dark
- [Kodachrome Mid-Century](../Kodachrome%20Mid-Century/characteristics.md) — the slide half of 1950s colour
- [Kodachrome 64](../Kodachrome-64/characteristics.md) — the stock emulation this preset avoids
