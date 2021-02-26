from cv2 import cv2
import numpy as np
import math
import glob
import os
from PIL import Image, ImageEnhance

<<<<<<< HEAD:imageProcessing.py

def gamma_correct(imgs_direc,processed_imgs):
    #'imgs_direc' directory where the photos without correction are
    #'processed_imgs' directory where the photos with the correction are going to be saved

    i=0
=======

def gamma_correct():

    i = 0
    # directory where the photos without correction are
    imgs_hsv_direc = 'timelapse_imgs'

    # directory where the photos with the correction are going to be saved
    processed_imgs = 'hsv_imgs'
>>>>>>> eb66cfd72c9da038b14450e7ec6263f46563f33a:gamma.py

    if not os.path.exists(processed_imgs):
        os.mkdir(processed_imgs)

    acum = 0

    for file in os.listdir(imgs_direc):
        filename = f"{imgs_direc}/{i}.jpg"
        image = cv2.imread(filename)

        # Converts the photos from RGB to HSV and calculates the avarage V value for each photo
        # to later apply the gamma correction needed

        hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        v_avg = cv2.mean(hsvImage)
        nameProcessed = f"{processed_imgs}/{i}.jpg"

        if round(v_avg[2]) >= 150:
            gamma_corr_img = np.array(255 * (image / 255)**1.1, dtype='uint8')
            cv2.imwrite(nameProcessed, gamma_corr_img)
        elif round(v_avg[2]) < 150 and round(v_avg[2]) >= 90:
            gamma_corr_img = image
            cv2.imwrite(nameProcessed, gamma_corr_img)
        elif round(v_avg[2]) < 90 and round(v_avg[2]) >= 85:
            gamma_corr_img = np.array(255 * (image / 255)**0.95, dtype='uint8')
            cv2.imwrite(nameProcessed, gamma_corr_img)
        elif round(v_avg[2]) < 85 and round(v_avg[2]) >= 70:
            gamma_corr_img = np.array(255 * (image / 255)**0.9, dtype='uint8')
            cv2.imwrite(nameProcessed, gamma_corr_img)
        elif round(v_avg[2]) < 70 and round(v_avg[2]) >= 60:
            gamma_corr_img = np.array(255 * (image / 255)**0.85, dtype='uint8')
            cv2.imwrite(nameProcessed, gamma_corr_img)
        elif round(v_avg[2]) < 60 and round(v_avg[2]) >= 50:
            gamma_corr_img = np.array(255 * (image / 255)**0.8, dtype='uint8')
            cv2.imwrite(nameProcessed, gamma_corr_img)
        elif round(v_avg[2]) < 50 and round(v_avg[2]) >= 55:
            gamma_corr_img = np.array(255 * (image / 255)**0.75, dtype='uint8')
            cv2.imwrite(nameProcessed, gamma_corr_img)
        else:
            gamma_corr_img = np.array(255 * (image / 255)**0.7, dtype='uint8')
            cv2.imwrite(nameProcessed, gamma_corr_img)
        print('Brightness: ', round(v_avg[2]), 'Photo:', i)
        acum = acum + round(v_avg[2])
        i = i + 1
<<<<<<< HEAD:imageProcessing.py


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

=======
>>>>>>> eb66cfd72c9da038b14450e7ec6263f46563f33a:gamma.py
