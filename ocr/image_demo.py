import pytesseract
from PIL import Image

img = Image.open('./data/2.jpg')


# text = pytesseract.image_to_string(img, lang='eng')
text = pytesseract.image_to_string(img, lang='chi_sim')


print(text)

