from PIL import Image

# Open an image file
image_path = 'T:/TajMahal.jpg'
img = Image.open(image_path)

# Convert to grayscale
gray_img = img.convert('L')

# Save the grayscale image
gray_img.save('T:/gray_image.jpg')

# Apply a threshold for black and white conversion
threshold = 128  
bw_img = gray_img.point(lambda x: 0 if x < threshold else 255, '1')

# Save the black and white image
bw_img.save('T:/bw_image.jpg')
