# Disco Warm Lightroom Preset — Characteristics

**Category**: Decade

The Disco Warm Lightroom preset recreates the colour of late-1970s New York nightlife photography: amber skin under direct flash, brown-gold shadows, saturated orange and red, a hot highlight roll-off and a vignette that mimics flash falloff. It is a low-key warm colour preset with moderate grain, designed for night interiors, flash portraits and dance-floor reportage rather than daylight.

## Historical Context

Studio 54 opened in 1977 in the former Gallo Opera House on West 54th Street, with Steve Rubell and Ian Schrager retaining much of the building's theatrical lighting ([Studio 54 — Wikipedia](https://en.wikipedia.org/wiki/Studio_54)). It ran for less than three years and became the decade's shorthand for glamour: Andy Warhol, a regular, called it "a dictatorship on the door but a democracy on the dance floor". Its image was made by press photographers working the room — Allan Tannenbaum, Rose Hartman, Ron Galella — whose flash-lit frames ran within days ([Vogue India gallery](https://www.vogue.in/fashion/gallery/see-these-21-photos-from-studio-54-that-prove-it-was-just-as-iconic-as-everyone-says)). *Saturday Night Fever* (December 1977) then fixed the lighting vocabulary — mirror ball, colour wash, hard rim — as thoroughly as it fixed the white suit ([Saturday Night Fever](https://en.wikipedia.org/wiki/Saturday_Night_Fever)). This preset takes the photography, not the poster.

## Photographic Technology

- **Direct on-camera flash was the key light.** A thyristor flash at 1/60 or slower against ambient tungsten gave the signature structure: a hard, close, correctly exposed subject in front of an under-exposed room. Slow-shutter "drag" pulled warm ambient and moving lights into the same frame, smearing highlights behind the subject.
- **High-speed colour negative, pushed.** 400 ASA film exposed at 800–1600 and push-processed gained contrast and coarse dye-cloud grain; pushing also shifts colour warm-magenta, a behaviour Kodak documents for its pushable colour stocks ([Kodak E-55](https://125px.com/docs/film/kodak/e55-2009_06.pdf)).
- **Tungsten and gels.** House lighting was incandescent (≈3200 K) with coloured gel accents; daylight film under tungsten goes amber, and no single balance handled magenta or green gels plus tungsten plus flash. The mixed cast is the look.
- **Reproduction was cheap.** Newspaper and magazine printing clipped highlights and thickened blacks, so published frames read harder than the negatives.

## Visual Signature

Amber highlights (35°/18) and brown-gold shadows (30°/12) — a strong warm grade at *both* ends with no cool counterweight at all. Orange is pushed +15 saturation and +15 luminance, the skin-and-sweat move: it brightens as well as saturates, so faces glow instead of going tangelo. Red and yellow follow at +10; blue is cut −10 so the background falls back. Contrast +25 with Highlights −45 keeps sequins and mirror-ball speculars from clipping, while Blacks −15 and a −12 vignette let the room go dark at the edges.

## Tonal Register

**Register**: low-key, warm-golden (amber)

Exposure +0.10 is nominal — the subject is lit by flash, so exposure is really set by the flash-to-ambient ratio. What defines the register is terminal warmth: there is no cyan or teal anywhere in the grade, unlike the "orange and teal" convention that later stood in for nightlife. On a cool frame the preset pulls everything amber; on an already-warm tungsten frame it doubles up, and orange clothing clips before skin does.

## Lighting & Subject Matter

On-camera flash with visible falloff, mirror-ball speckles, neon behind the bar, tungsten practicals, smoke, gel washes. Subject matter is dance-floor couples, satin and sequins, sweat, sunglasses indoors, crowded banquettes. Available-light frames work but lose the flash structure that makes the look read as 1977.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure +0.10, Contrast +25 | Nominal exposure; contrast supplies flash hardness |
| Basic | Highlights −45, Shadows +20 | Holds sequins and mirror-ball speculars; opens dark hair and suits |
| Basic | Whites +10, Blacks −15 | Small accents over a firm, uncrushed floor |
| Presence | No Saturation or Vibrance | Colour carried by HSL and grading, not a global push |
| HSL | Orange Sat +15, Orange Lum +15 | Skin glow; the defining "sweat and sequin" move |
| HSL | Yellow +10, Red +10, Blue −10 | Warm accents forward, background pushed back |
| Color Grading | Highlight 35/18, Shadow 30/12, blend 75 | Amber above, brown-gold below — no cool end |
| Effects | Grain 20 / Size 26 / Roughness 50 | Pushed 400-speed colour negative |
| Effects | Post-Crop Vignette −12 | Flash falloff into a dark room |

## Verification

**Structural**: Color, PV 15.4, `Adobe Color` Look, neutral curves, no Calibration, no Temperature or Tint. HSL saturation peaks at +15 / −10. Blacks −15, inside the floor. Vibrance and Saturation are both absent, so the gap rule is satisfied trivially.

**Grain rule engaged**: GrainAmount 20 with Sharpness 10, LuminanceSmoothing 0, no Clarity/Texture/Dehaze. Roughness 50 sits inside the 45–65 organic band and Size 26 stays below the point where grain visibly blurs detail.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 1970s amber register: warm highlight 35deg/18 and brown-gold shadow 30deg/12; Exposure +0.10 with Highlights -45 to keep the amber from clipping; saturation pushed on orange/red/yellow; grain 20.
- **Sources:** In-Depth Cine, 'Why Movies From The 70s & 80s Look Like This: Kodak 100T 5247' (saturated warm stock, magenta-leaning blues); NARA 'Film Preservation 101' (magenta dye fade)
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** Research supports the amber two-ended grade, the orange luminance lift and the flash-falloff vignette. No XMP changes. One recorded tension: the shadow grade at 30/12 is gentler than the hardest Studio 54 frames, which go nearly black between subject and background — a portability compromise, since a heavier shadow grade destroys available-light frames.

## Sources

- [Studio 54 — Wikipedia](https://en.wikipedia.org/wiki/Studio_54) — 1977 opening, Rubell/Schrager, Warhol's line.
- [Studio 54 gallery — Vogue India](https://www.vogue.in/fashion/gallery/see-these-21-photos-from-studio-54-that-prove-it-was-just-as-iconic-as-everyone-says) — Tannenbaum and Hartman flash frames.
- [Disco — Wikipedia](https://en.wikipedia.org/wiki/Disco) — the subculture's emergence and mass peak.
- [Saturday Night Fever — Wikipedia](https://en.wikipedia.org/wiki/Saturday_Night_Fever) — 1977 release, the film that fixed the vocabulary.
- [Kodak E-55 datasheet](https://125px.com/docs/film/kodak/e55-2009_06.pdf) — push-processing colour shift.

## See Also

- [Decade presets](../../docs/decade.md)
- [Gatsby Art Deco](../Gatsby%20Art%20Deco/characteristics.md) — champagne warmth in another decade
- [Diner Americana](../Diner%20Americana/characteristics.md) — mixed tungsten/neon night interiors, cooler shadows
- [Cinestill-800T](../Cinestill-800T/characteristics.md) — tungsten night colour with halation
