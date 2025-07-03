from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
from imgpred import predict_image
from livepredi import video_feed
from flask import send_from_directory


app = Flask(__name__)

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/static/<path:filename>')
def send_static(filename):
    return send_from_directory('static', filename, cache_timeout=3600)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')  

@app.route('/spechorpredi')
def spechorpredi():
    return render_template('spechorpredi.html')  # Choose speech or sign

@app.route('/speech')
def speech():
    return render_template('speech.html')  # Speech recognition page

@app.route('/sign')
def sign():
    return render_template('sign.html')  # Sign language options page

@app.route('/imgpred')
def imgpredi():
    return render_template('imgpred.html')  # Image prediction upload page

@app.route('/predict', methods=['POST'])
def predict():
    # Get model type (ASL or Gesture) from form
    model_type = request.form['model_type']

    # Check if the post request has the file
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # If no file is selected
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # If the file is allowed, process it
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('uploads', filename)
        file.save(filepath)

        # Call the predict_image function from imgpred.py
        label = predict_image(filepath, model_type)

        # Return prediction as JSON response
        return jsonify({'prediction': label}), 200
    else:
        return jsonify({'error': 'Invalid file format'}), 400

@app.route('/livepred')
def livepredi():
    return render_template('livepred.html')  # Live video page

@app.route('/video_feed')
def video_feed_route():
    return video_feed()  # Start video stream for ASL detection

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
