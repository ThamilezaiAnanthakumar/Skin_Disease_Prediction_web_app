# -*- coding: utf-8 -*-
"""Copy of app_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KlwLksKOucMrrmv7srAXay4A7JTfQKS6
"""




#https://github.com/ThamilezaiAnanthakumar/Skin_Disease_Prediction_web_app/commits/v2.3.4








import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
from tensorflow.keras.models import load_model


model_url = 'https://github.com/ThamilezaiAnanthakumar/Skin_Disease_Prediction_web_app/commits/v2.3.4'

# Path where the model will be saved locally
model_path = 'skin_disease_2.h5'

# Download the model if it doesn't exist locally
if not os.path.exists(model_path):
    st.write("Downloading the model from GitHub...")
    response = requests.get(model_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        with open(model_path, 'wb') as f:
            f.write(response.content)
        st.write("Model downloaded successfully!")
    else:
        st.error("Failed to download the model. Please check the model URL.")




#model_path='/content/skin_disease_2.h5' -- in cloab path
# Load the trained model
#model = load_model(model_path)  # Ensure this file exists in the directory
model = tf.keras.models.load_model(model_path)

# Define class labels (must match training labels)
classses =['BA-impetigo', 'FU-ringworm', 'VI-chickenpox', 'VI-shingles', 'FU-athlete-foot', 'FU-nail-fungus', 'BA- cellulitis', 'PA-cutaneous-larva-migrans']# Modify as per your dataset

# Function to preprocess image
def preprocess_image(img):
    img = img.resize((128, 128))  # Change size according to model input
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Expand dims for model input
    return img_array

# Streamlit UI
st.title("🩺 Skin Disease Prediction App")
st.write("Upload an image to predict the skin condition.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)  # Open image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    img_array = preprocess_image(img)

    # Make prediction
    prediction = model.predict(img_array)
    predicted_class = classes[np.argmax(prediction)]

    # Display Prediction
    st.success(f"🩹 Predicted Skin Disease: **{predicted_class}**")



