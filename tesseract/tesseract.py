from PIL import Image
import pytesseract

def img_to_str(img):
    img = Image.open(img)
    config = ('-l kor')
    txt = pytesseract.image_to_string(img, config=config)

    with open("./output/ocr.txt", "w") as f:
        f.write(txt)