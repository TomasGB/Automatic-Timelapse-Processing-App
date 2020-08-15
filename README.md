# Automatic Timelapse Processing App

This application is capable of taking the photos according to the specified time interval, apply color correction and finally exporting two mp4 files, one with color correction and the other without.

## How it works?

After taking the photos, runs the function 'AnalizarExposicion' declared in the file analizar_exposicion.py wich takes every photo, convert them from RGB to HSV, calculates the average V value, applies a suitable enhancement and saves them, then on these new photos runs the function 'EQ_Histograma' wich applies CLAHE (contrast limited adaptive histogram equalization) wich refines the overall look of the photos to finally export them as an mp4 file.

## Requierements

* OpenCV  [Link](https://opencv.org/)
* Pillow (PIL) [Link](https://python-pillow.org/)

## How to use:

* Open up command prompt / terminal
* Change directory with cd to the location of the program 
* Run by typing "python timelapse.py"
* First you need to enter how long do you want to take photos (enter the amount in minutes).
* Then enter the interval beetwen each photo (enter the amount in seconds).
* Finally type 'y' if you want to keep the original photos or 'n' if you want to delete them, and the same for the processed photos.

## Aditional comments

In the 'timelapse.py' file, in 'video = cv2.VideoCapture(0)'  the 0 indicates the default image capture device on your computer, if you have more than one maybe you will need to change that number.
