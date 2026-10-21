# Y2K Digicam Lightroom Preset — Characteristics

**Category**: Decade

The Y2K Digicam Lightroom preset recreates the daylight, general-purpose rendering of an early CCD compact: a cool-neutral cast, a magenta bias in skin, clipped white highlights, a strong flash-and-lens vignette, low global saturation and fine sensor grain. It is the everyday counterpart to `Presets/Creative/Y2K Flash Digicam.xmp`, which is the nightclub version of the same sensor generation.

## Historical Context

Between roughly 1999 and 2004 the point-and-shoot digital camera became an ordinary object. Resolution was the marketing story — 2 to 3 megapixels, then 5 — but the technical story was dynamic range. Consumer CCDs were linear devices with 8-bit converters, so once a pixel's charge well filled, it simply stopped responding: highlights did not roll off, they ended ([DPReview](https://www.dpreview.com/reviews/sonycd200/13)). Imaging Resource put it plainly in 2003: the range of light to dark a digicam CCD could capture "has always lagged badly behind film", which is why Fujifilm's Super CCD SR traded resolution for up to 400 per cent more highlight headroom ([Imaging Resource](https://www.imaging-resource.com/ir-archive/newsletter-archive/imaging-resource-newsletter-24-january-2003-new-fuji-ccd-enhances-dynamic-range-minolta-dimage-xi-a-favorite-subcompact-updated/)).

The look is now consumed as nostalgia rather than as a defect. Gen Z shooters seek out 2000s compacts for "fuchsia-tinted photos that looked straight from the early aughts" ([New York Times](https://www.nytimes.com/2023/01/07/technology/digital-cameras-olympus-canon.html)), and the style's vocabulary — graininess, overexposure, "migraine-inducing flash", "sometimes the wrong white balance is the right one" — is now deliberate ([Dazed](https://www.dazeddigital.com/fashion/article/59676/1/digital-cameras-trend-indie-sleaze-miu-miu-tiktok-bella-hadid-instagram-myspace)).

## Photographic Technology

- **Hard highlight clipping.** The Sony MVC-CD200 measured 8.8 bits and roughly 450:1 at ISO 100 — good for its class, and still a hard ceiling ([DPReview](https://www.dpreview.com/reviews/sonycd200/13)). The preset reproduces this with Whites +25 and Highlights +5: it pushes the top end rather than protecting it.
- **Auto white balance that guesses.** CCD-era AWB is unreliable indoors; testing of a later CCD compact found "a very slight magenta cast with the Auto white balance setting" under incandescent light, and a "fairly strong magenta cast" from the tungsten preset ([Imaging Resource](https://www.imaging-resource.com/cameras/canon-g12-review/exposure/)). A magenta skin bias is therefore a sensor-era property, not a stylistic flourish.
- **Over-saturated in-camera JPEGs.** Measured colour reproduction around 102 per cent saturation was normal for the class ([Reviewed](https://www.reviewed.com/cameras/content/fujifilm-finepix-f440-digital-camera-review)) — but early compacts also crushed subtlety, which is why this preset sits at Saturation -8 rather than boosting.
- **Grain is sensor noise.** Grain 15 at size 20 is fine and tight, matching luminance noise and JPEG blocking rather than film.

## Visual Signature

Both colour-grading wheels sit on hue 210 at saturation 10, which produces a cool cast at *both* ends of the tone scale — the signature that separates this preset from a simple blue-shadow grade. Tint +10 plus magenta +8 and red +5 give the skin bias; orange luminance +10 keeps faces from going grey inside the cool cast; green is pulled -15 so foliage does not go acid. Whites +25 with Highlights +5 blows the sky and white clothing the way a CCD does, and the -20 vignette is the strongest in the Decade folder because small-sensor compacts had both lens falloff and flash falloff.

## Tonal Register

**Register**: cool-neutral, mid-key, magenta-biased

Exposure +0.10 and Contrast +15 keep the median tone near the middle: this is a *daylight generalist* preset, not a low-key or high-key look. The visible coolness is graded (210/10 at both ends) rather than white-balanced, so it holds regardless of the source file. The absolute `Temperature="5100"` is close to neutral on a daylight frame, but renders much cooler than as-shot on a tungsten one — faithful to a camera whose AWB never quite got there, though not WB-neutral.

## Lighting & Subject Matter

Open shade, overcast daylight, on-camera flash as fill, indoor fluorescent. Subjects are everyday: friends, streets, pets, shop windows, holiday snapshots. The preset wants ordinary light and ordinary subjects; it reads as a period snapshot only when nothing in the frame is trying to be cinematic.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure +0.10, Contrast +15 | Mid-key, slightly crunchy JPEG contrast |
| Basic | Highlights +5, Shadows +10 | Pushes the top into clipping; opens shadows a little |
| Basic | Whites +25, Blacks -10 | The CCD blowout; blacks stay open |
| WB | Temperature 5100, Tint +10 | Daylight anchor plus the magenta AWB error |
| HSL | Sat Magenta +8, Red +5, Orange Lum +10 | Magenta skin bias, faces kept bright |
| HSL | Sat Green -15, Blue +5, Yellow +5 | Suppresses acid foliage; keeps sky and warm surfaces |
| Presence | Saturation -8 | Early-compact flatness rather than modern punch |
| Color Grading | Highlight 210/10, Shadow 210/10, Blend 75 | Cool cast at both ends — the defining move |
| Detail | Sharpness 10, Luminance Smoothing 0, Grain 15/20/40 | Fine sensor noise, grain-safe sharpening |
| Effects | Post-Crop Vignette -20 | Lens plus flash falloff |

## Verification

**Structural**: Treatment Color, ProcessVersion 15.4, Adobe Color Look block, neutral curves, **no Calibration** — the repo's approved calibration exception belongs to `Creative/Y2K Flash Digicam`, not here. Grain 15 is paired with Sharpness 10 and Luminance Smoothing 0, with Clarity/Texture/Dehaze absent. HSL saturation peaks at +10; Blacks -10 is above the floor.

**Temperature/Tint exception**: retained under the repo's "defining characteristic" rule. AWB drift and its magenta bias *are* the CCD signature; removing WB would leave only a blue split-tone. `Tint +10` is doing identifiable work here, not decorating a film emulation.

**Known caveat (repo-wide, not fixed)**: this file sets `Temperature`/`Tint` without `crs:WhiteBalance="Custom"`, a pattern shared by 78 look presets, whereas every `Presets/Utility/WB *.xmp` includes the attribute. If a host treats a missing `WhiteBalance` as "As Shot" and ignores the absolute temperature, the cool cast falls back to the two 210° wheels — most of the look survives, but the magenta skin bias weakens. Fixing it means editing 78 files, so it is recorded rather than patched here.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 2000s CCD point-and-shoot: Temp 5100 (cool cast) with Tint +10 (magenta), Whites +25 and Highlights +5 for blown flash highlights, mild grain 15/20, vignette -20 (flash falloff), Saturation -8.
- **Sources:** Cutaway, 'A history of color in film' (2000s saturated/pop looks); era CCD point-and-shoot flash characteristics
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** Values confirmed; before → after: no change. Correction to the sweep's wording: "Temp 5100 (cool cast)" is misleading on its own — 5100 K is near-neutral daylight, and the coolness the eye sees comes from the 210° wheels at both ends. The document now states this. Sources rebuilt below.

## Sources

- [Sony MVC-CD200 review: Dynamic Range — DPReview](https://www.dpreview.com/reviews/sonycd200/13) — 8-bit converters, CCD charge wells, measured 8.8 bits / 450:1; the mechanism behind hard highlight clipping.
- [New Fuji CCD Enhances Dynamic Range — Imaging Resource, 24 Jan 2003](https://www.imaging-resource.com/ir-archive/newsletter-archive/imaging-resource-newsletter-24-january-2003-new-fuji-ccd-enhances-dynamic-range-minolta-dimage-xi-a-favorite-subcompact-updated/) — CCDs are linear and clip; film has a shoulder; 400% headroom as the era's fix.
- [Canon G12 review: exposure and white balance — Imaging Resource](https://www.imaging-resource.com/cameras/canon-g12-review/exposure/) — AWB magenta cast under incandescent, tungsten-preset magenta shift, blown outdoor highlights on a CCD compact.
- [Fujifilm FinePix F440 review — Reviewed](https://www.reviewed.com/cameras/content/fujifilm-finepix-f440-digital-camera-review) — 102.3% saturation out of camera as normal for the class.
- [The Hottest Gen Z Gadget Is a 20-Year-Old Digital Camera — New York Times](https://www.nytimes.com/2023/01/07/technology/digital-cameras-olympus-canon.html) — the revival, and the "fuchsia-tinted photos" description of real 2000s compact output.
- [Say sleaze! The return of the digital camera — Dazed](https://www.dazeddigital.com/fashion/article/59676/1/digital-cameras-trend-indie-sleaze-miu-miu-tiktok-bella-hadid-instagram-myspace) — the aesthetic vocabulary: graininess, overexposure, wrong white balance as style.

## See Also

- [Decade presets](../../docs/decade.md)
- [Y2K Flash Digicam](../Y2K-Flash-Digicam/characteristics.md) — the direct-flash party variant, with the repo's calibration exception
- [Indie Sleaze](../Indie%20Sleaze/characteristics.md) — the same compact-camera generation at night
- [McBling Heyday](../McBling%20Heyday/characteristics.md) — the later, louder, more saturated digital register
