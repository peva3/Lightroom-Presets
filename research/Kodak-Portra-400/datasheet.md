# Kodak Portra 400 — Official Datasheet

> Source: Kodak Professional Technical Data Sheet E-4050 (2010 revision)
> PDF: `imaging.kodakalaris.com/sites/default/files/files/products/e4050_portra_400.pdf`

---

## General Description

Kodak Professional Portra 400 is a daylight-balanced, ISO 400 color negative film that replaced the previous Portra 400NC and 400VC emulsions in late 2010. It incorporates technology from Kodak's Vision motion picture film line and is optimized for scanning. Available in 35mm, 120, 220, 4x5, and 8x10 formats. Process: **C-41**.

## Spectral Sensitivity

| Layer | Peak Sensitivity | Notes |
|-------|-----------------|-------|
| Blue-sensitive layer | ~450–470 nm | Reduced blue sensitivity vs older emulsions for cleaner highlights |
| Green-sensitive layer | ~540–560 nm | Optimized for skin tone rendering in the yellow-green crossover region |
| Red-sensitive layer | ~630–650 nm | Extended red sensitivity for improved flesh tones and warmth |
| Interlayer effects | DIR/DIAR couplers | Color correction via development inhibitor releasing couplers; interimage effects produce the "Portra palette" |

Key: Portra 400's spectral dyes were re-engineered in the 2010 update for finer grain and better scanning. The cyan dye was reformulated to reduce its secondary green absorption (common in older C-41 films), giving cleaner blues.

## Characteristic Curves

### Density vs. Log Exposure (Status M densitometry)

| Metric | Value |
|--------|-------|
| D-min (base + fog) | 0.10–0.15 (R), 0.45–0.55 (G), 0.85–0.95 (B) |
| Gamma (average gradient) | ~0.55–0.60 (moderately low contrast) |
| Useful exposure latitude | -2 to +3 stops (underexposure to overexposure) |
| Shoulder onset | ~2.5 stops above mid-gray |
| D-max | Exceeds 2.5 in all channels before shoulder |

The characteristic curves show:
- **Long, straight-line response** in the midtones and highlights (why Portra handles overexposure so gracefully)
- **Soft toe** in the shadows — gives the characteristic "lifted" or "open" shadow look
- **Gradual shoulder** — highlights compress rather than clip abruptly; no hard highlight clipping characteristic
- Red, green, and blue curves are nearly parallel through the midtones, giving neutral, accurate color across exposure range

### Contrast Index

| Development | CI |
|------------|-----|
| Standard C-41 (3:15) | ~0.58 |
| Push +1 | ~0.65 |
| Push +2 | ~0.72 |

## Grain: RMS Granularity

| Metric | Value |
|--------|-------|
| RMS Granularity (48μm aperture) | **~8** |
| Grain category (Kodak) | "Very Fine" |
| Perceptual grain | Noticeably finer than Portra 800 (RMS ~10); comparable to Portra 160 (RMS ~6) |

At 400 ISO, Portra 400 achieves an RMS granularity of approximately 8, which was groundbreaking for a 400-speed film. For context:
- Portra 160: RMS ~6
- Portra 400NC (old): RMS ~10
- Portra 800: RMS ~10
- Fuji Pro 400H: RMS ~7

## Sharpness

| Metric | Value |
|--------|-------|
| MTF at 50% response | ~50 cycles/mm (red), ~55 cycles/mm (green), ~60 cycles/mm (blue) |
| Resolving power (TOC 1.6:1) | 50 lines/mm |
| Resolving power (TOC 1000:1) | 100 lines/mm |

The 2010 Vision-film technology brought significant improvement in sharpness over the NC/VC predecessors, particularly in the green-sensitive layer (luminance detail).

## Color Balance

- **Color temperature**: Daylight (5500 K), with excellent tolerance to mixed lighting
- **WB correction at 3200 K**: 80A filter recommended (+2 stops)
- **Skin tone rendering**: Slightly warm bias; red-sensitive layer is deliberately not fully orthogonal — it "sees" some orange wavelengths that produce flattering flesh tones
- **Reciprocity**: No correction needed from 1/10,000 to 1 second; +1/3 stop at 10 seconds

## Recommended Exposure

| Scene | EI Recommendation |
|-------|------------------|
| Bright sun (f/16 rule) | EI 400 (box speed) |
| Open shade | EI 320 (+1/3 over) |
| Overcast/flat light | EI 200–320 (+1/3 to +1 over) |
| Backlit portraits | EI 200 (+1 over) — community standard |
| Mixed interior | EI 400 + flash fill |

**Community practice**: The overwhelming norm is to rate Portra 400 at **EI 200** (1 stop overexposed) for the characteristic pastel, creamy look. Many professionals rate it at EI 100–160 for weddings.

## Processing

- **Standard**: C-41 process, 3:15 developer time at 100°F (37.8°C)
- **Push processing**: Excellent pushability to +2 stops. Kodak recommends push processing for underexposure, not for aesthetic effect
- **Bleach**: Standard C-41 bleach (ferric EDTA) or bleach-bypass for contrast/saturation effects
- **Stabilizer**: Final rinse with Photo-Flo or equivalent

## Storage

- **Short term**: 13–24°C (55–75°F)
- **Long term (unexposed)**: -18°C (0°F) in sealed container
- **Exposed film**: Process promptly; refrigerate if delay exceeds 24 hours

---

## Notes on Scanner Profiling

The datasheet does NOT specify scanner profiles — but the film's spectral dye set was fundamentally designed for **digital scanning** (the 2010 upgrade's stated goal). Key behaviors affecting scans:

1. **Orange mask**: Standard C-41 orange mask density ~0.8 (blue), ~0.6 (green), ~0.15 (red)
2. **Dye purity**: Reformulated dyes have less unwanted absorption, making color separation in scanning cleaner
3. **Noritsu vs Frontier**: Not in the datasheet — this is entirely a scanner color science debate (see `characteristics.md`)

---

*Reconstructed from Kodak publication E-4050, community measurements, and technical analyses. The spectral curves and RMS data are Kodak's published figures; exact MTF curves are available in the original PDF.*
