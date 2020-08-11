import cv2
import numpy as np
import glob 
import os
from PIL import Image, ImageEnhance


def ConvertirAVideoConCorreccion(imgs_corregidas,borrar_imgs_corregidas):
    i=0

    imgs_hsv_direc='timelapses-imgs'                                 #direccion donde estan las fotos sin correccion
    lista_imgs_hsv = glob.glob(f"{imgs_hsv_direc}/*.jpg")                   #glob busca todos los archivos con el formato especificado
    imgs_hsv_ordenadas = sorted(lista_imgs_hsv, key=os.path.getmtime)       # las ordena por numero
    imgs_corregidas ='hsv_imgs/gamma/corregidas'                            #direccion donde se van a guardar las fotos con la correccion hecha

    if not os.path.exists(imgs_corregidas):
        os.mkdir(imgs_corregidas)

    acum = 0

    #for file in os.listdir(imgs_hsv_direc)  Recorre todos los archivos de la direccion

    for file in os.listdir(imgs_hsv_direc):
        filename = f"{imgs_hsv_direc}/{i}.jpg"                      #Le da formato al nombre para que queden ordenadas
        image = cv2.imread(filename)                                
        hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)           #Convierte las fotos de BGR a HSV
        v_avg = cv2.mean(hsvImage)                                  #Calcula el promedio de los tres canales ([0]: Hue [1]: Saturation [2]:Value) de todos los pixeles de la foto
        img = Image.open(filename)                                  #Se abre la imagen para PIL
        nombrecorr = f"{imgs_corregidas}/{i}.jpg"                   #Les da nombre para la nueva direccion
        
        #Parametros limite para la correcion

        if v_avg[2] >= 40:
            img.save(nombrecorr)
        elif v_avg[2] < 40 and v_avg[2] > 35:
            en = ImageEnhance.Brightness(img)
            img = en.enhance(1.6)
            img.save(nombrecorr)
        else: 
            en = ImageEnhance.Brightness(img)
            img = en.enhance(1.7)
            img.save(nombrecorr)

        
        print(v_avg[2], 'imagen:',i)
        acum = acum + v_avg[2]
        i+=1

    v_medioTotal=acum/i

    print('Brillo promedio en todo el timelapse: ',v_medioTotal)

