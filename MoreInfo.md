# Learn More About Images and Pixels

## What is Grayscale - L mode?

Greyscale ("L" mode) is a mode in image processing where an image is represented using shades of gray, ranging from black to white. In this mode, each pixel of the image has a single intensity value, which represents the brightness of that pixel.

How "L" Mode Works in Python (Pillow)
"L" stands for Luminance.
In greyscale, each pixel's intensity is stored as an 8-bit value ranging from 0 to 255:
- 0 represents pure black.
- 255 represents pure white.
- Values in between represent varying shades of gray.

When an image is converted to "L" mode, color information (RGB or other formats) is discarded, and only brightness is retained.