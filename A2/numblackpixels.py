from PIL import Image
import numpy as np

# Checks to see if the pixel is white
def isBackground(pixel):
    if (pixel == 255):
        return True

    return False

# Loops through the image array to find connected regions
def connectedComponents(imgarr):
    equivList = [0]
    count = 0

    height, width = imgarr.shape
    for i in range(0, height):
        for j in range(0, width):
            if not (isBackground(imgarr[i][j])):
                if (i != 0 and j != 0):
                    # check up and left
                    up = imgarr[i - 1][j]
                    left = imgarr[i][j - 1]

                    if(isBackground(up) and isBackground(left)):
                        count += 1
                        equivList.append(count)
                    
                    elif (not isBackground(up) and not isBackground(left)):
                        index = up if up > left else left
                        equivList[index] = up if up < left else left

                elif (i == 0 and j == 0):
                    # checks if the first pixel is black
                    pixel = imgarr[i][j]

                    if (not isBackground(pixel)):
                        count += 1
                        equivList.append(count)

                elif (i != 0):
                    # check up
                    up = imgarr[i - 1][j]
                    
                    if (isBackground(up)):
                        count += 1
                        equivList.append(count)
                     
                elif (j != 0):
                    # check left
                    left = imgarr[i][j - 1]

                    if (isBackground(left)):
                        count += 1
                        equivList.append(count)
                    
                imgarr[i][j] = equivList[count]
                
    return imgarr, equivList

def updateComponents(imgarr, equivList):
    height, width = imgarr.shape
    for i in range(0, height):
        for j in range(0, width):
            pixel = imgarr[i][j]

            if (pixel != 255 and pixel > equivList[pixel]):
                imgarr[i][j] = equivList[pixel]
    
    return imgarr

def countBlackPixels(imgarr, equivList):
    count = [0]
    for _ in range(1, len(equivList)):
        count.append(0)

    height, width = imgarr.shape
    for i in range(0, height):
        for j in range(0, width):
            if (imgarr[i][j] != 255 and imgarr[i][j] != 0):
                count[imgarr[i][j]] += 1
        
    return count

## main ##
# Opens the image and sets its pixel data to an array.
img = Image.open('output.png').convert('L')
imgarr = np.array(img)

imgarr, equivList = connectedComponents(imgarr)

height, width = imgarr.shape
f = open("test.txt", "w+")
for i in range(height):
    for j in range(width):
        f.write("{0:0=3d}, ".format(imgarr[i][j]))
    f.write("\n")
    
imgarr = updateComponents(imgarr, equivList)
pixelCount = countBlackPixels(imgarr, equivList)

group = 1
for i in range(len(pixelCount)):
    if (pixelCount[i] > 0):
        print("Connected Region: {} Pixel Count: {}".format(group, pixelCount[i]))
        group += 1