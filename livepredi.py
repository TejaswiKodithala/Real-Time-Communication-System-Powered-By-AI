import cv2
import numpy as np
from tensorflow.keras.models import load_model
from flask import Response
import atexit

# Load trained models for ASL and Gesture
asl_model = load_model("asl_model.h5")
gesture_model = load_model("gesture_model.h5")

# Load class labels for ASL and Gesture
asl_classes = np.load("label_classes.npy")  # Ensure correct path
gesture_classes = np.load("gesturelabel_classes.npy")  # Ensure correct path

# Initialize camera
camera = cv2.VideoCapture(0)

# Check if camera is accessible
if not camera.isOpened():
    print("Error: Camera not accessible")
else:
    print("Camera initialized successfully")

# Release the camera on app exit
@atexit.register
def release_camera():
    if camera.isOpened():
        camera.release()
        print("Camera released")

# Preprocess the image before prediction
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (64, 64))
    normalized = resized / 255.0
    reshaped = np.reshape(normalized, (1, 64, 64, 1))  # Adding batch dimension
    return reshaped

# Function to predict ASL or Gesture based on image
def predict_image(image, model_type='asl'):
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

# Function to detect ASL or Gesture
def detect_asl_and_gesture():
    while True:
        success, frame = camera.read()
        if not success:
            print("Failed to grab frame")
            break
        else:
            # Alternate between ASL and Gesture model based on some condition
            # Here, we alternate based on time or user choice (you can replace this logic as needed)
            if int(cv2.getTickCount() / cv2.getTickFrequency()) % 2 == 0:
                # Use ASL model
                label = predict_image(frame, 'asl')
                model_label = "ASL"
            else:
                # Use Gesture model
                label = predict_image(frame, 'gesture')
                model_label = "Gesture"
            
            # Display the result
            cv2.putText(frame, f"{model_label}: {label}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def video_feed():
    return Response(detect_asl_and_gesture(), mimetype='multipart/x-mixed-replace; boundary=frame')
