from cv2 import cv2
import numpy as np
import math
import glob
import os


def gamma_correct():

    i = 0
    # directory where the photos without correction are
    imgs_hsv_direc = 'timelapse_imgs'

    # directory where the photos with the correction are going to be saved
    processed_imgs = 'hsv_imgs'

    if not os.path.exists(processed_imgs):
        os.mkdir(processed_imgs)

    acum = 0

    for file in os.listdir(imgs_hsv_direc):
        filename = f"{imgs_hsv_direc}/{i}.jpg"
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
