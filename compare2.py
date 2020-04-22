
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

    for i in range (4):
        name = str(i) + '.PNG'
        imageComp = cv2.imread(name)
        imageComp = cv2.cvtColor(imageComp, cv2.COLOR_BGR2GRAY)
        testImages[name] = imageComp
        imageNames.append(name)

    for i in range(5):
        name = 'm' + str(i + 1) + '.PNG'
        imageComp = cv2.imread(name)
        imageComp = cv2.cvtColor(imageComp, cv2.COLOR_BGR2GRAY)
        testImages[name] = imageComp
        imageNames.append(name)

    print(testImages, imageNames)

    while True:

        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(1305,67,1358,92))) # x1,y1,x2,y2 53,25
        # print(printscreen.shape, imageComp.shape)
        # print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        gray = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        cv2.imshow('window', gray)

        (score, diff) = compare_ssim(testImages[imageNames[counter]], gray, full=True)
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

        print("grade is " + str(highscoreName) + "%", imageNames[counter])

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        counter += 1
        if counter == len(imageNames):
            counter = 0

screen_record()
