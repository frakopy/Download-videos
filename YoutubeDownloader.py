from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time, os, re
from tkinter import messagebox
import threading
from tkinter import filedialog
from PIL import Image,ImageTk
import shutil



class app_video_download():
    
    def __init__(self):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 13 -weight bold"

        self.DIR_DESCARGAS = 'C:/Users/FRANK BOJORQUEZ/Downloads/'

        self.root = tk.Tk()
        self.root.title('Youtube Video Downloader Por Frank Bojorque')
        self.root.geometry("564x407")
        self.root.iconbitmap('youtube.ico')
        self.root.resizable(0, 0)
        self.root.configure(background="#ff4040")

        self.e1 = tk.Label(self.root)
        self.e1.place(relx=0.248, rely=0.064, height=46, width=295)
        self.e1.configure(background="#ff4040")
        self.e1.configure(disabledforeground="#a3a3a3")
        self.e1.configure(font=font9)
        self.e1.configure(foreground="#000000")
        self.e1.configure(text='''Ingresa la URL del video a descargar:''')

        self.Entry1 = tk.Entry(self.root)
        self.Entry1.place(relx=0.248, rely=0.162,height=40, relwidth=0.521)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.img1 = Image.open('download.png')
        self.img1 = self.img1.resize((247, 90), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.img1 = ImageTk.PhotoImage(self.img1)
        
        self.B1 = tk.Button(self.root, command=self.init_download, image=self.img1,borderwidth=0)
        self.B1.place(relx=0.300, rely=0.369, height=80, width=238)
        self.B1.configure(activebackground="#ececec")
        self.B1.configure(activeforeground="#000000")
        self.B1.configure(background="#ff4040")
        self.B1.configure(disabledforeground="#a3a3a3")
        self.B1.configure(foreground="#000000")
        self.B1.configure(highlightbackground="#d9d9d9")
        self.B1.configure(highlightcolor="black")
        self.B1.configure(pady="0")
        self.B1.configure(text='''Descargar''')

        self.img2 = Image.open('abrir_video2.png')
        self.img2 = self.img2.resize((120, 90), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.img2 = ImageTk.PhotoImage(self.img2)

        self.B2 = tk.Button(self.root, command=self.abrir_video, image=self.img2,borderwidth=0)
        self.B2.place(relx=0.420, rely=0.639, height=80, width=90)
        self.B2.configure(activebackground="#ececec")
        self.B2.configure(activeforeground="#000000")
        self.B2.configure(background="#ff4040")
        self.B2.configure(disabledforeground="#a3a3a3")
        self.B2.configure(foreground="#000000")
        self.B2.configure(highlightbackground="#d9d9d9")
        self.B2.configure(highlightcolor="black")
        self.B2.configure(pady="0")
        self.B2.configure(text='''Abrir''')

        self.root.mainloop()

    def eliminar_crear_widgets(self):
        self.e2.destroy()
        self.progressbar.destroy()

        self.B1 = tk.Button(self.root, command=self.init_download,image=self.img1,borderwidth=0)
        self.B1.place(relx=0.284, rely=0.369, height=90, width=247)
        self.B1.configure(activebackground="#ececec")
        self.B1.configure(activeforeground="#000000")
        self.B1.configure(background="#ff4040")
        self.B1.configure(disabledforeground="#a3a3a3")
        self.B1.configure(foreground="#000000")
        self.B1.configure(highlightbackground="#d9d9d9")
        self.B1.configure(highlightcolor="black")
        self.B1.configure(pady="0")
        self.B1.configure(text='''Descargar''')

    def download(self):

        self.url = self.Entry1.get()

        try:
            self.ydl_opts = {}
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.url])
                self.eliminar_crear_widgets()
            
            #Despues de descargar el archio lo movemos a la carpeta de las Descargas, nos apoyamos
            #con el metodo move del modulo shutils que sirve para copiar,mover entre otras operacions con archivos
            self.dir_origen = os.getcwd() 
            self.archivos_mp4 = [archivo for archivo in os.listdir(self.dir_origen) if '.mp4' in archivo]

            for archivo_mp4 in self.archivos_mp4:
                ruta_destino = self.DIR_DESCARGAS + archivo_mp4
                shutil.move(archivo_mp4, ruta_destino)

            messagebox.showinfo('Descarga exitosa', 'Se ha realizado la descarga con exito!!!')

        except:
            self.eliminar_crear_widgets()
            self.mensaje_error= 'UPPS ha ocurrido un problema con la descarga, la url ingresada no es valida o existe un problema con tu conexion a internet'
            messagebox.showerror('ERROR', self.mensaje_error )

    def init_download(self):

        self.url_ing = self.Entry1.get() 

        self.condiciones = [
            self.url_ing == '',
            re.match('(https:|http:)\W+[\w]+.[\w]+.[\w]+\W[\d|\W]+',self.url_ing),
            re.match('[\d|\W]+', self.url_ing)
            ]
        
        if any(self.condiciones):
            messagebox.showwarning('Advertencia', 'Por favor ingresa una URL valida para descargar...')

        elif re.match('(https:|http:)\W+www.youtube.com\W',self.url_ing):
            font9 = "-family {Segoe UI} -size 13 -weight bold"
            
            self.B1.destroy()  
            
            self.e2 = tk.Label(self.root)
            self.e2.place(relx=0.248, rely=0.300, height=46, width=295)
            self.e2.configure(background="#ff4040")
            self.e2.configure(disabledforeground="#a3a3a3")
            self.e2.configure(font=font9)
            self.e2.configure(foreground="#000000")
            self.e2.configure(text='''Descargando por favor espera...''')

            self.progressbar = ttk.Progressbar(self.root, mode="indeterminate")
            self.progressbar.configure(length=800)
            self.progressbar.place(relx=0.284, rely=0.400, width=250)
            self.progressbar.start(8)
            
            self.t1 = threading.Thread(target=self.download)
            self.t1.start()

        else:
            messagebox.showwarning('Advertencia', 'Por favor ingresa una URL valida para descargar...')

    def abrir_video(self):
        self.dir_archivo = filedialog.askopenfilename(initialdir=self.DIR_DESCARGAS,filetypes=[('Archivos MP4', '*.MP4')])
        if self.dir_archivo:
            os.startfile(self.dir_archivo)

if __name__ == "__main__":
    app = app_video_download()

