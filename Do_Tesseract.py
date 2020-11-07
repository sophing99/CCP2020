#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytesseract
import cv2


# In[2]:


def do_tesseract(img): #opencv imread가 되어있어야 한다.
    config = ('-l kor --oem2 --psm 4')
    return pytesseract.image_to_string(img,config=config)

# In[ ]:




