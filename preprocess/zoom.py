from PIL import Image
import os

def zoom(img_path, s, show):
    img = Image.open(img_path)

    zoom_img = img.resize((round(img.size[0]*s), round(img.size[1]*s)))
    zoom_img.save("./input/zoom_" + img_path.split('/')[-1])

    if show == True:
        return zoom_img.show()

