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

## What is Resampling in Images?

Resampling is the process of changing the size of an image, either by increasing (upscaling) or decreasing (downscaling) its dimensions.

- **Upscaling**: Making an image larger by adding pixels.
- **Downscaling**: Making an image smaller by removing pixels.

When resizing an image, we need to estimate the new pixel values based on the original ones. This estimation is called **resampling**.


Let me break it down step by step for better understanding:

What is Resampling in Images?
Resampling is the process of changing the size of an image, either by increasing (upscaling) or decreasing (downscaling) its dimensions.

Upscaling: Making an image larger by adding pixels.
Downscaling: Making an image smaller by removing pixels.
When resizing an image, we need to estimate the new pixel values based on the original ones. This estimation is called resampling.

### Why is Resampling Important?
If resampling isn't done carefully, the resized image might look distorted, blurry, or pixelated. The goal of resampling is to maintain the image's quality as much as possible by reducing artifacts (undesirable visual effects like jagged edges or blurriness).

Image.Resampling.LANCZOS is one of the resampling methods provided by the Pillow library in Python. It uses the Lanczos filter, a high-quality algorithm for resizing images, especially when downscaling (reducing size).

Why Use LANCZOS? - It ensures that when the image is resized to fit your ASCII art dimensions, the visual quality is preserved, so the ASCII art accurately represents the original image.