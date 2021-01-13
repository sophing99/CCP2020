#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytesseract
import cv2


# In[2]:


def tesseract(img): #opencv imread가 되어있어야 한다.
    config = ('-l kor')
    return pytesseract.image_to_string(img,config=config)

# In[ ]:




