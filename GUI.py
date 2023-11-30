##Práctica 6:
##Crear una práctica, que en primer lugar use widgets de la familia Ttk,
##y que además se gestione o bien con un txt, o bien con un XML
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup

raiz = tk.Tk()

archivo = open("documento.xml","r")
contenido = archivo.read()
xml = BeautifulSoup(contenido,"xml")

#DEFINICION DE FUNCIONES
def salir():
    raiz.destroy()

def aceptar():
    opcion = caja.get()
    if opcion == "Crear formulario":
        for formulario in xml.find_all("formulario"):
            tipo = formulario.get("tipo")
            texto = formulario.get("texto")
            if tipo == "etiqueta":
                ttk.Label(marco2,text=texto).pack(padx=10,pady=10)
            elif tipo == "campotxt":
                ttk.Entry(marco2).pack(padx=10,pady=10)
            elif tipo == "camponum":
                ttk.Spinbox(marco2,from_=0,to=100).pack(padx=10,pady=10)
            elif tipo == "boton":
                if texto == "Aceptar":
                    ttk.Button(marco2,text=texto).pack(padx=10,pady=10)
                if texto == "Borrar":
                    ttk.Button(marco2,text=texto).pack(padx=10,pady=10)
    elif tipo == "Crear tabla":
        ttk.Label(marco1,text=texto).pack(padx=10,pady=10)
    print(opcion)
    print("has aceptado")

#VENTANA PARTIDA
ventanapartida = tk.PanedWindow(raiz,orient=tk.HORIZONTAL)
marco1 = tk.Frame(ventanapartida)
marco2 = tk.Frame(ventanapartida)
ventanapartida.add(marco1)
ventanapartida.add(marco2)
ventanapartida.pack(fill=tk.BOTH,expand=True)

#DECLARACIONES
caja = ttk.Combobox(marco1,values=['Crear formulario','Crear tabla'])

#INICIO
for inicio in xml.find_all("inicio"):
    tipo = inicio.get("tipo")
    texto = inicio.get("texto")
    if tipo == "combobox":
        caja.pack(padx=10,pady=10)
    elif tipo == "etiqueta":
        ttk.Label(marco1,text=texto).pack(padx=10,pady=10)
    elif tipo == "boton":
        if texto == "Aceptar":
            ttk.Button(marco1,text=texto,command=aceptar).pack(padx=10,pady=10)
        if texto == "Salir":
            ttk.Button(marco1,text=texto,command=salir).pack(padx=10,pady=10)

#FORMULARIO
##for formulario in xml.find_all("formulario"):
##    tipo = formulario.get("tipo")
##    texto = formulario.get("texto")
##    if tipo == "etiqueta":
##        ttk.Label(marco2,text=texto).pack(padx=10,pady=10)
##    elif tipo == "campotxt":
##        ttk.Entry(marco2).pack(padx=10,pady=10)
##    elif tipo == "boton":
##        if texto == "Aceptar":
##            ttk.Button(marco1,text=texto,command=aceptar).pack(padx=10,pady=10)
##        if texto == "Borrar":
##            ttk.Button(marco1,text=texto,command=salir).pack(padx=10,pady=10)
#TABLA


#DIMENSIONES VENTANA RAIZ
anchuraventana = 300
alturaventana = 200
anchurapantalla =raiz.winfo_screenwidth()
alturapantalla = raiz.winfo_screenheight()
esquinax = int(anchurapantalla/2 - anchuraventana/2)
esquinay = int(alturapantalla/2 - alturaventana/2)
raiz.geometry(str(anchuraventana)+"x"+str(alturaventana)+"+"+str(esquinax)+"+"+str(esquinay))


raiz.mainloop()
