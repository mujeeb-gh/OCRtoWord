import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
import pyperclip
from PIL import Image

# Path to the Tesseract executable (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the preprocessed image using PIL (Python Imaging Library)
image_path = 'Images/text_1.png'
img = cv.imread(image_path)

# Image Preprocessing
img = cv.cvtColor(img,cv. COLOR_BGR2RGB)
# img = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# img = cv.Canny(img, 45, 45)
# norm_img = np.zeros((img.shape[0], img.shape[1]))
# img = cv.normalize(img, norm_img, 0, 255, cv.NORM_MINMAX)
# img = cv.threshold(img, 100, 255, cv.THRESH_BINARY)[1]
# img = cv.GaussianBlur(img, (1, 1), 0)



# Display Image
plt.imshow(img)
plt.show()
cv.imwrite("new.jpg", img)

image = Image.open("new.jpg")

# # Perform OCR on the image
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print(extracted_text)
pyperclip.copy(extracted_text)


