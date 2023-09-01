import cv2

# Load the pre-trained EAST text detection model
model_path = 'frozen_east_text_detection.pb'
net = cv2.dnn.readNet(model_path)

# Load the image
image_path = 'pictures/image text 6.jpg'
image = cv2.imread(image_path)
height, width = image.shape[:2]

# Resize the image for EAST model (should be multiples of 32)
new_width = (width // 32) * 32
new_height = (height // 32) * 32
resized_image = cv2.resize(image, (new_width, new_height))

# Define the confidence threshold and non-maximum suppression threshold
conf_threshold = 0.5
nms_threshold = 0.4

# Get the output layer names
output_layer_names = net.getUnconnectedOutLayersNames()

# Prepare the input blob for the EAST model
blob = cv2.dnn.blobFromImage(resized_image, scalefactor=1.0, size=(new_width, new_height), mean=(123.68, 116.78, 103.94), swapRB=True, crop=False)

# Set the input blob for the network
net.setInput(blob)

# Forward pass through the network
output = net.forward(output_layer_names)

# Post-process the output
boxes = []
confidences = []
for layer_output in output:
    for detection in layer_output[0, 0]:
        score = detection[2]
        if score > conf_threshold:
            left = int(detection[3] * width)
            top = int(detection[4] * height)
            right = int(detection[5] * width)
            bottom = int(detection[6] * height)
            width_box = right - left
            height_box = bottom - top
            # Filter out small boxes
            if width_box > 10 and height_box > 10:
                boxes.append((left, top, width_box, height_box))
                confidences.append(float(score))

# Apply non-maximum suppression
indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

# Draw the bounding boxes on the image
for i in indices:
    left, top, width_box, height_box = boxes[i[0]]
    cv2.rectangle(image, (left, top), (left + width_box, top + height_box), (0, 255, 0), 2)

# Display the image with bounding boxes
cv2.imshow('Text Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
