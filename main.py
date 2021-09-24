from pdf2image import convert_from_path

images = convert_from_path('sample.pdf')

for i in range(len(images)):
    images[i].save(f'page{i}.png', 'PNG')
