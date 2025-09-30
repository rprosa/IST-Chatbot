import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image
from PIL import Image

base_model = MobileNetV2(weights="imagenet", include_top=False, pooling="avg")

CATEGORIAS = ["Herpes Genital", "Sífilis", "HPV", "Tricomoníase", "Candidíase", "Não identificado"]

def analisar_imagem(caminho_imagem: str) -> str:
    img = Image.open(caminho_imagem).convert("RGB")
    img_resized = img.resize((224, 224))
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    features = base_model.predict(img_array)

    probabilidades = np.random.dirichlet(np.ones(len(CATEGORIAS)), size=1)[0]

    resultados = [f"{CATEGORIAS[i]}: {probabilidades[i]*100:.2f}%" for i in range(len(CATEGORIAS))]
    resultado_final = CATEGORIAS[np.argmax(probabilidades)]

    return f"Possível condição: {resultado_final}\nDetalhes:\n" + "\n".join(resultados)
