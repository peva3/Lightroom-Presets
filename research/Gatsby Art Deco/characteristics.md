# Gatsby Art Deco Lightroom Preset — Characteristics

**Category**: Decade

The Gatsby Art Deco Lightroom preset is the jazz-age colour look: warm gold and brass highlights, deep lacquer shadows, muted blue-greens held well back, and a hard, glossy contrast. It is a stylistic reconstruction rather than a film-stock emulation — 1920s colour photography existed, but it was rare, and the preset draws on the period's material palette as much as on any photographic process.

## Historical Context

The look takes its name from the 1925 *Exposition Internationale des Arts Décoratifs et Industriels Modernes*, the Paris fair that named Art Deco, and from Fitzgerald's *The Great Gatsby*, published the same year. Deco's vocabulary — geometry, stepped forms, lacquer, chrome, brass, ebony, ivory, jewel tones against black — describes interiors, posters and cinema foyers, and it is that palette which most period-styled photographs actually quote. Hollywood moved from orthochromatic to panchromatic stock through the late 1920s, and colour remained a special attraction.

## Photographic Technology

- **Monochrome**: orthochromatic film, sensitive to blue and blind to red, rendered red lips and dark fabrics almost black and skin pale — hence the heavy pancake makeup of the silent era. Panchromatic stock, which saw red properly, spread through the late 1920s and 1930s and changed how faces were lit and made up.
- **Colour, still**: the Autochrome plate (Lumière, 1907) was the only widely used colour process of the era. It is an additive screen process — microscopic dyed potato-starch grains, roughly four million to the square inch — with exposure times around thirty times longer than monochrome. The result is soft, warm and slightly pointillist, with muted rather than saturated colour.
- **Lighting**: carbon-arc and incandescent studio lamps with large reflectors, hard key light, and high-gloss sets that produce specular highlights on brass, glass and lacquer.
- **Print**: glossy gelatin silver for the monochrome work; the "gold" of the era is as often the subject's brass and lamplight as it is a toning choice.

## Visual Signature

- **Palette**: a warm gold axis with cool support. HSL pushes orange saturation +15 and luminance +10, yellow +12, while green is cut −20 and blue −15 — the Deco contrast of gilt against black lacquer, with emerald and sapphire present but desaturated. Highlights are graded `40° / 15`, shadows `30° / 12`.
- **Contrast**: hard and glossy. `Contrast +30` with `Highlights -50` and `Blacks -15` holds specular highlights on metal and glass while keeping the blacks dense; `Shadows +15` and `Whites +5` keep the image from going flat.
- **Texture**: visible, structured grain (`35 / 30 / 60`) and no added Clarity or Texture — the gloss comes from the tonal structure, not from micro-contrast.
- **Tonal distribution**: bimodal. Bright gold highlights and near-black grounds, with midtones compressed between them.

## Tonal Register

**Register**: warm-golden

The register is unambiguously warm-gold, and the preset is built for it: it adds orange and yellow saturation rather than muting, so a cool or overcast original will simply refuse to turn gold and instead go mustard. There is no global `Saturation` cut and no `Temperature` shift, so the starting white balance is left intact and the warm cast is produced entirely by HSL and the grading wheels — which makes it the most source-dependent preset in the Decade set. Validate on a warm, high-key or tungsten-lit frame.

## Lighting & Subject Matter

Hard key light with sharp falloff, practical lamps in frame, mirrors, chrome, champagne glass, beaded dresses, tuxedos, motor cars, ballrooms and rooftop parties. Poses are theatrical and frontal; the photograph is a performance of wealth rather than a document of it.

## Lightroom Translation

- **Basic**: `Exposure2012 -0.10`, `Contrast2012 +30`; `Highlights2012 -50` for specular control; `Shadows2012 +15`; `Whites2012 +5`; `Blacks2012 -15`.
- **Colour**: no global `Saturation` and no `Vibrance` — the only Decade preset in this group with a clean 0/0 pair, so the ±5 rule is trivially satisfied. HSL does the work: `Orange +15` / `Yellow +12` saturation with `LuminanceAdjustmentOrange +10`, against `Green -20` and `Blue -15`.
- **Color Grading**: highlights `40° / 15`, shadows `30° / 12`, `Blending 75` — a slightly harder blend than the sepia presets, so the gold does not bleed into the blacks.
- **Effects**: `GrainAmount 35 / GrainSize 30 / GrainRoughness 60`; `PostCropVignetteAmount -20`.
- **Detail**: `Sharpness 10`, `LuminanceSmoothing 0`; `Clarity`, `Texture`, `Dehaze` unset.
- **Tone Curve**: neutral on all four channels.

## Verification

Pass; no changes.

- **Colour, not monochrome**: unlike the sepia presets, this one keeps colour and lifts orange/yellow — consistent with an Art Deco material palette and with Autochrome's warm, muted rendering.
- **Contrast structure**: `+30` contrast with `Highlights -50` is the correct glossy structure; `Blacks -15` stays well inside the −30 portability floor.
- **Grain protection**: `Grain 35` with `Sharpness 10`, `LuminanceSmoothing 0`, and Clarity/Texture/Dehaze at 0 is fully compliant with STYLEGUIDE §VIII.2.
- **Register caveat**: this is a *look*, not an emulation. 1920s colour still photography means Autochrome, which is softer, cooler in the blues and visibly grainy; the preset's hard contrast and clean gold are closer to a modern period drama. Labelled accordingly rather than claiming film accuracy (STYLEGUIDE §XII.E).
- **No Temperature**: correctly omitted — warmth is produced by HSL and grading, so the preset survives a range of source white balances. Top HSL gain is `+15`, far from the ±60 cap.
- **Vibrance/Saturation**: both effectively 0, so the ±5 rule is trivially satisfied — the only preset in this group with a clean pair.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** `Contrast +30` with no Clarity/Texture push; warm `30–40°`; `Grain 35`; `Vignette -20`; muted blues (−15).
- **Preset adjustments:** none.

## Sources

- [Art Deco — Wikipedia](https://en.wikipedia.org/wiki/Art_Deco) — the 1925 Paris exposition, the movement's materials and its gold/black/jewel palette.
- [Autochrome Lumière — Wikipedia](https://en.wikipedia.org/wiki/Autochrome_Lumi%C3%A8re) — the additive starch-screen process that supplied the era's colour.
- [History of the autochrome — Science Museum Group](https://blog.scienceandmediamuseum.org.uk/autochromes-the-dawn-of-colour-photography/) — four million dyed starch grains per square inch, exposure roughly thirty times that of monochrome plates, and the resulting muted colour.
- [Early (Silent) Movie Make-up — Cosmetics and Skin](https://www.cosmeticsandskin.com/cdc/early-movie.php) — orthochromatic film's spectral response and why period faces were painted pale with dark lips.
- [Orthochromatic vs Panchromatic Film — The Darkroom](https://thedarkroom.com/orthochromatic-vs-panchromatic-film-a-photo-comparison/) — reds rendering dark under ortho stock, and the practical difference panchromatic made.

## See Also

- [Decade presets](../../docs/decade.md)
- [Autochrome (alternative process)](../alt-autochrome/) — the era's actual colour medium, softer and cooler than this preset.
- [Hollywood Glamour](../Hollywood%20Glamour/) — the same decade in monochrome, lit rather than gilded.
- [Prohibition Sepia](../Prohibition%20Sepia/) — the period's print look, for when the scene is a bar rather than a ballroom.
