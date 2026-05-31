# Ricoh High-Contrast Monochrome — Datasheet

## Product Overview

The **High-Contrast Black & White** (Hi-Contrast B&W, HC B&W) is an in-camera JPEG Image Control (previously "Effect Mode") found in the Ricoh GR series of compact APS-C cameras. It is one of the most celebrated camera JPEG profiles in photography, with a cult following among street photographers.

## Generational Breakdown

### GR (Original, 2013) — GR ENGINE V
- **Effect Mode**: "High Contrast B&W" (ハイコントラスト白黒)
- Listed alongside: Bleach Bypass, Retro, High-Key, Miniaturize
- Available in Effect Bracketing (auto-brackets Standard / High Contrast B&W / Bleach Bypass)
- In-camera RAW development supported — can apply effects to RAW after shooting
- JPEG-only; no Adobe Camera Matching profile shipped by Ricoh

### GR II (2015) — GR ENGINE V
- Image Control introduced as unified system combining effect modes and image settings
- **B&W Modes**: BW, BW Hard, BW Hi-Contrast (BW-MAX), BW Soft, Monochrome
- **BW Hi-Contrast MAX** (BW-MAX): highest contrast B&W setting in the GR II
- Lacks the fine-grained highlight/shadow split controls of GR III

### GR III / GR IIIx (2019/2021) — GR ENGINE 6
- **Image Control modes**: 12 base modes including:
  - Monotone
  - Soft Monotone
  - Hard Monotone
  - **Hi-Contrast B&W** (listed as "Hi-Contrast B&H" on some JP pages — translation artifact)
- Adjustable parameters (varies by mode):
  - Saturation, Hue, High/Low Key
  - Contrast, Contrast (Highlight), Contrast (Shadow)
  - Sharpness, Shading, Clarity
  - Toning, Filter Effect, Grain Effect
  - HDR Tone Level, Color Tone (firmware update)
- Highlight Correction, Shadow Correction
- Peripheral Illumination Correction
- High-ISO Noise Reduction
- **Key difference from GR II**: GR III's HC B&W has independent highlight/shadow contrast sliders, allowing the user to crush shadows while preserving highlight detail (or vice versa). GR II's implementation was a single global contrast value.

### GR IV Monochrome (2025, development announced)
- Dedicated monochrome-only camera
- Monochrome-specific sensor (no color filter array)
- Significantly more B&W image control options
- Represents Ricoh's full commitment to the monochrome JPEG aesthetic

## Official Ricoh Documentation

### Source: Ricoh Imaging (ricoh-imaging.co.jp/english)

From the GR III/IIIx Expressive Power feature page:

> **Image Control for pure image creation enjoyment**
>
> Featuring a creative Image Control function, which integrates effect modes into conventional image setting operations. Using 12 basic Image Control modes, the user can easily adjust various parameters to create photos the way you like. The parameter includes the saturation, hue, high/low key adjustment, contrast, contrast (highlight and shadow), sharpness, shading, clarity, toning, filter effect, grain effect, HDR tone level and color tone.

From the original GR (2013) features page:

> Effect mode offers various ways to expand shooting expression. In addition to the positive reputations of Positive Film Tone and Bleach Bypass, Retro, High-Key, and Miniaturize have been added. Detailed settings are possible, expanding the possibilities of photographic expression even further. These effects can also be applied during in-camera RAW processing.

### Key Facts About the Profile

1. **It is a JPEG engine profile** — not a physical sensor characteristic. The RAW file is a standard Bayer-pattern RAW without the effect applied.

2. **Ricoh provides NO Adobe Camera Matching profiles** — unlike Fujifilm (which has official LR profiles for their film simulations), Ricoh has never shipped `.dcp` profiles for Lightroom/Camera Raw. This is a major pain point for GR users who want to process RAW files with the HC B&W look.

3. **The effect CAN be applied during in-camera RAW development** — you can shoot RAW, then develop to JPEG in-camera with the HC B&W profile applied. This is the only official "RAW conversion" method Ricoh provides.

4. **Cross-generation incompatibility** — the HC B&W look differs noticeably between GR II and GR III. GR II's "Hi-Contrast BW-MAX" has its own cult following and is considered subtly different from GR III's implementation.

5. **GR IV Monochrome** represents the pinnacle — a dedicated monochrome sensor with dedicated image processing eliminates the need for color-to-B&W conversion entirely.

## Technical Architecture (HOW IT WORKS)

The HC B&W profile operates as part of the GR ENGINE pipeline:

```
RAW Sensor Data → GR ENGINE → Image Control Processing → JPEG
```

The Image Control processing layer applies:
1. **Color desaturation** (full B&W conversion — GR III's HC B&W has unique channel mixing; the GR II version leans toward red/green sensitivity similar to traditional panchromatic B&W film)
2. **Global contrast curve** — steep S-curve with heavy shadow crush and highlight push
3. **Per-pixel contrast enhancement** (similar to Clarity, but applied at the engine level)
4. **Grain synthesis** — digital noise added with frequency-weighted distribution (GR III allows Grain Effect 1–4)
5. **Peripheral illumination correction** — vignette compensation (can be toggled)
6. **Highlight/Shadow Correction** — dynamic range compression (separate from contrast)
7. **Toning** — optional warm/cool/sepia split-toning (GR III)

### Contrast Curve Characteristics

Based on community analysis (comparing SOOC JPEGs to RAWs):
- **Shadow region**: Approximately -3 to -4 stops underexposed vs. linear RAW. Near-pure black from roughly 15% luminance downward.
- **Midtones**: Rapid transition zone; midtones span only ~2 stops (vs. ~4 stops on Standard profile).
- **Highlights**: +1 to +2 stops pushed. Highlight rolloff is abrupt — the profile intentionally clips highlights rather than using a smooth shoulder. This is the "blooming" character.
- The curve resembles a pushed +2 stop development equivalent in film terms.

### Grain Characteristics

- GR III's "Grain Effect" parameter (1–4, or Off) adds synthetic luminance noise
- More prominent in shadow and midtone regions
- Has a frequency distribution designed to mimic pushed 35mm film grain
- Differs from Lightroom's grain generator — Ricoh's implementation applies grain before the contrast curve, meaning grain is amplified by the contrast processing
- At ISO 3200+, the sensor's natural noise compounds with the synthetic grain for an even grittier look

## Relationship to Daido Moriyama

Ricoh has a deep historical connection to Daido Moriyama:
- Moriyama famously used Ricoh GR film cameras (GR1, GR1s, GR1v, GR21) for his street work
- The original GR1 (1996) was Moriyama's primary camera for years
- Ricoh explicitly designed the digital GR series to carry forward the GR film camera's street photography DNA
- The High-Contrast B&W profile is Ricoh's digital homage to the "are, bure, boke" (rough/grainy, blurry, out-of-focus) aesthetic that Moriyama pioneered with the Provoke movement
- PerfeFilm's documentation notes: "Since Moriyama Daido used the Ricoh GR 28mm classic film camera series to take high-contrast B&W photos, Ricoh GR has been equated in terms of fast and convenient, intuitive shooting, and street photography."
- Moriyama now shoots digital (compact digital cameras), embracing the HC B&W workflows

## Sources
- Ricoh Imaging official product pages (ricoh-imaging.co.jp/english/products/gr/feature/, gr-3/feature/03.html)
- Ricoh GR official blog (grblog.jp/en/)
- PerfeFilm — Ricoh GR color profile documentation (perfefilm.com)
- Ritchie's Ricoh Recipes (ricohrecipes.com)
- GR Recipe community site (grrecipe.com)
