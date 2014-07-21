# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 14:53:33 2014

@author: Salvatore
"""
import numpy as np
from matplotlib import pyplot as plt

"""
draw an H with thickness=3 of h=24 and width=20 ad coords(x,y) passed if you pass
in_place=False it returns a copy of that image
"""
def draw_h(image, coords,in_place=True):

    green = [0,255,0]

    row,col = coords

    thick = 3
    h = 24
    l = 20    
    
    if not in_place:
        image = image.copy()
        
    image[row:(row+h),col:(col+thick),:]= green   
    image[row+((h/2)-(thick/2)):row+((h/2)+(thick/2)),col:col+l,:]=green  
    image[row:row+h,(col+l-thick):(col+l),:]=green  

    return image
    
"""
plot intensity values of a row of an image passed, it plot also for 
coloured images the 3 channels 
"""
def plot_intensity(image,row):
    if image.ndim < 3:
        image = image[...,np.newaxis]
    for ch in [image[...,i] for i in range(image.shape[-1])]:
        plt.plot(ch[row])