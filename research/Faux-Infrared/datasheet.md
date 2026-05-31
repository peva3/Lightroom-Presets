# Infrared Film Datasheet — How Real IR Film Works

## Overview

Infrared photography uses film or sensors sensitive to near-infrared light (700–900 nm), beyond the visible spectrum. The signature look — **glowing white foliage, dark skies, and surreal false colors** — is attributed to the **Wood Effect**, named after infrared photography pioneer Robert W. Wood (1910). Foliage strongly reflects infrared in the same way visible light reflects off snow. Chlorophyll fluorescence contributes marginally; the dominant cause is high IR reflectivity of healthy plant cell structures.

---

## Black-and-White Infrared Film

### Spectral Sensitivity
- Sensitive to wavelengths from ~700 nm to ~900 nm (near-infrared).
- Also retains significant inherent sensitivity to blue/UV wavelengths (silver halide base property).
- An **infrared-passing filter** (e.g., Wratten #25 red, #29 deep red, #89B/R72 opaque) is used to block visible blue/UV, leaving only IR + some visible red to expose the film.
- Without a filter, B&W infrared film looks nearly indistinguishable from conventional panchromatic film.

### Kodak High-Speed Infrared (HIE) — Discontinued 2007
- The most iconic B&W IR film.
- Sensitive to ~900 nm.
- **Clear polyester base** with no anti-halation layer → produces the characteristic **halation/glow** around highlights. This glow is NOT inherent to IR photography; it's an artifact of HIE's base design.
- Must be loaded/unloaded in total darkness.
- Developed in standard B&W chemistry (D-76, etc.).

### Other Historical B&W IR Films
| Film | Peak Sensitivity | Notes |
|------|-----------------|-------|
| Agfa Aviphot | ~770 nm | Aerial film; still available via resellers (Rollei IR 400, 80S, 400S) |
| Efke IR 820 | ~800 nm | Discontinued 2012; "Aura" variant had no anti-halation layer |
| Ilford SFX 200 | ~740 nm | "Extended red sensitivity"; not true deep IR |
| Konica Infrared 750 | ~800 nm | Discontinued 2006 |

### Common IR-Passing Filters (Wratten System)
| Filter | 50% Cutoff | Visual Appearance | Effect |
|--------|-----------|-------------------|--------|
| #25 Red | 600 nm | Red | Subtle IR effect, blue blocked |
| #29 Deep Red | 620 nm | Very dark red | Stronger IR, most blue/red blocked |
| #89B / R72 | 720 nm | Opaque black | Pure IR, all visible blocked |
| #87 | 795 nm | Opaque black | Deep IR only |
| #87C | 850 nm | Opaque black | Extreme deep IR |

---

## Color Infrared Film — Kodak Aerochrome / Ektachrome EIR

### Background
- Developed during WWII for **camouflage detection** — healthy vegetation reflects IR differently than green paint.
- Consumer version: **Kodak Ektachrome Infrared (EIR)**, code 2236, 35mm 36-exposure.
- Aerial version: **Kodak Aerochrome III Infrared**, codes 1443 and SO-734.
- **ALL color infrared film discontinued by 2011.** Remaining stock is expired and hand-rolled by specialists.

### Three-Layer Emulsion Structure

Color infrared reversal film has a fundamentally different layer stack than conventional E-6 film:

| Layer (top to bottom) | Conventional Film Sensitizes To | IR Film Sensitizes To | Final Dye (Conventional) | Final Dye (IR Film) |
|------------------------|-------------------------------|----------------------|--------------------------|---------------------|
| Top | Blue light | **Infrared (700–900 nm)** | Yellow | **Cyan** |
| (Internal yellow filter) | Carey Lea silver (blocks blue) | **Absent** (no internal filter) | — | — |
| Middle | Green light | Green light | Magenta | **Yellow** |
| Bottom | Red light | Red light | Cyan | **Magenta** |

### Why an External Yellow Filter Is Required
- Silver halide emulsions are inherently sensitive to blue/UV in ALL layers.
- In conventional film, an internal yellow (Carey Lea silver) filter behind the blue layer prevents blue from reaching green/red layers.
- In IR color film, there is **no blue-sensitive layer** — but the green- and red-sensitive layers still have inherent blue sensitivity.
- Therefore, a **Wratten #12 yellow filter** (or equivalent) must be used externally to block blue/violet wavelengths.
- Without this filter, the image has a strong blue/cyan cast.

### False-Color Mapping
The film performs a spectral remapping:

| Real-World Wavelength | Mapped to Visible Color |
|----------------------|------------------------|
| Infrared (700–900 nm) | **Red** |
| Visible Red (~600–700 nm) | **Green** |
| Visible Green (~500–600 nm) | **Blue** |
| Visible Blue / Violet (~400–500 nm) | **Blocked by yellow filter** |

**Result:** Healthy vegetation (high IR reflectance) → **bright red/magenta/pink**. Skies (low IR, high blue) → near-black when filtered. This produces the surreal Aerochrome look.

### Aging Behavior
- EIR loses infrared sensitivity as it ages → cyan color cast in slides (fewer IR-sensitive grains develop).
- Peak sensitivity is within ~21 days of purchase; stabilizes at lower sensitivity thereafter.
- Requires cold storage; must be loaded/unloaded in total darkness (like HIE).

### Processing
- Originally E-4 process; later compatible with E-6 chemistry.
- Optimal results via **AR-5 process** (Kodak's recommended process for aerial IR film).
- E-6 yields acceptable but slightly shifted results.

---

## The Wood Effect — Why Foliage Glows White

1. **Chlorophyll is transparent to near-infrared.** Healthy plant cell walls (cellulose) strongly scatter and reflect IR wavelengths.
2. **The spongy mesophyll layer** in leaves acts as a diffuse IR reflector.
3. This effect is so strong that in B&W IR photography, foliage appears as bright as snow.
4. **Water absorbs infrared** — lakes, rivers, and moist soil appear very dark.
5. **Rayleigh scattering is reduced at IR wavelengths** — skies appear dramatically dark, haze penetrates, clouds pop brilliantly.
6. **Human skin** reflects some IR, giving a milky, ethereal look; eyes (which absorb IR) appear black.

---

## Key Physics Summary

| Phenomenon | Visible Light | Near-Infrared (700–900 nm) |
|-----------|--------------|---------------------------|
| Foliage reflectance | Low-moderate (green) | Very high (>70%) |
| Sky brightness (Rayleigh) | High (blue) | Very low (dark) |
| Atmospheric haze (Mie) | Moderate | Very low (penetrates) |
| Water reflectance | Moderate | Very low (absorbs) |
| Shadow detail | Normal | Darker (less IR scatter) |
| Cloud contrast | Normal | Very high |

---

## Sources
- Wikipedia: Infrared photography
- Kodak publication TI-2323 (Ektachrome Infrared film structure)
- Kodak publication F-13 (HIE Infrared film)
- Begleiter, *Infrared Photography Handbook*
- White, *Infrared Photography*
