import cv2
import os

# Diretório das imagens originais
input_dir = "data/splash_arts"
# Diretório onde os esboços serão salvos
output_dir = "data/sketches"
os.makedirs(output_dir, exist_ok=True)

# Função para gerar esboço a partir de uma imagem
def generate_sketch(image_path, save_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)
    inverted_blurred = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

    cv2.imwrite(save_path, sketch)
    print(f"Esboço salvo em: {save_path}")

# Iterar sobre todas as imagens no diretório
for img_name in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_name)
    sketch_path = os.path.join(output_dir, img_name)
    generate_sketch(img_path, sketch_path)

print("Geração de esboços completa!")