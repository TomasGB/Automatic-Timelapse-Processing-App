from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import timelapse

ventana = Tk()
ventana.geometry("570x500")
ventana.title("Procesador de timelapses automatico - Tomas Gomez Bermudez")
ventana.config(background="#151515")

titulo = Label(ventana, text="Procesador de timelapses automatico", padx=100, pady=30, bg="#151515", foreground="#DE4C12", font="Helvetica 16 bold")
titulo.grid(column="0", row="0", columnspan="3")

#Frame Crear Timelapse

groupCrear = LabelFrame(ventana, text="Crear Timelapse", labelanchor=N, padx=25, pady=10, bg="#151515", foreground="#FFFFFF", font="Helvetica 12 bold")
groupCrear.grid(column="1", row="3")

Duracion_label = Label(groupCrear, text="Duracion (minutos)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Duracion_label.pack()
Duracion_Entry= Entry(groupCrear, width="35")
Duracion_Entry.pack()

Intervalos_label = Label(groupCrear, text="Intervalo entre fotos (segundos)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Intervalos_label.pack()
Intervalos_Entry = Entry(groupCrear, width="35")
Intervalos_Entry.pack()

Fotos_label = Label(groupCrear, text="Conservar fotos sin procesar (y/n)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Fotos_label.pack()
Fotos_Entry = Entry(groupCrear, width="35")
Fotos_Entry.pack()

FotosP_label = Label(groupCrear, text="Conservar fotos procesadas (y/n)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
FotosP_label.pack()
FotosP_Entry = Entry(groupCrear, width="35")
FotosP_Entry.pack()

"""
#Frame Procesar fotos existentes

groupProcesar = LabelFrame(ventana, text="Procesar Fotos Previas",labelanchor=N, padx=25, pady=17, bg="#151515", foreground="#FFFFFF", font="Helvetica 12")
groupProcesar.grid(column="1", row="3")

Fotos_label2 = Label(groupProcesar, text="Conservar fotos sin procesar (y/n)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Fotos_label2.pack()
Fotos_Entry2 = Entry(groupProcesar, width="35")
Fotos_Entry2.pack()

FotosP_label2 = Label(groupProcesar, text="Conservar fotos procesadas (y/n)" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
FotosP_label2.pack()
FotosP_Entry2 = Entry(groupProcesar, width="35")
FotosP_Entry2.pack()

Carpeta_label = Label(groupProcesar, text="Seleccione la carpeta de las fotos" ,pady=5, bg="#151515", foreground="#FFFFFF", font="Helvetica 10")
Carpeta_label.pack()

def Buscar():
    direccion = filedialog.askdirectory()
    return direccion

botonBuscar = ttk.Button(groupProcesar, text="Buscar", command=Buscar)
botonBuscar.pack( pady=15)
"""
#Empezar

def FuncEmpezar():
    duracionG = int(Duracion_Entry.get())
    intervaloFoto = float(Intervalos_Entry.get())
    fotos = str( Fotos_Entry.get())
    fotosp = str(FotosP_Entry.get())
    timelapse.timelapseCrear(duracionG,intervaloFoto,fotos,fotosp)

    estado = 'Timelapse finalizado.'
    progreso = Label(ventana, text=estado, bg="#151515", foreground="#FFFFFF", font="Helvetica 14" )
    progreso.grid(column="0",row="5",columnspan="3")
    
    
botonEmpezar = ttk.Button(ventana, text="Empezar", command= FuncEmpezar)
botonEmpezar.grid(column="0", row="4",columnspan="3", pady=25 )

ventana.mainloop()