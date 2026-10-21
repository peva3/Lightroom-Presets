# Y2K Digicam — Community Recipes

Ranges for a 1999-2004 CCD compact look in daylight: cool cast, magenta skin, clipped whites, open noisy shadows, tight grain. The shipped `Y2K Digicam.xmp` is the generalist version; the flash-party extreme lives in `Y2K Flash Digicam`.

## Reference Looks

- **Canon PowerShot / Olympus / Sony Cyber-shot daylight snapshots** — blown skies, flat shadows, JPEG colour ([DPReview](https://www.dpreview.com/reviews/sonycd200/13) on the sensor's clipping behaviour).
- **Wrong-AWB interiors** — magenta under tungsten, cyan under fluorescent ([Imaging Resource](https://www.imaging-resource.com/cameras/canon-g12-review/exposure/)).
- **2000s family albums and early Myspace uploads** — compression, noise, no highlight recovery ([Dazed](https://www.dazeddigital.com/fashion/article/59676/1/digital-cameras-trend-indie-sleaze-miu-miu-tiktok-bella-hadid-instagram-myspace)).
- **Gen-Z digicam revival frames** — the same look, now intentional ([NYT](https://www.nytimes.com/2023/01/07/technology/digital-cameras-olympus-canon.html)).

## Slider Starting Points

| Panel | Range | Notes |
|---|---|---|
| Exposure | 0.00 to +0.35 | Compacts already expose bright |
| Contrast | +5 to +25 | JPEG contrast, not film contrast |
| Highlights | 0 to +20 | Positive values are correct for CCD clipping |
| Shadows | 0 to +25 | Lift, do not crush — CCDs had noisy open shadows |
| Whites | +15 to +35 | The blowout |
| Blacks | -20 to 0 | Never below -30 |
| Temperature | 4800-5300 | Absolute; 5100 is near-neutral daylight |
| Tint | +5 to +15 | The magenta bias |
| Saturation | -15 to 0 | Early compacts were flat, not punchy |
| HSL Sat | Green -25…-5, Magenta +5…+15, Red 0…+10, Blue 0…+10 | Magenta and red carry skin |
| HSL Lum | Orange +5…+15 | Face brightness |
| Color Grading | Shadow 200-225 / 5-15, Highlight 200-225 / 5-15, Blend 70-80 | Cool at *both* ends is the signature |
| Grain | 10-25 / size 15-25 / rough 30-50 | Tight sensor noise; keep Clarity/Texture at 0 |
| Vignette | -30 to -10 | Lens plus flash falloff |

## Common Mistakes

- **Treating 5100 K as "cool".** It is near-neutral daylight; the coolness comes from grading both ends at ~210°. Setting Temperature 4200 instead produces a blue photograph, not a digicam photograph.
- **Adding Calibration.** RedHue/RedSaturation shifts are the nuclear option and the repo allows them only in `Y2K Flash Digicam`. Here they turn skin plastic.
- **Recovering the highlights.** Pulling Highlights negative produces a modern HDR file. Early CCDs clipped; a little clipping is the evidence.
- **Heavy grain.** Size 40+ reads as pushed 35mm. Keep size near 20 and roughness under 50.
- **Crushing blacks to "add contrast".** The era's shadows are noisy and open. Crushing them removes the texture that identifies the sensor.
- **Applying it to a night flash frame.** That is the other preset; this one has no falloff model and will simply look blue and flat.

## See Also

- [Y2K Digicam characteristics](characteristics.md)
- [Y2K Flash Digicam](../Y2K-Flash-Digicam/community-recipes.md) — night, direct flash, calibration exception
- [Indie Sleaze](../Indie%20Sleaze/community-recipes.md) — later, warmer party flash
- [Decade presets](../../docs/decade.md)
