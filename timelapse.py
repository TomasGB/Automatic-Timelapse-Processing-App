# Python program to save a  
# video using OpenCV 
  
import os   
import cv2 
import datetime
import time
import glob  
   
# Create an object to read  
# from camera 
video = cv2.VideoCapture(0) 
   
# We need to check if camera 
# is opened previously or not 
if (video.isOpened() == False):  
    print("Error reading video file") 
  

frame_width = int(video.get(3)) 
frame_height = int(video.get(4)) 
   
size = (frame_width, frame_height) #720px
  
#cv2.VideoWriter('nombre del archivo con extencion',  cv2.VideoWriter_fourcc(*'Codec'), fps, resolucion)
result = cv2.VideoWriter('timelapse.avi',  cv2.VideoWriter_fourcc(*'MJPG'), 24.97, size) 

duracion=20
intervaloFoto = 0.5 
imgs_direc = 'timelapses-imgs'

if not os.path.exists(imgs_direc):
    os.mkdir(imgs_direc)

ahora = datetime.datetime.now()
fin = ahora + datetime.timedelta(seconds=duracion)

i = 0


while datetime.datetime.now() < fin:
    ret, frame = video.read()
    print('Tiempo restante:',fin-datetime.datetime.now())
    filename = f"{imgs_direc}/{i}.jpg"
    i+=1
    cv2.imwrite(filename, frame)
    time.sleep(intervaloFoto) #controla cada cuanto se saca una foto
    #result.write(frame)
    #cv2.imshow('Frame', frame) # para capturar video
    if cv2.waitKey(1) & 0xFF == ord('s'): 
            break

borrar_imgs = True

def ConvertirAVideo(result,imgs_direc,borrar_imgs=True):
    lista_imgs = glob.glob(f"{imgs_direc}/*.jpg")
    imgs_ordenadas = sorted(lista_imgs, key=os.path.getmtime)

    for file in imgs_ordenadas:
        image_frame = cv2.imread(file)
        print('procesando...')
        result.write(image_frame)
    if borrar_imgs:
        for file in lista_imgs:
            os.remove(file)

ConvertirAVideo(result,imgs_direc,borrar_imgs)


# When everything done, release  
# the video capture and video  
# write objects 
video.release() 
result.release() 
    
# Closes all the frames 
cv2.destroyAllWindows() 
   
print("El Timelapse termino de procesarse.") 