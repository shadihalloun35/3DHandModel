# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:42:58 2021

@author: shadi
"""

import HandTracking

if __name__=="__main__":
    
    startTime = 0
    currentTime = 0
    maxHandToModel = 2
    HandTracking.HandleHandTracking(maxHandToModel, startTime, currentTime)
    
    
    
    