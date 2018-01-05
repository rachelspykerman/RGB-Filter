import cv2
import numpy as np

def maxRGB(image):
    [B,G,R] = cv2.split(image)

    maxColor = np.maximum((np.maximum(R,G)),B)

    # for each pixel in the red channel whose value is less than the maxColor, set it to 0
    R[R < maxColor] = 0
    G[G < maxColor] = 0
    B[B < maxColor] = 0

    return cv2.merge([B,G,R])


image = cv2.imread("images/dog.jpeg")
imgMax = maxRGB(image)
cv2.imshow("Max RGB Filter", np.hstack([image,imgMax]))
cv2.waitKey(0)
