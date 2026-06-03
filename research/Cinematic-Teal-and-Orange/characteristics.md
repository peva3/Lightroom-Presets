# Characteristics Lightroom Preset — Cinematic Teal & Orange

## Aesthetic Breakdown

The Cinematic Teal and Orange Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. The Teal & Orange look is the defining color palette of the 21st-century blockbuster. It's a high-contrast, complementary-color grade where shadows are pushed into cool teal/cyan territory and highlights into warm amber/orange. The result is a hyper-saturated, visually "sticky" image that maximizes color contrast — and by extension, perceived depth and dimensionality — on screen.

## Split-Tone Mechanics

At its core, this is a **split-tone operation**:

| Zone | Target Hue | Technique |
|---|---|---|
| **Shadows** | Teal (180°–210° hue) | HSL panel: desaturate blues/aquas slightly, then tint shadows toward cyan in Split Toning or Calibration panel. |
| **Midtones** | Preserved or gently warmed | Keep midtone saturation lower to protect skin tones. |
| **Highlights** | Orange-Amber (25°–45° hue) | HSL panel: push yellows toward orange, desaturate competing greens. Split Toning highlights to warm amber. |
| **Blacks** | Faded teal (crushed) | Tone curve: lift blacks slightly, add blue in RGB curves for teal tint. |

### Typical Lightroom Split Toning Recipe
- **Shadows**: Hue ~200°–220°, Saturation 15–35%
- **Highlights**: Hue ~35°–50°, Saturation 10–25%
- **Balance**: Shifted toward shadows (−20 to −40) to keep warmth primarily in highlights

### Calibration Panel (Critical)
The Calibration panel is the secret weapon for Teal/Orange:
- **Red Primary**: Hue shifted toward orange (+15 to +40), Saturation +10 to +25
- **Green Primary**: Hue shifted toward teal (−20 to −60), Saturation +5 to +20
- **Blue Primary**: Hue shifted toward cyan (−10 to −25), Saturation −10 to −30 (reduced to prevent oversaturation)

This panel works at the sensor/primitives level before the HSL panel, giving a more organic, "baked-in" look than split toning alone.

## Skin Tone Line Protection

The **skin tone line** is the central challenge of teal/orange grading. Skin tones live in the orange/red region of the vectorscope (roughly along the "flesh tone line" at ~147° on a vectorscope, or Hue ~15°–35° in Lightroom HSL).

### The Problem
When you push orange globally, skin tones become radioactive — oversaturated, unnatural, "Oompa Loompa" orange. When you push teal into shadows, skin in shadow areas turns sickly cyan.

### Protection Techniques

1. **HSL Luminance Keying**: In Resolve, use a qualifier to isolate skin tones and exclude them from the orange push. In Lightroom, use the **HSL panel** to target orange luminance (+10 to +25) and reduce orange saturation (−5 to −15), then use the **Calibration panel** or **Color Grading** to apply the overall look.

2. **Midtone Isolation**: Skin lives primarily in midtones. By keeping the split-tone balance shifted toward shadows (e.g., −30), you reduce the orange tint bleeding into midtone skin.

3. **Luminance Separation**: Bright skin (highlights on forehead, nose, cheeks) will pick up the orange highlight tint; shadow-side skin will pick up teal. The key is keeping the saturation low enough (10–20%) that this reads as natural ambient color rather than body paint.

4. **The "S" Curve in RGB Channels**: Instead of a global white-balance shift, use individual RGB tone curves:
   - **Red channel**: Lift highlights (warmth)
   - **Blue channel**: Lift shadows (coolness)  
   - **Green channel**: Slight midtone boost to prevent magenta shift

5. **Selective Color Adjustments (Photoshop)**: Pro colorists often grade the background separately from skin. This is why the look works best on scenes with strong depth separation (close-ups against defocused backgrounds).

### Acceptable Skin Hue Range
- Natural caucasian skin: Hue 15°–30°
- Natural darker skin: Hue 10°–25°
- Teal/Orange "acceptable" range: Hue 18°–35° (slightly warmer than natural is acceptable to audiences)
- "Broken" skin: Hue >40° (too orange), Saturation >70% in orange channel

## Kodak 2383 Print Film Connection

The Teal & Orange look didn't emerge from nowhere — it's deeply rooted in the color science of **Kodak Vision 2383 print film**.

### What Is Kodak 2383?
Kodak Vision Color Print Film 2383 is the industry-standard motion picture print film used to strike theatrical release prints from a digital intermediate or film negative. It has a distinctive color response:

- **Cyan-shifted shadows**: The D-min (minimum density) of 2383 has a characteristic cyan/teal cast in the blacks
- **Warm yellow-orange highlights**: The dye set produces warm, golden highlights
- **High contrast**: Designed for projection, 2383 has a steep characteristic curve with deep blacks
- **Slight desaturation**: Print film naturally desaturates compared to the negative, but with rich, "creamy" color

### The Digital Intermediate Pipeline
When films transitioned to Digital Intermediate (DI) workflows in the early 2000s, colorists discovered they could emulate — and then exaggerate — the 2383 look:

1. **Early DI (2000–2005)**: Colorists used LUTs that emulated 2383 color response. The cyan shadows / warm highlights were a byproduct of accurate print emulation.

2. **The Discovery**: Colorists realized that pushing the 2383 emulation further than physically possible created a more "cinematic" look than real film ever did. The teal became more saturated, the orange more vibrant.

3. **The Michael Bay Era**: Films like *Transformers* (2007) and *Bad Boys II* (2003) took this to an extreme, defining the modern blockbuster palette.

### Technical Reference: 2383 Print Density Curves
- **Cyan dye**: Peaks in red absorption (gives cyan appearance)
- **Magenta dye**: Broad green absorption  
- **Yellow dye**: Blue absorption (warmth in highlights)
- **Interimage effects**: The chemical coupling between dye layers in 2383 naturally produces color contrast — adjacent colors push away from each other on the spectrum (i.e., cyan pushes toward orange).

This interimage effect is what gives print film its "3D pop" and is exactly what the teal/orange grade emulates digitally: maximizing perceptual color separation between foreground (orange skin/warmth) and background (cool teal).

### The LUT Legacy
Every major post-production facility has a "2383 LUT" — a 3D LUT that maps digital color to 2383 print response. In fact, the default LUT in many grading workflows is:
- **Input**: LogC / S-Log / REDlog → **Output**: Rec.709 with 2383 emulation

Colorists then grade *under* this LUT (or apply it at the end of the chain), meaning the teal/orange bias is baked into the viewing transform itself.

## The Rivalry: Teal/Orange vs. Bleach Bypass

Before Teal/Orange, the dominant "cinematic" look was **bleach bypass** (skip-bleach):
- Desaturated, harsh, metallic
- Popular in late 90s / early 2000s (Saving Private Ryan, Fight Club, Seven)
- Low color contrast

Teal/Orange is essentially the *inverse* of bleach bypass — maximum color contrast rather than minimum. It emerged as the antidote to the desaturated look and became dominant around 2005–2010.

## Why It Works (Perceptual Theory)

1. **Complementary Contrast**: Teal (~180°) and Orange (~30°) are near-exact complements on the color wheel. Complementary colors create maximum visual contrast and "vibrate" against each other.

2. **Natural Occurrence**: Teal shadows and warm highlights occur in nature — golden hour light against blue shadows, firelight against night sky, skin against sky. The grade exaggerates what our visual system already finds pleasing.

3. **Skin Tone Anchoring**: Human skin, regardless of ethnicity, lives in the orange/red region. By pushing *everything else* toward teal, skin naturally separates from the background without explicit masking.

4. **The "Memory Color" Effect**: Audiences remember skies as blue, fires as orange, and skin as warm. Teal/orange reinforces these memory colors rather than challenging them.

## Criticisms

- **Overuse and homogeneity**: By 2015, nearly every blockbuster had the same grade. Audiences and critics began noticing.
- **Cultural colonialism of color**: Some critics argue the grade imposes a specific (Hollywood) color aesthetic on global cinema.
- **Skin tone stereotyping**: The orange push can flatten skin tone diversity — all skin mapped to the same warm hue range.
- **Todd Miro's viral 2011 blog post**: "Abusing the Teal & Orange Look" became one of the most-shared posts in color grading history, comparing frame after frame of identically-graded blockbusters.
- **r/colorists**: The subreddit regularly sees "teal and orange is overdone" threads, but also acknowledges it as the entry point that got most colorists into grading.

## See Also

- [Creative Presets](../../docs/creative.md)
- [Color Negative Presets](../../docs/color-negative.md)
- [Video Presets](../../docs/video.md)
- [All Lightroom Preset Categories](../../docs/index.md)

