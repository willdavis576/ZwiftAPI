
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

import numpy as np
from PIL import ImageGrab
import time

def screen_record():
    counter = 0
    last_time = time.time()
    highscore = 0
    highscoreName = 0

    testImages = {}
    imageNames = []

    for i in range (5):
        name = str(i) + '.PNG'
        imageComp = cv2.imread(name)
        b,g,r = cv2.split(imageComp)
        (thresh, blackAndWhiteImage2) = cv2.threshold(r, 170, 255, cv2.THRESH_BINARY)
        (thresh, blackAndWhiteImage) = cv2.threshold(blackAndWhiteImage2, 220, 255, cv2.THRESH_BINARY)
        testImages[name] = blackAndWhiteImage
        imageNames.append(name)

    for i in range(5):
        name = 'm' + str(i + 1) + '.PNG'
        imageComp = cv2.imread(name)
        b,g,r = cv2.split(imageComp)
        (thresh, blackAndWhiteImage2) = cv2.threshold(r, 170, 255, cv2.THRESH_BINARY)
        (thresh, blackAndWhiteImage) = cv2.threshold(blackAndWhiteImage2, 220, 255, cv2.THRESH_BINARY)
        testImages[name] = blackAndWhiteImage
        imageNames.append(name)

    # name = "fail.PNG"
    # testImages[name] = cv2.imread(name)
    # imageNames.append(name)

    # print(testImages, imageNames)

    while True:

        # 800x600 windowed mode
        test =  np.array(ImageGrab.grab(bbox=(1305,67,1358,92))) # x1,y1,x2,y2 53,25
        test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
        # print(printscreen.shape, imageComp.shape)
        # print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        b,g,r = cv2.split(test)
        (thresh, first) = cv2.threshold(r, 170, 255, cv2.THRESH_BINARY)
        (thresh, second) = cv2.threshold(first, 220, 255, cv2.THRESH_BINARY)
        cv2.imshow('window', second)
        cv2.imshow("comp", testImages[imageNames[counter]])
        cv2.imshow("og", test)
        cv2.imshow("red", r)

        (score, diff) = compare_ssim(testImages[imageNames[counter]], second, full=True)
        diff = (diff * 255).astype("uint8")
        # print("SSIM:" + str(score) + " " + str(counter))
        # if score > 0.35:
            # print("grade is " + str(counter) + "%")

        if score >= highscore:
            highscore = score
            if 'm' in imageNames[counter]:
                result = imageNames[counter].replace('m', '')
                result = result.replace('.PNG', '')
                result = "-" + result

            if 'm' not in imageNames[counter]:
                result = imageNames[counter]
                result = result.replace('.PNG', '')

            highscoreName = result



        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        counter += 1
        if counter == len(imageNames):
            print("grade is " + str(highscoreName) + "%")
            counter = 0
            highscore = 0

screen_record()
