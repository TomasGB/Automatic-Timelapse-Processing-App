import os   
import cv2 
import datetime
import time
import glob
import histogramEQ
import gamma

def timelapseCrear(duracionG,intervaloFoto,fotosp,dispositivo):

    video = cv2.VideoCapture(dispositivo) 

    if (video.isOpened() == False):  
        print("Error reading video file") 
    

    frame_width = int(video.get(3)) 
    frame_height = int(video.get(4)) 
    size = (frame_width, frame_height)
    
    #cv2.VideoWriter('filename',  cv2.VideoWriter_fourcc(*'Codec'), fps, resolution)
    # 0x7634706d codec code for mp4 format

    result = cv2.VideoWriter('timelapse.mp4',  0x7634706d, 24.97, size)
    resultCorr = cv2.VideoWriter('timelapse_eq.mp4',  0x7634706d, 24.97, size)

    #Configurar los parametros del el timelapse
    
    fotosp = fotosp.lower()
    
    borrar_imgs = False

    if fotosp == 'y' : 
        borrar_imgs_corregidas = False 
    elif fotosp == 'n' :
        borrar_imgs_corregidas = True
    else:
        print('There was an error')

    duracion = duracionG * 60

    imgs_direc = 'timelapse_imgs'

    if not os.path.exists(imgs_direc):
        os.mkdir(imgs_direc)

    ahora = datetime.datetime.now()
    fin = ahora + datetime.timedelta(seconds=duracion)

    i = 0

    #takes the photos in the specified duration

    while datetime.datetime.now() < fin:
        ret, frame = video.read()
        print('Time left:',fin-datetime.datetime.now())
        filename = f"{imgs_direc}/{i}.jpg"
        i+=1
        cv2.imwrite(filename, frame)
        time.sleep(intervaloFoto)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
                break

    def ConvertirAVideo(result,imgs_direc,borrar_imgs):
        lista_imgs = glob.glob(f"{imgs_direc}/*.jpg")
        imgs_ordenadas = sorted(lista_imgs, key=os.path.getmtime)

        for file in imgs_ordenadas:
            image_frame = cv2.imread(file)
            print('processing photos...')
            result.write(image_frame)

        if borrar_imgs:
            for file in lista_imgs:
                os.remove(file)
            
    imgs_corregidas ='hsv_imgs'
    eq_direc='eq_imgs'

    if not os.path.exists(eq_direc):
        os.mkdir(eq_direc)

    #creates the timelapse without processing
    ConvertirAVideo(result,imgs_direc,borrar_imgs)

    #timelapse processing
    gamma.gamma_correct()
    histogramEQ.EQ_Histograma(imgs_corregidas,eq_direc)

    #creates the timelapse with processing
    ConvertirAVideo(resultCorr,eq_direc,borrar_imgs_corregidas)

    video.release() 
    result.release()
    resultCorr.release() 
    print("The Timelapse it's finished.") 