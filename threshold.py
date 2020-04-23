import cv2

number = 4
filename = str(number) + '.PNG'

img = cv2.imread(filename)
b,g,r = cv2.split(img)
# cv2.imshow("test10", r)
# grayImage = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
# (thresh, blackAndWhiteImage3) = cv2.threshold(r, 150, 255, cv2.THRESH_TRUNC)

(thresh, blackAndWhiteImage2) = cv2.threshold(r, 170, 255, cv2.THRESH_BINARY)

(thresh, blackAndWhiteImage) = cv2.threshold(blackAndWhiteImage2, 220, 255, cv2.THRESH_BINARY)

# cv2.imwrite("bw" + str(number) + ".PNG", r/)

# cv2.imshow("test2", blackAndWhiteImage2)
# cv2.imshow("test3", r)
cv2.imshow("test", blackAndWhiteImage)
# cv2.imshow("test1",img)
cv2.waitKey(0)
