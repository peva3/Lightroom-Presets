# Indie Sleaze Lightroom Preset — Characteristics

**Category**: Decade

The Indie Sleaze Lightroom preset recreates the 2006-2012 party-photography look: direct on-camera flash, hot white speculars, a cool drift in the shadows, midtones pulled slightly flat, and enough grain to stand in for a small-sensor JPEG. It is the only preset in the Decade folder built around a flash-lit subject in a dark room, and it is deliberately less bright and less cold than `Presets/Creative/Y2K Flash Digicam.xmp`, which is the harder, earlier version of the same idea.

## Historical Context

The look has a single dominant author. Mark Hunter started posting party photographs to a site called Polaroid Scene in 2004; after a cease-and-desist he renamed it thecobrasnake.com, and for the rest of the decade it functioned as the scene's morning-after newspaper ([Wikipedia](https://en.wikipedia.org/wiki/Mark_Hunter_(photographer)); [Vogue](https://www.vogue.com/article/the-cobrasnake-y2ks-archive-mark-hunter-book-indie-sleaze)). By 2005 he was making a living from it, shooting with a point-and-shoot and then a $600 Canon PowerShot Pro 1, running "like a coked-up paparazzo, shoving his camera in people's faces and punctuating the dim interior with photo flashes" ([WIRED, 2005](https://www.wired.com/2005/08/the-shiny-happy-people/)).

The era has a clean terminus. Hunter's own book covers 2004 to 2010, stopping at the launch of Instagram because "there was a true change in the imagery and style" ([Nylon](https://www.nylon.com/nylon-nights/the-cobrasnake-mark-hunter-y2k-archive-book)). The style is now named retroactively: "high flash and absolutely no Facetune allowed" ([PAPER](https://www.papermag.com/meg-superstar-princess-the-cobra-snake)). What was a delivery mechanism — unedited files uploaded the same night — became an aesthetic.

## Photographic Technology

- **Compact digital, direct flash, no diffusion.** Small sensor, slow lens, weak stabilisation: the flash is the only reliable light in the room, so it becomes the key, and everything beyond a few metres falls to black.
- **No editing.** Hunter uploaded hundreds of frames unedited ([Dazed](https://www.dazeddigital.com/fashion/article/56193/1/the-cobrasnake-indie-sleaze-2000s-mark-hunter-photo-book-sky-ferreira-lady-gaga)). No highlight recovery, no white balance correction — hence the era's affection for "sometimes the wrong white balance is the right one" ([Dazed, 2023](https://www.dazeddigital.com/fashion/article/59676/1/digital-cameras-trend-indie-sleaze-miu-miu-tiktok-bella-hadid-instagram-myspace)).
- **Grain here is sensor noise, not film.** The preset's Grain 18 at size 22 is a stand-in for small-sensor luminance noise and JPEG blocking. Grain *size* is kept low for that reason — large grain reads as 35mm film and misdates the look.
- **Blown whites are structural.** A flash a metre from a face clips it. The preset reproduces the clip with Whites +20 and +0.25 EV, and then uses Highlights -15 to stop digital clipping from going magenta.

## Visual Signature

Whites +20 with a +0.25 EV push makes skin and clothing blow first; the shadow wheel sits at hue 200 (a cool blue) at only 10 saturation, which is the "flash is warm, the room is cold" split that defines the era better than any overall cast. Highlights are graded at hue 40/10 so the flash pool stays warm rather than clinical. Colour is muted rather than vivid — Saturation -15 with Vibrance -13 — and green is pulled -15 to keep club lighting from turning neon. Orange luminance +12 keeps faces from going grey inside all that restraint.

## Tonal Register

**Register**: high-key at the subject, low-key in the room

The histogram is bimodal by construction: a blown flash subject against a near-black background. Exposure +0.25, Whites +20 and Blacks -22 put the subject in the top quarter and the room in the bottom tenth, with very little in between — that thin midtone separation is the look's fingerprint. It is not a high-key *image*; a frame evenly lit at this exposure would just look washed out.

## Lighting & Subject Matter

Direct flash at one to two metres, in clubs, house parties, backstage rooms and smoking areas. Subjects are close, often groups, often mid-laugh, often holding a drink. The preset expects motion and imperfection; it fails on tripod-lit portraits and on landscapes, where the flash falloff has nothing to fall off.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure +0.25, Contrast +20 | Pushes the flash exposure, keeps separation |
| Basic | Highlights -15, Shadows +5 | Just enough recovery to stop magenta clipping |
| Basic | Whites +20, Blacks -22 | Blown speculars, closed background |
| HSL | Orange Lum +12, Sat Orange +10 | Faces survive the desaturation |
| HSL | Sat Green -15, Blue -5, Red +5 | Club green suppressed, skin warmth held |
| Presence | Saturation -15, Vibrance -13 | Muted, unfiltered-looking; 2-point gap, inside the ±5 rule |
| Color Grading | Shadow 200/10, Highlight 40/10, Blend 75 | Cool room, warm flash — the split that reads as "flash" |
| Detail | Sharpness 10, Luminance Smoothing 0, Grain 18/22/48 | Small-sensor noise, grain-safe sharpening |
| Effects | Post-Crop Vignette -15 | Flash falloff, no lens-profile correction |

## Verification

**Structural**: Treatment Color, ProcessVersion 15.4, Adobe Color Look block, neutral curves, no Calibration, no Temperature/Tint — the cool cast is graded (shadow 200/10) rather than white-balanced, so the preset will not fight a camera's auto WB. Grain 18 is paired with Sharpness 10 and Luminance Smoothing 0, with Clarity/Texture/Dehaze absent. HSL saturation peaks at +10; Vibrance -13 against Saturation -15 is a 2-point gap; Blacks -22 is above the -30 floor.

**Differentiation from `Creative/Y2K Flash Digicam`**: that preset is a harder, colder, brighter flash look — Exposure +0.70, Temperature 4900, Highlights +25, Shadows -25, Clarity +15, Texture +12, Dehaze -5, vignette -12 with midpoint 30, plus calibration shifts (RedHue +15, RedSat +15, GreenHue -10, BlueHue -10) that are an approved exception for that file only. Indie Sleaze has none of those: it is warmer, softer, one stop darker and grainier, which is the difference between a 2002 party snapshot and a 2008 blog post.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** Mid-2000s flash-and-grain: cool shadow drift (200deg/10), Whites +20 for the on-camera flash, desaturated (Vibrance -13 / Saturation -15 within 5 points), grain 18; blacks -22.
- **Sources:** Cutaway, 'A history of color in film' (2000s saturated/pop looks); era CCD point-and-shoot flash characteristics
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** Values confirmed; no XMP change. One nuance now documented rather than "fixed": Highlights -15 is a recovery slider, so the blowout is produced by Whites +20 and the exposure push, not by the highlight slider. The sweep's generic film-history sources have been replaced with the Cobrasnake-era primary record.

## Sources

- [The Shiny, Happy People — WIRED, Aug 2005](https://www.wired.com/2005/08/the-shiny-happy-people/) — Hunter's point-and-shoot origins, the PowerShot Pro 1, flash-in-a-dark-room method, the photoblog business model.
- [Mark Hunter (photographer) — Wikipedia](https://en.wikipedia.org/wiki/Mark_Hunter_(photographer)) — Polaroid Scene (2004), the Cobrasnake rename, the mid-2000s to early-2010s span.
- [Revisiting Indie Sleaze, as It Happened — Vogue](https://www.vogue.com/article/the-cobrasnake-y2ks-archive-mark-hunter-book-indie-sleaze) — the blog as the scene's distribution channel; the "5 megabytes of fame" framing.
- [The Cobrasnake on the chaos and hedonism of the Indie Sleaze era — Dazed](https://www.dazeddigital.com/fashion/article/56193/1/the-cobrasnake-indie-sleaze-2000s-mark-hunter-photo-book-sky-ferreira-lady-gaga) — hundreds of unedited uploads; "super candid" method; 2004-2010 chronology.
- [What Indie Sleaze Was Really Like at the Time — Vice](https://www.vice.com/en/article/akvkpj/what-indie-sleaze-was-really-like-at-the-time) — the look's definition and the pre-smartphone party context.
- [Say sleaze! The return of the digital camera — Dazed, 2023](https://www.dazeddigital.com/fashion/article/59676/1/digital-cameras-trend-indie-sleaze-miu-miu-tiktok-bella-hadid-instagram-myspace) — graininess, overexposure, "migraine-inducing flash", and wrong-white-balance as deliberate style.

## See Also

- [Decade presets](../../docs/decade.md)
- [Y2K Flash Digicam](../Y2K-Flash-Digicam/characteristics.md) — the harder, colder flash variant
- [Y2K Digicam](../Y2K%20Digicam/characteristics.md) — the same sensor generation in daylight
- [McBling Heyday](../McBling%20Heyday/characteristics.md) — the same years, glossy and saturated instead of muted
