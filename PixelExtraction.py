#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 23:51:09 2020

@author: alyssaunell
"""
import cv2
import numpy as np


for i in range(30):
    counter = 0
    print('i', i)
    if i<10:
        print('1')
        filename='control-000'+str(i)+' copy.png'
    else:
        filename='control-00'+str(i)+' copy.png'
    path='/Users/alyssaunell/Desktop/UROP/PNGs/ControlPNGs/'+filename
#    finpath='/Users/alyssaunell/Desktop/UROP/Edited/Control/e'+filename
#    print(cv2.__version__)
    print('2')
    
    # VIDEO EXPERIMENT
    vidObj = cv2.VideoCapture(path)
    success = True

    while success:
      
        # vidObj object calls read 
        # function extract frames 
        success, frame = vidObj.read()
        finpath='/Users/alyssaunell/Desktop/UROP/Edited Grey/Control/Control copy '+str(i)+'/'+str(counter)+filename
        print(finpath)
        if not success:
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([43,0,0])
        upper_red = np.array([150,20,255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        print('3')
        cv2.imshow('res',res)
        cv2.imwrite(finpath,res)
        
        counter += 1
        print("Counter:", counter)
    
    
    
#    IMAGE FORMAT
#    frame = cv2.imread(path)
#    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#    lower_red = np.array([0,35,0])
#    upper_red = np.array([255,255,255])
#    mask = cv2.inRange(hsv, lower_red, upper_red)
#    res = cv2.bitwise_and(frame,frame, mask= mask)
#    cv2.imshow('frame',frame)
#    cv2.imshow('mask',mask)
#    print('3')
#    cv2.imshow('res',res)
#    cv2.imwrite(finpath,res)
    #k = cv2.waitKey(5) & 0xFF
cv2.waitKey(0)
print('17')
    
cv2.destroyAllWindows()
    #frame.release()
    
print('8')
