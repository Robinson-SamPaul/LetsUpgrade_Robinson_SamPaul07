# coding: utf-8
import cv2

img1 = cv2.imread('images\Loki1.jpg')
img2 = cv2.imread('images\Loki.jpg')

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

addedImg = img1+img2
blendImg = cv2.addWeighted(img1, 0.3, img2, 0.7, gamma = 0.7)

cv2.imshow("a", addedImg)
cv2.imshow("b", blendImg)

cv2.imwrite("Blended.png", blendImg)

cv2.waitKey(0)
