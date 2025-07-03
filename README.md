# Real-Time-Communication-System-Powered-By-AI

## 📌 Project Overview

This project aims to create a **Real-Time Communication System** that leverages **Artificial Intelligence** to aid specially-abled individuals in expressing themselves effectively. The system converts visual gestures into text or speech, providing a meaningful and accessible way for users with speech or hearing impairments to communicate with others in real-time.


## 🧠 Features

- 🤖 AI-Powered Gesture Recognition
- 🧩 Pre-trained deep learning model for hand gesture classification
- 🔊 Real-time speech synthesis using recognized inputs
- 💬 Text output for visual feedback
- 📸 Webcam-based live input stream
- 💡 Simple and intuitive user interface
- 🧑‍🦽 Designed with accessibility in mind


## 🛠️ Technologies Used

**Python 3.x**
**TensorFlow / Keras** – Deep learning for gesture recognition
**OpenCV** – Real-time video processing
**NumPy** – Data manipulation
**Pyttsx3 / gTTS** – Text-to-speech conversion
**Tkinter / Flask** (optional) – GUI / Web interface


## 🗂️ Dataset

- Hand gesture dataset containing **15,750 training images** and **2,250 testing images** across **9 gesture classes**.
- The dataset is structured into folders labeled by gesture name.
- Preprocessed and augmented to enhance model accuracy.


## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/real-time-ai-comm-system.git
   cd real-time-ai-comm-system
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model (if needed)**

   ```bash
   python train_model.py
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

## 🧪 Model Training

* CNN-based architecture used for classifying hand gestures.
* Achieved high accuracy with augmented data and optimized layers.
* Model saved as `.h5` file for deployment.

## ⚙️ How It Works

The **Real-Time Communication System Powered by AI** enables specially-abled individuals to communicate using hand gestures, which are recognized by an AI model and converted into text or speech in real-time.

### 🔁 Workflow:

1. **🎥 Video Capture**
   - A webcam captures live hand gestures from the user.
   - The video feed is processed frame-by-frame using OpenCV.

2. **🧠 Gesture Recognition**
   - Each frame is passed to a Convolutional Neural Network (CNN) trained on a labeled gesture dataset.
   - The model classifies the gesture into one of the predefined categories (e.g., "Hello", "Yes", "No").

3. **📝 Display Output**
   - The predicted gesture is mapped to a corresponding word or phrase.
   - This text is displayed on the user interface for visual confirmation.

4. **🔊 Speech Generation**
   - The output text is passed to a Text-to-Speech (TTS) engine like `pyttsx3` or `gTTS`.
   - The system plays the generated audio to "speak" the user's gesture.

### 📌 Example:
- A user shows the gesture for “Thank You”.
- The model recognizes it, displays **“Thank You”** on the screen, and speaks it aloud.


## 🎯 Use Case

This system is ideal for:

* Individuals with speech or hearing disabilities
* Educational institutions and special schools
* Smart accessibility tools in hospitals or public spaces


## 📈 Future Enhancements

* Add voice command-to-gesture translation
* Integrate with wearable devices
* Improve gesture vocabulary with dynamic learning
* Support for multiple regional languages


