import pytesseract
config = ('-l kor')
str = pytesseract.image_to_string('./threshold_zoom_crop_test.jpg', config = config)
print(str)