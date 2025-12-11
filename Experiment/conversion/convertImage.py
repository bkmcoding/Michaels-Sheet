from pdf2image import convert_from_path

# Replace 'example.pdf' with the path to your PDF file
images = convert_from_path('hw2.pdf')

# You can now iterate through the 'images' list to access each page as a PIL Image object
for i, image in enumerate(images):
    # Save each page as an image file (e.g., JPEG)
    image.save(f'page_{i+1}.jpg', 'JPEG')