import os
import glob
from PIL import Image
import cv2

src = cv2.imread("./test.jpg", cv2.IMREAD_COLOR)

dst2 = cv2.resize(src, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imwrite('./test.jpg', dst2)