# Grunge Lightroom Preset — Characteristics

**Category**: Decade

The Grunge Lightroom preset recreates the colour strand of the Seattle 1991-94 look: desaturated, olive-shifted, under-exposed, heavily grained and vignetted, with the blacks closed down and no clean highlight anywhere. It is deliberately the least glamorous preset in the Decade folder. It also has to be honest about what it is emulating — the defining Sub Pop imagery of the period is black and white, so this preset models the *other* grunge: cheap colour lab prints, cross-processed editorial, and flash-lit club frames printed badly.

## Historical Context

Sub Pop was founded in Seattle in 1988 and built a single visual identity around one photographer. Charles Peterson was the label's house photographer, shooting Green River, Mudhoney, Soundgarden and Nirvana from the front of the pit; Bruce Pavitt's assessment was that the label "wanted one really strong identity" and that Peterson "should get the credit for setting it up" ([Seattle Times, 1995](https://archive.seattletimes.com/archive/19951023/2148380/the-vision-of-charles-peterson----seattle-photographers-style-finds-clear-success-in-the-blur-of-the-international-rock-scene)). The technique — flash balanced against a long shutter speed so the ambient light smears while the flash freezes — was adapted from Garry Winogrand's rodeo work.

The fashion system arrived in 1992 and immediately split the scene. Marc Jacobs's Spring/Summer 1993 collection for Perry Ellis translated thrift-store flannel into cashmere and silk; *Vogue* ran Steven Meisel and Grace Coddington's "Grunge & Glory" in December 1992; Cathy Horyn's verdict, "Grunge is anathema to fashion", outlived the collection ([AnOther](https://www.anothermag.com/fashion-beauty/7476/marc-jacobs-s-s93-nirvana-tribute-at-perry-ellis)). The palette that came out of that collision — plaid, thermal grey, faded denim, bruised colour — is what this preset is keyed to.

## Photographic Technology

- **Flash plus slow shutter.** Peterson's rig was a Nikon FE2, a 24mm lens, an off-camera Vivitar 285 flash and Tri-X ([Lens Magazine](https://lensmagazine.net/charles-peterson-an-exclusive-interview/)). Blown highlights and a bright foreground against a dim, moving background are structural, not a filter.
- **Pushed consumer film.** ISO 400 pushed to 800 or 1600 gave coarse, irregular grain and blocked shadows — the origin of Grain 40 at size 30 and roughness 65.
- **Colour was the exception, and it was cross-processed.** By 1995 Peterson's colour work was described as "a rich, cross-processed brew" ([Seattle Times](https://archive.seattletimes.com/archive/19951023/2148380/the-vision-of-charles-peterson----seattle-photographers-style-finds-clear-success-in-the-blur-of-the-international-rock-scene)); slide film in C-41 yields exactly the green-shifted shadows and hard contrast this preset grades. Cheap one-hour labs added their own casts ([The Darkroom](https://thedarkroom.com/cross-processing-film/)).
- **Mixed light, uncorrected.** Tungsten backstage, flash on the subject, overcast daylight outside — three white points with no correction applied.

## Visual Signature

A yellow-green shadow cast at hue 90 (saturation 12) with highlights barely tinted warm (hue 40 at 5) is the core move: the image looks like it was printed on paper that has aged. Green saturation is down 30 and green hue moved -20, toward yellow — so foliage and flannel go olive rather than staying emerald. Blue is cut 20, orange 10, yellow 15, and a global Saturation of -22 sits on top. Shadows are pushed *down* (-10) rather than lifted, which is what produces the muddy, underexposed midtones of a badly printed frame.

## Tonal Register

**Register**: low-key, muddy olive

At -0.30 EV with Blacks -25, Shadows -10 and a -20 vignette, the histogram sits low and the median tone is dirty rather than open. This is not the same as "faded" — there is no lifted black point and no matte curve; the image is dark *and* desaturated, which is the difference between a 1992 lab print and a 2015 matte preset.

## Lighting & Subject Matter

Direct flash in a small dark room, overcast Pacific Northwest daylight, fluorescent backstage corridors. Subjects are close and unposed: bands mid-motion, clothes worn rather than styled, parking lots, rehearsal rooms, cheap interiors. The preset punishes clean studio light — with nothing to muddy, it just looks under-exposed.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure -0.30 | Underexposed print, not a corrected file |
| Basic | Contrast +30, Highlights -50 | Hard separation; recovers flash speculars |
| Basic | Shadows -10, Blacks -25 | Closes the midtones and the black point — the "muddy" move |
| HSL | Hue Green -20, Sat Green -30 | Foliage and flannel toward olive, not cyan |
| HSL | Sat Orange -10, Yellow -15, Blue -20 | Kills the clean primaries |
| Presence | Saturation -22 | Global mute; no Vibrance to create a selective-colour gap |
| Color Grading | Shadow 90/12, Highlight 40/5, Blend 65 | Yellow-green shadows, faintly warm tops |
| Detail | Sharpness 10, Luminance Smoothing 0, Grain 40/30/65 | Coarse pushed-film texture, grain-safe sharpening |
| Effects | Post-Crop Vignette -20 | Cheap lens, dark corner, small room |

## Verification

**Structural**: Treatment Color, ProcessVersion 15.4, Adobe Color Look block, neutral curves, no Calibration, no Temperature/Tint. Grain 40 is paired with Sharpness 10 and Luminance Smoothing 0, and Clarity/Texture/Dehaze are all absent. `Vibrance` is absent rather than set, so the repo's "Vibrance within 5 points of Saturation, or remove it" rule is satisfied by removal — and with Saturation at -22 a Vibrance of 0 would in any case be *below* saturation, not above it, so the selective-colour failure mode cannot occur. HSL saturation peaks at -30; Blacks -25 is above the -30 floor.

**Known limitation**: the preset is colour-only. The most recognisable grunge photographs are Tri-X, so this preset cannot reproduce the Sub Pop house style and does not claim to.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 1991 register: olive-green shadow cast (90deg/12 with green saturation -30); Saturation -22; crushed blacks (-25) and Highlights -50; grain 40; Exposure -0.30.
- **Sources:** Cutaway, 'A history of color in film' (1990s desaturation, cold-white fills); NARA film preservation notes
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** Values confirmed against the file; no XMP change. The sweep's secondary sources could not be verified as URLs, so the source list below is rebuilt around Peterson's own technique and the 1992 fashion record.

## Sources

- [Charles Peterson — official biography](https://www.charlespeterson.net/bio) — Sub Pop house photographer; SLR, flash plus long exposure, black-and-white film as the scene's method.
- [The Vision of Charles Peterson — Seattle Times, 23 Oct 1995](https://archive.seattletimes.com/archive/19951023/2148380/the-vision-of-charles-peterson----seattle-photographers-style-finds-clear-success-in-the-blur-of-the-international-rock-scene) — Pavitt on the label identity; Winogrand-derived flash/long-shutter technique; Peterson's colour work as a "rich, cross-processed brew".
- [Charles Peterson: an exclusive interview — Lens Magazine](https://lensmagazine.net/charles-peterson-an-exclusive-interview/) — Nikon FE2, 24mm, Vivitar 285, Tri-X; the stage-diver frame and its method.
- [Marc Jacobs' S/S93 Nirvana Tribute at Perry Ellis — AnOther](https://www.anothermag.com/fashion-beauty/7476/marc-jacobs-s-s93-nirvana-tribute-at-perry-ellis) — December 1992 "Grunge & Glory", flannel/thermal palette, the anti-glamour framing.
- [Cross Processing Explained — The Darkroom](https://thedarkroom.com/cross-processing-film/) — E-6-in-C-41 contrast and colour-cast behaviour, the source of green-shifted shadows in colour grunge frames.

## See Also

- [Decade presets](../../docs/decade.md)
- [Hip Hop Golden Era](../Hip%20Hop%20Golden%20Era/characteristics.md) — the same years, warm and saturated instead
- [Cross-Processed](../Cross-Processed/characteristics.md) — the green-shadow mechanism used here, in isolation
- [Bleach Bypass](../Bleach%20Bypass/characteristics.md) — the other route to desaturated, crushed, grainy imagery
