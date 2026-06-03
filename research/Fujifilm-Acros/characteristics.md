# Fujifilm Acros — Full Aesthetic Characteristics for Lightroom Presets

## Overview

Fujifilm Acros is Fuji's most celebrated black-and-white film stock and in-camera simulation. It represents the gold standard for monochrome rendering in the Fuji ecosystem — praised across the industry for its fine grain, rich midtone separation, and exceptional shadow detail. The in-camera simulation is widely considered Fujifilm's best film simulation, period, and is often described as the most "analog-like" of all digital monochrome simulations. This document serves as a reference for creating a Lightroom preset that emulates Acros.

## Film Stock Aesthetic

### Grain
- **RMS granularity ~7** — among the finest of any traditional B&W film
- Grain is visible but extremely fine and "tight" — not clumpy or sandy
- At box speed (ISO 100): barely perceptible grain even in large prints
- Pushed to 200-400: grain becomes moderately visible but remains elegant
- Stand development in Rodinal (as used in the 35mmc comparison): produces much more pronounced grain, with a gritty, characterful texture

### Tonal Rendering
- **Wide tonal range**: 14+ zones of discernible density
- Extraordinary highlight retention — highlights roll off smoothly, without harsh clipping
- Deep, dense blacks with preserved shadow detail
- Rich midtone separation — subjects appear three-dimensional
- Slightly lower contrast than Kodak T-Max 100; more nuanced midtones than Ilford Delta 100

### Spectral Sensitivity (Panchromatic)
- Extended red sensitivity (not as extreme as Kodak's T-grain films)
- Slightly compressed blue response, giving skies a natural density without filtration
- **Red filter behavior**: Well-known for how Acros handles red filtration — skies go dramatically dark while maintaining cloud separation
- **Green response**: Moderate; foliage renders with rich midtones
- Skin tones: Excellent — the panchromatic balance produces flattering, natural skin rendering without the "chalky" look some films produce

### Reciprocity (Original Acros)
- The single most celebrated technical characteristic of original Acros
- **No compensation needed for exposures up to 120 seconds**
- For exposures up to 1000 seconds: only +1/2 stop
- This made Acros the undisputed king of long-exposure B&W photography
- *Note*: Acros II (manufactured by Harman) does not match this level of reciprocity performance

## In-Camera Acros Simulation Aesthetic

### What Makes It Special

The Acros simulation is fundamentally different from simple B&W conversions or desaturation. Key characteristics:

1. **Grain that behaves like film**: As ISO increases, simulated grain increases organically — not as a uniform overlay but as a density-dependent structure. This is the simulation's most praised technical feature.

2. **Film-like tonal compression**: The simulation applies non-linear tonal mapping that mimics the characteristic curve of real panchromatic film. Highlights compress gently (unlike digital's harsh clipping); shadows open up with texture preserved.

3. **Built-in base "look"**: Even with all parameters at zero, Acros JPEGs look distinctly different from Monochrome-JPEGs or desaturated RAWs. There's an inherent "filmic" quality baked into the tone curve.

### Grain Rendering — Deep Dive

The Acros grain algorithm (source: Fuji X Weekly, Fujifilm technical literature):

| ISO Setting | Grain Behavior |
|-------------|----------------|
| ISO 200-400 | Very fine, barely visible; smooth tonality |
| ISO 800-1600 | Moderate, visible grain; adds texture without obscuring detail |
| ISO 3200-6400 | Pronounced grain structure; gritty, film-like texture |
| ISO 12800+ | Heavy grain; reminiscent of pushed Tri-X or T-Max P3200 |

Adding the **Grain Effect: Weak** setting layers additional grain *on top of* the baseline Acros grain. **Grain Effect: Strong + Large** produces the heaviest grain texture — used in recipes emulating pushed or high-ISO film stocks like Kodak T-Max P3200 and pushed Ilford HP5.

### Tonal Curve Default Behavior

| Zone | Behavior |
|------|----------|
| Deep shadows | Rich, inky blacks; ~2 stops of shadow detail retention |
| Lower midtones | Smooth gradation; good separation of dark grays |
| Midtones | Rich and dimensional; the simulation's sweet spot |
| Upper midtones | Gradual compression begins; still good detail |
| Highlights | Excellent roll-off; resists harsh digital clipping |
| Specular highlights | Clean, not blown to pure white; retains some texture |

### The Acros "Filter" Variants in Practice

Based on extensive community testing (Fuji X Weekly, r/fujifilm):

- **Acros+R** is by far the most popular variant among landscape and street photographers. It darkens blue skies (making clouds pop), lightens reds, and produces the most dramatic overall contrast. Ritchie Roesch notes it behaves more like an **orange** filter than a true red filter.

- **Acros+G** is preferred for portraits, especially with red-haired subjects. It darkens red tones (lips, freckles, reddish skin) and lightens greens, producing moody, dramatic faces. One commenter on Fuji X Weekly noted: *"Acros+G was meant for kids with red hair and freckles."*

- **Acros+Y** is the subtlest option — a gentle yellow filter effect. Useful for slightly darkening skies while maintaining natural skin tones. Good general-purpose outdoor option.

- **Acros (standard)** — used when no filter simulation is desired; the pure Acros tone curve.

### Digital vs. Real Film Comparison (from Dale Rogers' 35mmc Shootout)

Dale Rogers compared Fujifilm X-Pro3 Acros-R JPEGs against real Acros 100 II film (developed in Rodinal 1:100 stand):

> *"Fujifilm did a great job on the Acros digital film simulation. I was surprised the shots were similar in look and feel."*

Key differences noted:
- **Film highlights**: More graceful, smoother roll-off. Film preserved more highlight detail.
- **Digital shadows**: More recoverable shadow detail (even in JPEGs).
- **Film contrast**: Higher native contrast with Rodinal stand development; more "punch."
- **Digital smoothness**: Cleaner midtones; less grain than the Rodinal-developed film.

Community consensus from the article: most commenters **preferred the film** for its boldness, character, highlight handling, and timeless quality. The digital simulation was praised as an excellent approximation but was described as slightly "flatter" and less characterful.

## Aesthetic Use Cases

### Where Acros Shines
- **Street photography**: The most popular Fuji film sim for street — eliminates color distraction, emphasizes light, form, and moment
- **Portraits**: With Acros+G or Acros+Y, produces timeless, textured portraits
- **Long exposure**: Acros+R + low ISO = dramatic skies and silky water
- **Architecture**: Clean lines, deep blacks, rich tonal separation
- **Documentary/photojournalism**: Classic film aesthetic without needing actual film
- **Minimalism**: When color is distraction and texture is voice

### Where Acros May Not Be Ideal
- Need maximum shadow detail at extreme low light (Monochrome or RAW may be better)
- Want ultra-clean, grain-free B&W (use Monochrome with NR)
- Need Acros look on X-Trans I/II cameras (must use Monochrome + custom settings)

## Acros as a Base for Recipes

Acros is the foundation for the most popular B&W Film Simulation Recipes (Fuji X Weekly). Notably:
- **Kodak Tri-X 400** (most popular B&W recipe overall) uses Acros base + modified tone curve to achieve Kodak's classic press-film look
- **Kodak T-Max P3200** uses Acros + heavy grain + aggressive tone curve
- **Agfa Scala** uses Acros for its contrasty, reversal-film look
- **Ilford HP5 Plus** (original X-Trans III recipe) uses Acros

This versatility — the ability to convincingly emulate completely different film stocks — demonstrates Acros's flexible tonal architecture.

## Expert Recognition

**Ritchie Roesch** (Fuji X Weekly, 2024): *"Acros is Fujifilm's crowning achievement in monochrome photography. [...] Acros is unique because Grain is applied algorithmically and varies depending on ISO and exposure, giving it an organic analog-like feel."*

**Dale Rogers** (35mmc, 2020): *"Fujifilm did a great job on the ACROS digital film simulation. I was surprised the shots were similar in look and feel."*

**Multiple commenters** on 35mmc.com comparison article: Consensus that film Acros still wins for character and highlight handling, but digital Acros is an excellent substitute, especially when customized with the in-camera JPEG parameters.

---

## See Also

For related Lightroom presets and film stock references:

- [Fujifilm Classic Negative](../Fujifilm-Classic-Negative/characteristics.md)
- [Fuji Neopan 400](../Fuji-Neopan-400/characteristics.md)
