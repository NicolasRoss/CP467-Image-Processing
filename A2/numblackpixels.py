import numpy as np
import cv2
from PIL import Image


img = cv2.imread('rose.png')
img = cv2.bitwise_not(img)
grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY)[1]
ret, labels = cv2.connectedComponents(img)

def imshow_components(labels):
    # Map component labels to hue val
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    # cvt to BGR for display
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue==0] = 0

    cv2.imshow('labeled.png', labeled_img)
    cv2.waitKey()



def countPixels(labels):
    counts = dict()
    for label in labels:
        # print(label)
        for num in label:
            # print(type(num))
            if(int(num) != 0):
                if num not in counts:
                    counts[num] = 1
                else:
                    counts[num] += 1
    return counts


imshow_components(labels)

counts = countPixels(labels)

print(counts)