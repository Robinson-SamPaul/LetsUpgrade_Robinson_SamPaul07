import cv2

cap = cv2.VideoCapture(0)
b = 0

while b == 0:

    a = int(input("Enter your choice to select 5 lokis (0-4): "))

    if a == 0:
        img = cv2.imread('images\Loki.jpg')
        b = 1

    elif a == 1:
        img = cv2.imread('images\Loki1.jpg')
        b = 1

    elif a == 2:
        img = cv2.imread('images\Loki2.jpg')
        b = 1

    elif a == 3:
        img = cv2.imread('images\Loki3.jpg')
        b = 1

    elif a == 4:
        img = cv2.imread('images\Loki4.jpg')
        b = 1

    else:
        b = 0

while True:

    flag, frame = cap.read()

    if not flag:
        print("Couldn't access the Camera")
        break

    img = cv2.resize(img, (frame.shape[1], frame.shape[0]))
    blendFrame = cv2.addWeighted(frame, 0.8, img, 0.2, gamma = 0.1)
    cv2.imshow("Blended Frame", blendFrame)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cap.release()
cap.destroyAllWindows()
