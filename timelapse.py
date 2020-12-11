import os   
import cv2
import datetime
import time
import glob
import histogramEQ
import gamma

def timelapseCrear(durationG,photosInterval,procPhotosKeep,device):

    video = cv2.VideoCapture(device) 

    if (video.isOpened() == False):  
        print("Error reading video file") 
        return quit
    

    frame_width = int(video.get(3)) 
    frame_height = int(video.get(4)) 
    size = (frame_width, frame_height)
    
    #cv2.VideoWriter('filename',  cv2.VideoWriter_fourcc(*'Codec'), fps, resolution)
    #0x7634706d codec code for mp4 format

    result = cv2.VideoWriter(f'timelapse.mp4',  0x7634706d, 24.97, size)
    resultCorr = cv2.VideoWriter(f'timelapse_processed.mp4',  0x7634706d, 24.97, size)

    #Timelapse parameters config
    
    procPhotosKeep = procPhotosKeep.lower()
    
    delete_imgs = False

    if procPhotosKeep == 'y' : 
        delete_processed_imgs = False 
    elif procPhotosKeep == 'n' :
        delete_processed_imgs = True
    else:
        print('There was an error')

    duration = durationG * 60

    imgs_direc = 'timelapse_imgs'

    if not os.path.exists(imgs_direc):
        os.mkdir(imgs_direc)

    now = datetime.datetime.now()
    end = now + datetime.timedelta(seconds=duration)

    i = 0

    #takes the photos in the specified duration

    while datetime.datetime.now() < end:
        ret, frame = video.read()
        print('Time left:',fin-datetime.datetime.now())
        filename = f"{imgs_direc}/{i}.jpg"
        i+=1
        cv2.imwrite(filename, frame)
        time.sleep(photosInterval)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
                break

    def ConvertirAVideo(result,imgs_direc,delete_imgs):
        list_imgs = glob.glob(f"{imgs_direc}/*.jpg")
        imgs_ordered = sorted(list_imgs, key=os.path.getmtime)

        for file in imgs_ordered:
            image_frame = cv2.imread(file)
            print('processing photos...')
            result.write(image_frame)

        if delete_imgs:
            for file in list_imgs:
                os.remove(file)
            
    processed_imgs ='hsv_imgs'
    eq_direc='eq_imgs'

    if not os.path.exists(eq_direc):
        os.mkdir(eq_direc)

    #creates the timelapse without processing
    ConvertirAVideo(result,imgs_direc,delete_imgs)

    #timelapse processing
    gamma.gamma_correct()
    histogramEQ.EQ_Histograma(processed_imgs,eq_direc)

    #creates the timelapse with processing
    ConvertirAVideo(resultCorr,eq_direc,delete_processed_imgs)

    video.release() 
    result.release()
    resultCorr.release() 
    print("The Timelapse it's finished.") 