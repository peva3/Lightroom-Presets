# Foma Fomapan 100 — Film Characteristics

## Overview
Fomapan 100 is a classic cubic-grain black-and-white negative film produced by Foma Bohemia (Hradec Kralove, Czech Republic). It has been in continuous production for decades and is known for its affordability, traditional grain structure, and distinctive Eastern European character. One of the most popular budget B&W films worldwide.

## Key Characteristics
- **ISO**: 100 (nominal)
- **Grain**: Moderate — classic cubic grain, more visible than modern T-grain 100-speed films
- **Sharpness**: Good — moderate acutance, good edge definition
- **Contrast**: Moderate — slightly higher than Western 100-speed films
- **Tonal Range**: Good midtones, slightly compressed shadows, tendency toward deeper blacks
- **Spectral Sensitivity**: Traditional panchromatic — slightly reduced red compared to modern films
- **Development**: Very responsive to developer choice — dramatically different in Rodinal vs. D-76 vs. XTOL
- **Exposure Latitude**: Good — tolerates underexposure better than overexposure

## Historical Context
- Produced by Foma Bohemia in the Czech Republic since the Cold War era
- Originally formulated for the Soviet/Eastern Bloc market
- Became popular in Western markets after the fall of the Iron Curtain for its low price
- Distinct from Western films — uses different sensitizing dyes and emulsion recipes
- Modern Fomapan 100 has been updated but retains the classic cubic-grain character
- Often the first film photography students try due to affordability

## Visual Signature
- Classic, old-school B&W character — not "modern" or "clean"
- Slightly higher contrast than Ilford Delta 100 or Kodak T-Max 100
- Grain is visible and characterful — part of the aesthetic
- Deep, rich blacks with good shadow separation
- In Rodinal: pronounced grain, high acutance, dramatic — the "Czech Tri-X" look
- In XTOL: smoother, more modern, comparable to Western 100-speed films
- A true "budget classic" that punches above its price

## Sources
- Foma Bohemia Technical Data Sheet (Fomapan 100)
- Massive Dev Chart entries for Fomapan 100
- Community reviews (Photrio, 35mmc, Reddit r/analog)
- Foma product documentation

---

## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** ISO 100 traditional cubic grain, "more visible than modern T-grain 100s" (preset GrainAmount 30 / GrainSize 25 — above Delta 100's 15/20 and T-Max 100's 15/18, correct); slightly higher contrast than Western 100s with a tendency to deep blacks (Contrast +20 vs Delta 100 +15, Blacks −25 — correct). Two drifts: (1) this folder says "slightly reduced red compared to modern films", yet GrayMixer Red +25 is a *stronger* red boost than Delta 100's +10 — the opposite of the documented sensitivity; (2) GrainAmount 30 for an RMS ~13–14 emulsion is generous. Neither crosses the defining-trait threshold.
- **Sources:** Foma Bohemia Fomapan 100 data sheet and Massive Dev Chart entries cited here; Foma 200/400 datasheets for family grain ordering (Fomapan 400 RMS 17.5, Fomapan 200 RMS 14); beyondtheaperture three-film comparison (Fomapan 100/200/400 close in grain, 400 coarsest).
- **Preset adjustments:** none
