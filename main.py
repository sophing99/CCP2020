import argparse
from tesseract.tesseract import *
from preprocess.crop import *
from preprocess.zoom import *
from preprocess.threshold import *

parser = argparse.ArgumentParser(description="Implementation of ocr")

#########################
####### parameters ######
#########################
parser.add_argument("-img", "--input_img", default="./input/test_01.jpg", type=str, help="Input image path")
parser.add_argument("-z", "--zoom_parameter", default=1.5, type=float, help="Zoom in/out parameter")
parser.add_argument("-show", "--show_image", default=False, type=bool, help="Show zoom in/out image")

def main():
    global args
    args = parser.parse_args()
    ## crop
    my_roi = PolygonDrawer("Crop", args.input_img)
    my_roi.run()

    ## preprocessing
    zoom("./input/crop_" + args.input_img.split('/')[-1], args.zoom_parameter, args.show_image)
    threshold("./input/zoom_crop_" + args.input_img.split('/')[-1], "global")

    ## tesseract
    img_to_str("./input/threshold_zoom_crop_" + args.input_img.split('/')[-1])

if __name__ == "__main__":
    main()

