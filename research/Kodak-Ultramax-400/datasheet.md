# Kodak Ultramax 400 — Technical Datasheet

## Official Product Name
Kodak Ultra Max 400 Film / Kodak GC 400 / Kodak Eastman UltraMax 400

## Basic Specifications

| Property | Value |
|----------|-------|
| Film type | Color negative (C-41 process) |
| ISO speed | ISO 400/27° |
| Formats | 35mm (24 and 36 exposure rolls) |
| Process | C-41 standard |
| Grain | RMS granularity: ~26 (consumer-grade, noticeably grainier than Portra 400) |
| Base | Acetate |
| Sharpness | Good sharpness for consumer-grade 400-speed film |
| Latitude | Good exposure latitude (±2 stops), best at box speed |

## Spectral Sensitivity / Color Response

- **Film is daylight-balanced** (5500K)
- Under tungsten/incandescent light, produces warm amber/yellow cast without filtration
- Three emulsion layers optimized for consumer printing:
  - **Red-sensitive layer**: High contrast, strong red/orange saturation
  - **Green-sensitive layer**: Moderate saturation, slight cyan bias in shadows
  - **Blue-sensitive layer**: High sensitivity, contributes to warm yellow cast in highlights

## Characteristic Curves (from Kodak published data)

*Note: Official full datasheet PDF (E4051) is not publicly accessible via direct link; the following is compiled from partial datasheet data, community measurement, and Kodak marketing materials.*

### Sensitometric Data
- **D-min** (base + fog): ~0.20–0.25 (typical for consumer C-41)
- **Gamma (contrast)**: ~0.62–0.68 (higher contrast than Portra 400, which runs ~0.55–0.60)
- **Shoulder**: Moderate highlight compression; highlights retain warmth but can blow out with >2 stops overexposure
- **Toe**: Good shadow detail retention at box speed; underexposure of >1 stop reveals noticeable grain

### Color Dye Density Peaks
- **Cyan dye**: Peak at ~660nm (red record) — contributes to slightly cool/teal shadow tendency
- **Magenta dye**: Peak at ~545nm (green record) — balanced
- **Yellow dye**: Peak at ~440nm (blue record) — contributes to warm golden cast

## Grain Structure

- **Grain category**: Consumer-grade, visibly grainier than professional films at ISO 400
- **Print Grain Index (PGI)**: ~46 (compared to Portra 400's ~48, interestingly similar per Kodak spec, but Ultramax grain appears coarser in actual scans due to higher acutance/sharpening in emulsion)
- Grain is most visible in mid-tones and underexposed areas
- Sky/blue areas show grain prominently
- Half-frame and 110 format amplify grain significantly

## Exposure Recommendations

| Lighting Condition | Suggested EI | Notes |
|-------------------|-------------|-------|
| Bright sun | 400 | Best results |
| Cloudy/shade | 320 | Slight overexposure for shadow detail |
| Golden hour | 400 | Film's warm cast naturally complements golden light |
| Flash | 400 | Pairs well with flash for consumer cameras |
| Overcast | 200 | Some shooters prefer +1 stop for muted overcast light |
| Tungsten | 400 | Warm amber cast expected; use 80A filter to correct |

## Storage & Handling

- Store at ≤21°C (70°F) for short term
- Refrigerate at ≤13°C (55°F) for extended storage
- Process promptly after exposure
- Standard C-41 processing (3min 15sec developer at 38°C/100°F)

## Product Codes

| Format | Product Code |
|--------|-------------|
| 35mm 24exp | 1024389 |
| 35mm 36exp | 7518335 (Eastman) |
| 35mm 3-pack | 1453694 |

## Key Takeaways for Preset Creation

1. **Higher contrast** than Portra 400 — requires stronger tone curve shaping
2. **Warm-leaning white balance** — golden/yellow cast even in daylight
3. **Saturated reds and oranges** — need to push these in HSL
4. **Noticeable grain** — add grain simulation at moderate levels (~25–35 in Lightroom)
5. **Cooler shadows with teal tendency** — split-toning with cool/teal in shadows
6. **Slightly compressed highlights** — watch highlight clipping, emulate gentle shoulder roll-off
