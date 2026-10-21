# Edwardian Pictorialist Lightroom Preset — Characteristics

**Category**: Decade

The Edwardian Pictorialist Lightroom preset renders the soft-focus platinum print of the Photo-Secession years: a long, luminous grey scale with no true black, highlights that roll off instead of clipping, and a diffuse surface. It is the quietest preset in the Decade set — the effect comes from removing contrast and detail, not from adding anything.

## Historical Context

Pictorialism dominated artistic photography from the late 1880s to roughly the First World War. Stieglitz founded the Photo-Secession in 1902 and launched *Camera Work* in 1903, whose hand-pulled photogravures carried the movement's prints to subscribers; Steichen, Clarence H. White, Käsebier, Coburn and Frederick H. Evans were among its members. The movement argued that photography was a fine art and that the manipulated print — softly focused, toned, often matte — was the artist's object. Its subject was mood: mist, dusk, rain, backlit trees, allegorical figures, children in half-light.

## Photographic Technology

- **Negative**: large-format plates, often 8×10, contact printed — so no enlargement grain anywhere in the chain.
- **Print**: platinum and platinum/palladium above all, plus gum bichromate, photogravure and bromoil. Platinum is the tonal key: the metal sits in the paper fibres rather than in gelatin, giving a matte surface, a very long straight-line range, and — critically — **blacks lighter than a silver print's**. Tones run from neutral black through warm black and reddish brown to blue-black.
- **Commerce**: platinum cost roughly fifty times silver by 1907 and commercial platinum paper stopped around 1916; later pictorialism is usually palladium or silver, slightly cooler and denser.
- **Optics**: soft-focus lenses and diffusion screens, or deliberate defocus. The image is veiled rather than simply out of focus: edges bleed, specular highlights bloom.

## Visual Signature

- **Palette**: near-neutral with a warm bias — `Saturation -10` only, then highlights `38° / 8` and shadows `32° / 10` at `Blending 80`. Green and blue saturation drop to −30 so foliage and sky recede; orange and yellow gain +5 so skin and lamplight stay alive.
- **Contrast**: low, never crushed. `Contrast -15`, `Highlights -40`, `Shadows +25` and `Blacks +5` — the positive blacks value is the signature: a platinum print has no true black, and the deepest tone sits visibly above the paper's maximum density.
- **Texture**: matte and grain-free in the image; paper tooth and any gum marks are the only texture. `GrainAmount 0` is correct, not an omission.
- **Tonal distribution**: high-key leaning and long, most of the image in the upper midtones with a slow shoulder.

## Tonal Register

**Register**: neutral (soft, high-key-leaning)

Deliberately neutral rather than sepia: platinum's own tones run from warm black to blue-black and printers varied them print by print, so a fixed brown would over-claim. Because the preset removes contrast rather than adding it, it is stable across warm and cool originals and reads best on soft, backlit or overcast frames. On a hard, saturated original the negative Clarity looks like a smeared filter rather than a print.

## Lighting & Subject Matter

Overcast and north light, backlight through trees, mist over water, rain on glass, single-window interiors. Subject matter is atmospheric and often allegorical: bathers, gardens, cathedral interiors, streets at dusk, portraits dissolved into background.

## Lightroom Translation

- **Basic**: `Exposure2012 +0.10` (prints were made light), `Contrast2012 -15`, `Highlights2012 -40`, `Shadows2012 +25`, `Blacks2012 +5` — the platinum curve expressed with sliders: long scale, open shadows, no floor.
- **Local contrast**: `Clarity2012 -25` and `Dehaze -10` do the diffusion. This overrides the "grain presets keep Clarity/Dehaze at 0" rule on purpose — soft-focus diffusion *is* the defining trait, and `GrainAmount` is 0, so there is no grain to smear.
- **Colour**: `Saturation -10`, with `Green -30` and `Blue -30` to quiet foliage and sky, `Orange +5` and `Yellow +5` to hold skin. `Temperature 5800` supplies a neutral-warm base.
- **Color Grading**: highlights `38° / 8`, shadows `32° / 10`, `Blending 80` — a whisper of warmth, consistent with warm-black platinum.
- **Effects**: `PostCropVignetteAmount -20`; `GrainAmount 0`. **Detail**: `Sharpness 10`, `LuminanceSmoothing 0`.

## Verification

Pass; no changes.

- **No true black**: `Blacks +5` with `Shadows +25` encodes the platinum characteristic that the darkest tone sits above a silver print's black — the central technical claim of this dossier.
- **Long scale, soft shoulder**: `Highlights -40` with `Contrast -15`; `Exposure +0.10` keeps the print light.
- **Grain-free**: `GrainAmount 0` is correct for a contact print, so the styleguide's grain-protection rule does not constrain Clarity/Dehaze here and their negative values are the look.
- **Vibrance**: absent from the XMP, satisfying the "remove Vibrance entirely" alternative. The 10-point gap against `Saturation -10` is small and on the desaturating side; pushing Saturation lower would kill the last of the platinum warmth, so it is left alone.
- **Flag — Temperature 5800**: absolute WB, a portability risk; retained as the neutral-warm base the grade assumes.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Checked:** `Clarity -25` / `Dehaze -10` for diffusion; `Contrast -15` with `Blacks +5`; warm 32–38°; `GrainAmount 0`; `Vignette -20`.
- **This pass:** no preset change; platinum tonal-range evidence and the Clarity/Dehaze override note added.

## Sources

- [Pictorialism in America — The Metropolitan Museum of Art](https://www.metmuseum.org/essays/pictorialism-in-america) — the movement's rejection of the point-and-shoot and its labour-intensive printing.
- [The Alfred Stieglitz Collection: Pictorialism — Art Institute of Chicago](https://archive.artic.edu/stieglitz/pictorialism/) — Photo-Secession context and *Camera Work*.
- [Platinum print — Wikipedia](https://en.wikipedia.org/wiki/Platinum_print) — matte surface, long range, warm-black to blue-black tones, lighter maximum density, 1916 end of commercial paper.
- [The Photo-Secession Movement — Utah Museum of Fine Arts](https://umfa.utah.edu/the-photo-secession-movement-pioneering-artistry-in-early-photography/) — soft focus, gentle lighting, platinum as the default medium.

## See Also

- [Decade presets](../../docs/decade.md)
- [Platinum Print](../alt-platinum-print/) — the process at full strength.
- [Gum Bichromate](../alt-gum-bichromate/) — the pigment process used alongside platinum.
- [Bromoil](../alt-bromoil/) — the later, brushier pictorial print.
