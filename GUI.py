##Práctica 6:
##Crear una práctica, que en primer lugar use widgets de la familia Ttk,
##y que además se gestione o bien con un txt, o bien con un XML
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup

raiz = tk.Tk()

#DEFINICION DE FUNCIONES
def salir():
    raiz.destroy()

def aceptar():
    print("has aceptado")


archivo = open("documento.xml","r")
contenido = archivo.read()
xml = BeautifulSoup(contenido,"xml")
for inicio in xml.find_all("inicio"):
    tipo = inicio.get("tipo")
    texto = inicio.get("texto")
    funcion = inicio.get("funcion")
    if tipo == "combobox":
        ttk.Combobox(raiz,values=['Crear formulario','Crear tabla','Salir']).pack(padx=10,pady=10)
    elif tipo == "etiqueta":
        ttk.Label(raiz,text=texto).pack(padx=10,pady=10)
    elif tipo == "boton":
        if texto == "Aceptar":
            ttk.Button(raiz,text=texto,command=aceptar).pack(padx=10,pady=10)
        if texto == "Salir":
            ttk.Button(raiz,text=texto,command=salir).pack(padx=10,pady=10)

#INICIO:un combobox en la raiz con las dos opciones y un boton para aceptar alguna de ellas
##ttk.Label(raiz,text="Escoge la opción que quieras realizar").pack(padx=10,pady=10)
##ttk.Combobox(raiz,values=['Crear formulario','Crear tabla','Salir']).pack(padx=10,pady=10)
##ttk.Button(raiz,text="Aceptar").pack(padx=10,pady=10)
#CREAR EL FORMULARIO

#CREAR UNA TABLA

#FRAMES
formulario = tk.Frame(raiz,padx=50,pady=50)
tk.Label(formulario,text="Hola Salva desde un Frame").pack(padx=10,pady=10)
tk.Button(formulario,text="Pulsar").pack(padx=10,pady=10)
formulario.pack()
#DIMENSIONES VENTANA RAIZ
anchuraventana = 300
alturaventana = 200
anchurapantalla =raiz.winfo_screenwidth()
alturapantalla = raiz.winfo_screenheight()
esquinax = int(anchurapantalla/2 - anchuraventana/2)
esquinay = int(alturapantalla/2 - alturaventana/2)
raiz.geometry(str(anchuraventana)+"x"+str(alturaventana)+"+"+str(esquinax)+"+"+str(esquinay))


raiz.mainloop()
