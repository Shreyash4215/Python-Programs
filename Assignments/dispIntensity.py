from PIL import Image

# Open an image file
image_path = 'T:/TajMahal.jpg'
img = Image.open(image_path)

# Get the intensity value at (10, 10)
pixel_value = img.getpixel((10, 10))

print(f"Intensity value at (10, 10): {pixel_value}")
