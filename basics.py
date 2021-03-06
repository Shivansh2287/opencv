import cv2 as cv
import numpy as np


img = cv.imread('./Resources/Photos/cats 2.jpg')
cv.imshow('cats', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('greay', gray)


lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

cv.waitKey(0)
