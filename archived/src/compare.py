from PIL import Image, ImageChops


img1 = Image.open(r'C:\Users\AVachev\Code\image_comparison\archived\resources\source_images\REF_Image.jpeg')
img2 = Image.open(r'C:\Users\AVachev\Code\image_comparison\task\IMAGE_2.png')

img1 = img1.convert('RGB')
img2 = img2.convert('RGB')

difference = ImageChops.difference(img1, img2)

if difference.getbbox():
    difference.save(r'C:\Users\AVachev\Code\image_comparison\archived\results\difference.png')
    difference.close()
else:
    print('Images are identical.')