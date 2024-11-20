from PIL import Image


def process_and_overlay(image1_path, image2_path, output_path):
    """
    Processes two images and overlays the second on top of the first.

    Args:
        image1_path: Path to the first image.
        image2_path: Path to the second image.
        output_path: Path to save the output image.
    """

    # Open the images
    image1 = Image.open(image1_path).convert("L")  # Convert to grayscale
    image2 = Image.open(image2_path).convert("RGBA")  # Convert to RGBA for transparency

    # Resize image2 to match image1 (optional, adjust as needed)
    image2 = image2.resize(image1.size)

    # Apply red filter and 50% transparency to image2
    pixels = image2.load()
    black_range = [0, 1]

    # Run through each pixel
    for x in range(image2.width):
        for y in range(image2.height):
            r, g, b, a = pixels[x, y]
            # Check if in black range meaning no difference to original image
            if r not in black_range or g not in black_range or b not in black_range:
                pixels[x, y] = (255, 0, 0, 255)  # Red color to pixels that show difference
            else:  # If pixel is black
                pixels[x, y] = (r, g, b, 0)  # Set alpha to 0 (transparent) for identical pixels

    # Create a new Image with the same size as image1
    output_image = Image.new("RGBA", image1.size)

    # Paste image1 onto the output image
    output_image.paste(image1)

    # Paste image2 (with transparency) onto the output image
    output_image.paste(image2, (0, 0), image2)

    # Save the output image
    output_image.save(output_path)


if __name__ == "__main__":
    # Example usage:
    image1_path = '../resources/source_images/IMAGE_1.png'
    image2_path = '../results/difference.png'
    output_path = '../results/overlay_image.png'
    process_and_overlay(image1_path, image2_path, output_path)