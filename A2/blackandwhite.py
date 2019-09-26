from PIL import Image
import numpy as np

# Opens the image and sets its pixel data to an array.
img = Image.open('rose.png').convert('L')
imgarr = np.array(img)

# Loops through the image array making each pixel black or white.
height, width = imgarr.shape
for i in range(0, height):
    for j in range(0, width):
        if (imgarr[i][j] <= 127):
            imgarr[i][j] = 0

        elif (imgarr[i][j] > 127):
            imgarr[i][j] = 255
    
output = Image.fromarray(imgarr, 'L')
output.save("output.png")
