# Kodak Vision3 250D (5207/7207) — Technical Datasheet

## Identification

| Property | Value |
|---|---|
| **Manufacturer** | Eastman Kodak Company |
| **Product Line** | Kodak Vision3 Color Negative Film |
| **Stock Code** | 5207 (35mm), 7207 (16mm) |
| **Emulsion Type** | Color Negative |
| **Process** | ECN-2 (Eastman Color Negative 2) |
| **ISO (EI)** | 250 (Daylight) |
| **Color Balance** | Daylight (5500K) |
| **Formats** | 65mm, 35mm (perf & unperf), 16mm, Super 8 |
| **Production** | 2007–present |
| **Generation** | Vision3 (3rd generation, succeeding Vision2) |

## Spectral Sensitivity

The Kodak Vision3 250D emulsion uses Kodak's proprietary **Advanced Dye Layering Technology (ADLT)** and **2-electron sensitization**. The spectral sensitivity layers are:

- **Blue-sensitive layer**: Peak sensitivity ~450–480nm with tailored response for sky rendering. Controlled shoulder to prevent cyan overshoot in skies.
- **Green-sensitive layer**: Peak sensitivity ~540–560nm. Broad, symmetrical response for natural foliage and skin undertones.
- **Red-sensitive layer**: Peak sensitivity ~650–680nm. Extended red sensitivity with smooth roll-off for natural lip tones and warm highlights.
- **Interlayer effects**: Vision3 uses enhanced DIR/DAR couplers (Development Inhibitor Releasing / Development Accelerator Releasing) for interlayer interimage effects that produce rich color separation without oversaturation.

Key spectral characteristic: Vision3 250D shows elevated sensitivity in the **red-orange region (620–660nm)** compared to Vision2, contributing to the warm daylight look and golden skin tones. Blue sensitivity is slightly suppressed relative to previous generations, reducing blue-channel noise in shadows.

## Characteristic Curves (Sensitometry)

### Status M Densitometry

| Parameter | Value (Typical) |
|---|---|
| **D-min (Base + Fog)** | 0.20–0.25 R, 0.50–0.55 G, 0.85–0.90 B |
| **D-max** | ~2.8–3.0 (all channels) |
| **Gamma (mid-scale contrast)** | ~0.55–0.65 |
| **Latitude** | ~12 stops (-4 to +8 relative to normal) |
| **Shoulder onset** | ~3.0 log H (highlights) |
| **Toe onset** | ~-2.0 log H (shadows) |

### Curve Shape Characteristics

1. **Toe (Shadow Region)**: Gentle downward roll-off in shadows. Deep blacks compress gradually — not an abrupt clip. The 250D has less toe compression than 50D, giving punchier shadows.

2. **Linear Midtones**: Extended linear region spanning ~6 stops. This is where the Vision3 line is class-leading — neutral, straight-line response in the midtones means predictable color separation and consistent skin rendering across exposure levels.

3. **Shoulder (Highlight Region)**: Generous shoulder with smooth compression. Vision3 250D can hold highlight detail 4+ stops above middle gray before hard clipping. This is the "cinematic S-curve" — highlights compress but never blow out digitally-looking.

### RGB Tracking

The three color records (R, G, B) are designed to track in near-parallel through the midtones, meaning:
- Neutral grays stay neutral through the tonal range (no warm/cool shifts in shadows or highlights)
- Saturation builds evenly across the luminance range
- The "look" comes from interlayer interimage effects rather than curve separation

## Grain Structure

| Parameter | Value |
|---|---|
| **RMS Granularity** | ~4–5 (measured at 1.0 density, 48μm aperture) |
| **Grain character** | Fine, tight, "structured" — not mushy |
| **Color noise** | Low — Vision3 dye couplers produce clean color clouds |
| **Grain vs. sensitivity** | Best-in-class for ISO 250 speed class |

The Vision3 generation reduced grain by approximately 1-stop worth compared to Vision2. At EI 250, grain in 35mm is visible but not objectionable. In Super 35 / APS-C crops, grain becomes a subtle texture. In 16mm, grain is a defining characteristic.

## Sharpness / MTF

- **MTF at 50% response**: ~40 cycles/mm (35mm format)
- **MTF at 30% response**: ~55 cycles/mm
- **Acutance**: High — Vision3's sharpness comes from edge contrast enhancement via DIR couplers rather than raw resolution, giving a "crisp but not digital" look

## Kodak Vision3 250D vs. Other Vision3 Stocks

| Stock | ISO | Balance | Contrast | Grain | Typical Use |
|---|---|---|---|---|---|
| **50D (5203)** | 50 | Daylight | Lower | Finest | Bright daylight exteriors |
| **200T (5213)** | 200 | Tungsten | Medium | Very fine | Studio / mixed lighting |
| **250D (5207)** | 250 | Daylight | Higher | Fine | Diffuse daylight, overcast, shade |
| **500T (5219)** | 500 | Tungsten | Medium | Moderate | Low light, interiors, night |

The 250D is the **highest contrast Vision3 stock** — intentionally so, as it is designed for low-contrast lighting conditions (overcast, shade, window light). When used in high-contrast sunlight, expect clipped shadows/highlights.

## Sources

- Kodak EASTMAN EXR / Vision / Vision2 / Vision3 technical publications (archived)
- [Dehancer — Kodak Vision3 250D Profile](https://www.dehancer.com/profiles/film/kodak-vision3-250d)
- [FilmBox (Video Village) — Vision3 ECN-2 System](https://www.videovillage.co/filmbox/)
- Cinematography.com forums — Vision3 250D user discussions
- Kodak Motion Picture Film Product Guide (H-1-5207)
