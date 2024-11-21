from PIL import Image, ImageChops


img1 = Image.open(r'C:\Users\user\Code\image_comparison\tests\20241120_161444\resources\IMAGE_2.png')
img2 = Image.open(r'C:\Users\user\Code\image_comparison\tests\20241120_161444\resources\REF_Image.jpeg')

img1 = img1.convert('RGB')
img2 = img2.convert('RGB')

difference = ImageChops.difference(img1, img2)

if difference.getbbox():
    difference.save(r'differences.png')
    difference.show()
    difference.close()
else:
    print('Images are identical.')