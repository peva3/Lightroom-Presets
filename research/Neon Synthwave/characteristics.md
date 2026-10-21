# Neon Synthwave Lightroom Preset — Characteristics

**Category**: Decade

The Neon Synthwave Lightroom preset recreates the print-and-poster half of 1980s neon imagery: magenta highlights, cyan-blue shadows, greens pulled almost out of the frame, and a hard, clean contrast with no grain at all. It is built for the outrun/retro-futurist visual language — chrome type, grid horizons, rain-slick streets — rather than for the texture of the video tape those images were once distributed on. That distinction matters inside this repo: the Decade preset is the *artwork*, `Presets/Creative/1980s VHS Synthwave.xmp` is the *playback*.

## Historical Context

The imagery this preset borrows did not come from a film stock; it came from lighting and from graphic design. On *Blade Runner* (1982) Jordan Cronenweth, ASC lit the New York Street set with "dozens of neon signs", dimming the in-frame tubes to just above the point where they would flicker so the colour stayed saturated on film, while off-camera neons were run at full brightness as the key ([American Cinematographer](https://theasc.com/article/blade-runner-cronenweths-photography/)). The result was not a colour cast but a colour *system*: hard backlight, smoke, deep shadow, saturated emissive colour.

The magenta-and-cyan pair has a second, more prosaic origin. IBM's Color Graphics Adapter (1981) offered a four-colour mode of white, black, cyan and pink, and that palette is widely credited as the root of the outrun look ([Aesthetics of Design](https://www.aesdes.org/2024/01/24/aesthetics-exploration-synthwave/)). *TRON* (1982) supplied the perspective grid. Neither was a photographic reference; both were screen artefacts that later became a photographic vocabulary.

The movement itself is post-2000: bedroom producers, then *Drive* (2011) and *Hotline Miami* (2012) fixed the look for a mass audience. Design writing is blunt that what is being copied "is not the 1980s exactly, it is 1980s packaging — VHS sleeves, arcade cabinet art, airbrushed album covers" ([vocab.design](https://vocab.design/synthwave)).

## Photographic Technology

There is no emulated emulsion here. The preset targets a rendered or printed image: anamorphic lens flares, smoke-hazed backlight, practical neon — then a poster-grade reproduction with clean blacks and no visible grain.

That is why `GrainAmount` is absent (0) while `Dehaze="+10"` is present. Dehaze adds the airless, glossy separation of an airbrushed sleeve; grain would re-introduce the analogue decay that belongs to the VHS preset. The repo's grain rule (grain > 0 requires Sharpness 10 and Clarity/Texture/Dehaze at 0) does not apply because there is no grain to protect.

## Visual Signature

Highlights sit on magenta (hue 315 at 25); shadows sit on cyan-blue (hue 210 at 22). Greens are cut by 45 saturation so foliage, signage and clothing cannot compete with the neon; magenta is lifted +35 and blue +15, with a small orange +10 so skin does not go dead. Contrast is +35 with Highlights -60 and Shadows +30, which produces the flat, poster-like tonal compression of an illustration. Blacks stop at -20 and the vignette is -18 — dark enough to seal the frame, not so dark that the grid disappears.

## Tonal Register

**Register**: low-key, cool-shadowed, magenta-highlight

Exposure is -0.20 with a -18 vignette and -20 blacks, so the frame is deliberately under the midpoint: neon reads as emissive only when it sits against darkness. Both colour-grading wheels are cool (210 and 315), so the preset must never be pushed toward warm-golden — that is `Miami Vice` and `Disco Warm` territory. The one warm element is the +10 orange HSL saturation, which exists only to keep faces from turning into part of the background.

## Lighting & Subject Matter

Night, wet asphalt, practical neon, headlights, CRT glow, rain on glass. Subjects are cityscapes, cars shot from behind, silhouettes, arcades. The preset assumes a scene with its own light sources; applied to flat daylight it simply produces a cold, contrasty picture with a violet cast and no neon to justify it.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure -0.20, Contrast +35 | Sinks the frame and hardens it — poster contrast |
| Basic | Highlights -60, Shadows +30 | Compresses the top, opens the bottom: illustration, not photograph |
| Basic | Whites +15, Blacks -20 | Bright emissives, sealed blacks |
| Presence | Dehaze +10 | Airless, glossy separation; no grain to conflict with it |
| HSL | Sat Magenta +35, Blue +15, Orange +10 | The neon pair, plus a skin lifeline |
| HSL | Sat Green -45 | Removes the one hue that fights magenta/cyan |
| Color Grading | Highlight 315/25, Shadow 210/22, Blend 70 | The whole look: magenta tops, cyan-blue bottoms, clean zone separation |
| Detail | Sharpness 10, Luminance Smoothing 0, no grain | Digital purity — the artwork, not the tape |
| Effects | Post-Crop Vignette -18 | Seals the corners around the grid |

## Verification

**Structural**: Treatment Color, ProcessVersion 15.4, Adobe Color Look block, all four ToneCurvePV2012 curves neutral, no Calibration, no Temperature/Tint. HSL saturation peaks at -45 (inside the ±60 cap); Blacks -20 is above the -30 floor; Vibrance and Saturation are both absent, so the ±5 gap rule is not engaged.

**Differentiation from `1980s VHS Synthwave`**: the Creative preset carries Grain 45 at size 42, Clarity -23, Texture -25, Dehaze -15, Highlights -90, Shadows +50, Balance +30 and eight hue warps (Green -45, Purple +23, Red +20, Blue -20). That is chroma bleed and tape softening. This preset has no grain, no negative clarity/texture, positive dehaze, no hue warps and only four saturation moves. They are not variants of each other; one degrades the signal, the other cleans it.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 1980s neon: shadow 210deg/22 and highlight 315deg/25 with Blending 70; greens gutted (-45), magenta +35; Contrast +35, Highlights -60, Dehaze +10 for the glossy video look.
- **Sources:** In-Depth Cine, Kodak 5247 analysis; Filmmakers Academy, 'Magenta: Movie Color Palettes'; Cutaway, 'A history of color in film' (1980s/90s/2000s sections)
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** The sweep's "Blending 50" is a transcription error: the file reads `crs:ColorGradeBlending="70"`, which is the correct value for clean zone separation and matches the poster register. No XMP change; the document now states the actual value. The sweep's cited sources could not be re-verified as URLs, so the Sources list below is rebuilt from sources checked in this pass.

## Sources

- [Blade Runner: Cronenweth's Photography — American Cinematographer](https://theasc.com/article/blade-runner-cronenweths-photography/) — neon practicals on dimmers, hard backlight, smoke, high contrast; the lighting grammar behind the palette.
- [Aesthetics Exploration: Synthwave — Aesthetics of Design](https://www.aesdes.org/2024/01/24/aesthetics-exploration-synthwave/) — IBM CGA four-colour palette as the origin of magenta/cyan; TRON grid; retro-futurist lineage.
- [Synthwave (outrun) — vocab.design](https://vocab.design/synthwave) — the fixed poster composition, chrome type, "1980s packaging" rather than the decade itself; vaporwave distinction.
- [Outrun: The Aesthetic Deconstructed — Joel Chan](https://medium.com/@cywjoel/outrun-the-aesthetic-deconstructed-dbd3cd8679b7) — sun, grid, type conventions; why the palette is short and dark-dominant.
- [Purple Skies, Cyan Grids — University of Melbourne Student Union](https://umsu.unimelb.edu.au/news/article/7797/Purple-Skies-Cyan-Grids-The-Synthwave-Aesthetic/) — chronology of the 2000s-2010s revival, which dates the look after the decade it depicts.

## See Also

- [Decade presets](../../docs/decade.md)
- [VHS / Synthwave 1980s](../VHS-Synthwave-1980s/characteristics.md) — the tape-degradation treatment this preset deliberately refuses
- [Miami Vice](../Miami%20Vice/characteristics.md) — the pastel, daylight-warm 1980s register
- [Cyberpunk Neon City](../Cyberpunk%20Neon%20City/community-recipes.md) — the same neon logic pushed toward dystopia
