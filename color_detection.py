import cv2
from PIL import Image
import numpy as np

#This function converts a give color into HSV colorspace and returns the upper and lower limit of the color range
def get_limits(color):
    col = np.uint8([[color]])
    col_hsv = cv2.cvtColor(col, cv2.COLOR_BGR2HSV)
    lower_l = col_hsv[0][0][0] - 10, 100, 100
    upper_l = col_hsv[0][0][0] + 10, 255, 255

    lower_l = np.array(lower_l, dtype=np.uint8)
    upper_l = np.array(upper_l, dtype=np.uint8)

    return lower_l, upper_l

#Yellow color in BGR
COLOR = [0, 255, 255]

#Getting feed from the webcam
wc = cv2.VideoCapture(0)
while True:
    ret, frame = wc.read()
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_l , upper_l = get_limits(color= COLOR)
    mask = cv2.inRange(frameHSV, lower_l, upper_l)
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()
    
    #Drawing bounded box for the object of the desired color
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        #Drawing box according to co-ordinates given by the bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("frame", frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        #Break the loop of q is pressed 
        break


wc.release()
cv2.destroyAllWindows()