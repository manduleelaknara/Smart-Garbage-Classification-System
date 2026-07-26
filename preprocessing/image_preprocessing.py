import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return None

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image / 255.0

    return image

print("Image preprocessing module loaded.")
