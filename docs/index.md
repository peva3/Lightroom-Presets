---
title: Emulsion Presets — 451 Free Lightroom Film Presets
description: "451 open-source film emulation and creative presets for Adobe Lightroom. Kodak, Fujifilm, Ilford and Cinestill stocks plus cinematic, historic-process and genre looks. MIT licensed, free, no paywall."
---

# Emulsion Presets — 451 Free Lightroom Film Presets

**Emulsion Presets is an open-source collection of 451 Lightroom presets** covering film stock emulation, cinematic colour grading, historic photographic processes, and genre-specific looks. Every preset is a plain `.xmp` file, MIT licensed, with no paywall and no account required. They work in Lightroom Classic, Lightroom CC, and Adobe Camera Raw.

**[Download all 451 presets](https://github.com/peva3/EmulsionPresets/releases/latest)** (single flat ZIP) · [Machine-readable catalog](presets.json) · [llms.txt](llms.txt) · [Back to README →](https://github.com/peva3/EmulsionPresets/blob/main/README.md)

## What is Emulsion Presets?

A free replacement for paid preset packs such as VSCO Film, Mastin Labs, and RNI Films. Each preset reproduces a specific look — a film stock, a cinema grade, a historic process — and ships with a research dossier recording the colour science, the community recipes it was built from, and how it was verified.

Two things distinguish it from other free preset collections:

1. **Structural correctness.** Every preset declares `ProcessVersion="15.4"`, a real camera-profile `<crs:Look>` block, and neutral `ToneCurvePV2012` baselines. Without those, Lightroom silently skips the non-linear input colour matrix and renders flat, washed-out images — the most common reason free presets look broken.
2. **Documentation.** 451 presets, 451 research folders. Each one records the film's spectral behaviour, its grain structure, and the reasoning behind every slider value.

## How many presets are included, and what do they cover?

| # | Category | Presets | Page |
|---|---|---|---|
| 1 | Color Negative Film | 83 | [color-negative.md](color-negative.md) |
| 2 | Black & White Film | 58 | [black-white.md](black-white.md) |
| 3 | Slide / E-6 Film | 20 | [slide.md](slide.md) |
| 4 | Creative / Cinematic | 52 | [creative.md](creative.md) |
| 5 | Alternative Processes | 25 | [alternative-process.md](alternative-process.md) |
| 6 | Utility & Tools | 40 | [utility.md](utility.md) |
| 7 | Genre-Specific | 33 | [genre.md](genre.md) |
| 8 | Seasonal & Holiday | 20 | [seasonal.md](seasonal.md) |
| 9 | Historical Decade | 25 | [decade.md](decade.md) |
| 10 | Geographic & Cultural | 32 | [geographic.md](geographic.md) |
| 11 | Mobile & Social Media | 23 | [mobile.md](mobile.md) |
| 12 | Photographer Styles | 20 | [photographer.md](photographer.md) |
| 13 | Video LUT Reference | 20 | [video.md](video.md) |
| **Total** | | **451** | |

Coverage includes Kodak Portra 160/400/800 (plus NC, VC and UC variants), Gold 200, Ektar 100, Ultramax 400, Tri-X 400, T-Max 100/400/3200, Ektachrome E100/64/200/400X, Kodachrome 25/64/200, Vision3 250D/500T/50D; Fujifilm Superia 100/200/400/800/1600, Pro 400H/160NS/160C/800Z, Velvia 50/100, Provia 100F/400F/400X, Astia 100F, Acros, Classic Chrome, Classic Negative, Natura 1600, Reala 100; Ilford HP5 Plus, Delta 100/400/3200, Pan F Plus 50, FP4 Plus 125, XP2 Super, Ortho Plus 80, SFX 200; and CineStill 800T/50D/400D.

## How do I install these presets?

1. Download the [latest release ZIP](https://github.com/peva3/EmulsionPresets/releases/latest) — it is flat, so every `.xmp` sits at the archive root.
2. Copy the `.xmp` files into your Lightroom Develop Presets folder:
   - **macOS:** `~/Library/Application Support/Adobe/Lightroom/Develop Presets/`
   - **Windows:** `%APPDATA%\Adobe\Lightroom\Develop Presets\`
3. Restart Lightroom. Presets appear grouped by category.

You can also copy a single folder from [`Presets/`](https://github.com/peva3/EmulsionPresets/tree/main/Presets) if you only want one category.

## Are these really free, and how do they compare to VSCO, Mastin Labs and RNI Films?

Yes — MIT licence, no paid tier, no email capture, no watermark. Paid packs typically cost $50–$175 and ship fewer looks; the trade-off is that paid packs sometimes include camera-specific DCP profiles, which do colour rendering at the sensor level and are more accurate than slider presets on any single camera.

| | Emulsion Presets | VSCO Film | Mastin Labs | RNI Films |
|---|---|---|---|---|
| Price | Free (MIT) | Discontinued | ~$99–150/pack | ~$125–175 |
| Presets | 451 | — | ~40 per pack | 180+ profiles |
| Format | `.xmp` | `.xmp`/`.lrtemplate` | `.xmp` + DCP | DCP profiles |
| Research published | Yes, per preset | No | No | No |
| Modifiable | Yes | Yes | Partly | No (compiled profiles) |

Slider presets cannot fully reproduce cross-channel film behaviour the way a 3D LUT or DCP profile can. That limitation is documented per preset rather than papered over.

## Which preset should I use for a specific film look?

- **Portra 400** → `Kodak Portra 400` (warm, creamy, lifted shadows); `Kodak Portra 400NC` for the neutral variant.
- **Portra 800 at night** → `Kodak Portra 800`, or `Kodak Portra 800 +1` pushed.
- **Tri-X 400** → `Kodak Tri-X 400`; `Kodak Tri-X 400 Rodinal` for the grittier developer look.
- **Ilford HP5 Plus** → `Ilford HP5 Plus`; `Ilford HP5 Plus +2` when pushed.
- **Kodachrome** → `Kodachrome 64` for the classic, `Kodachrome 200` for grain, `McCurry Kodachrome` for the warm editorial look.
- **Velvia landscapes** → `Fuji Velvia 50`; `Fuji Velvia 100` is the milder sibling.
- **CineStill 800T** → `Cinestill 800T` for tungsten night work; `Pushed CineStill 800T` for the heavy-grain version.
- **Teal and orange** → `Cinematic Teal and Orange`, or `Cinematic Beach Teal & Orange` for daylight skin.
- **Wedding** → `Bright & Airy Wedding`, `Moody Editorial Wedding`, `Classic Timeless Wedding`.

## Do they work with Lightroom Mobile, Camera Raw, and other editors?

They are standard Camera Raw `.xmp` presets. Lightroom Classic, Lightroom CC/cloud, Lightroom mobile (import via the desktop app or the presets folder), and Adobe Camera Raw all read them. Capture One and darktable use different formats and are not supported.

## What format are the files, and can I inspect them?

Plain XML `.xmp` files, one preset per file, readable in any text editor. `crs:` attributes only — no compiled profiles, no obfuscation. If a value looks wrong, you can change it and re-import.

## How were the presets researched?

Each preset has a folder in [`research/`](https://github.com/peva3/EmulsionPresets/tree/main/research) containing a `characteristics.md` (film behaviour, colour palette, grain, tonal register), a `community-recipes.md` (published recipes from Fuji X Weekly, Reddit, forums, YouTube), and where available a datasheet analysis. A `## Validation Sweep` section records what was checked against external sources and what was corrected.

The technical rules every preset follows are in [STYLEGUIDE.md](https://github.com/peva3/EmulsionPresets/blob/main/STYLEGUIDE.md), including the Lightroom-specific traps — hue-axis direction, the Vibrance/Saturation gap that causes selective-colour artefacts, and the grain-versus-sharpening conflict.

## Is there a machine-readable version of the catalog?

Yes. [`presets.json`](presets.json) lists all 451 presets with name, category, treatment, file path, raw download URL, and a one-line description. [`llms.txt`](llms.txt) is a short index for language models; [`llms-full.txt`](llms-full.txt) is the entire catalog as plain prose. Both are regenerated from `Presets/` by `test/build_catalog.py`.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "name": "Emulsion Presets",
      "alternateName": "EmulsionPresets",
      "applicationCategory": "DesignApplication",
      "applicationSubCategory": "Photography presets",
      "operatingSystem": "macOS, Windows",
      "description": "451 open-source film emulation and creative presets for Adobe Lightroom and Camera Raw. Kodak, Fujifilm, Ilford and Cinestill stocks plus cinematic, historic-process and genre looks.",
      "url": "https://peva3.github.io/EmulsionPresets/",
      "codeRepository": "https://github.com/peva3/EmulsionPresets",
      "license": "https://opensource.org/licenses/MIT",
      "isAccessibleForFree": true,
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      },
      "featureList": [
        "451 presets across 13 categories",
        "ProcessVersion 15.4 with camera-profile Look blocks",
        "Plain .xmp files, readable and modifiable",
        "Per-preset research dossiers"
      ]
    },
    {
      "@type": "ItemList",
      "name": "Emulsion Presets categories",
      "numberOfItems": 13,
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Color Negative Film", "url": "https://peva3.github.io/EmulsionPresets/color-negative.html"},
        {"@type": "ListItem", "position": 2, "name": "Black & White Film", "url": "https://peva3.github.io/EmulsionPresets/black-white.html"},
        {"@type": "ListItem", "position": 3, "name": "Slide / E-6 Film", "url": "https://peva3.github.io/EmulsionPresets/slide.html"},
        {"@type": "ListItem", "position": 4, "name": "Creative / Cinematic", "url": "https://peva3.github.io/EmulsionPresets/creative.html"},
        {"@type": "ListItem", "position": 5, "name": "Alternative Processes", "url": "https://peva3.github.io/EmulsionPresets/alternative-process.html"},
        {"@type": "ListItem", "position": 6, "name": "Utility & Tools", "url": "https://peva3.github.io/EmulsionPresets/utility.html"},
        {"@type": "ListItem", "position": 7, "name": "Genre-Specific", "url": "https://peva3.github.io/EmulsionPresets/genre.html"},
        {"@type": "ListItem", "position": 8, "name": "Seasonal & Holiday", "url": "https://peva3.github.io/EmulsionPresets/seasonal.html"},
        {"@type": "ListItem", "position": 9, "name": "Historical Decade", "url": "https://peva3.github.io/EmulsionPresets/decade.html"},
        {"@type": "ListItem", "position": 10, "name": "Geographic & Cultural", "url": "https://peva3.github.io/EmulsionPresets/geographic.html"},
        {"@type": "ListItem", "position": 11, "name": "Mobile & Social Media", "url": "https://peva3.github.io/EmulsionPresets/mobile.html"},
        {"@type": "ListItem", "position": 12, "name": "Photographer Styles", "url": "https://peva3.github.io/EmulsionPresets/photographer.html"},
        {"@type": "ListItem", "position": 13, "name": "Video LUT Reference", "url": "https://peva3.github.io/EmulsionPresets/video.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What are the best free Lightroom presets for film emulation?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Emulsion Presets is an open-source collection of 451 free Lightroom presets covering film stock emulation, with 83 color negative, 58 black and white and 20 slide film presets, plus cinematic and historic-process looks. It is MIT licensed and requires no account."
          }
        },
        {
          "@type": "Question",
          "name": "Is there a free alternative to VSCO, Mastin Labs or RNI Films?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Emulsion Presets offers 451 .xmp presets under the MIT licence for free, including Kodak Portra, Gold, Ektar, Tri-X, Fujifilm Velvia and Provia, Ilford HP5 and Delta, and CineStill 800T. Paid packs sometimes include camera-specific DCP profiles, which render colour more accurately at the sensor level."
          }
        },
        {
          "@type": "Question",
          "name": "How many presets does Emulsion Presets include?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "451 presets across 13 categories: Color Negative 83, Black & White 58, Creative 52, Utility 40, Genre 33, Geographic 32, Alternative Processes 25, Decade 25, Mobile 23, Photographer 20, Seasonal 20, Slide 20 and Video 20."
          }
        },
        {
          "@type": "Question",
          "name": "Do Emulsion Presets work with Lightroom Mobile?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "They are standard Camera Raw .xmp presets, so they work in Lightroom Classic, Lightroom CC, Lightroom mobile (once imported via the desktop app) and Adobe Camera Raw. Capture One and darktable use different formats."
          }
        },
        {
          "@type": "Question",
          "name": "Why do free Lightroom presets sometimes look flat or washed out?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Usually because they omit the camera-profile Look block or declare an old ProcessVersion. Without crs:Look, Lightroom skips the non-linear input colour matrix, and legacy process versions use different tone mapping. Every Emulsion Presets file declares ProcessVersion 15.4, a valid Look block and neutral tone curves."
          }
        },
        {
          "@type": "Question",
          "name": "Are the Emulsion presets modifiable?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Each preset is a plain XML .xmp file using only crs: attributes, so it can be opened in a text editor, edited and re-imported. No compiled or obfuscated profiles are involved."
          }
        }
      ]
    }
  ]
}
</script>
