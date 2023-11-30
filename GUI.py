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
    def aceptarformulario():
        marco2.destroy()
        ventanapartida.add(marco3)
        for mensaje in xml.find_all("mensaje"):
            tipo = mensaje.get("tipo")
            texto = mensaje.get("texto")
            if tipo == "etiqueta":
                ttk.Label(marco3,text=texto,background="white").pack(padx=10,pady=10)
        print("DESTRUCCION")
    opcion = caja.get()
    #FORMULARIO
    if opcion == "Crear formulario":
        for formulario in xml.find_all("formulario"):
            tipo = formulario.get("tipo")
            texto = formulario.get("texto")
            if tipo == "etiqueta":
                ttk.Label(marco2,text=texto,background="white").pack(padx=10,pady=10)
            elif tipo == "checkbutton":
                ttk.Checkbutton(marco2,text=texto).pack(padx=10,pady=10)
            elif tipo == "campotxt":
                ttk.Entry(marco2).pack(padx=10,pady=10)
            elif tipo == "camponum":
                ttk.Spinbox(marco2,from_=0,to=100).pack(padx=10,pady=10)
            elif tipo == "boton":
                ttk.Button(marco2,text=texto,command=aceptarformulario).pack(padx=10,pady=10)
    elif opcion == "Crear tabla":
        marco3.destroy()
        ventanapartida.add(marco4)
        for formulario in xml.find_all("formulario"):
            tipo = formulario.get("tipo")
            texto = formulario.get("texto")
            if tipo == "etiqueta":
                ttk.Label(marco4,text=texto,background="white").pack(padx=10,pady=10)
    print(opcion)
    print("has aceptado")

#VENTANA PARTIDA
ventanapartida = tk.PanedWindow(raiz,orient=tk.HORIZONTAL)
marco1 = tk.Frame(ventanapartida)
marco2 = tk.Frame(ventanapartida,background="white")
marco3 = tk.Frame(ventanapartida,background="white")
marco4 = tk.Frame(ventanapartida,background="white")
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
