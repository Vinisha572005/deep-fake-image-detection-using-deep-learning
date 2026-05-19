# 🛡️ AI-Powered Deepfake Image Detection System

An AI-based Deepfake Image Detection system developed using **Deep Learning**, **TensorFlow**, and **Streamlit** to identify whether an uploaded image is **REAL** or **DEEPFAKE**.

---

# 📌 Project Overview

Deepfake technology uses Artificial Intelligence to generate manipulated or synthetic media that appears realistic. This project aims to detect forged or AI-generated facial images using a Convolutional Neural Network (CNN).

The system provides a simple web interface where users can upload an image and receive an authenticity prediction.

---

# 🚀 Features

✅ Deepfake Image Detection  
✅ CNN-Based Classification  
✅ Streamlit Web Interface  
✅ Image Upload Functionality  
✅ Real-Time Prediction  
✅ User-Friendly Dashboard  

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| TensorFlow/Keras | Deep Learning |
| CNN | Image Classification |
| Streamlit | Web Application |
| Pillow (PIL) | Image Processing |
| NumPy | Numerical Operations |

---

# 📂 Project Structure

```text
Deepfake-Image-Detection/
│
├── app.py
├── image_model.py
├── train_image_model.py
├── requirements.txt
│
├── models/
│     └── deepfake_cnn.h5
│
├── datasets/
│     └── images/
│           ├── real/
│           └── fake/
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Deepfake-Image-Detection.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Deepfake-Image-Detection
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📊 Dataset Preparation

Create dataset folders:

```text
datasets/images/real/
datasets/images/fake/
```

- Add real images inside `real/`
- Add deepfake/manipulated images inside `fake/`

---

# 🏋️ Train CNN Model

Run:

```bash
python train_image_model.py
```

After training, the model will be saved inside:

```text
models/deepfake_cnn.h5
```

---

# ▶️ Run Application

Start Streamlit app:

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

# 🖼️ Application Workflow

```text
Image Upload
      ↓
Image Preprocessing
      ↓
CNN Model Prediction
      ↓
REAL / DEEPFAKE Result
```

---

# 🧪 Model Architecture

The project uses a Convolutional Neural Network (CNN) consisting of:

- Convolution Layers
- MaxPooling Layers
- Flatten Layer
- Dense Layers
- Dropout Regularization

---

# 📈 Future Enhancements

- Video Deepfake Detection
- Real-Time Webcam Detection
- Grad-CAM Visualization
- Confidence Score Display
- Mobile Application Support
- Transformer-Based Detection Models

---

# 📸 Screenshots

## Home Page

<img width="1365" height="678" alt="output1" src="https://github.com/user-attachments/assets/8aae69e8-6f23-4d55-b13f-acbf3fb41b7f" />


## Prediction Result

_<img width="1365" height="620" alt="output3" src="https://github.com/user-attachments/assets/8eb0ef04-f30e-404c-bf98-919c2cb11403" />

<img width="1357" height="620" alt="output4" src="https://github.com/user-attachments/assets/88be9637-3b38-4949-929f-fd3610d5c1e2" />

---

# 🛠️ Requirements

```text
streamlit
tensorflow
numpy
pillow
```

---

# 📚 Learning Outcomes

Through this project, the following concepts were implemented:

- Deep Learning
- CNN Architecture
- Image Classification
- Streamlit Web Deployment
- AI-Based Security Systems

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository and submit a pull request for improvements.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed by 
Vinisha M

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.
