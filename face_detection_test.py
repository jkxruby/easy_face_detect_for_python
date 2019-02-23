import cv2 as cv
import numpy as np
'''
def face_detect_demo():  # 图像识别部分
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("/Users/jkx/PycharmProjects/awesome_web/venv/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(gray, 1.02, 5)   # 最后一个数字可调，用于人脸检测的强度
    for x, y, w, h in faces:
        cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1)
    cv.imshow("result", src)

print("--------- the face detection ---------")
src = cv.imread("/Users/jkx/Desktop/太祖.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)

cv.imshow("input image", src)
face_detect_demo()
cv.waitKey(0)

cv.destroyAllWindows()
'''


def face_detect_demo(image):   # 视频识别部分
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("/Users/jkx/PycharmProjects/awesome_web/venv/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(gray, 1.02, 50)   # 最后一个数字越小，越容易误判，越大，越容易不判
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 1)
    cv.imshow("result", image)

print("--------- the face detection ---------")
capture = cv.VideoCapture(0)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)

while(True):
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    face_detect_demo(frame)
    c = cv.waitKey(10)
    if c == 27: # ESC
        break

cv.waitKey(0)
#cv.destroyAllWindows()

