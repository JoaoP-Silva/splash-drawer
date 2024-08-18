import os
import requests
from bs4 import BeautifulSoup
import time

# Função para baixar a imagem a partir da URL
def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Imagem salva em: {save_path}")
    else:
        print(f"Falha ao baixar a imagem de {url}")

# URL do site
base_url = "https://www.weststudio.com/project/league-of-legends-splash-art"

# Diretório onde as imagens serão salvas
save_directory = "data/splash_arts"
os.makedirs(save_directory, exist_ok=True)

# Faz a requisição para a página
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontra todos os elementos com a classe "project-image-block"
blocks = soup.find_all('div', class_='project-image-block')

for block in blocks:
    img_tag = block.find('img')
    if img_tag and 'src' in img_tag.attrs:
        img_url = img_tag['src']
        img_name = os.path.basename(img_url)
        save_path = os.path.join(save_directory, img_name)
        download_image(img_url, save_path)
        # Adiciona um intervalo entre as requisições para não sobrecarregar o servidor
        time.sleep(1)

print("Download completo!")