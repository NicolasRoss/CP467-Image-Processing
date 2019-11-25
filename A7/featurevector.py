import numpy as np
import cv2


def featureVector(imgname):
    #read image
    img = cv2.imread(imgname)
    #image to gray
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #cv2.imshow("gray",img)
    height, width, channels = img.shape

    #set vector variables
    region1,region2,region3,region4,region5,region6,region7,region8, region9 = 0,0,0,0,0,0,0,0,0
    #get x parameters
    incrementX = width//3
    block1x = width//3
    if (width%3) == 0:
        block1x -=1

    block2x = block1x+incrementX
    block3x = block2x+incrementX
    #get y parameters
    incrementY = height//3
    block1y = height//3
    if (height%3) == 0:
        block1y -=1
    block2y = block1y+incrementY
    block3y = block2y+incrementY

    #Set colors to 0 or 255

    for i in range(0, height):
        for j in range(0, width):
            if (img_gray[i][j] <= 127):
                img_gray[i][j] = 0

            elif (img_gray[i][j] > 127):
                img_gray[i][j] = 255

    #Calculate region ratios
    black = 0
    white = 0
    for i in range(0, block1y+1):
        for j in range(0,block1x+1):
            if img_gray[i,j] == 0:
                black+=1

            else:
                white+=1

    region1 = black/white

    black = 0
    white = 0
    for i in range(0, block1y+1):
        for j in range(block1x+1,block2x+1):
            if img_gray[i,j] == 0:
                black+=1

            else:
                white+=1

    region2 = black/white

    black = 0
    white = 0
    for i in range(0, block1y+1):
        for j in range(block2x+1,block3x+1):
            if img_gray[i,j] == 0:
                black+=1

            else:
                white+=1

    region3 = black/white

    black = 0
    white = 0
    for i in range(block1y+1, block2y+1):
        for j in range(0,block1x+1):
            if img_gray[i,j] == 0:
                black+=1

            else:
                white+=1
                
    region4 = black/white

    black = 0
    white = 0
    for i in range(block1y+1, block2y+1):
        for j in range(block1x+1,block2x+1):
            if img_gray[i,j] == 0:
                black+=1

            else:
                white+=1

    region5 = black/white

    black = 0
    white = 0
    for i in range(block1y+1,block2y+1):
        for j in range(block2x+1,block3x+1):
            if img_gray[i,j] == 0:
                black+=1

            else:
                white+=1

    region6 = black/white

    black = 0
    white = 0
    for i in range(block2y+1, block3y+1):
        for j in range(0,block1x+1):
            if img_gray[i,j] == 0:
                black+=1

            else:
                white+=1
                
    region7 = black/white

    black = 0
    white = 0
    for i in range(block2y+1, block3y+1):
        for j in range(block1x+1,block2x+1):
            if img_gray[i,j] == 0:
                black+=1

            else:
                white+=1

    region8 = black/white

    black = 0
    white = 0
    for i in range(block2y+1, block3y+1):
        for j in range(block2x+1, block3x+1):
            if img_gray[i,j] == 0:
                black+=1

            else:
                white+=1

    region9 = black/white

    featureVector = [region1,region2,region3,region4,region5,region6,region7,region8,region9]

    # cv2.imshow("number", img_gray)
    # cv2.waitKey()

    return featureVector