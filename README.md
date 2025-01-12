# Image to ASCII Art

This Python script converts an image into ASCII art by representing the image using characters instead of pixels. It uses the brightness of each pixel to map it to a corresponding character from a predefined greyscale palette, where lighter characters represent bright pixels and darker characters represent dark pixels.

## Features

- Converts an image (only JPG, PNG) into ASCII art.
- Customizes the size of the ASCII art output by setting the maximum height and the character width-to-height ratio.
- Saves the generated ASCII art as a `.txt` file.

## Requirements

- Python 3.x
- Pillow library (for image processing)

### Install Dependencies

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Running the script

Use Command:

```bash
python3 main.py path-to-file maximum-height char-width-to-height-ratio
```

Sample Command:

```bash
python3 main.py piplup.png 40 2.5
```

## Steps to get an ASCII Image

### 1. Defining Grayscale Mapping
Define the characters to represent brightness levels in the image. " -.':rLIVRQ" - Lighter characters (e.g., space " ") represent bright areas, while darker characters (e.g., "Q") represent dark areas.

### 2. Converting Image to Grayscale
Convert image to greyscale ("L" mode), where pixel values range from 0 (black) to 255 (white).

### 3. Calculating Aspect Ratio
Adjust the width based on the height of the ASCII art and the character width to height ratio. This ensures the resized image matches the proportions of the original image when converted to ASCII.

### 4. Resizing Image
Apply high-quality resampling to reduce image artifacts during resizing.

### 5. Generate ASCII Art
Replace each pixel with a character.

### 6. Save to .txt file
Create a new text file with the same name as the input image but with a .txt extension and write the generated ASCII art to the file.

### Sample Output:

<img width="810" alt="Screenshot 2024-12-18 at 11 09 19 PM" src="https://github.com/user-attachments/assets/c1f10d8e-d6d4-4d1b-8a9e-28b58875ab6d" />

Learn More about Images and its conversion to ASCII from the file **MoreInfo.md**
