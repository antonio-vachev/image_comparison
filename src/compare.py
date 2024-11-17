from PIL import Image, ImageChops


img1 = Image.open('../resources/source_images/IMAGE_1.png')
img2 = Image.open('../resources/source_images/IMAGE_2.png')

difference = ImageChops.difference(img1, img2)

if difference.getbbox():
    difference.save('../results/difference.png')
    difference.show()
    difference.close()