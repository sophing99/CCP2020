#!/usr/bin/env python
# coding: utf-8

import cv2
import os


def isdir(dir_name):
    if not (os.path.isdir(dir_name)):
        os.mkdir(dir_name)
    return
        
def img_resize_small(img): #축소
    img_raw = cv2.imread(img, cv2.IMREAD_COLOR)
    height, width = img_raw.shape[0:2]
    resized_image = []
    
    img_name = img.split('/')
    img_name = img_name[len(img_name)-1].split('.')[0]
    
    isdir('./data/{}_resize'.format(img_name))
    
    for i in range (1, 6): #마지막 6은 원본 크기
        resize_height = int(0.2*i*height)
        resize_width = int(0.2*i*width)
        cv2.imwrite('./data/{}_resize/{}_small_{}.jpg'.format(img_name, img_name, i),cv2.resize(img_raw, (resize_width, resize_height), interpolation=cv2.INTER_CUBIC))
    return


def img_resize_large(img): #확대
    img_raw = cv2.imread(img, cv2.IMREAD_COLOR)
    height, width = img_raw.shape[0:2]
    resized_image = []
    
    img_name = img.split('/')
    img_name = img_name[len(img_name)-1].split('.')[0]
    
    isdir('./data/{}_resize'.format(img_name))
    
    for i in range (1, 6):
        resize_height = int((1+i)*height)
        resize_width = int((1+i)*width)
        cv2.imwrite('./data/{}_resize/{}_large_{}.jpg'.format(img_name, img_name, i),cv2.resize(img_raw, (resize_width, resize_height), interpolation=cv2.INTER_CUBIC))
    return


