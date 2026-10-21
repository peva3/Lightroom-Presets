# Cyanotype Classic Lightroom Preset — Complete Aesthetic Breakdown

## Core Aesthetic Signature

The cyanotype classic Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. The cyanotype process, invented by Sir John Herschel in 1842, produces distinctive Prussian blue monochrome prints. It was the first successful non-silver photographic printing process and was famously used by Anna Atkins for her botanical photograms — the first book illustrated with photographs. The classic cyanotype has deep blue shadows and bright cyan-blue highlights, with a characteristic tonal range that emphasizes texture and form over color.

## Historical Context

**Era:** 1842 (Herschel) | 1843–1853 (Anna Atkins)

Ferric ammonium citrate + potassium ferricyanide → Prussian blue (ferric ferrocyanide). UV exposure converts iron(III) to iron(II), which reacts with ferricyanide to form the insoluble blue pigment. Water development washes away unexposed sensitizer.

## Visual Characteristics

Monochrome Prussian blue image. Deep navy shadows, mid-blue midtones, pale cyan-blue highlights. No true white — the paper base is always cream or slightly blue-tinted. Slightly matte surface. Moderate contrast with good shadow detail retention.

## Emotional & Artistic Vocabulary

Scientific, archival, ethereal, melancholic. The blue monochrome creates emotional distance while retaining documentary precision.

### Key Descriptors


## Technical Notes for Digital Emulation

This preset is designed to capture the essential visual character of the cyanotype classic process using Lightroom's slider-based toolset. It prioritizes the emotional/aesthetic impact over perfect chemical accuracy, which would require a 3D LUT or DCP camera profile.

### Limitations of Slider-Based Simulation
- True process-specific spectral sensitivity cannot be replicated with sliders
- Chemical stain patterns are simulated through grain and color grading
- Paper/plate texture is approximated through grain settings

## Sources
- Wikipedia and photographic history references
- Alternative Photography (alternativephotography.com)
- Christopher James: *The Book of Alternative Photographic Processes*
- Community knowledge from r/analog, r/Darkroom, and photography forums

## See Also

- [Alternative Process Presets](../../docs/alternative-process.md)
- [Black White Presets](../../docs/black-white.md)
- [Creative Presets](../../docs/creative.md)
- [All Lightroom Preset Categories](../../docs/index.md)


## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** Prussian-blue-only rendering (Monochrome + Adobe Monochrome look; shadow 220deg/sat35, mid 218/20, highlight 215/5); contrasty, tonal compression (Contrast +30, Highlights -25) so midtones stay few; no calibration or WB values; grain 20.
- **Sources:** AlternativePhotography.com, 'Cyanotypes - how blue can you get?' and 'Toning Cyanotypes'; Graphics Atlas process 319 (cyanotype); Photrio thread 'Paper white in cyanotypes'
- **Preset adjustments:** none - drift noted: highlight saturation 5 leaves near-paper-white highlights, whereas the process keeps a faint cyan in the paper base. Not a defining contradiction (the image still reads Prussian blue end to end).
