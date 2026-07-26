from tensorflow.keras.applications import MobileNetV2

def create_model():

    # Load the MobileNetV2 model without the final classification layer
    model = MobileNetV2(
        weights="imagenet",
        include_top=False,
        input_shape=(224, 224, 3)
    )

    return model


if __name__ == "__main__":
    model = create_model()
    print("MobileNetV2 model loaded successfully.")
