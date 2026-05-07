# 🐱 Cat vs 🐶 Dog Classifier

A deep learning web application that classifies images of cats and dogs using a Convolutional Neural Network (CNN) built with TensorFlow and deployed with Flask.

---

## 🚀 Features

-  Cat vs Dog image classification
-  TensorFlow CNN model
-  Modern Flask web interface
-  Upload and predict images instantly
-  Confidence score prediction
-  Responsive UI design
-  Data augmentation support
-  Model performance evaluation

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| TensorFlow / Keras | Deep learning framework |
| Flask | Backend web framework |
| HTML / CSS | Frontend UI |
| NumPy | Numerical processing |
| Matplotlib | Visualization |
| Scikit-learn | Evaluation metrics |
| Jupyter Notebook | Model training |
| Kaggle Dataset | Training dataset |

---

## 📂 Project Structure

```bash
Cat-Dog-classifier/
│
├── dataset/
│   ├── train/
│   │   ├── cats/
│   │   └── dogs/
│   │
│   └── test/
│       ├── cats/
│       └── dogs/
│
├── model/
│   └── cat_dog_model.keras
│
├── notebooks/
│   ├── traing_transfer_learning.ipynb
│   └── training.ipynb
│
├── static/
│   └── uploads/
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📦 Dataset

Dataset used from Kaggle:

🔗 https://www.kaggle.com/datasets/dineshpiyasamara/cats-and-dogs-for-classification

The dataset contains:
- Cats images
- Dogs images
- Training and testing folders

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Akila-Prabath/Cat-Dog-classifier.git
cd Cat-Dog-classifier
```

---

### 2️⃣ Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Flask Application

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

## 🧠 Model Architecture

This project was developed using two deep learning approaches:

### 🔹 Scratch CNN Model
A custom CNN model was first trained from scratch using TensorFlow and Keras.

#### Performance
| Metric | Result |
|---|---|
| Training Accuracy | ~72% |
| Validation Accuracy | ~48% |

The scratch model showed overfitting and lower validation performance.

---

### 🚀 Transfer Learning Model (Final Model)

The final model uses the pretrained Xception architecture with transfer learning for better accuracy and performance.

```python
pretrained_model = tf.keras.applications.xception.Xception(
    include_top=False,
    input_shape=(128,128,3),
    weights='imagenet',
    pooling='max'
)

for layer in pretrained_model.layers:
    layer.trainable = False

model = tf.keras.Sequential([
    pretrained_model,

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),

    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

### 📈 Final Model Performance

| Metric | Result |
|---|---|
| Training Accuracy | ~99% |
| Validation Accuracy | ~95% |

The transfer learning model achieved significantly higher accuracy and better generalization, making it the final deployed model.

### Evaluation Methods

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 🖼️ Application UI

### Features

- Modern responsive design
- Two-column layout
- Image upload panel
- Prediction result display
- Confidence percentage
- Uploaded image preview

---

## 🧪 Training the Model

Open Jupyter Notebook:

```bash
jupyter notebook
```

Run:

```bash
notebooks/traing_transfer_learning.ipynb
```

The notebook includes:
- Data preprocessing
- Data augmentation
- CNN model training
- Evaluation
- Prediction testing

---

## 📦 requirements.txt

```txt
tensorflow
flask
numpy
pillow
matplotlib
pandas
scikit-learn
jupyter
kaggle
seaborn
opencv-python
```

---

## 🚀 Future Improvements

- 🔥 MobileNetV2 Transfer Learning
- 🌐 React Frontend
- 📱 Mobile Responsive Enhancements
- ☁️ Cloud Deployment
- 🎥 Real-time Webcam Detection
- 🐾 Multi-animal Classification

---

## 📸 Screenshots

### 🏠 Home Page
<img width="1914" height="890" alt="Screenshot (489)" src="https://github.com/user-attachments/assets/843adfa2-f2e1-4a16-ad3c-7e11b47e7cba" />

Modern AI-powered image classification interface.

### 📷 Prediction Result

Displays:
- Uploaded image
- Prediction label
- Confidence percentage

---

## 👨‍💻 Author

### Akila Prabath

Software Engineering Undergraduate  
Passionate about:
- AI & Machine Learning
- Full Stack Development
- Computer Vision
- Deep Learning

GitHub:
🔗 https://github.com/Akila-Prabath

---

## ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the repository  
📢 Share the project

---

## 📄 License

This project is licensed under the MIT License.
