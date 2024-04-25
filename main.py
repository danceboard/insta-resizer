from PIL import Image, ImageFilter
import os

def resize_and_blur(image_path, output_directory):
    # Open the image
    original_image = Image.open(image_path)

    # Convert the image to RGB mode to remove alpha channel if present
    original_image = original_image.convert("RGB")

    # Resize the image to fit within 1080x1080 while maintaining aspect ratio
    original_image.thumbnail((1080, 1080))

    # Calculate the background image size to match the final image
    bg_width, bg_height = original_image.size

    # Create a blurred version of the image
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(10))

    # Create a new blank image with the same size as the resized image
    final_image = Image.new("RGB", (1080, 1080))

    # Resize the blurred image to match the final image size
    blurred_image = blurred_image.resize((1080, 1080))

    # Paste the blurred image onto the final image as the background
    final_image.paste(blurred_image, (0, 0))

    # Resize the original image to stretch the longer edge to full size
    if bg_width > bg_height:
        resized_original_image = original_image.resize((1080, int(1080 * bg_height / bg_width)))
    else:
        resized_original_image = original_image.resize((int(1080 * bg_width / bg_height), 1080))

    # Calculate the position to paste the resized original image at the center
    paste_x = (1080 - resized_original_image.width) // 2
    paste_y = (1080 - resized_original_image.height) // 2

    # Paste the resized original image onto the final image
    final_image.paste(resized_original_image, (paste_x, paste_y))

    # Save the final image in the output directory with the same name as input file, always as PNG
    output_path = os.path.join(output_directory, os.path.splitext(os.path.basename(image_path))[0] + ".png")
    final_image.save(output_path)

    return output_path

def process_images():
    input_directory = "./input"
    output_directory = "./output"

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Get a list of all files in the input directory
    image_files = [file for file in os.listdir(input_directory) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

    processed_files = []

    for image_file in image_files:
        image_path = os.path.join(input_directory, image_file)
        output_path = resize_and_blur(image_path, output_directory)
        processed_files.append((image_path, output_path))

    print("\nProcessed images:")
    for i, (input_path, output_path) in enumerate(processed_files, start=1):
        print(f"{i}. Input: {input_path} -> Output: {output_path}")

    print(f"\nTotal {len(processed_files)} images processed.")

if __name__ == "__main__":
    process_images()
