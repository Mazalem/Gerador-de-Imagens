import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Gerador de Imagens", layout="centered")

st.title("Gerador de Imagens")
st.markdown("Escreva um prompt em inglês e receba uma imagem gerada por inteligência artificial.")

# Entrada do usuário
prompt = st.text_input("Escreva seu prompt (em inglês):", "")

if st.button("Gerar Imagem"):
    if prompt.strip():
        with st.spinner("Gerando Imagem..."):
            img = generate_image(prompt)  # chama função do modelo
            img_pil = Image.fromarray(np.array(img))
            st.image(img_pil, caption=prompt, use_column_width=True)
    else:
        st.warning("Por favor, insira o prompt primeiro.")
