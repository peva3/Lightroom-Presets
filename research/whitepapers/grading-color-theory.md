# Color Theory for Image Editing: Contrast, Harmony, and Mood

**Sources:**
- Wikipedia - Color Theory (https://en.wikipedia.org/wiki/Color_theory) — Last edited 2026
- Wikipedia - Complementary Colors (https://en.wikipedia.org/wiki/Complementary_colors) — Last edited 2026
- Wikipedia - Color Balance (https://en.wikipedia.org/wiki/Color_balance)

**Authors:** Wikipedia contributors (synthesized from multiple articles)

---

## Color Theory Overview

Color theory is a historical body of knowledge describing the behavior of colors — namely in color mixing, color contrast effects, color harmony, color schemes and color symbolism. Traditional color theory tends to be more subjective and have artistic applications, while color science tends to be more objective and have functional applications.

Color theory dates back at least as far as Aristotle's treatise On Colors. A formalization of "color theory" began in the 18th century, initially within a partisan controversy over Isaac Newton's theory of color (Opticks, 1704).

---

## Complementary Colors

Complementary colors are pairs of colors which, when combined or mixed, cancel each other out (lose chroma) by producing a grayscale color like white or black. When two highly chromatic complementary colors are placed next to each other, they create a strong contrast.

### Which Pairs Are Complementary?

This depends on the color model:

**Modern Color Theory (RGB/CMY models):**
- Red ↔ Cyan
- Green ↔ Magenta
- Blue ↔ Yellow

**Traditional RYB Model (artists' color wheel):**
- Red ↔ Green
- Yellow ↔ Purple
- Blue ↔ Orange

**Opponent Process Theory:**
- Red–Green
- Blue–Yellow

### Historical Development

- **Isaac Newton (1704)**: Devised a circle showing a spectrum of seven colors, observing that colors opposite each other provided the greatest contrast
- **Benjamin Thompson, Count Rumford (1794)**: Coined the term "complement" to describe two colors that, when mixed, produce white
- **Johann Wolfgang von Goethe (1810)**: Presented his Theory of Colours, stating yellow and blue as the primary opposition (light vs. darkness)
- **Thomas Young (1802)**: Showed that white light could be created from just three colors: red, green, and blue
- **Hermann von Helmholtz**: Resolved the debate by showing additive colors (light) and subtractive colors (pigments) operate by different rules with different primary and complementary pairs

### Eugene Chevreul's Law of Color Contrast (1839)

Chevreul formalized three types of contrast:

1. **Simultaneous contrast**: Appears in two colors viewed side by side — each appears tinted with the complement of the other
2. **Successive contrast**: The afterimage left on an achromatic background after viewing a color
3. **Mixed contrast**: The afterimage left on another color

This is the theoretical foundation for why complementary color schemes (orange/teal, warm/cool) are so effective in color grading.

### Practical Application

In his 1839 book, Chevreul demonstrated scientifically that "the arrangement of complementary colors is superior to any other harmony of contrasts." His work was read by Impressionist painters like Monet, Renoir, and Van Gogh, who put it into practice.

Van Gogh wrote: "searching for oppositions of blue with orange, of red with green, of yellow with purple, searching for broken colors and neutral colors to harmonize the brutality of extremes."

---

## Color Contrast

### Warm vs. Cool Colors

The distinction between "warm" and "cool" colors has been important since at least the late 18th century. Warm colors are often said to be hues from red through yellow, browns and tans included; cool colors are often said to be the hues from blue-green through blue-violet.

**Perceptual effects:**
- Warm colors advance or appear more active in a painting
- Cool colors tend to recede
- In interior design or fashion, warm colors arouse or stimulate, while cool colors calm and relax

### Color Mixing Principles

**Additive mixing** (light, screens, RGB):
- Red + Green = Yellow
- Red + Blue = Magenta
- Green + Blue = Cyan
- All three at full = White

**Subtractive mixing** (pigments, inks, CMYK):
- Cyan + Magenta = Blue
- Cyan + Yellow = Green
- Magenta + Yellow = Red
- All three = Black/brown

### Tints and Shades

When mixing pigments, adding black produces shades, adding white produces tints. However, this can shift hue:
- Darkening yellow/orange/red with black shifts toward greenish/blue
- Lightening red/orange with white shifts toward blue

Better practice: darken by adding the complementary color (e.g., add purple to yellow), lighten by adding an adjacent warmer hue (e.g., add orange to red+white mix).

---

## Color Harmony and Color Schemes

Color harmony is a complex notion because human responses to color are both affective and cognitive. A modern conceptual model:

```
Color harmony = f(Col 1,2,3,…,n) × (ID + CE + CX + P + T)
```

Where factors include:
- **ID**: Individual differences (age, gender, personality, affective state)
- **CE**: Cultural experiences
- **CX**: Prevailing context (setting, ambient lighting)
- **P**: Intervening perceptual effects
- **T**: Effects of time (prevailing social trends)

### Color Scheme Types

1. **Monochromatic**: Single hue with varying saturation and brightness
2. **Analogous**: Colors adjacent on the color wheel (e.g., blue, blue-green, green)
3. **Complementary**: Colors opposite on the color wheel (e.g., orange and blue)
4. **Split-complementary**: A base color plus the two colors adjacent to its complement
5. **Triadic**: Three colors equally spaced on the color wheel
6. **Tetradic (Double Complementary)**: Two complementary pairs

### Black and White in Harmony

Black and white have long been known to combine well with almost any other colors:
- Black decreases the apparent saturation or brightness of colors paired with it
- White shows off all hues to equal effect

---

## Color Balance (White Balance)

In photography and image processing, color balance is the global adjustment of the intensities of the colors (typically red, green, and blue primary colors). An important goal is to render specific colors — particularly neutral colors like white or grey — correctly.

### Psychological Color Balance

Humans relate to flesh tones more critically than other colors. Trees, grass and sky can all be off without concern, but if human flesh tones are 'off' then the human subject can look sick or dead.

### Chromatic Colors

Color balancing an image affects not only the neutrals, but other colors as well. An image that is not color balanced is said to have a color cast, as everything in the image appears to have been shifted towards one color.

### Von Kries Chromatic Adaptation

Johannes von Kries proposed converting color to LMS color space (Long, Medium, Short wavelength cone responses) and scaling the three LMS values independently. A 3x3 matrix converts RGB or XYZ to LMS, then the three LMS primary values are scaled to balance the neutral; the color can then be converted back to the desired final color space.

The best-performing chromatic adaptation spaces include: Sharp, Bradford, CMCCAT, and ROMM.

---

## Implications for Preset Design

1. **Complementary contrast creates visual interest**: The orange/teal Hollywood look works because skin tones are orange, and teal is the complement
2. **Warm highlights + cool shadows** is a fundamental split-toning technique rooted in complementary color theory
3. **Avoid simultaneous contrast casualties**: When boosting one hue, consider how it makes adjacent hues appear
4. **Skin tones are sacred**: White balance shifts that fix a mood can ruin portraits; use secondary/HSL to protect skin
5. **Color harmony is contextual**: A preset that looks great on a sunset portrait may look terrible on an office interior
6. **Chevreul's principle**: Adjacent colors affect each other — a blue background makes orange skin appear more orange (boosting perceived saturation)
