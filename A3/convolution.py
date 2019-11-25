import numpy as np
from PIL import Image, ImageFilter

def addBorder(imgArr):
    width, height = imgArr.shape
    temp = np.array([[0 for x in range(height + 4)] for y in range(width + 4)]).astype('int8')
    
    for i in range(1, width-1):
        for j in range(1,height-1):
            t = imgArr[i][j]
            temp[i+1][j+1] = t
    return temp


def blur_vert(img, ker):
    newImg = img
    width, height = img.shape
    for i in range(len(width)):
        for j in range(len(height)):
            newImg[i][j] = 1



    return newImg


def blur_hor(img, ker):
    newImg = img
    width, height = img.shape

    return newImg

img = Image.open("rose.png")

kerHor = [0,0,0,1/3,1/3,1/3,0,0,0]
kerVert = [0,1/3,0,0,1/3,0,0,1/3,0]
kernelHor = ImageFilter.Kernel((3,3), kerHor)
kernelVert = ImageFilter.Kernel((3,3), kerVert)

for i in range(20):
    img = img.filter(kernelHor)

img2 = img
img2.show()
# img2.save("tapping.jpg")

imgArray = np.array(img)


# output = Image.fromarray(outArr, 'L')
# output.save("output.png")


