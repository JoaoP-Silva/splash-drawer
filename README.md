<p align="right">
  <a target="_blank" href="https://colab.research.google.com/github/JoaoP-Silva/splash-drawer/blob/main/splash_drawer.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
</p>

# splash-drawer
A pix2pix model trained to generate League of Legends splash arts from sketches.

# Introduction
_splah-drawer_ is a pix2pix model trained to generate League of Legends splash arts from sketches.

![example](https://github.com/user-attachments/assets/98dafef7-1759-4e79-b587-0f410b26ed61)

The network is trained in an adversarial way, where we have a generator model and a discriminator model. However, unlike conventional GANs, the pix2pix model conditions both models, generator and discriminator, on an "real" image. 

In this project, the pix2pix model was trained to generate splash art images of league of legends champions, conditioned on the original splash art image. In this way, the splash-drawer works as a splash art generator, which receives a sketch input and generates a league of legends style splash art.

# Scripts
The _scripts_ folder contains a colletion of useful methods to help with the setup of the project. Every script in the folder must be called from the root DIR.

```python 
python3 scripts/scrapper.py #example
```
The model was trained with 78 splash art images from the [WestStudio website](https://www.weststudio.com/project/league-of-legends-splash-art). To uncompress the database, call ```sh scripts/unzip_data.sh```. 

The images were downloaded from the web using [scripts/scrapper.py](https://github.com/JoaoP-Silva/splash-drawer/blob/main/scripts/scrapper.py). To make the training easier, all images were resized to 256x256px using [scripts/resize.py](https://github.com/JoaoP-Silva/splash-drawer/blob/main/scripts/resize.py). Sketches were obtained using the OpenGL lib in [scripts/gen_scketches.py](https://github.com/JoaoP-Silva/splash-drawer/blob/main/scripts/gen_sketches.py).

# Train the model
The model training code is in the jupyter notebook [splash_drawer.ipynb](https://github.com/JoaoP-Silva/splash-drawer/blob/main/splash_drawer.ipynb). The code was entirely based on [Jason Browlee's](https://machinelearningmastery.com/how-to-develop-a-pix2pix-gan-for-image-to-image-translation/) amazing blog article.
