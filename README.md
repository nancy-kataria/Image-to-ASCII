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
pyhton3 main.py path-to-file maximum-height char-width-to-height-ratio
```

Sample Command:

```bash
pyhton3 main.py piplup.png 40 2.5
```

### Sample Output:

<img width="810" alt="Screenshot 2024-12-18 at 11 09 19 PM" src="https://github.com/user-attachments/assets/c1f10d8e-d6d4-4d1b-8a9e-28b58875ab6d" />
