
# Production date: ‎Sunday, ‎3 ‎September ‎2023, ‏‎15:42:51

# Modification date: Thursday, ‎23 ‎December ‎2021, ‏‎19:08:30

"""
B03 = r
B06 = g
B08 = b

Il faut écrire 3 fonctions qui font les calculs des index suivants:
NDWI: Normalized Differentiated Water Index
PI: Plastic Index
FDI: Floating Debris Index
18 h 25
Les formules sont les suivantes:
NDWI = (B03 – B08)/(B03 + B08) ==> (r - b) / (r + b)
PI = B08/(B08 + B04) ==> b / (b + g)
FDI = B08 – [B06 + (B11 – B06) * 832.8-664.6 * 10]
18 h 25
Pour cela tu peux t’inspirer du code que nous avons utilisé l’an dernier pour NDVI
"""
import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def get_dnwi(image, image_path):
    image = cv2.imread(image_path)
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom == 0] = 0.00001
    nvdi_image = (r.astype(float) - b.astype(float))/bottom
    return nvdi_image

def get_pi(image, image_path):
    image = cv2.imread(image_path)
    b, g, r = cv2.split(image)
    bottom = (b.astype(float) + g.astype(float))
    bottom[bottom == 0] = 0.00001
    nvdi_image = b.astype(float)/bottom
    return nvdi_image

image_path = "C:\Users\emirh\OneDrive\Bureau\My World(Don't change)\dosyalar\Kodlarim\Python\Astro Pi\image.png"

image = Image.open("image.png")

get_dnwi(image, image_path)

image = Image.open("image.png")

get_pi(image, image_path)
