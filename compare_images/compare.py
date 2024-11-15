from PIL import Image, ImageChops

img1 = Image.open(r'C:\Users\AVachev\Code\image_comparison\source_images\IMAGE_1.png')
img2 = Image.open(r'C:\Users\AVachev\Code\image_comparison\source_images\IMAGE_2.png')

difference = ImageChops.difference(img1, img2)

if difference.getbbox():
    difference.save(r'C:\Users\AVachev\Code\image_comparison\difference_images\difference.png')
    difference.show()