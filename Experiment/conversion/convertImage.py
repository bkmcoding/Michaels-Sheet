from pdf2image import convert_from_path

images = convert_from_path('hw2.pdf')

for i, image in enumerate(images):
    image.save(f'page_{i+1}.jpg', 'JPEG')