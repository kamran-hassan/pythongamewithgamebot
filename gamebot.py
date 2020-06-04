import numpy as np
import cv2
from PIL import ImageGrab as ig
import time 
from pynput.keyboard import Key, Controller

def inputgenrator(t):
        keyboard = Controller()
        keyboard.press(t)
        time.sleep(0.2)
        keyboard.release(t)
        print("generated input is ", t, end ="\n")

x= True
time.sleep(5)  # this time is given for selecting the game window in which the input is going to hit

while x:
    screen = ig.grab(bbox=(50,50,700,530))
    img = np.array(screen)
    img_bW  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    thres,img_bW = cv2.threshold(img_bW,10,255,cv2.THRESH_BINARY)
    contours, hierachy = cv2.findContours(img_bW,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours), end = "\n")
    x = [0,0]
    y = [0,0]
    for c in contours:
        M = cv2.moments(c)
        if M["m00"] != 0:
            i = 0 if len(c)>7 else 1
            x[i] = (int(M["m10"] / M["m00"]))
            y[i] = (int(M["m01"] / M["m00"]))
        else:
            i = 0 if len(c)>7 else 1
            x.insert(i,0)
            y.insert(i,0)
        cv2.drawContours(img, [c], 0,(0,255,0),3)
        cv2.circle(img,(x[i],y[i]),4,(255,255,255),-1)
    
    if (len(contours) == 2):
        if(x[0]-x[1]>20):
            inputgenrator('d')
        elif(x[0]-x[1]<-20):
            inputgenrator('a')
        if(y[0]-y[1]<-20):
            inputgenrator('w')
        elif(y[0]-y[1]>20):
            inputgenrator('s')  

    if (len(contours)==1):
        cv2.putText(img,"reached destination",(250,250), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    
    cv2.imshow("FINAL WINDOW",img)
    
    
    if cv2.waitKey(25) & 0xFF == ord('c'):
        cv2.destroyAllWindows()
        x =False
