# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 22:47:27 2021

@author: Asus
"""

import cv2
import numpy as np
import os

#Read the images from your directory

path="D:\imagestiching\images"
destpath="D:\imagestiching\save/"
def showFull(path):
    images=[]
    for name in os.listdir(path):
        images.append(cv2.imread(os.path.join(path,name)))
        stitcher = cv2.Stitcher.create()
        ret,pano = stitcher.stitch(images)
    try:
        cv2.imshow('total',pano)
        cv2.imwrite(destpath+'total.jpg',pano)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print(" not stiched ")
        
        
        
showFull(path)