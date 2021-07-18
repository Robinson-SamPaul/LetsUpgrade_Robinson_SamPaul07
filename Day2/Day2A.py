# coding: utf-8

import cv2
import numpy as np

img = cv2.imread('images/Loki.jpg')
zero = np.zeros((img.shape[0], img.shape[1]), np.uint8)

b, g, r = cv2.split(img)

blue = cv2.merge([b, zero, zero])
green = cv2.merge([zero, g, zero])
red = cv2.merge([zero, zero, r])

cv2.imshow('Blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

cv2.waitKey(0)
