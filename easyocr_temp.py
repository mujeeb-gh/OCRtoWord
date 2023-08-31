# import matplotlib.pyplot as plt
# import numpy as np
import easyocr
import pyperclip

IMAGE_PATH = "Images/text_1.png"

reader = easyocr.Reader(['en'], gpu= False)
result = reader.readtext(IMAGE_PATH, detail= 0)
print(result)
pyperclip.copy(str(result))