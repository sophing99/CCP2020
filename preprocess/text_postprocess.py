import re

def text_postprocess(text, img_name):

    text = ''.join(text.split())
    text = re.sub('{' and '}' and '…', '', text)
    text2 = re.findall(r"[\w']+", text)
    text3 = " ".join(text2)

    ##save result as txt
    text_name = './output/' + img_name.split('/')[-1][0:-4] + '.txt'
    f = open(text_name, 'w', encoding='UTF8')
    f.write(text3)
    f.close()

    return text3