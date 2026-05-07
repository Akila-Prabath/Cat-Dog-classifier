from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import webbrowser
from threading import Timer

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model('model/cat_dog_model.keras')

# Upload folder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Prediction function
def predict(img_path):

    # Resize image to 128x128
    img = image.load_img(img_path, target_size=(128, 128))

    # Convert image to array
    img_array = image.img_to_array(img)

    # Normalize image
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)

    confidence = prediction[0][0]

    if confidence > 0.5:
        result = "Dog 🐶"
        confidence_percent = round(confidence * 100, 2)
    else:
        result = "Cat 🐱"
        confidence_percent = round((1 - confidence) * 100, 2)

    return result, confidence_percent


# Home route
@app.route('/', methods=['GET', 'POST'])
def index():

    result = None
    confidence = None
    image_path = None

    if request.method == 'POST':

        file = request.files['file']

        if file:

            # Save uploaded image
            image_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(image_path)

            # Predict image
            result, confidence = predict(image_path)

    return render_template(
        'index.html',
        result=result,
        confidence=confidence,
        image=image_path
    )


# Open browser automatically
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")


# Run Flask app
if __name__ == "__main__":

    Timer(1, open_browser).start()

    app.run(debug=True)