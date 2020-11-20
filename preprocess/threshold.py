#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Filename : threshold
# @Date : 2020-11-20-16-21
# @Project : ccp
# @Author : seungmin

from PIL import Image
import cv2

def rgb_to_gray(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def threshold(img_path, s):
    img = cv2.imread(img_path, 0)
    if s == "global":
        img_th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    elif s == "mean":
        img_th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
    elif s == "gaussian":
        img_th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)
    else:
        print("Not implemented...")

    img_th = Image.fromarray(img_th)
    img_th.save("./input/threshold_" + img_path.split('/')[-1])

    return img_th