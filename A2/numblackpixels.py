from PIL import Image
import numpy as np
import sys

def isWhite(imgarr, i , j):
    return inBounds(imgarr, i , j) and imgarr[i][j] == 255

def inBounds(imgarr, i , j):
    return i >= 0 and j >= 0 and i < len(imgarr) and j < len(imgarr[i])

def countRecursive(imgarr, visited, i, j, compCount):
    visited[i][j] = 1
    
    if not isWhite(imgarr, i, j):
        visited[i][j] += compCount
        # print(visited)
        for dI in range(-1, 2):
            for dJ in range(-1, 2):
                adjI = i + dI
                adjJ = j + dJ
                
                if inBounds(imgarr, adjI, adjJ) and not visited[adjI][adjJ]:
                    visited = countRecursive(imgarr, visited, adjI, adjJ, compCount)

    return visited

def countComponents(imgarr):
    compCount = 0
    height, width = imgarr.shape
    visited = [[0] * width for i in range(height)]
    
    for i in range(height):
        for j in range(width):
            if visited[i][j] < 1:
                if not isWhite(imgarr, i, j):
                    compCount += 1
                    visited = countRecursive(imgarr, visited, i, j, compCount)

                if visited[i][j] < 1:
                    visited[i][j] = 1
    
    return visited, compCount

def countBlackPixels(imgarr, compCount):
    count = [0] * compCount
    height = len(imgarr)
    width = len(imgarr[0])
    for i in range(height):
        for j in range(width):
            if imgarr[i][j] > 1:
                count[imgarr[i][j] - compCount] += 1

    return count

def main():
    # Opens the image and sets its pixel data to an array.
    # img = Image.open('output.png').convert('L')
    # imgarr = np.array(img)
    imgarr = np.array([[255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                       [255,   0, 255, 255,   0, 255, 255,   0, 255, 255],
                       [255, 255,   0,   0, 255, 255,   0,   0, 255, 255],
                       [255, 255, 255,   0, 255, 255, 255,   0, 255, 255],
                       [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                       [255,   0, 255, 255, 255, 255,   0, 255, 255, 255],
                       [255, 255,   0, 255, 255,   0,   0,   0, 255, 255],
                       [255, 255, 255,   0, 255, 255,   0, 255, 255, 255],
                       [255, 255, 255,   0, 255, 255,   0, 255,   0, 255],
                       [255, 255, 255, 255, 255, 255, 255, 255, 255,   0]])

    visited, compCount = countComponents(imgarr)
    count = countBlackPixels(visited, compCount)
    for i in range(len(visited)):
        print(visited[i])
    for i in range(len(count)):
        print("Component {} has {} black pixels.".format(i + 1, count[i]))

if __name__ == "__main__":
    main()