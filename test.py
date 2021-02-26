from cv2 import cv2 as cv

cam = cv.VideoCapture(2,cv.CAP_DSHOW)

cam.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

cam2 = cv.VideoCapture(2,cv.CAP_DSHOW)

cam2.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam2.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cam2.set(cv.CAP_PROP_GAMMA, 0.7)


r, frame = cam.read()
r2, frame2 = cam2.read()

frame_width = int(cam.get(3)) 
frame_height = int(cam.get(4)) 
size = (frame_width, frame_height)
print(size)

while(cam.isOpened()):

    # Capture frame-by-frame
    ret, frame = cam.read()
    r2, frame2 = cam2.read()
    if ret == True:
        cv.imshow('Frame',frame)
        cv.imshow('Frame2',frame2)
        print(cam.get(22))
        print(cam2.get(22))
    # Press Q on keyboard to  exit

        if cv.waitKey(25) & 0xFF == ord('q'):
            break
        else: 
            pass

cam.release()
cam2.release()

#closing all open windows  
cv.destroyAllWindows()  