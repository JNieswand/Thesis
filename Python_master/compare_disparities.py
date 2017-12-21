# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:23:08 2017

@author: jnieswand
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load an color image in grayscale
img = cv2.imread('C:/Users/jnieswand/Documents/Thesis/Data_master/epi_struct_vs_gdepthstructure_w_gt/complextestscene_basicST/disparity_imwrite.png',1)
channel =cv2.split(img)[0]
plt.figure(figsize = (10,10))
plt.imshow(channel)
img2 = cv2.imread('C:/Users/jnieswand/Documents/Thesis/Data_master/epi_struct_vs_gdepthstructure_w_gt/complextestscene_refocus_correspondence/final_disparity_imwrite.png',1)
channel2 =cv2.split(img2)[0]
plt.figure(figsize = (10,10))
plt.imshow(channel2)
print(channel2[245,590])
img3 = cv2.imread('C:/Users/jnieswand/Documents/Thesis/Data_master/epi_struct_vs_gdepthstructure_w_gt/complextestscene_refocus_correspondence/gt_complete.png',1)
plt.figure(figsize = (10,10))
gt =cv2.split(img3)[0]
plt.imshow(gt)
plt.figure(figsize = (10,10))
diff = cv2.absdiff(channel, channel2)
diff[channel == 0] = 0
plt.imshow(diff)
plt.colorbar()
plt.figure(figsize = (10,10))
diff = cv2.absdiff(gt, channel2)
diff[channel == 0] = 0
diff[diff>60] = 60
plt.imshow(diff)
plt.colorbar()
plt.figure(figsize = (10,10))
diff = cv2.absdiff(gt, channel)
diff[diff>60] = 60
diff[channel == 0] = 0
plt.imshow(diff)
plt.colorbar()