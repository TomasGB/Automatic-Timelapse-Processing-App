import cv2
import numpy as np
import math
import glob 
import os

def gamma_correct():
    i=0

    imgs_hsv_direc= 'timelapse_imgs'                 #direccion donde estan las fotos sin correccion
    lista_imgs_hsv = glob.glob(f"{imgs_hsv_direc}/*.jpg")                   #glob busca todos los archivos con el formato especificado
    imgs_hsv_ordenadas = sorted(lista_imgs_hsv, key=os.path.getmtime)       # las ordena por numero
    imgs_corregidas = 'hsv_imgs'                            #direccion donde se van a guardar las fotos con la correccion hecha

    if not os.path.exists(imgs_corregidas):
        os.mkdir(imgs_corregidas)

    acum = 0

    for file in os.listdir(imgs_hsv_direc):
        filename = f"{imgs_hsv_direc}/{i}.jpg"
        image = cv2.imread(filename)                                
        hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)           #Convierte las fotos de BGR a HSV
        v_avg = cv2.mean(hsvImage)
        nombrecorr = f"{imgs_corregidas}/{i}.jpg"

        if round(v_avg[2]) >= 150:
            gamma_corr_img = np.array(255*(image/255)**1.2,dtype='uint8')
            cv2.imwrite(nombrecorr,gamma_corr_img)
        elif round(v_avg[2]) < 150 and round(v_avg[2]) >= 90:
            gamma_corr_img = image
            cv2.imwrite(nombrecorr,gamma_corr_img)
        elif round(v_avg[2]) < 90 and round(v_avg[2]) >= 85:
            gamma_corr_img = np.array(255*(image/255)**0.95,dtype='uint8')
            cv2.imwrite(nombrecorr,gamma_corr_img)
        elif round(v_avg[2]) < 85 and round(v_avg[2]) >= 70:
            gamma_corr_img = np.array(255*(image/255)**0.9,dtype='uint8')
            cv2.imwrite(nombrecorr,gamma_corr_img)
        elif round(v_avg[2]) < 70 and round(v_avg[2]) >= 60:
            gamma_corr_img = np.array(255*(image/255)**0.85,dtype='uint8')
            cv2.imwrite(nombrecorr,gamma_corr_img)
        elif round(v_avg[2]) < 60 and round(v_avg[2]) >= 50:
            gamma_corr_img = np.array(255*(image/255)**0.8,dtype='uint8')
            cv2.imwrite(nombrecorr,gamma_corr_img)
        elif round(v_avg[2]) < 50 and round(v_avg[2]) >= 55:
            gamma_corr_img = np.array(255*(image/255)**0.75,dtype='uint8')
            cv2.imwrite(nombrecorr,gamma_corr_img)
        else: 
            gamma_corr_img = np.array(255*(image/255)**0.7,dtype='uint8')
            cv2.imwrite(nombrecorr,gamma_corr_img)
        print('Exposicion: ',round(v_avg[2]), 'imagen:',i)
        acum = acum + round(v_avg[2])
        i = i + 1

