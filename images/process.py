import os
from PIL import Image

# Define input and output directories
input_folder = "slideshow (full)"
output_folder = "slideshow"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".jpg"):  # Specifically targeting JPEG files
        # Open the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Ensure the image is in RGB mode
        img = img.convert("RGB")
        
        # Get the image size
        width, height = img.size
        
        # Initialize vertical bounding box coordinates
        min_y, max_y = height, 0
        
        # Find the top and bottom boundaries of non-white pixels
        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))
                # If the pixel is not white (non-background)
                if pixel != (255, 255, 255):  # Check RGB values
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)
        
        # Check if a valid vertical range was found
        if min_y < max_y:
            # Crop the image to the vertical bounding box, keeping full width
            cropped = img.crop((0, min_y, width, max_y + 1))
            
            # Save the cropped image to the output folder with maximum quality
            output_path = os.path.join(output_folder, filename)
            cropped.save(output_path, "JPEG", quality=100, optimize=True, progressive=True)
            print(f"Cropped top and bottom for: {filename}")
        else:
            print(f"No non-background pixels found in: {filename}")

