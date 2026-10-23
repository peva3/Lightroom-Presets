# Emulsion Presets — 451 Free Lightroom Film Presets (Open Source)

**Emulsion Presets is a free, open-source library of 451 Lightroom presets** for film emulation and colour grading: Kodak Portra, Gold, Ektar, Tri-X and Kodachrome; Fujifilm Superia, Pro 400H, Velvia, Provia, Acros and Classic Chrome; Ilford HP5, Delta and Pan F; CineStill 800T; plus cinematic looks, historic processes and genre-specific grades.

It is a free alternative to paid packs such as **VSCO Film, Mastin Labs and RNI Films**. Every preset is a plain `.xmp` file under the MIT licence — no paywall, no account, nothing to install beyond copying a folder. They work in Lightroom Classic, Lightroom CC and Adobe Camera Raw.

**[Download all 451 presets →](https://github.com/peva3/EmulsionPresets/releases/latest)** — one flat ZIP, ready to import.

[![Presets](https://img.shields.io/badge/presets-451-blue)](presets.json)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![ProcessVersion](https://img.shields.io/badge/ProcessVersion-15.4-orange)](STYLEGUIDE.md)

- [Machine-readable catalog](presets.json) · [llms.txt](llms.txt) · [Full index](docs/index.md) · [Changelog](CHANGELOG.md)
- [Browse the documentation site →](https://peva3.github.io/EmulsionPresets/)

## What's included?

| # | Category | Presets |
|---|---|---|
| 1 | Color Negative Film | 83 |
| 2 | Black & White Film | 58 |
| 3 | Slide / E-6 Film | 20 |
| 4 | Creative / Cinematic | 52 |
| 5 | Alternative Processes | 25 |
| 6 | Utility & Tools | 40 |
| 7 | Genre-Specific | 33 |
| 8 | Seasonal & Holiday | 20 |
| 9 | Historical Decade | 25 |
| 10 | Geographic & Cultural | 32 |
| 11 | Mobile & Social Media | 23 |
| 12 | Photographer Styles | 20 |
| 13 | Video LUT Reference | 20 |
| | **Total** | **451** |

**Featured film stocks.** Kodak: Portra 160/400/800 (plus NC, VC, UC), Gold 200, Ektar 100, Ultramax 400, ColorPlus 200, Pro Image 100, Tri-X 400, T-Max 100/400/3200, Plus-X 125, Panatomic-X, Technical Pan, Ektachrome E100/64/200/400X, Kodachrome 25/64/200, Vision3 50D/250D/500T.
Fuji: Superia 100/200/400/800/1600, Pro 400H/160NS/160C/800Z, NPS 160, Reala 100, Natura 1600, Velvia 50/100, Provia 100F/400F/400X, Sensia 100, Astia 100F, Fortia SP 50, Acros, Neopan 400/1600, Eterna, Nostalgic Negative.
Ilford: HP5 Plus, Delta 100/400/3200, Pan F Plus 50, FP4 Plus 125, XP2 Super, Ortho Plus 80, SFX 200.
CineStill: 800T, 50D, 400D. Also Agfa, Adox, Rollei, Foma, ORWO, Ferrania and Lomography stocks.

## Why do free Lightroom presets often look flat or washed out?

Because they omit the camera-profile Look block or declare an old `ProcessVersion`. Without `crs:Look`, Lightroom skips the non-linear input colour matrix entirely; with a legacy process version it uses different tone mapping. Either way the image renders flat and desaturated, and no amount of slider tweaking fixes it.

Every preset here declares `ProcessVersion="15.4"`, a valid `<crs:Look>` block (Adobe Color, Adobe Monochrome, or Adobe Vivid for slide film), and neutral `ToneCurvePV2012` baselines across all four curves. Structural checks run on every file before commit.

## How do I install them?

1. Download the [latest release ZIP](https://github.com/peva3/EmulsionPresets/releases/latest) — flat, all `.xmp` files at the root.
2. Copy them into your Develop Presets folder:
   - **macOS:** `~/Library/Application Support/Adobe/Lightroom/Develop Presets/`
   - **Windows:** `%APPDATA%\Adobe\Lightroom\Develop Presets\`
3. Restart Lightroom. Presets appear grouped by category.

Prefer one category? Copy just that folder from [`Presets/`](Presets).

## How do these compare to VSCO, Mastin Labs and RNI Films?

| | Emulsion Presets | VSCO Film | Mastin Labs | RNI Films |
|---|---|---|---|---|
| Price | Free (MIT) | Discontinued | ~$99–150/pack | ~$125–175 |
| Presets | 451 | — | ~40 per pack | 180+ profiles |
| Format | `.xmp` | `.xmp`/`.lrtemplate` | `.xmp` + DCP | DCP profiles |
| Research published | Per preset | No | No | No |
| Modifiable | Yes | Yes | Partly | No |

Paid packs sometimes include camera-specific DCP profiles, which apply colour rendering at the sensor level and are more accurate on a given camera than slider presets. That trade-off is documented per preset rather than hidden.

## Are the presets researched, or just slider guesses?

Every preset has a dossier in [`research/`](research): film characteristics (spectral response, grain, tonal register), community recipes (Fuji X Weekly, Reddit, forums, YouTube), datasheet analysis where available, and a `## Validation Sweep` section recording what was checked and corrected.

The engineering rules live in [STYLEGUIDE.md](STYLEGUIDE.md) — including the Lightroom-specific traps: the hue-axis direction (negative green hue moves foliage toward olive, not cyan), the Vibrance/Saturation gap that produces selective-colour artefacts, and the grain-versus-sharpening conflict that turns organic grain into digital noise.

## Tips for best results

- **White balance first.** Many presets assume a temperature; if colour feels off, adjust WB before anything else.
- **Exposure is yours.** These are calibrated starting points for well-exposed RAW files — expect to move Exposure ±0.3 EV.
- **Grain scales with resolution.** Grain was tuned around 24MP; reduce Amount on lower-resolution files.
- **Stack them.** A film preset for colour, then a creative preset (Matte Fade, Cinematic Dream) as a second pass.

## For agents and language models

[`presets.json`](presets.json) lists all 451 presets with category, treatment, file path, download URL and a one-line description. [`llms.txt`](llms.txt) is a short index; [`llms-full.txt`](llms-full.txt) is the whole catalog as prose. Both are generated from `Presets/` by [`test/build_catalog.py`](test/build_catalog.py), so they cannot drift.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Research first, keep presets simple, validate XML before committing.

## Citation

If you use these in teaching or writing, see [CITATION.cff](CITATION.cff).

## License

MIT — [LICENSE](LICENSE). Free for personal and commercial use.
