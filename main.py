from tkinter import Label,Grid,LabelFrame,Entry,Tk,N
from tkinter import filedialog
from tkinter import ttk
import timelapse
import threading 

def FuncEmpezar():

    def procesando():
        progress.pack(pady=15)
        progress.start(10)
        duracionG = float(Duracion_Entry.get())
        intervaloFoto = float(Intervalos_Entry.get())
        fotosp = str(FotosP_Entry.get())
        dispositivo = int(Dispositivo_Entry.get())
        timelapse.timelapseCrear(duracionG,intervaloFoto,fotosp,dispositivo)
        progress.stop()
        progress.pack_forget()
        progreso.config(text="Timelapse finished.")

    progreso.config(text="Processing...")
    t = threading.Thread(target=procesando)
    t.start()

ventana = Tk()
ventana.geometry("525x500")
ventana.title("Automatic Timelapse Processor - Tomas Gomez Bermudez")
ventana.config(background="#151515")

titulo = Label(ventana, text="Automatic Timelapse Processor", padx=100, pady=30, bg="#151515", foreground="#DE4C12", font="Helvetica 16 bold")
titulo.grid(column="0", row="0", columnspan="3")

#Frame Crear Timelapse

groupCrear = LabelFrame(ventana, text="Create Timelapse", labelanchor=N, padx=25, pady=10, bg="#151515", foreground="#FFFFFF", font="Helvetica 12 bold")
groupCrear.grid(column="1", row="3")

Duracion_label = Label(groupCrear, text="Duration (minutes)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Duracion_label.pack()
Duracion_Entry= Entry(groupCrear, width="35")
Duracion_Entry.pack()

Intervalos_label = Label(groupCrear, text="Interval between photos (seconds)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Intervalos_label.pack()
Intervalos_Entry = Entry(groupCrear, width="35")
Intervalos_Entry.pack()

FotosP_label = Label(groupCrear, text="Keep processed photos (y/n)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
FotosP_label.pack()
FotosP_Entry = Entry(groupCrear, width="35")
FotosP_Entry.pack()

Dispositivo_label = Label(groupCrear, text="Video capture device" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Dispositivo_label.pack()
Dispositivo_Entry = Entry(groupCrear, width="35")
Dispositivo_Entry.pack()

progreso = Label(ventana, text=" ", bg="#151515", foreground="#FFFFFF", font="Helvetica 14")
progreso.grid(column="0",row="5",columnspan="3")

botonEmpezar = ttk.Button(ventana, text="Empezar", command= FuncEmpezar)
botonEmpezar.grid(column="0", row="4",columnspan="3", pady=25 )

progress = ttk.Progressbar(groupCrear, length = 100, mode = 'indeterminate')

ventana.mainloop()