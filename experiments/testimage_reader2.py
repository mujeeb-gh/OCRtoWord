from PIL import Image
import base64, cv2

# with open("experiments/Images/text_1.png", "rb") as f:
#     image = Image.open(f)

image = cv2.imread("experiments/Images/text_1.png")

encoded_image = base64.b64encode(image)
print(type(encoded_image))