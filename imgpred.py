import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained models for ASL and Gesture
asl_model = load_model("asl_model.h5")
gesture_model = load_model("gesture_model.h5")

# Load class labels for ASL and Gesture
asl_classes = np.load("label_classes.npy")  # Ensure correct path
gesture_classes = np.load("gesturelabel_classes.npy")  # Ensure correct path

# Preprocess the image before prediction
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (64, 64))
    normalized = resized / 255.0
    reshaped = np.reshape(normalized, (1, 64, 64, 1))  # Adding batch dimension
    return reshaped

# Predict image based on selected model type
def predict_image(filepath, model_type):
    # Read the image
    image = cv2.imread(filepath)

    # Preprocess the image
    processed_image = preprocess_image(image)

    # Make prediction based on the selected model
    if model_type == 'asl':
        prediction = asl_model.predict(processed_image)
        label = asl_classes[np.argmax(prediction)]
    elif model_type == 'gesture':
        prediction = gesture_model.predict(processed_image)
        label = gesture_classes[np.argmax(prediction)]
    else:
        raise ValueError("Invalid model type")

    return label
