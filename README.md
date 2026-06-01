# Lightroom Presets — 419 Free XMP Presets

The most comprehensive open-source film emulation and creative preset library on GitHub. All presets are free, modern (ProcessVersion 15.4), and STYLEGUIDE-compliant.

## Categories

| # | Category | Presets | Page |
|---|---|---|---|
| 1 | Color Negative Film | 78 | [docs/color-negative.md](docs/color-negative.md) |
| 2 | Black & White Film | 46 | [docs/black-white.md](docs/black-white.md) |
| 3 | Slide / E-6 Film | 16 | [docs/slide.md](docs/slide.md) |
| 4 | Creative / Cinematic | 42 | [docs/creative.md](docs/creative.md) |
| 5 | Alternative Processes | 25 | [docs/alternative-process.md](docs/alternative-process.md) |
| 6 | Utility & Tools | 40 | [docs/utility.md](docs/utility.md) |
| 7 | Genre-Specific | 32 | [docs/genre.md](docs/genre.md) |
| 8 | Seasonal & Holiday | 20 | [docs/seasonal.md](docs/seasonal.md) |
| 9 | Historical Decade | 25 | [docs/decade.md](docs/decade.md) |
| 10 | Geographic & Cultural | 32 | [docs/geographic.md](docs/geographic.md) |
| 11 | Mobile & Social Media | 23 | [docs/mobile.md](docs/mobile.md) |
| 12 | Photographer Styles | 20 | [docs/photographer.md](docs/photographer.md) |
| 13 | Video LUT Reference | 20 | [docs/video.md](docs/video.md) |
| **Total** | | **419** | [docs/index.md](docs/index.md) |

## Installation

1. Download the `.xmp` files from the `Presets/` folder in this repo — organized into subfolders by category.
2. Copy the `.xmp` files into your Lightroom Develop Presets folder:
   - **macOS:** `~/Library/Application Support/Adobe/Lightroom/Develop Presets/`
   - **Windows:** `%APPDATA%\Adobe\Lightroom\Develop Presets\`
3. Restart Lightroom. Presets will appear grouped by folder name.

## Usage Tips

- **White Balance is key.** Many film presets assume a specific temperature. If colors feel off, adjust WB first — Portra presets expect warmth, Cinestill expects cool/tungsten.
- **Exposure varies.** Apply the preset, then tweak the Exposure slider. These are starting points calibrated for well-exposed RAW files.
- **Grain scales with resolution.** Grain settings were tuned for 24MP images. Reduce Grain Amount for lower-res shots.
- **Stack 'em.** Try applying a film preset for color, then adding a creative preset (like Matte Fade or Cinematic Dream) as a second pass.
- **Process Version.** All presets use Process Version 15.4 (Camera Raw 6). Older versions may render differently.

## Architecture

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
