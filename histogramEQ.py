import cv2
import os
from PIL import Image, ImageEnhance

def EQ_Histograma(imgs_corregidas,eq_direc):
    i = 0
    for file in os.listdir(imgs_corregidas):
        print('Equalizando foto: ',i)
        filename = f"{imgs_corregidas}/{i}.jpg"
        img_eq = cv2.imread(filename, 1)
        img_eq = cv2.cvtColor(img_eq, cv2.COLOR_HSV2RGB)
        R, G, B = cv2.split(img_eq)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        output2_R = clahe.apply(R)
        output2_G = clahe.apply(G)
        output2_B = clahe.apply(B)
        
        imgen_eq = cv2.merge((output2_R, output2_G, output2_B))
        img = Image.open(filename)
        nombreeq = f"{eq_direc}/{i}.jpg"

        img.save(nombreeq)
        os.remove(filename)
        i +=1
        
