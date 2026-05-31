# Fujifilm Acros 100 — Film & In-Camera Simulation Datasheet

## Fuji Neopan Acros 100 (Original)

- **Introduced**: 1952
- **Discontinued**: 2018
- **ISO**: 100 (nominal)
- **Type**: Panchromatic black-and-white negative film
- **Formats**: 35mm, 120 (medium format), sheet film
- **Base**: Cellulose triacetate
- **Grain**: Extremely fine (RMS granularity ~7)
- **Resolving power**: Very high (contract: ~125 lines/mm, low contrast: ~63 lines/mm)
- **Spectral sensitivity**: Panchromatic with extended red sensitivity (slightly less red-sensitive than Kodak T-Max, more than traditional cubic-grain films)
- **Reciprocity**: **Best in class** — no exposure compensation needed for exposures up to **120 seconds**. For 1000 seconds, only +1/2 stop required. This was a standout feature of original Acros.
- **Developing times (typical)**: D-76 stock 20°C: 9.5 min; Rodinal 1+50: 14 min; HC-110 Dilution B: 6 min

## Neopan Acros 100 II (2019–Present)

- **Introduced**: November 2019
- **Manufacturer**: Produced by **Harman Technology** (Ilford's parent company) under license for Fujifilm
- **ISO**: 100
- **Formats**: 35mm, 120
- **Key changes from original**: Slightly different emulsion — *not* identical to the original. Re-formulated to be produceable on Harman's coating line. Very similar visual characteristics.
- **Reciprocity**: Good, but **not** as exceptional as original Acros (Harman's coating technology differs from Fujifilm's original)
- **Grain/Fineness**: Still very fine grain, among the finest 100-speed B&W films
- **Developing**: Compatible with standard B&W developers. Behaves similarly to Ilford Delta 100 (given Harman production).
- **Spectral Sensitivity**: Panchromatic; slightly different red response curve vs original (some users report slight tone differences with red filters)

## Fujifilm Acros In-Camera Simulation

The **Acros Film Simulation** is available on all Fujifilm X-Trans III and later cameras (X-Pro2, X-T2, X100F, X-T20, X-E3, and all subsequent X and GFX cameras). Note: *not* available on X-Trans I, X-Trans II, or Bayer-sensor Fujifilm cameras. These older models use the simpler **Monochrome** film simulation instead.

### Simulation Architecture

| Parameter | Description |
|-----------|-------------|
| **Base** | Modelled after Fuji Neopan Acros 100 panchromatic film |
| **Gradation** | Smooth tonal transition from shadows to highlights; excellent highlight roll-off |
| **Blacks** | Deep, rich blacks with preserved shadow detail |
| **Contrast** | Moderate-to-strong default contrast, highly customizable |
| **Grain Algorithm** | **Unique**: Grain amount scales automatically with ISO setting. Higher ISO = more visible grain (organic, film-like behavior) |
| **Grain Structure** | Very fine grain at low ISO; becomes noticeably more pronounced at ISO 1600+ |

### Variants (Color Filter Simulations)

| Variant | Effect | Best For |
|---------|--------|----------|
| **Acros** | Standard panchromatic rendering; no filter simulation | General use, any subject |
| **Acros+Y** | Simulates yellow filter: sky slightly darkened, blues slightly deepened, skin tones lightened | Portraits, general outdoor |
| **Acros+R** | Simulates red/orange filter: sky dramatically darkened, reds lightened, blues deepened | **Landscape**, dramatic skies, architecture |
| **Acros+G** | Simulates green filter: reds darkened (lips, skin blemishes), greens lightened | Portraits (especially red-haired subjects), foliage-heavy scenes |

**Important**: Acros+R behaves more like an *orange* filter than a true red filter. The tonal shifts are more subtle than using physical color filters on real film.

### Customizable JPEG Parameters (in-camera)

Fuji cameras expose these Acros JPEG parameters for full creative control:

- **Grain Effect**: Off / Weak / Strong; Size: Small / Large
- **Color Chrome Effect**: Off / Weak / Strong (affects monochrome tone mapping)
- **Color Chrome FX Blue**: Off / Weak / Strong
- **Monochromatic Color (Toning)**: Warm/Cool cast setting (WC ±9, MG ±9)
- **Dynamic Range**: DR100 / DR200 / DR400 / DR-Auto
- **Highlight Tone**: -2 to +4
- **Shadow Tone**: -2 to +4
- **Sharpness**: -4 to +4
- **High ISO NR**: -4 to +4
- **Clarity**: -5 to +5 (X-Trans IV+; causes brief processing delay if non-zero)
- **White Balance**: Full K-value and tint shift control

### Compatibility by Sensor Generation

| Generation | Cameras | Acros Available? | Grain Effect? | Color Chrome? | Clarity? |
|-----------|---------|:---:|:---:|:---:|:---:|
| X-Trans I | X-Pro1, X-E1, X-M1 | No | No | No | No |
| X-Trans II | X-T1, X-T10, X-E2, X100S/T, X70 | No | No | No | No |
| X-Trans III | X-Pro2, X-T2, X-T20, X100F, X-E3, X-H1 | Yes | Weak/Strong | No | No |
| X-Trans IV | X-Pro3, X-T3, X-T4, X-T30, X100V, X-S10, X-E4 | Yes | Strong/Large | Yes | Yes (-5 to +5) |
| X-Trans V | X-H2, X-H2s, X-T5, X-S20, X100VI, X-T50, X-M5, X-E5 | Yes | Strong/Large | Yes | Yes (-5 to +5) |
| GFX 50S/50R | (X-Trans III era) | Yes | Weak/Strong | No | No |
| GFX 100/100S/100 II | (IV/V era) | Yes | Strong | Yes | Yes |

### Default Acros Settings (Unmodified)

Acros out of the box (no recipe applied) uses:
- Highlight: 0
- Shadow: 0
- Noise Reduction: 0
- Sharpness: 0
- Grain Effect: Off
- Clarity: 0
- Monochromatic Color: Off
- Dynamic Range: DR100

### How Acros Differs from Monochrome Sim

The Acros simulation is fundamentally different from the older Monochrome film simulation. Acros features:
1. Built-in grain that scales with ISO (Monochrome has no built-in grain)
2. Different tonal response curves (modeled on Neopan Acros film)
3. Smoother highlight roll-off
4. Deeper, more filmic blacks
5. More elaborate gradation across midtones

Ritchie Roesch (Fuji X Weekly): *"The tonality and grain structure of the Acros film simulation cannot be replicated by the Monochrome film simulation."*
