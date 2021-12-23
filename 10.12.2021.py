import cv2 as cv

img1 = cv.cvtColor(cv.imread("rudolf.png"), cv.COLOR_BGR2GRAY) # rudolf.png contains "Weihnachtsschlange" by R. Udolf
img2 = cv.cvtColor(cv.imread("sklaus.png"), cv.COLOR_BGR2GRAY) # sklaus.png contains "Weihnachts-Algorithmus" by S. Klaus

img1[img1 >= 128] = 255
img1[img1 < 128] = 0

img2[img2 >= 128] = 255
img2[img2 < 128] = 0

r = img1 ^ img2

cv.imshow("Result", r)
cv.imwrite("Result.png", r)
cv.waitKey(0)
