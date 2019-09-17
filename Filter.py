from PIL import Image
import numpy as np

img = Image.open('pepe.png')
imgarr = np.array(img)

width, height = img.size
newimg = [[0 for x in range(width + 2)] for y in range(height + 2)]

for i in range(0, width):
    for j in range(0, height):
        temp = imgarr[i][j]
        newimg[i + 1][j + 1] = temp

print(newimg)
#output = Image.fromarray(imgarr, 'L')
#output.save("output.png")
