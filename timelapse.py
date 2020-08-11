import os   
import cv2 
import datetime
import time
import glob
import analizar_exposicion

  
# Crea el objeto para leer de la camara
video = cv2.VideoCapture(0) 
   
# Checkea que ande la camara

if (video.isOpened() == False):  
    print("Error reading video file") 
  

frame_width = int(video.get(3)) 
frame_height = int(video.get(4)) 
   
size = (frame_width, frame_height) #720px
  
#cv2.VideoWriter('nombre del archivo con extencion',  cv2.VideoWriter_fourcc(*'Codec'), fps, resolucion)
#result = cv2.VideoWriter('timelapse.avi',  cv2.VideoWriter_fourcc(*'MJPG'), 24.97, size) 
# 0x7634706d es el codigo del codec para formato mp4

result = cv2.VideoWriter('timelapse.mp4',  0x7634706d, 24.97, size)
resultCorr = cv2.VideoWriter('timelapse_Corregido.mp4',  0x7634706d, 24.97, size)

#Configurar los parametros del el timelapse

print('Ingrese durante cuanto tiempo desea grabar (minutos):' )
DuracionDeGrabar=int(input())#180 #en minutos
duracion = DuracionDeGrabar*60 
print('Ingrese el intervalo entre cada foto (segundos): ')
intervaloFoto = float(input())#1
print('Conservar las fotos (y/n):')
Fotos = input()
Fotos = Fotos.lower()

if Fotos == 'y' : 
    borrar_imgs = False 
elif Fotos == 'n' :
    borrar_imgs = True
else:
    print('Hubo un error')

print('Conservar las fotos Corregidas (y/n):')
FotosCorr = input()
FotosCorr = FotosCorr.lower()

if FotosCorr == 'y' : 
    borrar_imgs_corregidas = False 
elif FotosCorr == 'n' :
    borrar_imgs_corregidas = True
else:
    print('Hubo un error')


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
    if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

def ConvertirAVideo(result,imgs_direc,borrar_imgs):
    lista_imgs = glob.glob(f"{imgs_direc}/*.jpg")
    imgs_ordenadas = sorted(lista_imgs, key=os.path.getmtime)

    for file in imgs_ordenadas:
        image_frame = cv2.imread(file)
        print('procesando fotos...')
        result.write(image_frame)
    if borrar_imgs:
        for file in lista_imgs:
            os.remove(file)

imgs_corregidas ='hsv_imgs/gamma/corregidas'

#"""imgs_direc,borrar_imgs"""

ConvertirAVideo(result,imgs_direc,borrar_imgs)

analizar_exposicion.ConvertirAVideoConCorreccion(imgs_corregidas,borrar_imgs_corregidas)

ConvertirAVideo(resultCorr,imgs_corregidas,borrar_imgs)

# When everything done, release  
# the video capture and video  
# write objects 


video.release() 
result.release()
resultCorr.release() 
    
# Closes all the frames 
cv2.destroyAllWindows() 
   
print("El Timelapse termino de procesarse.") 