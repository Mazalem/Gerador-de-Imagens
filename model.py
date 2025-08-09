import keras_cv
from tensorflow import keras

# Otimização para velocidade
keras.mixed_precision.set_global_policy("mixed_float16")

# Carrega Stable Diffusion 512x512
model = keras_cv.models.StableDiffusion(
    img_width=512,
    img_height=512,
    jit_compile=True
)

def generate_image(prompt: str):
    images = model.text_to_image(prompt, batch_size=1)
    return images[0]  # retorna a imagem única
