from PIL import Image
import numpy as np
import sys

def isWhite(imgarr, i , j):
    return imgarr[i][j] == 255

def inBounds(imgarr, i , j):
    return i >= 0 and j >= 0 and i < len(imgarr) and j < len(imgarr[i])

def countComponents(imgarr):
    height, width = imgarr.shape
    equivList = [0]
    for i in range(height):
        for j in range(width):
            if not isWhite(imgarr, i, j):
                up = imgarr[i - 1][j]
                left = imgarr[i][j - 1]
                upleft = imgarr[i - 1][j - 1]

                # surrounding pixels are inbounds
                if inBounds(imgarr, i - 1, j) and inBounds(imgarr, i, j - 1) and inBounds(imgarr, i - 1, j - 1):
                    # if surrounding pixels black
                    if not isWhite(imgarr, i - 1, j) and not isWhite(imgarr, i, j - 1) and not isWhite(imgarr, i - 1, j - 1):
                        imgarr[i][j] = min(up, min(left, upleft))
                    # if upper-left and upper pixel black
                    elif not isWhite(imgarr, i - 1, j) and isWhite(imgarr, i, j - 1) and not isWhite(imgarr, i - 1, j - 1):
                        imgarr[i][j] = min(up, upleft)
                    # if left and upper-left pixel black
                    elif isWhite(imgarr, i - 1, j) and not isWhite(imgarr, i, j - 1) and not isWhite(imgarr, i - 1, j - 1):
                        imgarr[i][j] = min(left, upleft)
                    # if left and upper pixel black
                    elif not isWhite(imgarr, i - 1, j) and not isWhite(imgarr, i, j - 1) and isWhite(imgarr, i - 1, j - 1):
                        minP = min(left, up)
                        maxP = max(left, up)
                        imgarr[i][j] = minP
                        equivList[maxP] = equivList[minP] if equivList[minP] < equivList[maxP] else equivList[maxP]

                    # if upper-left pixel black
                    elif isWhite(imgarr, i - 1, j) and isWhite(imgarr, i, j - 1) and not isWhite(imgarr, i - 1, j - 1):
                        imgarr[i][j] = upleft
                    # if left pixel black
                    elif isWhite(imgarr, i - 1, j) and not isWhite(imgarr, i, j - 1) and isWhite(imgarr, i - 1, j - 1):
                        imgarr[i][j] = left
                    # if upper pixel black
                    elif not isWhite(imgarr, i - 1, j) and isWhite(imgarr, i, j - 1) and isWhite(imgarr, i - 1, j - 1):
                        imgarr[i][j] = up
                    # if none are black
                    elif isWhite(imgarr, i - 1, j) and isWhite(imgarr, i, j - 1) and isWhite(imgarr, i - 1, j - 1):
                        equivList.append(len(equivList))
                        imgarr[i][j] = len(equivList) - 1
                # upper pixels not in bounds
                elif not inBounds(imgarr, i - 1, j) and inBounds(imgarr, i, j - 1) and not inBounds(imgarr, i - 1, j - 1):
                    # if left pixel black
                    if not isWhite(imgarr, i, j - 1):
                        imgarr[i][j] = left
                    # if left pixel white
                    elif isWhite(imgarr, i, j - 1):
                        equivList.append(len(equivList))
                        imgarr[i][j] = len(equivList) - 1
                # left pixels not in bounds
                elif inBounds(imgarr, i - 1, j) and not inBounds(imgarr, i, j - 1) and not inBounds(imgarr, i - 1, j - 1):
                    # if upper pixel black
                    if not isWhite(imgarr, i - 1, j):
                        imgarr[i][j] = up
                    # if upper pixel white
                    elif isWhite(imgarr, i - 1, j):
                        equivList.append(len(equivList))
                        imgarr[i][j] = len(equivList) - 1
                # no pixels are in bounds
                elif not inBounds(imgarr, i - 1, j) and not inBounds(imgarr, i, j - 1) and not inBounds(imgarr, i - 1, j - 1):
                    #if pixel is black
                    equivList.append(len(equivList))
                    imgarr[i][j] = len(equivList) - 1
  
            elif isWhite(imgarr, i , j):
                if not isWhite(imgarr, i - 1, j) and not isWhite(imgarr, i, j - 1):
                    minP = min(imgarr[i - 1][j], imgarr[i][j - 1])
                    maxP = max(imgarr[i - 1][j], imgarr[i][j - 1])
                    equivList[minP] = min(equivList[minP], equivList[maxP])

    return imgarr, equivList

def updateComp(imgarr, equivList):
    height, width = imgarr.shape
    for i in range(height):
        for j in range(width):
            pixel = imgarr[i][j]

            if not isWhite(imgarr, i , j) and pixel > equivList[pixel]:
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

def main():
    # Opens the image and sets its pixel data to an array.
    img = Image.open('output.png').convert('L')
    imgarr = np.array(img)
    # imgarr = np.array([[255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
    #                    [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
    #                    [255, 255, 255, 255, 255, 255,   0,   0,   0, 255],
    #                    [255, 255, 255, 255, 255, 255,   0,   0,   0,   0],
    #                    [255, 255, 255, 255,   0,   0,   0, 255,   0,   0],
    #                    [255,   0, 255, 255,   0,   0, 255, 255,   0, 255],
    #                    [255, 255,   0, 255,   0, 255,   0, 255, 255, 255],
    #                    [255, 255, 255,   0,   0, 255, 255, 255, 255, 255],
    #                    [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
    #                    [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]])
    
    imgarr, equivList = countComponents(imgarr)
    imgarr = updateComp(imgarr, equivList)
    count = countBlackPixels(imgarr, equivList)
    f = open("test.txt", "w+")
    height, width = imgarr.shape
    for i in range(height):
        for j in range(width):
            f.write("{0:0=3d}, ".format(imgarr[i][j]))
        f.write("\n")
    
    print(equivList)
    group = 1
    for i in range(len(count)):
        if (count[i] > 0):
            print("Connected Region: {} Pixel Count: {}".format(group, count[i]))
            group += 1 

if __name__ == "__main__":
    main()
