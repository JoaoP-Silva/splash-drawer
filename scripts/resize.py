import cv2
import os

input_dir = "data/original_splash_arts"
output_dir = "data/splash_arts"
os.makedirs(output_dir, exist_ok=True)

# New size
target_size = (256, 256)

def resize_image(image_path, save_path):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, target_size)
    cv2.imwrite(save_path, resized_image)
    print(f"Imagem redimensionada e salva em: {save_path}")

# Iterate over all images
for img_name in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_name)
    save_path = os.path.join(output_dir, img_name)
    resize_image(img_path, save_path)

print("Redimensionamento completo!")
