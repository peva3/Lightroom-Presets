# Split-Toning and Color Grading Wheel Theory

**Source:** Synthesized from Wikipedia Color Grading, Color Theory, and Color Balance articles, plus ACESCentral LMT documentation

**Last Updated:** June 2026

---

## What is Split-Toning?

Split-toning (also called color grading or three-way color correction) is the technique of applying different color tints to the shadows, midtones, and highlights of an image independently. It originated in darkroom photography where chemical toners (sepia, selenium, gold) would differentially affect silver densities in prints.

In digital imaging, split-toning is implemented via:
- **Lift/Gamma/Gain controls** with hue wheels (DaVinci Resolve, Baselight)
- **Color Grading panel** in Lightroom (shadows, midtones, highlights with hue + saturation)
- **Three-way color corrector** in Premiere Pro, Final Cut
- **Curves** applied per-channel to specific tonal ranges

---

## The Three-Way Paradigm

The professional color grading paradigm divides the tonal range into three regions:

### Lift (Shadows / Offset)
- Controls the darkest parts of the image
- Raising lift brings up the black point
- Adding hue shifts the entire shadow region
- Most commonly pushed toward cool (blue/teal) for the Hollywood look

### Gamma (Midtones)
- Controls the middle brightness range
- Most critical for overall color perception
- Where main color balancing happens
- Adding hue here affects the dominant color cast of the image

### Gain (Highlights)
- Controls the brightest parts of the image
- Adjusts the white point
- Commonly pushed toward warm (orange/yellow) to complement cool shadows
- Overly aggressive gain adjustments can clip highlights

### Offset (Global)
- Shifts the entire image equally
- Quick way to adjust overall color balance
- Less precise but useful for matching shots

---

## The Color Grading Wheels

### How Wheels Work

Each wheel represents hue on a circle (0-360°) and saturation as distance from center. User picks:
1. A hue angle (the direction on the wheel)
2. A saturation strength (how far from center)
3. A balance control (adjusts the boundary between shadow-mid and mid-highlight)

### Common Wheel Strategies

**Complementary Split (Orange/Teal)**
- Shadows: Teal/Cyan (180-210°)
- Midtones: Neutral or warm-leaning
- Highlights: Warm/Orange (25-45°)
- Why it works: Skin tones in mids, color contrast between warm highlights and cool shadows creates depth

**Analogous Toning (Warm)**
- Shadows: Warm brown/amber
- Midtones: Golden yellow
- Highlights: Light cream/warm white
- Effect: Vintage, nostalgic, sunset feel

**Cool Monochrome**
- Shadows: Deep blue
- Midtones: Slightly cool, neutral
- Highlights: Cool cyan or white
- Effect: Clinical, modern, dystopian, winter

**Cross-Processed Look**
- Shadows: Green/teal
- Midtones: Yellow-green shift
- Highlights: Magenta/purple
- Effect: Emulates E-6 film processed in C-41 chemistry

---

## Split-Toning Color Theory

### Complementary Harmony in Grading

The most powerful split-tone combinations use complementary or near-complementary colors:

| Shadow Hue | Highlight Hue | Emotional Effect |
|---|---|---|
| Teal (180°) | Orange (30°) | Cinematic, dramatic, blockbuster |
| Blue (240°) | Yellow (60°) | Balance, natural contrast |
| Purple (270°) | Gold (45°) | Regal, warm luxury |
| Cyan (195°) | Red (0°) | Aggressive, intense |
| Green (120°) | Magenta (300°) | Unnatural, surreal |
| Navy (225°) | Amber (35°) | Moody, introspective |

### The Opponent Process Connection

The human visual system processes color through opponent channels:
- **Red vs. Green** (L-M cone opponent)
- **Blue vs. Yellow** (S - (L+M) cone opponent)

Split-toning that aligns with these opponent channels creates natural perceptual contrast. This is why orange/teal (a blue/yellow opponent pair modified) feels so effective — it directly engages the visual system's contrast mechanisms.

---

## Luminance-Based Color Grading

### Controlling Saturation by Luminance

In addition to hue-based toning, sophisticated grading controls color intensity by brightness level:
- **Shadow desaturation**: Reducing color in shadows (common in film emulation)
- **Highlight color preservation**: Keeping strong colors in midtones
- **Specular desaturation**: Removing color from the brightest specular highlights

This approximates film behavior where:
- Dense (dark) areas lose chroma
- Midtones carry the saturation
- Extreme highlights blow out to white

### The Saturation-Luminance Curve

A typical film-like saturation distribution:
- 0-10% luminance: Very low saturation (near black, no color)
- 10-25% luminance: Rising but subdued saturation
- 25-65% luminance: Peak saturation zone
- 65-90% luminance: Declining saturation
- 90-100% luminance: Very low saturation (near white)

---

## Practical Split-Toning in Lightroom

### Color Grading Panel (Lightroom v10+)

The three-wheel Color Grading panel replaces the old Split Toning panel:
- **Shadows wheel**: Independent hue + saturation control
- **Midtones wheel**: Added in v10 (previously not available)
- **Highlights wheel**: Independent hue + saturation control
- **Blending slider**: Controls overlap between shadow/midtone and midtone/highlight
- **Balance slider**: Shifts the midpoint boundary between shadow and highlight dominance

### Luminance Slider (Each Wheel)

Each wheel has a luminance slider that brightens or darkens that tonal region. This is distinct from the hue/saturation:
- Negative luminance: Darkens that tonal range
- Positive luminance: Brightens that tonal range

### Global Wheel

A fourth control applies a uniform color tint across the entire image. Useful as a base cast before split-toning.

---

## Common Split-Toning Formulas

### Cinematic Teal and Orange
```
Shadows: Hue 210° (Teal), Sat 15-25
Midtones: Hue 35° (Warm), Sat 5-10
Highlights: Hue 40° (Orange), Sat 10-20
Blending: 60-70 (smoother transitions)
Balance: -10 to +10 (depending on exposure)
```

### Vintage Fade
```
Shadows: Hue 30° (Brown), Sat 10-15, Lum -20
Midtones: Hue 50° (Yellow), Sat 5-10
Highlights: Hue 45° (Gold), Sat 5-10, Lum +10
Blending: 80 (very smooth)
```

### Moody Blue Hour
```
Shadows: Hue 220° (Blue), Sat 20-30, Lum -30
Midtones: Hue 210° (Cool), Sat 5-10
Highlights: Hue 230° (Blue), Sat 10-15
Blending: 50
```

### Cross-Processed E6→C41
```
Shadows: Hue 160° (Green-Cyan), Sat 20-30
Midtones: Hue 70° (Yellow-Green), Sat 15-20
Highlights: Hue 320° (Magenta), Sat 15-25
Blending: 40 (sharper transitions for contrasty cross-process look)
```

---

## Split-Toning vs. Color Grading Wheels: Distinctions

### Traditional Split-Toning
- Only shadows and highlights (2-way)
- No midtone control
- Simpler, more limited palette
- Found in older software (Lightroom pre-v10, basic photo editors)

### Three-Way Color Grading
- Shadows + Midtones + Highlights (3-way)
- Full midtone control enables more nuanced looks
- Each wheel has hue, saturation, and luminance
- Blending and balance controls for smoothness
- Found in professional video tools (DaVinci Resolve, Baselight) and Lightroom v10+

---

## Pitfalls in Split-Toning

1. **Over-saturation of split tones**: Keep saturation values modest (5-30 range is usually sufficient)
2. **Competing with HSL adjustments**: If you've already desaturated blues for a film look, adding blue to shadows creates mud
3. **Skin tone contamination**: Midtone wheel affects skin — be very careful with saturation here
4. **Banding**: Extreme split-toning on 8-bit images can cause visible banding; work in 16-bit
5. **Complementary overload**: Maximum complementary contrast can feel garish; near-complements often work better
6. **Luminance mismatch**: Don't brighten shadows and darken highlights simultaneously — this fights the natural contrast of the image
7. **Color mixing in blend zones**: The transition areas between shadow-midtone and midtone-highlight are where hues mix; check these carefully

---

## Implications for XMP Preset Design

1. **Color Grading panel is safer than HSL**: HSL can nuke entire color channels at extreme values; Color Grading applies gentler, controlled tints
2. **Combine with tone curve for film looks**: Tone curve sets the contrast structure; split-toning adds the color mood
3. **Keep split-tone saturation modest**: Values above 25-30 often look artificial in still photography
4. **Midtone wheel is powerful but dangerous**: A small midtone shift affects the entire image's color cast
5. **Blending 50-70 looks natural**: Lower blending values create more dramatic, stylized transitions; higher values look more organic
6. **Test on diverse images**: A split-tone preset that works on portraits may fail on landscapes where there's no warm skin to balance
7. **The original working presets were smart about this**: They used minimal split-toning — just enough to establish mood without overwhelming the image
