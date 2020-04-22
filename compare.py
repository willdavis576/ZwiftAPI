
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2


images = [cv2.imread('testpic.PNG')]
counter = 0

for i in range(4):
    images.append(cv2.imread(str(counter) + '.png'))
    counter += 1

# convert the images to grayscale
gray = []

for i in range(len(images)):
    gray.append(cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY))
    cv2.imshow(str(counter), cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY))
    cv2.waitKey(0)

#
# for i in range(len(gray)):
#     cv2.imshow(str(counter), gray[i])

cv2.waitKey(0)

for i in range(len(gray)):
    (score, diff) = compare_ssim(gray[0], gray[i], full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))
