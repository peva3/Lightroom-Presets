# Selenium Tone — Community Recipes & Reference Values

> Compiled from darkroom toning threads (Photrio, r/Darkroom, APUG), toner datasheets, and
> published print-toning walkthroughs. Values are expressed as translation targets for the
> Lightroom ColorGrade panel, not as literal darkroom times.

## Recipe A: "Weak selenium" (subtle archive tone)
- Kodak Rapid Selenium Toner 1+40, 3–5 min at 20 °C.
- Visual result: a whisper of warmth in the lower midtones; most viewers read the print as
  neutral until it is placed beside an untoned print.
- ColorGrade target: ShadowHue ≈ 20–30 (red-brown), ShadowSat 5–8; highlight sat ~0.

## Recipe B: "Classic eggplant" (the recognisable selenium look)
- Kodak Rapid Selenium Toner 1+10 to 1+20, 5–10 min, or 1+3 for a strong shift.
- Visual result: purple-brown / aubergine in the shadows, deepening to near-black at the toe.
- ColorGrade target: ShadowHue ≈ 280–300 (violet), HighlightHue ≈ 285, ShadowSat 8–12,
  HighlightSat 5–10. Balance negative (−10 to −25) to weight the tint downward.

## Recipe C: "Split sepia + selenium"
- Full sepia first, then selenium. The sepia warms the highlights, the selenium cools and
  deepens the shadows — the historical origin of the warm/cool split look.

## Community consensus points
- Selenium is the *only* common toner that reliably increases D-max; photographers use it for
  the deeper blacks as much as for the hue.
- Over-toning selenium turns prints flat and metallic-looking — keep saturation modest.
- Colour shift is far more visible in the shadows; do not tint the highlights heavily.
- Digital emulation must keep `Blacks2012` negative. A lifted black point instantly reads as
  "faded" rather than "toned".

## Quality assessment
Sources agree on the hue family (violet/purple-brown at strength, red-brown when weak) and on the
D-max increase. No source suggests sepia-style bleaching — any emulation that washes out the
whites is wrong for this toner.
