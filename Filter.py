from PIL import Image
import numpy as np

# Opens the image and sets its pixel data to an array.
img = Image.open('pepe.png') 
imgarr = np.array(img)

# Initializes a temperary array with bordering 0's to prevent a black border.
width, height = img.size
tmpArr = [[0 for x in range(width + 2)] for y in range(height + 2)]

# Adds the pixel data to the temperary array.
##### Doesn't work yet #####
for i in range(0, width):
    for j in range(0, height):
        temp = imgarr[i][j]
        tmpArr[i + 1][j + 1] = temp

#output = Image.fromarray(imgarr, 'L')
#output.save("output.png")
