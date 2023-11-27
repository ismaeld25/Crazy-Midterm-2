##color detection
import cv2
import time
import numpy as np
# Read the video
cap = cv2.VideoCapture(0)

# Read the first frame
ret, frame = cap.read()

#color detection
def detection(frame):
    global color
    color=''
    ret, frame = cap.read()
    cv2.imshow('video',frame)
    global cx, cy
    b, g, r = cv2.split(frame)
    cv2.imshow('frame', frame)
    print('1')
    ret,thresh1 = cv2.threshold(r,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(b,127,255,cv2.THRESH_BINARY)
    ret,thresh3 = cv2.threshold(g,127,255,cv2.THRESH_BINARY)

    rav=np.sum(thresh1) #gets sum of colors
    print("red values",rav)
    gav=np.sum(thresh3)
    print('green values',gav)
    if rav>gav:
        color ='Red'
    if gav>rav:
        color ='Green'
    return color

while True:
    detection(frame)
    print(color)
    if cv2.waitKey(1) == ord('q'): # Exit if the 'q' key is pressed
        break
cap.release() # Release the camera
cv2.destroyAllWindows() # Close all windows
