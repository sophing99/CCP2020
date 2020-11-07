#!/usr/bin/env python
# coding: utf-8

import cv2
import Do_Tesseract


def img_resize_small(img): #축소
    img_raw = cv2.imread(img, cv2.IMREAD_COLOR)
    height, width = img_raw.shape[0:2]
    resized_image = []
    
    for i in range (1, 6): #마지막 6은 원본 크기
        resize_height = int(0.2*i*height)
        resize_width = int(0.2*i*width)
        resized_image.append(cv2.resize(img_raw, (resize_width, resize_height), interpolation=cv2.INTER_CUBIC))
    return resized_image


def img_resize_large(img): #확대
    img_raw = cv2.imread(img, cv2.IMREAD_COLOR)
    height, width = img_raw.shape[0:2]
    resized_image = []
    
    for i in range (1, 6):
        resize_height = int((1+i)*height)
        resize_width = int((1+i)*width)
        resized_image.append(cv2.resize(img_raw, (resize_width, resize_height), interpolation=cv2.INTER_CUBIC))
    return resized_image



def my_function(img):
    result_small = []
    result_large = []
    
    small = img_resize_small(img)
    large = img_resize_large(img)
    
    for img in (small):
        result_small.append(Do_Tesseract.do_tesseract(img))
        
    for img in (large):
        result_large.append(Do_Tesseract.do_tesseract(img))
        
    return result_small, result_large