import pytesseract as tess
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance, ImageFilter

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image and preprocess
image_path = 'experiments/Images/text_1.png'
image = Image.open(image_path)

# Preprocessing
preprocessed_image = image.filter(ImageFilter.GaussianBlur(radius=1))
preprocessed_image = preprocessed_image.convert("L")  # Convert to grayscale

# Enhance contrast
enhancer = ImageEnhance.Contrast(preprocessed_image)
preprocessed_image = enhancer.enhance(2.0)  # You can adjust the enhancement factor


# Perform OCR with additional configuration
custom_config = r'--oem 3 --psm 6'  # OCR Engine mode and Page Segmentation mode
detected_text = tess.image_to_string(preprocessed_image, lang='eng', config=custom_config)

print(detected_text)


