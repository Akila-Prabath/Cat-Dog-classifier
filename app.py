from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = tf.keras.models.load_model('model/model.h5')

def predict(img_path):
    img = image.load_img(img_path, target_size=(150,150))
    img_array = image.img_to_array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    return "Dog 🐶" if prediction[0][0] > 0.5 else "Cat 🐱"

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        path = os.path.join('static/uploads', file.filename)
        file.save(path)

        result = predict(path)
        return render_template('index.html', result=result, image=path)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)