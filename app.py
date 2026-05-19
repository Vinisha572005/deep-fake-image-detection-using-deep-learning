import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ======================
# LOAD MODEL
# ======================
model = tf.keras.models.load_model("deepfake_model_final.keras")

# ======================
# TITLE
# ======================
st.title("🧠 Deepfake Image Detection")
st.write("Upload an image to check whether it is REAL or FAKE")

# ======================
# IMAGE UPLOAD
# ======================
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # ======================
    # PREPROCESS IMAGE
    # ======================
    img = image.resize((128, 128))
    img_array = np.array(img) / 255.0

    # Ensure 3 channels
    if img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]

    img_array = np.expand_dims(img_array, axis=0)

    # ======================
    # PREDICTION
    # ======================
    prediction = model.predict(img_array)[0][0]

    # ======================
    # RESULT
    # ======================
    if prediction > 0.5:
        st.success(f"✅ REAL IMAGE (Confidence: {prediction:.2f})")
    else:
        st.error(f"❌ FAKE IMAGE (Confidence: {1 - prediction:.2f})")