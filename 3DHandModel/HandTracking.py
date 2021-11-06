# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 17:06:36 2021

@author: shadi
"""

import cv2
import mediapipe as mp 

def HandleHandTracking():
        cap = cv2.VideoCapture(0)
        
        mpHand = mp.solutions.hands
        hands = mpHand.Hands()
        
        while True:
            
            success, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            result = hands.process(imgRGB)
            cv2.imshow("Image", img)
            cv2.waitKey(1)
        
