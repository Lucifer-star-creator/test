import cv2 #for image processing
import easygui #to open the filebox
import numpy as np #to store image
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

""" fileopenbox opens the box to choose file
and help us store file path as string """

def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)

def cartoonify(ImagePath):
    # read image
    originalmage = cv2.imread(ImagePath)
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BAYER_BG2BGR)
   # print(image) # image is stored in form of numbers
    if originalmage is None:
        print("Cannot find any image.Choose appropirate files")
        sys.exit()
    Resized1 = cv2.resize(originalmage, (960,540))
    #plt.imshow(Resized1, cmap='gray)
    #converting an image to grayscale
    grayScaleImage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (960, 540))
    #plt.imshow(ReSized2, cmap='gray')
    #applying median blur to smoothen an image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    REsized3 = cv2.resize(smoothGrayScale, (960,540))
    #plt.imshow(Resized3, cmap='gray)
    #retrieving the edges for cartoon effect
    #by using thresholding technique
    getedge = cv2.adaptiveThreshold(smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 9 , 9)
    Resized4 = cv2.resize(getedge, (960,540))
    #ptl.imshow(Resized4, cmap='gray')
    #applying bilateral filter to remove noise 
    #and keep edge sharp as required
    colorImage = cv2.bilateralFilter(originalmage,9,300,300)
    Resized5 = cv2.resize(colorImage, (960,540))
    # plt.imshow(Resized5, cmap='gray')
    