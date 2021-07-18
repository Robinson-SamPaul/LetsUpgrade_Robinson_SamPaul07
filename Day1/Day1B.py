import cv2

cap = cv2.VideoCapture(0)

while True:

    flag, frame = cap.read()

    if not flag:
        print("Couldn't access the Camera")
        break

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)

    if k == ord('q'):
        break

cap.release()
cap.destroyAllWindows()
