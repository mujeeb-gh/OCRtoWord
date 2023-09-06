import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
# import pyperclip
from PIL import Image

# Path to the Tesseract executable (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the preprocessed image using PIL (Python Imaging Library)
image_path = 'experiments/Images/sign.png'
# img = Image.open(image_path)
img = cv2.imread(image_path)

def get_skew_angle(image):
    # image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    edges = cv2.Canny(blurred, 50, 150, apertureSize=3)
    # Use Hough Line Transform to detect lines in the image
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)
    # Calculate the skew angle by averaging the angles of detected lines
    angle_sum = 0.0
    for rho, theta in lines[:, 0]:
        angle_sum += np.degrees(theta)
    skew_angle = angle_sum / len(lines)
    return skew_angle

def correct_skew(image):
    # Get the skew angle
    skew_angle = get_skew_angle(image)
    # Load the image
    # image = cv2.imread(image_path)
    # Rotate the image to correct skew
    rotated_image = cv2.warpAffine(image, cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), skew_angle, 1.0), (image.shape[1], image.shape[0]), flags=cv2.INTER_LINEAR)
    return rotated_image

def remove_noise(image):
  return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 3, 15)

# Image Preprocessing
# 1 - Normalization
norm_img = np.zeros((img.shape[0], img.shape[1]))
# img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)

# 2 - Skew Correction - not working right
# img = correct_skew(img)

# 3 - Image Scaling not working right
# 4 - Noise Removal
# img = remove_noise(img)

# 5 - Thinning and Skeletonization - not working right
kernel = np.ones((1,1),np.uint8)
# img = cv2.erode(img, kernel, iterations = 1)

# 6- Greyscale
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]



# img = cv.cvtColor(img,cv. COLOR_BGR2RGB)
# img = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# img = cv.Canny(img, 45, 45)
# norm_img = np.zeros((img.shape[0], img.shape[1]))
# img = cv.normalize(img, norm_img, 0, 255, cv.NORM_MINMAX)
# img = cv.threshold(img, 100, 255, cv.THRESH_BINARY)[1]
# img = cv.GaussianBlur(img, (1, 1), 0)



# Display Image
plt.imshow(img)
plt.show()
# cv.imwrite("new.jpg", img)

# image = Image.open("new.jpg")

# # Perform OCR on the image
extracted_text = pytesseract.image_to_string(img)

# Print the extracted text
print(extracted_text)
# pyperclip.copy(extracted_text)


