import cv2
import os
from PIL import Image, ImageEnhance

def EQ_Histograma(processed_imgs,eq_direc):
    
    i = 0
    for file in os.listdir(processed_imgs):
        print('Equalizing photo: ',i)
        filename = f"{processed_imgs}/{i}.jpg"
        img_eq = cv2.imread(filename, 1)
        img_eq = cv2.cvtColor(img_eq, cv2.COLOR_HSV2RGB)
        R, G, B = cv2.split(img_eq)

        #apply CLAHE to each RGB channel
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        output2_R = clahe.apply(R)
        output2_G = clahe.apply(G)
        output2_B = clahe.apply(B)
        
        #Merge the channels again
        img_eq = cv2.merge((output2_R, output2_G, output2_B))
        img = Image.open(filename)
        nameEq = f"{eq_direc}/{i}.jpg"

        img.save(nameEq)
        os.remove(filename)
        i +=1
