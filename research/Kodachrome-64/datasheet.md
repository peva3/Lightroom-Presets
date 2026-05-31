# Kodachrome 64 — Technical Datasheet

## Film Overview

| Property | Value |
|---|---|
| **Manufacturer** | Eastman Kodak |
| **Type** | Color reversal (slide) film |
| **Process** | K-14 (non-substantive) |
| **ISO** | 64/19° (daylight balanced) |
| **Introduced** | 1974 (K-14 generation; successor to Kodachrome-X) |
| **Discontinued** | June 22, 2009 |
| **Final processing** | December 30, 2010 (Dwayne's Photo, Parsons, Kansas) |
| **Formats** | 135, 120 (discontinued 1996), 126, 110 |
| **Dynamic range** | ~2.3D / ~8 stops (Kodak characteristic curves) |
| **Resolution equivalent** | ~20 megapixels per 24×36mm frame |

## Emulsion Structure

Kodachrome is **non-substantive** — unlike E-6 or C-41 films, it contains **no dye couplers in the emulsion layers**. All dyes are formed during processing.

### Layer stack (top to bottom):

1. **Blue-sensitive layer** → dyed **yellow** during processing
2. **Yellow filter layer** (Carey Lea silver + Lippmann emulsion) — blocks blue light from penetrating deeper layers during exposure; becomes opaque during first development
3. **Blue-green sensitive layer** → dyed **magenta** during processing
4. **Blue-red sensitive layer** → dyed **cyan** during processing
5. **Acetate film base**
6. **Rem-jet anti-halation backing** (removed in first processing step)

Because dye couplers are not embedded in the emulsion, each layer is **thinner** than substantive films. This means:
- Less light scatter during exposure → **superior sharpness**
- Visible **relief image** on the emulsion side
- Dyes are purer (formed in-solution rather than in-emulsion)

## K-14 Processing — The Complete Sequence

The K-14 process is extraordinarily complex, requiring **four separate developers**, **8+ chemical tanks**, and **precise re-exposure steps** using colored light. Normal E-6 film uses one color developer.

### Step-by-step:

| Step | Action | Detail |
|---|---|---|
| 1 | **Backing removal** | Alkaline bath softens cellulose acetate phthalate binder; spray wash removes rem-jet anti-halation backing |
| 2 | **First developer** (B&W) | PQ developer (phenidone/hydroquinone) reduces all exposed silver halide to metallic silver in all three layers; forms three superimposed negative silver images. Yellow filter layer becomes opaque. |
| 3 | **Wash** | Stops development, removes developer |
| 4 | **Red light re-exposure** | Through the film *base* — foggs remaining silver halide *only in the cyan (red-sensitive) layer* |
| 5 | **Cyan developer** | Color developer + cyan dye coupler in solution. Developer reduces fogged silver; oxidized developer byproducts react with cyan coupler → cyan dye precipitates in red-sensitive layer |
| 6 | **Wash** | |
| 7 | **Blue light re-exposure** | From the *top* — foggs remaining silver halide in blue-sensitive (yellow) layer. Opaque yellow filter layer prevents light reaching magenta layer. |
| 8 | **Yellow developer** | Color developer + yellow coupler → yellow dye forms in blue-sensitive layer |
| 9 | **Wash** | |
| 10 | **Magenta developer** | Contains a chemical *fogging agent* rather than light re-exposure. Makes remaining silver halide in green-sensitive layer developable. Dev + magenta coupler → magenta dye. |
| 11 | **Wash** | |
| 12 | **Conditioner** | Prepares metallic silver for bleach |
| 13 | **Bleach** | Ferric EDTA converts metallic silver back to silver halide |
| 14 | **Fix** | Dissolves and removes all silver halide, leaving only the three dye images |
| 15 | **Final wash** | Removes fixer |
| 16 | **Rinse** | Wetting agent prevents water spots |
| 17 | **Dry** | |

### Why K-14 dyes are irreplaceable

The dyes in Kodachrome are fundamentally different from E-6 films:

- **Dyes formed in solution**, not in the emulsion matrix. The couplers exist in the developer bath; the reaction between oxidized developer and coupler happens in-solution, and the resulting dye molecule *precipitates* into the layer.
- This produces dyes of **exceptional purity** — no unused couplers remain in the film after processing.
- In substantive films (E-6/C-41), couplers are embedded in the emulsion, and unused couplers remain after development, eventually contributing to color degradation.
- The specific dye set (cyan/magenta/yellow) used in K-14 was proprietary and uniquely tuned over decades. The exact chemical formulas were trade secrets.

**No one has access to these exact dyes anymore.** The chemical manufacturing chain for K-14 chemistry was dismantled in 2009-2010. Recreating it would require re-establishing a supply chain for specialty organic chemicals that no longer have commercial-scale demand.

---

## Archival Stability

### Dark storage (remarkable):
- Yellow dye (least stable): ~20% loss in **185 years** (Wilhelm Research)
- Post-1938 Kodachrome slides stored in darkness retain accurate color and density to this day
- Because no unused color couplers remain, there is nothing left to degrade

### Projection (poor):
- Fade time under projection: **~1 hour** (vs. Fujichrome's ~2.5 hours)
- High-intensity light rapidly degrades the dyes
- Kodachrome was designed for viewing, not repeated projection

### Unprocessed film latency:
- Exposed but unprocessed Kodachrome can survive decades (documented case: 19 years lost in a Canadian forest, successfully processed)

---

## Digital Scanning Challenges

1. **Blue color cast** — requires dedicated Kodachrome ICC profiles or IT8 calibration targets for accurate scanning
2. **Infrared incompatibility** — cyan dye absorbs into near-IR spectrum; the relief image on the emulsion side interacts with infrared. Digital ICE and similar IR dust removal systems **fail on Kodachrome** and can cause sharpness loss
3. **Massive dynamic range** — Kodachrome 25 reaches 3.6-3.8D (12 stops). Multi-exposure scanning (e.g., SilverFast Multi-Exposure) is recommended
4. **SilverFast** offers a dedicated "Kodachrome Mode" with custom ICC profiles per scanner model

---

## Product Timeline (Kodachrome 64)

| Era | Product | Years |
|---|---|---|
| Pre-K-14 | Kodachrome-X (ASA 64) | 1962–1974 |
| K-14 | Kodachrome 64, 35mm daylight | 1974–2009 |
| K-14 | Kodachrome 64 Professional, 35mm | 1983–2009 |
| K-14 | Kodachrome 64 Professional, 120 | 1986–1996 |

---

## Sources

- Eastman Kodak Company, "KODACHROME 64 and 200 Films" (datasheet PDF, characteristic curves)
- Kodak, "Processing Steps — Processing Kodachrome Film" (Z-50 manual)
- Wilhelm Imaging Research, "The Permanence and Care of Color Photographs"
- Lane, William S. (2005), "Process K-14, Kodachrome Films, Marketing Technical Support"
- Penichon, Sylvie (2013), "Twentieth Century Colour Photographs"
