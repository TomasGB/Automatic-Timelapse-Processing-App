import os   
import cv2 
import datetime
import time
import glob
import analizar_exposicion
import histogramEQ

# Crea el objeto para leer de la camara
video = cv2.VideoCapture(0) 
   
# Checkea que ande la camara

if (video.isOpened() == False):  
    print("Error reading video file") 
  

frame_width = int(video.get(3)) 
frame_height = int(video.get(4)) 
   
size = (frame_width, frame_height) #720px
  
#cv2.VideoWriter('nombre del archivo con extencion',  cv2.VideoWriter_fourcc(*'Codec'), fps, resolucion)
# 0x7634706d es el codigo del codec para formato mp4

result = cv2.VideoWriter('timelapse.mp4',  0x7634706d, 24.97, size)
resultCorr = cv2.VideoWriter('timelapse_eq.mp4',  0x7634706d, 24.97, size)

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


imgs_direc = 'timelapse_imgs'

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
    if borrar_imgs_corregidas:
        for file in lista_imgs:
            os.remove(file)


imgs_corregidas ='hsv_imgs'
eq_direc='eq_imgs'

if not os.path.exists(eq_direc):
    os.mkdir(eq_direc)

#crea el timelapse sin procesar
ConvertirAVideo(result,imgs_direc,borrar_imgs)

#procesamiento del timelapse
analizar_exposicion.AnalizarExposicion()
histogramEQ.EQ_Histograma(imgs_corregidas,eq_direc)
print('Fotos equalizadas')
ConvertirAVideo(resultCorr,eq_direc,borrar_imgs_corregidas)

video.release() 
result.release()
resultCorr.release() 

print("El Timelapse termino de procesarse.") 