# The comments and explanations here are for my own reference

# PIL is used for image processing
# The Image module allows loading, manipulating, and saving images.
from PIL import Image
import argparse

# Defining the characters used to represent brightness levels in the image
GREYSCALE = list("QRVILr:'.- ")  # 11 tonal ranges of 24 pixels each
# recent changes made : changed " -.':rLIVRQ" to "QRVILr:'.- " reversed it, so that black color is highlighted most. Creating an inverted image

# image file - path to image file
# max height - height of the ASCII art (in rows of characters, specified by the user.)
# char_width_height_ratio - since characters are not square, this compensates for their shape
def image_to_ascii(image_file, max_height, char_width_height_ratio):
    try:
        # Open and convert the image to greyscale
        img = Image.open(image_file).convert("L")
    except Exception as e:
        print(f"Error opening image file: {e}")
        return
    
    # Resize the image while maintaining the aspect ratio

    # Extracts the original dimensions, used to calculate the new size that will preserve the aspect ratio.
    width, height = img.size
    # Calculating the new width of the image in characters.
    new_width = int(width / height * max_height * char_width_height_ratio)
    new_size = (new_width, max_height)
    # using the Lanczos filter, a high-quality algorithm for resizing images, especially when downscaling (reducing size)
    img = img.resize(new_size, Image.Resampling.LANCZOS)

    # Generate ASCII art
    ascii_art = ""

    # for every row, print all columns
    for y in range(img.height):
        for x in range(img.width):
            # calculating the brightness (luminance) of the pixel at position (x, y).
            # getPixel(x,y) - Retrieves the greyscale brightness value of the pixel, ranges 0-255
            lum = 255 - img.getpixel((x, y))

            # Mapping the luminance to a character in the GREYSCALE list

            # we have 11 grayscale characters, each character repreesents a range of 256 / 11 ≈ 23 brightness levels
            ascii_art += GREYSCALE[min(lum // (256 // len(GREYSCALE)), len(GREYSCALE) - 1)]

        # move to next row
        ascii_art += "\n"

    # Save ASCII art to a file
    output_file = image_file.rsplit(".", 1)[0] + ".txt"
    try:
        with open(output_file, "w") as file:
            file.write(ascii_art)
        print(f"ASCII art saved to {output_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    # Describing the script and defining the command-line arguments
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("image_file", help="Path to the input image file.")
    parser.add_argument("max_height", type=int, help="Maximum height of the ASCII art in characters.")
    parser.add_argument("char_width_height_ratio", type=float, help="Width-to-height ratio of a character.")
    args = parser.parse_args()

    image_to_ascii(args.image_file, args.max_height, args.char_width_height_ratio)
