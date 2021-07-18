# coding: utf-8
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('images/Loki.jpg')
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img3 = cv2.imread('images/Loki.jpg', 0)
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img4 = img2

plt.subplot(2, 2, 1)
plt.imshow(img1)
plt.title("BGR IMAGE")

plt.subplot(2, 2, 2)
plt.imshow(img2)
plt.title("RGB IMAGE")

plt.subplot(2, 2, 3)
plt.imshow(img3)
plt.title("GRAY IMAGE")

plt.subplot(2, 2, 4)
plt.imshow(img4[:300,75:300])
plt.title("CROPPED IMAGE")

plt.show()
