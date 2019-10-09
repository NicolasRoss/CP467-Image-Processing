from PIL import Image
import numpy as np

# Checks to see if the pixel is white
def isBackground(pixel):
    if (pixel == 255):
        return True

    return False

# Loops through the image array to find connected regions
def connectedComponents(imgarr):
    comp = 1

    height, width = imgarr.shape
    for i in range(0, height):
        for j in range(0, width):
            if not (isBackground(imgarr[i][j])):
                if i == 0 and j == 0:
                    # checks if first pixel is black 
                    imgarr[i][j] = comp
                
                elif i == 0 and not isBackground(imgarr[i][j - 1]):
                    # checks if pixels in first row are black and connected
                    imgarr[i][j] = imgarr[i][j - 1]

                elif i == 0 and isBackground(imgarr[i][j - 1]): 
                    comp += 1
                    imgarr[i][j] = comp

                elif j == 0 and not isBackground(imgarr[i - 1][j]):
                    # checks if pixels in first col are black and connected
                    imgarr[i][j] = imgarr[i - 1][j]
                
                elif j == 0 and not isBackground(imgarr[i - 1][j + 1]):
                        imgarr[i][j] = imgarr[i - 1][j + 1]

                elif j == 0 and isBackground(imgarr[i - 1][j]):
                    comp += 1
                    imgarr[i][j] = comp

                if i != 0 and j != 0:
                    # checks if pixels are connected and black
                    up = imgarr[i - 1][j]
                    left = imgarr[i][j - 1]
                    upleft = imgarr[i - 1][j - 1]

                    if j < width - 1:
                        upright = imgarr[i - 1][j + 1]
                        
                        if not isBackground(upleft) and isBackground(upright):
                            imgarr[i][j] = upleft
                        
                        elif isBackground(upleft) and not isBackground(upright):
                            imgarr[i][j] = upright

                        elif not isBackground(upleft) and not isBackground(upright):
                            imgarr[i][j] = upright if upright < upleft else upleft
                        
                        elif isBackground(left) and isBackground(up) and isBackground(upleft) and isBackground(upright):
                            comp += 1
                            imgarr[i][j] = comp

                    elif j == (width - 1):
                        if not isBackground(upleft):
                            imgarr[i][j] = upleft

                        elif isBackground(left) and isBackground(up) and isBackground(upleft):
                            comp += 1
                            imgarr[i][j] = comp
                        
                        
                    if not isBackground(left) and isBackground(up):
                        imgarr[i][j] = left
                    
                    elif isBackground(left) and not isBackground(up):
                        imgarr[i][j] = up

                    elif not isBackground(left) and not isBackground(up):
                        imgarr[i][j] = left if left < up else up

                
    return imgarr, comp

def updateComponents(imgarr):
    height, width = imgarr.shape
    for i in range(height):
        for j in range(width):
            if not (isBackground(imgarr[i][j])):
                if i != (height - 1) and j != 0:
                    downleft = imgarr[i + 1][j - 1]
                    down = imgarr[i + 1][j]

                    if not isBackground(down):
                        imgarr[i][j] = down if down < imgarr[i][j] else imgarr[i][j]

                    if not isBackground(downleft):
                        imgarr[i][j] = downleft if downleft < imgarr[i][j] else imgarr[i][j]

    return imgarr

def countComponents(imgarr, comp):
    count = [0] * comp
    height, width = imgarr.shape
    for i in range(height):
        for j in range(width):
            pixel = imgarr[i][j]

            if not isBackground(pixel):
                count[pixel - 1] += 1
    
    return count

## main ##
# Opens the image and sets its pixel data to an array.
# img = Image.open('output.png').convert('L')
# imgarr = np.array(img)
imgarr = np.array([[  0,   0,   0,   0,   0,   0],
                   [  0, 255, 255, 255, 255,   0],
                   [  0, 255,   0, 255, 255,   0],
                   [  0, 255, 255,   0, 255,   0],
                   [  0, 255, 255, 255,   0,   0],
                   [  0,   0,   0,   0,   0,   0]])
imgarr, comp = connectedComponents(imgarr)
# imgarr = updateComponents(imgarr)
count= countComponents(imgarr, comp)
print(imgarr)
comp = 0
for num in count:
    if num > 0:
        comp += 1
        print("Component: {} Number of black pixels: {}".format(comp, num))
