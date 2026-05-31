# Kodak Portra 160 — Official Datasheet Reference

> **Source:** Kodak Technical Publication E-4051 (Portra 160)  
> **Film type:** Daylight-balanced color negative film, ISO 160, C-41 process  
> **Formats:** 135, 120, 220, 4×5 sheet, 8×10 sheet

---

## Spectral Sensitivity

Kodak Portra 160 uses Kodak's proprietary **T-GRAIN emulsion technology** across all color layers. The spectral sensitivity curves (per Kodak Tech Pub E-4051) show:

- **Red-sensitive layer:** Peak sensitivity ~650 nm, broad response across 580–680 nm. Smooth cyan-dye-forming layer optimized for accurate reds in Caucasian skin tones.
- **Green-sensitive layer:** Peak sensitivity ~550 nm, broad response 500–600 nm. Magenta-dye-forming layer tuned for natural green foliage and subtle skin undertones.
- **Blue-sensitive layer:** Peak sensitivity ~450 nm, extending 380–500 nm. Yellow-dye-forming layer with high UV filtration (built-in UV absorber) and controlled shoulder to prevent sky blowout.

### Interlayer DIR Couplers
All three emulsion layers incorporate **Development Inhibitor Releasing (DIR) couplers**, which provide:
- Edge enhancement (perceived sharpness)
- Interimage effects for cleaner color separation
- Controlled saturation in mixed-lighting conditions

---

## Characteristic Curves

Kodak's published characteristic density curves for Portra 160 show:

| Channel | D-min (Base+Fog) | D-max | Gamma (average) | Shoulder onset |
|---------|-----------------|-------|-----------------|----------------|
| Red (Cyan dye) | ~0.25 | ~2.60 | ~0.55 | ~2.0 log lux·s |
| Green (Magenta dye) | ~0.25 | ~2.75 | ~0.55 | ~2.0 log lux·s |
| Blue (Yellow dye) | ~0.25 | ~2.85 | ~0.60 | ~2.1 log lux·s |

- **Linear range:** Approx. −2.0 to +3.0 stops from middle gray (≈ 5+ stops of usable dynamic range before compression).
- **Shoulder behavior:** Extremely gradual highlight roll-off — this is the signature "soft contrast" that preserves highlight detail without clipping.
- **Toe behavior:** Smooth shadow detail preservation, approximately −4 stops from middle gray.
- **Color balance across exposure:** All three curves maintain parallelism across a wide range, meaning color neutrality holds even at +2 to +3 stops overexposure (common practice: shoot Portra 160 at ISO 100–125 for pastel skin).

---

## Grain RMS

| Film | RMS Granularity (48 µm aperture) |
|------|-----------------------------------|
| **Portra 160** | **~4** |
| Portra 400 | ~5–6 |
| Portra 800 | ~7–8 |
| Ektar 100 | ~4 |

Portra 160 has the **finest grain of any Kodak color negative film in the current lineup** — tied with Ektar 100 but with far smoother, less saturated rendering. The T-GRAIN structure in all layers ensures grain texture is essentially invisible in 4×5, imperceptible in 120, and extremely fine in 135.

---

## MTF / Sharpness

- **MTF at 50% contrast:** Resolves beyond 50 lp/mm (TOC 1.6:1 contrast ratio)
- **Edge acutance:** Enhanced via DIR couplers — perceived sharpness exceeds that of many ISO 100 films despite the higher speed
- **Scanning note:** Grain aliasing is minimal even at 4000 dpi scans due to tight grain distribution

---

## Reciprocity Characteristics

| Exposure time | Adjustment needed |
|--------------|-------------------|
| 1/10,000 s – 1 s | No correction |
| 10 s | +0.5 stop + no filter |
| 100 s | +1.0 stop + no filter |

Portra 160 has excellent reciprocity — usable up to ~120 seconds with minimal color shift, making it practical for long-exposure landscape work.

---

## Printing & Scanning

- **Optical printing:** Designed for RA-4 printing with excellent neutrality on Kodak Supra Endura papers
- **Digital scanning:** Wide color gamut exceeds sRGB; recommended scanning as flat DNG/TIFF with manual inversion for best results
- **Scanner profiling:** Frontier SP-3000 and Noritsu HS-1800 are common lab scanners; each imparts a distinct baseline color interpretation (Frontier = cooler/cyan-leaning, Noritsu = warmer/magenta-leaning)
- **Kodak's official Cineon conversion:** Available via their discontinued Cineon system but not required for modern workflows

---

## Storage & Handling

- **Unexposed:** Store at ≤13°C (55°F). For long-term storage >6 months, store at −18°C (0°F) or lower.
- **Exposed:** Process promptly. If delay >1 week, refrigerate. Allow 2–3 hours to warm before opening sealed containers.
- **Shelf life:** Excellent — can produce good results 5+ years past expiration if cold-stored.

---

## Key Technical Takeaways for Digital Emulation

1. **Dynamic range exceeds most digital sensors in highlights** — the shoulder compression is the single hardest thing to emulate digitally.
2. **RMS 4 grain** means the film is essentially grain-free in medium format and large format; in 35mm, apply grain *only* in the lowest-frequency luminance channel.
3. **Spectral sensitivity is tuned for skin** — the red channel has a gentle slope, and the green-magenta layer is intentionally flat across flesh tones (550–620 nm).
4. **DIR couplers provide natural edge contrast** — emulate via subtle mid-frequency clarity, not sharpening.
5. **No color correction filters needed** for daylight (5500K) or electronic flash.
