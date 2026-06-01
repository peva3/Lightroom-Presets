# Project: Lightroom Presets (peva3/Lightroom-Presets)

## Overview
48 XMP Lightroom presets across 4 categories:
- **Color Negative** (16): Film stock emulations — Portra, Gold, Ektar, Fuji, etc.
- **Black White** (6): Tri-X, HP5, Delta 3200, Acros, T-Max 3200, Ricoh HC
- **Slide** (4): Kodachrome 64, Velvia 50, Astia 100F, Ektachrome E100
- **Creative** (22): Cinestill, bleach bypass, cyberpunk, VHS, WKW, etc.

## Critical Findings: XMP Color Issues

### The "B&W with one color" bug
Multiple presets were creating a selective-color effect (near-monochrome with one boosted hue). Root causes identified:

1. **Vibrance >> Saturation gap**: When `Vibrance - Saturation > 10`, Lightroom desaturates globally (via Saturation) then selectively boosts midtones (via Vibrance), creating a selective-color effect. **Fix**: Keep Vibrance within 5 points of Saturation, or remove Vibrance entirely.

2. **Calibration panel** (`CalibrationRedHue/Sat`, `CalibrationGreenHue/Sat`, `CalibrationBlueHue/Sat`): The original working XMPs had ZERO calibration values. Adding calibration shifts global primary interpretation, which compounds unpredictably with HSL + split toning. **Fix**: Remove calibration entirely unless absolutely needed.

3. **Temperature/Tint**: Original XMPs had no WB adjustments. Adding WB shifts before HSL/split toning creates color conflicts. **Fix**: Use only for presets where WB is a defining characteristic (e.g., Ultramax's warm cast). Remove from generic film emulations.

4. **Extreme HSL saturation** (> |60|): Nukes entire color channels. **Fix**: Cap at ±60.

### The retuning disaster
The intermediate "retune all 48" commit (`339fe11`) made presets far too aggressive. The fuzzy-merge agents compounded this by adding Calibration, Temperature/Tint, and extreme Vibrance values from aggregated community recipes. The result was presets with 55-68 attributes that looked broken on real photos.

### Original working XMPs (old/ folder)
The `old/` directory contains the reference versions. They are SIMPLE — 8-15 attributes each, no calibration, no WB adjustments, no extreme values. They prioritize subtlety over "pop."

## Research Methodology
- Each preset has `research/{preset}/` with community-recipes.md, characteristics.md, and sometimes datasheet.md / reference-packs.md
- Community values were compiled from Reddit (r/Lightroom, r/postprocessing, r/analog), YouTube, Fuji X Weekly, Mastin Labs, RNI, VSCO
- Wayback Machine (web.archive.org) provides Reddit archival data without rate limits: `https://web.archive.org/web/2025*/https://old.reddit.com/r/SUBREDDIT/search?q=...`
- Reddit's robots.txt blocks Wayback archiving of `/comments/*` and `/search` pages, so most archival attempts return 404

## File Structure
```
Presets/
├── Color-Negative/ (16)
├── Black-White/ (6)
├── Slide/ (4)
└── Creative/ (22)
research/
├── {preset-name}/
│   ├── community-recipes.md
│   ├── characteristics.md
│   ├── datasheet.md (optional)
│   ├── reference-packs.md (optional)
│   └── various preset-specific files
test/
├── render.py — CLI to apply XMP presets to images
└── merge_presets.py — compare/merge old vs new XMP values
old/ — reference original XMPs (flat, no subfolders)
```

## Render Pipeline (`test/render.py`)
Applies XMP presets to RAW/JPEG using rawpy + numpy + scikit-image. Converts crs: attributes to image processing ops. Not a perfect Lightroom match but good for visual iteration. Usage:
```
python3 test/render.py <image> batch [output-dir]
python3 test/render.py <image> "Preset Name" [output.jpg]
```

## Git History
- `4c91f9b`: Initial 30 presets (original working values)
- `4113475`: Moved to subfolders, added TOC/gitignore
- `874d202`: Added 5 Tier 1 presets (Portra 800, Classic Negative, Ultramax 400, VHS, WKW)
- `43c4a15`: Added 13 Tier 2+3 presets (48 total)
- `339fe11`: RETUNE ALL 48 — broke everything with aggressive values
- Latest: Restored original values, applied community fixes

## Key Rules for Agents
1. NEVER add Calibration panel values (RedHue/Sat, GreenHue/Sat, BlueHue/Sat, ShadowTint) — they create color channel imbalance. **Exception**: `Canon Color Science` uses calibration as its defining characteristic (emulates Canon's in-camera color science via calibration shifts), so calibration values are allowed there.
2. Keep Vibrance within 5 points of Saturation, or remove Vibrance
3. Avoid Temperature/Tint unless it's a defining characteristic of the film stock
4. Cap all HSL adjustments at ±60
5. Keep presets SIMPLE — the working originals had 8-15 attributes, not 60+
6. Research first: check `research/{preset}/` before modifying XMPs
7. Always verify on a real image before committing
