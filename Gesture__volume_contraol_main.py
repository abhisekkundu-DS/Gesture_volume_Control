#import all module
# import open cv2 for computer vission or image or video capture
import cv2
# import current data timme
import time
# import jaxlib
# create a nd array
import numpy as np
#mediapipe module use in objrct  tracking in video and others work
import mediapipe as mp
#previous we make this handtraking module
import HandTraking as htm # this handtraking module use as htm
# this module is yes for mathematical work
import math
# under this module use for volume tracking/control in python
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
# from jax import devices
#is a Python library that provides an interface to the Windows Core Audio API
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume

# this part use for parameter
wCam , hCam = 640, 480

#capture this video using webcum as 0
cap =  cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)
#present time set as 0
pTime = 0

# detect hand as object
detector = htm.handDetector(detectionCon = 0.7)
# volume control


device = AudioUtilities.GetSpeakers()
interface = device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
volume = cast(interface,POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
# print(volume.GetMasterVolumeLevel())


#create volume range as 0 to 100
volRange = volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(0,None)#set the volume
minVol = volRange[0]#set volume as 0 in lower value
maxVol = volRange[1]#set volume as 1 in higher value
vol = 0#vol a as first se 0
#assigm as volume bar in starting 0
volBar = 0
# assign value of percent in starting as 0
volPer = 0 #


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw = False)
    if len(lmList) !=0:
        # print(lmList[4],lmList[8]) # get output only two no 4 and 8 in hand point

        x1 , y1 = lmList[4][1], lmList[4][2]
        x2 , y2 = lmList[8][1], lmList[8][2]
        # find out the middle point of 4 and 8 no point in hand
        cx , cy = (x1+x2)//2,(y1+y2)//2
        # two find unique draw a bigger circle 4, 8 except  other circle
        cv2.circle(img, (x1, y1), 15,(255,0,255), cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(255,0,255), cv2.FILLED)
        # join two line 4 and 8 in a st'line
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        # draw a circle between 4 and 8 point middele point
        cv2.circle(img,(cx,cy),10,(255,0,255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(int(length))

        # hand Range  50  - 300
        # volume Range -65 to 0

        vol = np.interp(length,[50,300],[minVol,maxVol])
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)



        # if length is less the 50 condsider a min
        if length <50:
            #to min point represent as a green colour solid circle when 4 and 8 no point distance are minium
            cv2.circle(img ,(cx,cy),10,(0,255,0),cv2.FILLED)

    #create a rectangle box to show ths music volume bar
    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)


    #this rectangle fill with a solid colour and depent on volume
    cv2.rectangle(img, (50,int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)


    # to show the over all percentage in present time volume percentage
    cv2.putText(img,f'{int(volPer)}%',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)

    #time management block
    cTime = time.time()#current time
    fps = 1/(cTime - pTime)#find this fps rate per second
    pTime = cTime  # value of current time insert in present time


    cv2.putText(img,f'FPS:{(fps)}',(48,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)


    #otput generate block
    cv2.imshow('Img',img)  # to show this video as output is img
    cv2.waitKey(1)
