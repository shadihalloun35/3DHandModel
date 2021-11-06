# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 17:06:36 2021

@author: shadi
"""

import cv2
import mediapipe as mp 

def HandleHandTracking(maxHandToModel):
        cap = cv2.VideoCapture(0)
        
        mpHand = mp.solutions.hands
        
        #hands = mpHand.Hands(False,maxHandToModel)
        
        hands = mpHand.Hands()
        mpDraw = mp.solutions.drawing_utils
        while True:
            
            success, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            result = hands.process(imgRGB)
            
            print(result.multi_hand_landmarks)
            
            if result.multi_hand_landmarks:
                for handLms in result.multi_hand_landmarks:
                    mpDraw.draw_landmarks(img, handLms)
            
            
            
            
            
            cv2.imshow("Image", img)
            cv2.waitKey(1)
        
