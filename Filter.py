from PIL import Image
import numpy as np

# Opens the image and sets its pixel data to an array.
img = Image.open('pepe.png') 
imgarr = np.array(img)

# Filter that will be applied to the image.
kernel = [[-1, -1, -1],
          [-1, 8, -1],
          [-1, -1, -1]]
size = sum(len(x) for x in kernel)

# Initializes a temperary array and the output array.
width, height = imgarr.shape
tmpArr = np.array([[0 for x in range(height + 2)] for y in range(width + 2)]).astype('int8') # Adds bordering 0's to prevent black border
outArr = np.array([[0 for x in range(height)] for y in range(width)]).astype('int8')

# Adds the pixel data to the temperary array.
for i in range(0, width):
    for j in range(0, height):
        temp = imgarr[i][j]
        tmpArr[i + 1][j + 1] = temp

for i in range(0, width):
    for j in range(0, height):
        outArr[i][j] = (kernel[0][0] * tmpArr[i][j]) + (kernel[0][1] * tmpArr[i][j + 1]) + (kernel[0][2] * tmpArr[i][j + 2]) + \
                       (kernel[1][0] * tmpArr[i + 1][j]) + (kernel[1][1] * tmpArr[i + 1][j + 1]) + (kernel[1][2] * tmpArr[i + 1][j + 2]) + \
                       (kernel[2][0] * tmpArr[i + 2][j]) + (kernel[2][1] * tmpArr[i + 2][j + 1]) + (kernel[2][2] * tmpArr[i + 2][j + 2])

output = Image.fromarray(np.asarray(outArr))
output.save("output.png")
