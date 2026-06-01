# Film Grain Simulation: Physical Emulsion Modeling in Dehancer

**Source URL:** https://blog.dehancer.com/how-does-film-grain-work-in-dehancer-ofx-plugin/ + https://www.dehancer.com/help/article/grain
**Authors:** Pavel Kosenko, Dmitry Novak, Nailya Safarova, Denis Svinarchuk
**Date:** February 2020 (Updated February 2023)

**Document Source:** Dehancer Blog and Dehancer Official Documentation

---

## Two Approaches to Grain Simulation

There are two fundamentally different methods for simulating film grain:

1. **Natural grain** — Scans of actual film footage, overlaid on digital images. While "honest" in origin, this grain isn't structurally related to the image, looks superimposed, and has significant limitations in controlling size, texture, and density.

2. **Procedural (computer generated) grain** — Mathematically generated based on physical properties of real emulsion. This is Dehancer's approach.

## The Dehancer Approach: 3D Physical Grain Modeling

After years of film study and darkroom printing/scanning experiments, Dehancer created a **reliable mathematical 3D model** for generating flexibly controlled analogue-like procedural grain.

### Key Physical Properties Modeled

1. **Image consists of grain.** Grain isn't overlaid on the image — the image itself entirely consists of grain. Image detail depends on grain size, and visible details typically do not exceed grain size.

2. **Emulsion has thickness.** Light passing through multiple emulsion layers is reflected, refracted, and diffused in complex ways. The film base is not flat.

3. **Silver halides have volume.** Each granule is rotated differently relative to the film plane and casts shadows.

4. **Grain shape types.** Classic rounded grain and flat "T-grain" varieties are modeled.

5. **Cluster formations.** Silver halides are distributed unevenly in the emulsion depth. Tiny grains form complex conglomerations.

6. **Grain in highlights.** Maximum grain in highlights corresponds to maximum negative density (Dmax) — the heaviest accumulation of silver halides. When printed to positive, these areas carry the most grain texture. Due to human perception, grain appears less noticeable in highlights but cannot be null.

7. **Grain in shadows.** Shadows correspond to minimum exposure (Dmin), the most transparent areas of the negative. During printing, print media gets maximum light in these areas, making the grain of the print media itself visible, along with residual negative grain.

### 3D Particle System

The algorithm generates grain based on **local color and brightness characteristics**, making grain structurally related to the image. Granules are 3D particles in a volumetric space, each rotated relative to the image plane. Granules are randomly shifted and group into clusters. The resulting halide structure is **superimposed over the original image** (not the image over the grain), incorporating light reflection, refraction, and diffusion effects in the emulsion layers.

During printing simulation, initial negative grain becomes positive and is built into the image as an integral part — it does not look overlaid.

## Grain Parameters

### Grain Profiles
Dehancer provides grain profiles for 8mm, 16mm, 35mm, and 65mm formats, each in ISO 50, 250, and 500 variants.

### Custom Settings

**Film Type:**
- **Negative grain** — More pronounced in highlights, slightly higher microcontrast (typical for negative films)
- **Positive grain** — Softer grain, less pronounced in highlights (typical for slide/reversal films)

**Processing Mode:**
- **Analogue** — Full physical simulation, computationally intensive, lifelike result
- **Noise** — High-performance simplified grain for dithering, draft renders, and heavy compression environments (YouTube, social media)

**Size** — Determines silver halide granule dimensions. Higher values correspond to more photosensitive (and more granular) emulsions. Grain size is automatically corrected based on image dimensions.

**Amount** — Total grain density, corresponding to negative optical density.

**Shadows / Midtones / Highlights** — Grain distribution between tonal zones, matching scene texture and grading look.

**Film Resolution** — Set to 100 keeps source sharpness; lowering gradually loses detail (image becomes blurred). At 50, detail balances with current grain size/amount. Since the smallest film detail cannot exceed grain size, it's recommended to always lower Resolution according to grain Size and Amount.

**Chroma** — Grain color contrast (chromaticity), controlling dye density within the selected film's gamut.

## Practical Observations

- At high Amount values, irregularities in grain distribution across emulsion layers and cluster formations become clearly visible.
- Grain in shadows prevents flat blacks — this mimics how real film works without clipping.
- At maximum Size (10) and Amount (100), individual granules give way to grain cluster textures due to natural emulsion irregularities and photochemical processing effects.
- Grain color gamut corresponds to the selected film profile. When grain is applied without a film profile, maximum Chroma corresponds to a hypothetical color film with extra-saturated dyes.

## Performance

Procedural grain eliminates the need for large scan files (tens to hundreds of high-resolution scans needed to avoid repeating patterns in scanned grain approaches). The computational cost is approximately 5% of Dehancer's total plugin performance.

## Key Design Principle

> "Real grain on film isn't just overlaid on top of an image, but in fact the image itself entirely consists of grain. Dehancer literally reconstructs the shot, using the local color and brightness characteristics along with a complex physical modelling of a film emulsion."
