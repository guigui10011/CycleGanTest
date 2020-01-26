from PIL import Image


# im = Image.open('/mnt/c/Users/guigu/Desktop/Projects/pytorch-CycleGAN-and-pix2pix/imgs/leonardo-da-vinci-1128923.jpg')
# im = im.crop((460, 1060, 4800, 1640))

im = Image.open('/mnt/c/Users/guigu/Desktop/Projects/pytorch-CycleGAN-and-pix2pix/imgs/icon-1971099.jpg')
print(im.size)
im = im.crop((50, 690, 9200, 2800))
im.save('/mnt/c/Users/guigu/Desktop/Projects/pytorch-CycleGAN-and-pix2pix/imgs/crop_2.jpg')

# (left, top, right, bottom)