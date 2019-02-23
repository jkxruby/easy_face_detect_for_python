import cv2 as cv
import numpy as np


print("--------- the face detection ---------")
src = cv.imread("")
cv.namedWindow("input image", cv.WINDOWS_AUTOSIZE)
cv.imshow("input", src)
face_detect_demo()
cv.waitKey(0)

cv.destroyAllWindows()
