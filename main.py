from tkinter import Label,Grid,LabelFrame,Entry,Tk,N
from tkinter import filedialog
from tkinter import ttk
import timelapse
import threading 
from cv2 import cv2

def devicePreview():
    cap = cv2.VideoCapture(int(Device_Entry.get()),cv2.CAP_DSHOW)

    if (cap.isOpened() == False):
        print('No video device')
        progress_label.config(text="There is no device, please try other number.", font="Helvetica 9")
        return quit
    
    progress_label.config(text=" ", font="Helvetica 9")
    while(True):
            ret, frame = cap.read()
            cv2.imshow('press "q" to close', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    cap.release()
    cv2.destroyAllWindows()

def FuncStart():

    def processing():
        progress.pack(pady=15)
        progress.start(10)
        durationG = float(Duration_Entry.get())
        photosInterval = float(Intervals_Entry.get())
        resolution = str(Resolution_Entry.get())
        processedPhotos = str(ProcessedPhotos_Entry.get())#fotoP
        device = int(Device_Entry.get())

        video = cv2.VideoCapture(device, cv2.CAP_DSHOW)
        if (video.isOpened() == False):  
            print("Error reading video file")
            progress.stop()
            progress.pack_forget()
            progress_label.config(text="There was an error, please try again.", font="Helvetica 9")
            return quit
        else:
            timelapse.timelapseCrear(durationG,photosInterval,resolution,processedPhotos,device)
            progress.stop()
            progress.pack_forget()
            progress_label.config(text="Timelapse finished.", font="Helvetica 10")

    t = threading.Thread(target=processing)
    t.start()
    

window = Tk()
window.geometry("335x550")
window.title("Timelapsing! - Tomas Gomez Bermudez")
window.iconbitmap('imgs/timelapsingicon.ico')
window.config(background="#151515")

title = Label(window, text="Timelapsing!", padx=100, pady=30, bg="#151515", foreground="#DE4C12", font="Helvetica 16 bold")
title.grid(column="0", row="0")

#Frame Create Timelapse

groupCreate = LabelFrame(window, text="Create Timelapse", labelanchor=N, padx=25, pady=10, bg="#151515", foreground="#FFFFFF", font="Helvetica 12 bold")
groupCreate.grid(column="0", row="3")

Duration_label = Label(groupCreate, text="Duration (minutes)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Duration_label.pack()
Duration_Entry= Entry(groupCreate, width="35")
Duration_Entry.pack()

Intervals_label = Label(groupCreate, text="Interval between photos (seconds)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Intervals_label.pack()
Intervals_Entry = Entry(groupCreate, width="35")
Intervals_Entry.pack()

Resolution_label = Label(groupCreate, text="Resolution (480, 720, 1080, 2k, 4k)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Resolution_label.pack()
Resolution_Entry = Entry(groupCreate, width="35")
Resolution_Entry.pack()

ProcessedPhotos_label = Label(groupCreate, text="Keep processed photos (y/n)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
ProcessedPhotos_label.pack()
ProcessedPhotos_Entry = Entry(groupCreate, width="35")
ProcessedPhotos_Entry.pack()

Device_label = Label(groupCreate, text="Video capture device" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Device_label.pack()
Device_Entry = Entry(groupCreate, width="35")
Device_Entry.pack()

progress_label = Label(window, text=" ", bg="#151515",pady=10, foreground="#FFFFFF", font="Helvetica 14")
progress_label.grid(column="0",row="6",columnspan="3")

beginButton = ttk.Button(window, text="Start", command= FuncStart)
beginButton.grid(column="0", row="4",columnspan="1", pady=10 )

progress = ttk.Progressbar(groupCreate, length = 100, mode = 'indeterminate')

previewButton = ttk.Button(window, text="Preview", command= devicePreview)
previewButton.grid(column="0", row="5",columnspan="1", pady=5 )

Name_label = Label(window, text="Developed by Tomas Gomez Bermudez", bg="#151515",pady=5, foreground="#FFFFFF", font="Helvetica 9")
Name_label.grid(column="0",row="7")

window.mainloop()