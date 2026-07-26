import cv2
import os

def resize_image(image_path, output_path, size=(224, 224)):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Cannot read: {image_path}")
        return

    resized = cv2.resize(image, size)
    cv2.imwrite(output_path, resized)

print("Image resize module loaded.")
