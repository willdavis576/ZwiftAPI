import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record():
    last_time = time.time()
    while True:
        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(1305,67,1358,92))) # x1,y1,x2,y2
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
