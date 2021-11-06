# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 17:06:36 2021

@author: shadi
"""

import cv2
import mediapipe as mp 

def HandleHandTracking():
        cap = cv2.VideoCapture(0)
        
        while True:
            
            success, img = cap.read()
            cv2.imshow("Image", img)
            cv2.waitKey(1)
        
