import keras_cv
from tensorflow import keras

# Otimização para velocidade
keras.mixed_precision.set_global_policy("mixed_float16")

# Cache do modelo no Streamlit
import streamlit as st
@st.cache_resource
def load_model():
    return keras_cv.models.StableDiffusion(
        img_width=512,
        img_height=512,
        jit_compile=True
    )

model = load_model()

def generate_image(prompt: str):
    images = model.text_to_image(prompt, batch_size=1)
    return images[0]
