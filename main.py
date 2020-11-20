import os, sys
import glob

import argparse
from tesseract.tesseract import *
from preprocess.zoom import *
from preprocess.threshold import *

parser = argparse.ArgumentParser(description="Implementation of ocr")

#########################
####### parameters ######
#########################
parser.add_argument("-img", "--input_img", default="./input/test_01.jpg", type=str, help="Input image path")
parser.add_argument("-z", "--zoom_parameter", default=2, type=float, help="Zoom in/out parameter")
parser.add_argument("-show", "--show_image", default=False, type=bool, help="Show zoom in/out image")


def main():
    global args
    args = parser.parse_args()

    ## preprocessing
    zoom(args.input_img, args.zoom_parameter, args.show_image)
    threshold(args.input_img, "gaussian")
    ## tesseract
    img_to_str("./input/zoom_test_01.jpg")

if __name__ == "__main__":
    main()

