# Lightroom Presets — 445 Free XMP Presets

The most comprehensive open-source film emulation and creative preset library on GitHub. Free and open-source alternative to VSCO, Mastin Labs, and RNI Films. All presets are modern (ProcessVersion 15.4), STYLEGUIDE-compliant, and ready for Lightroom Classic & CC.

**[Download all 445 presets](https://github.com/peva3/Lightroom-Presets/releases)** (flat ZIP) · [Changelog](CHANGELOG.md) · [Release v3.1.0](https://github.com/peva3/Lightroom-Presets/releases/tag/v3.1.0)

## Featured Film Stocks

**Kodak:** Portra 160 · 400 · 800, Gold 200, Ektar 100, Ultramax 400, Tri-X 400, T-Max 100 · 400 · 3200, Ektachrome E100 · 64 · 200 · 400X, Kodachrome 64 · 25 · 200, Vision3 250D · 500T · 50D, ColorPlus 200, Plus-X 125, Panatomic-X 32, Technical Pan, Verichrome Pan, Recording Film 2475

**Fuji:** Superia X-TRA 400 · 800 · 1600, Pro 400H · 160NS · 160C · 800Z, Velvia 50 · 100, Provia 100F · 400F · 400X, Astia 100F, Acros, Classic Chrome, Classic Negative, Neopan 400 · 1600, Natura 1600, Reala 100, Fortia SP 50, Eterna, Nostalgic Negative

**Ilford:** HP5 Plus, Delta 3200 · 400 · 100, Pan F Plus 50, FP4 Plus 125, XP2 Super, Ortho Plus 80, SFX 200

**Cinestill:** 800T · 50D · 400D · Pushed 800T

**Creative Styles:** VHS Synthwave · Cyberpunk Neon · Bleach Bypass · Cross-Process · Teal & Orange · Wes Anderson Pastel · Wong Kar-Wai 80s HK · Polaroid SX-70 · Super 8 Home Movie · Matte Fade · Cinematic Dream · Disposable Camera · Aerochrome · Lomography Purple/Metropolis · Film Soup · Classic Cuban Negative · Moody Cinematic Film · High-Key Coastal Pastel · Cinematic Dream Tuned · Medina Teal & Orange · Portugal Nostalgic

**Alternative Processes:** Cyanotype · Wet Plate Tintype/Ambrotype · Daguerreotype · Platinum/Palladium · Autochrome · Salt Print · Van Dyke Brown · Gum Bichromate · Solarization · Holga/Diana/Pinhole · Redscale · Lith Print · Bromoil · Calotype · Film Soup

**Genre:** Wedding · Newborn · Real Estate · Food · Product · Fashion · Sports · Concert · Astro · Underwater · Aerial · Wildlife · Street

**+250 more** — 445 presets total across 13 categories. [Browse all categories →](docs/index.md)

## Categories

| # | Category | Presets | Page |
|---|---|---|---|
| 1 | Color Negative Film | 83 | [color-negative.md](docs/color-negative.md) |
| 2 | Black & White Film | 58 | [black-white.md](docs/black-white.md) |
| 3 | Slide / E-6 Film | 20 | [slide.md](docs/slide.md) |
| 4 | Creative / Cinematic | 47 | [creative.md](docs/creative.md) |
| 5 | Alternative Processes | 25 | [alternative-process.md](docs/alternative-process.md) |
| 6 | Utility & Tools | 40 | [utility.md](docs/utility.md) |
| 7 | Genre-Specific | 32 | [genre.md](docs/genre.md) |
| 8 | Seasonal & Holiday | 20 | [seasonal.md](docs/seasonal.md) |
| 9 | Historical Decade | 25 | [decade.md](docs/decade.md) |
| 10 | Geographic & Cultural | 32 | [geographic.md](docs/geographic.md) |
| 11 | Mobile & Social Media | 23 | [mobile.md](docs/mobile.md) |
| 12 | Photographer Styles | 20 | [photographer.md](docs/photographer.md) |
| 13 | Video LUT Reference | 20 | [video.md](docs/video.md) |
| **Total** | | **445** | [All categories →](docs/index.md) |

## Why Free and Open Source?

VSCO, Mastin Labs, and RNI Films sell preset packs for $50–$150+. This project provides a larger, free, open-source alternative — 445 XMP presets with modern ProcessVersion 15.4, researched from community recipes (Reddit, YouTube, forums, Fuji X Weekly), and validated against real film characteristics. No proprietary formats, no paywalls, just `.xmp` files you can inspect, modify, and share.

## How to Install (Lightroom Classic & CC)

1. Download the `.xmp` files from the `Presets/` folder in this repo — organized into subfolders by category.
2. Copy the `.xmp` files into your Lightroom Develop Presets folder:
   - **macOS:** `~/Library/Application Support/Adobe/Lightroom/Develop Presets/`
   - **Windows:** `%APPDATA%\Adobe\Lightroom\Develop Presets\`
3. Restart Lightroom. Presets will appear grouped by folder name.

## Tips for Best Results

- **White Balance is key.** Many film presets assume a specific temperature. If colors feel off, adjust WB first — Portra presets expect warmth, Cinestill expects cool/tungsten.
- **Exposure varies.** Apply the preset, then tweak the Exposure slider. These are starting points calibrated for well-exposed RAW files.
- **Grain scales with resolution.** Grain settings were tuned for 24MP images. Reduce Grain Amount for lower-res shots.
- **Stack 'em.** Try applying a film preset for color, then adding a creative preset (like Matte Fade or Cinematic Dream) as a second pass.

## Technical Architecture

All presets follow the [STYLEGUIDE.md](STYLEGUIDE.md). Key rules:
- ProcessVersion 15.4, proper Camera Profile Look blocks, neutral ToneCurvePV2012
- No Calibration panel (except Canon Color Science)
- No Temperature/Tint unless defining (Ultramax warm cast, Super 8, etc.)
- Grain presets: Sharpness ≤ 10, Clarity/Texture/Dehaze = 0
- HSL saturation capped at ±60
- |Vibrance − Saturation| ≤ 5

See the [AGENTS.md](AGENTS.md) for the full research methodology and [CONTRIBUTING.md](CONTRIBUTING.md) to contribute.

## License

MIT — [LICENSE](LICENSE)
