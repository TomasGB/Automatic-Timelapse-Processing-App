# Automatic Timelapse Processing App

This application is capable of taking the photos according to the specified time interval, apply gamma correction, histogram equalization and finally exporting two mp4 files, one with color correction and the other without.

## How it works?

After taking the photos, runs the function 'gamma_correct' declared in the file ```imageProcessing.py``` wich takes every photo, convert them from RGB to HSV, calculates the average V value, applies a suitable gamma correction and saves them, then on these new photos runs the function 'Histogram_EQ' wich applies CLAHE (contrast limited adaptive histogram equalization) wich refines the overall look of the photos to finally export them as an mp4 file.

## Dependencies

-   OpenCV [Link](https://opencv.org/)
-   Pillow (PIL) [Link](https://python-pillow.org/)

## How to use:

-   Open up command prompt / terminal.
-   Install the dependencies.
-   Change directory with cd to the location of the files.
-   Run  ```main.py```.
-   First you need to enter how long do you want to take photos (enter the amount in minutes).
-   Then enter the interval between each photo (enter the amount in seconds).
-   Then type 'y' if you want to keep the processed photos or 'n' if you want to delete them.
-   Finally choose the video capture device.

## Aditional comments:

In the ```timelapse.py``` file, in ```video = cv2.VideoCapture(device)``` , device it's used to indicate the image capture device on your computer, if you want to use the default device use 0, if you have more than one maybe you will need to change it to the correct number.




## User Interface

<img src="imgs/timelapseUI.gif" width="250" height="450">

## Examples

![gif](imgs/timelapse_github.gif)

![gif](imgs/timelapse_github3.gif)

![gif](imgs/timelapse_2.gif)


