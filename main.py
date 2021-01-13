import argparse

from allergy.allergy_check import *
from allergy.input_allergy import *
from allergy.compare_allergy import *
from tesseract.tesseract import *
from preprocess.crop import *
from preprocess.zoom import *
from preprocess.threshold import *
from preprocess.text_postprocess import *
import pytesseract

parser = argparse.ArgumentParser(description="Implementation of ocr")

#########################
####### parameters ######
#########################
parser.add_argument("-img", "--input_img", default="./input/test.jpg", type=str, help="Input image path")
parser.add_argument("-z", "--zoom_parameter", default=1.5, type=float, help="Zoom in/out parameter")
parser.add_argument("-show", "--show_image", default=False, type=bool, help="Show zoom in/out image")

def main():
    global args
    args = parser.parse_args()

    ## allergy contain
    user_allergy = input_allergy()

    ## crop
    my_roi = PolygonDrawer("Crop", args.input_img)
    my_roi.run()


    ## image preprocessing
    zoom("./input/crop_" + args.input_img.split('/')[-1], args.zoom_parameter, args.show_image)
    threshold("./input/zoom_crop_" + args.input_img.split('/')[-1], "global")

    ## tesseract
    config = ('-l kor')
    text = pytesseract.image_to_string('./input/threshold_zoom_crop_test.jpg', config=config)

    ## text postprocessing and save as text
    text = text_postprocess(text, args.input_img)

    ## allergy in food
    result = allergy_check(text)

    ## compare with user info
    match_allergy = compare_allergy(user_allergy, result)

    return match_allergy

if __name__ == "__main__":

    result = main()
    if not result:
        print("해당 식품에는 알러지 유발 성분이 포함되어 있지 않습니다")

    else:
        print("해당 식품에는 알러지 유발 성분이 포함되어 있습니다")
        for allergy in result:
            print(allergy)

