import cv2 as cv
import numpy as np
import math
import featurevector as fv

def euclideanDistance(v1, v2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(v1, v2)]))

v1 = fv.featureVector('0.png')
f = open('feature_vectors.txt', 'r')

distance = []
for line in f:
    line = line.strip()
    v2 = line.split(',')
    for i in range(len(v2)):
        v2[i] = float(v2[i])
    distance.append(euclideanDistance(v1, v2))

f.close()
print(distance)
print(distance.index(min(distance)))
    
