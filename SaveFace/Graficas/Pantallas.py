import tkinter as tk
from tkinter import ttk, Button
import tkinter

from LogicaBasica.Verificacion import verificarUsuario, verificarContraseña
from DetecciónRostros.Detecciónderostros import reconocimientoA,reconocimientoB,reconocimientoC
#import cv2


from tkinter import *
from PIL import Image, ImageTk #pip install Pillow
from tkinter.ttk import Label
import cv2 #pip install opencv-contrib-python
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk, Button
import tkinter
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle 
from mtcnn.mtcnn import MTCNN
#import numpy as np
import os
#import imutils
import cv2
import tkinter as tk
from tkinter import ttk, Button
import tkinter
is_on = False

def show_frame(frame):
    frame.tkraise()
    frametop=tkinter.Canvas(ventana) ## Frametop corresponde la barra verde superior que dice "Saveface" 
    frametop.config(width=2000,height=75) 
    frametop.place(x=0,y=0) 
    frametop.config(bg="#046b17") 
    frametop.create_text(100, 40, fill="white",text="SaveFace",font=("Arial",24,'bold')) 

    
ventana =tkinter.Tk()   #Creacion de ventana 
ventana.title("SaveFace") #Titulo de ventana
ventana.config(bg="white") #Fondo blanco
ventana.geometry('1500x720')  #


#---------- Declaracion de frames a usar -------#
framelogin = tk.Frame(ventana,bg="white")
framelogin.config(height=1900,width=1900)
framecam = tk.Frame(ventana,bg="white")
framecam.config(height=1900,width=1900)
frame3 = tk.Frame(ventana)

for frame in (framelogin, framecam, frame3): #For para mostrar los frames
    frame.grid(row=0,column=0,sticky='nsew')
    
    
#-----------------------------------------------#
    
    
    
#+++++++++++++++FRAME LOGIN+++++++++++++++++++++++++++++++#

miframe=tkinter.Canvas(framelogin)
miframe.config(width=740,height=620)
miframe.config(bg="white")
miframe.configure(relief="solid")
miframe.config(bd=0.5)
miframe.create_text(50, 50, text="Inicio",font=("Arial",14))
miframe.place(x=400,y=100)
        
btn2 = Button(miframe,text="Ingresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[Login()])
btn2.place(x=280,y=400)
btn2.config(width="12")
btn2.configure(relief="solid")
btn2.config(bd=0.5)
        
btn3 = Button(miframe,text="Crear Cuenta",font=("Arial",14,'bold') , bg='#858282',fg='white') ## Boton crear cuenta
btn3.place(x=280,y=550)
btn3.config(width="12")
btn3.configure(relief="solid")
btn3.config(bd=0.5)
miframe.create_text(155, 110, text="Correo Electrónico",font=("Arial",14)) ##Se crea un texto desde miframe
entry = ttk.Entry(miframe) ## Entrada de correo
entry.place(x=75, y=130,width="600",height="40")

entry2 = ttk.Entry(miframe) ## Entrada de contraseña
entry2.place(x=75, y=260,width="600",height="40")
miframe.create_text(125, 240, text="Contraseña",font=("Arial",14))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 
#+++++++++++++++FRAME CAM+++++++++++++++++++++++++++++++#  
miframe1=tkinter.Canvas(framecam)
miframe1.config(width=840,height=420)
miframe1.config(bg="white")
miframe1.configure(relief="solid")
miframe1.config(bd=0.5)
miframe1.create_text(50, 50, text="Camara",font=("Arial",14))
miframe1.place(x=50,y=100)

btncam = Button(framecam,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
btncam.place(x=1000,y=150)
btncam.config(width="12")
btncam.configure(relief="solid")
btncam.config(bd=0.5)

btncam1 = Button(framecam,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
btncam1.place(x=1000,y=250)
btncam1.config(width="12")
btncam1.configure(relief="solid")
btncam1.config(bd=0.5)


my_label = tk.Label(framecam, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
my_label.place(x=750,y=550)
# Define Our Images
# Create A Button
triggerA=False;
triggerC=False;
triggerB=False;
btnrec = Button(framecam,text="Reconocimiento C",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[ReconocimientoC(triggerC)]) ## Boton crear cuenta
btnrec.place(x=1000,y=550)
btnrec.config(width="15")
btnrec.configure(relief="solid")
btnrec.config(bd=0.5)
btnrec1 = Button(framecam,text="Reconocimiento B",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[ReconocimientoB(triggerB)]) ## Boton crear cuenta
btnrec1.place(x=1000,y=450)
btnrec1.config(width="15")
btnrec1.configure(relief="solid")
btnrec1.config(bd=0.5)
btnrec2 = Button(framecam,text="Reconocimiento A",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[ReconocimientoA(triggerA)]) ## Boton crear cuenta
btnrec2.place(x=1000,y=350)
btnrec2.config(width="15")
btnrec2.configure(relief="solid")
btnrec2.config(bd=0.5)

labelnombre= Label(framecam,text="Introduzca el nombre del rostro en pantalla",font=("Arial",10,'bold'))
labelnombre.place(x=1000,y=600)
entryNombre = ttk.Entry(framecam) ## Entrada de nombre
entryNombre.place(x=1000, y=620,width="200",height="40")
nombrerostro="Hola"
def switch():
    global is_on
     
    # Determine is on or off
    if is_on:
        print("buton rec",btnrec)
        on_button.config(image = off)
        my_label.config(text = "Cámara apagada", bg="white",fg = "black",font = ("Arial", 14))
        is_on = False
    else:
       
        on_button.config(image = on)
        my_label.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
        is_on = True
        if(triggerC==True):
            reconocimientoC(nombrerostro)
        if(triggerB==True):
            reconocimientoB(nombrerostro)
        if(triggerA==True):
            reconocimientoA(nombrerostro)

    
on = PhotoImage(file = "on.png")
off = PhotoImage(file = "off.png")
on_button = Button(framecam, image = off, bd = 0,command = switch)
on_button.place(x=750,y=600)

 

# FUNCIONES             #
#########################

def Login():
    usuario=entry.get()
    contraseña=entry2.get()
    if(verificarUsuario(usuario)== True and verificarContraseña(contraseña) == True):
        print("Login Succesfull")
        show_frame(framecam)
    else:
        print("Usuario o contraseña incorrecta")

def ReconocimientoC(variableRec):
    if variableRec==False:
        global nombrerostro
        nombrerostro=entryNombre.get()
        global triggerA
        global triggerC
        global triggerB
        triggerA=False
        triggerB=False
        triggerC=True
        return True

def ReconocimientoB(variableRec):
    if variableRec==False:
        global nombrerostro
        nombrerostro=entryNombre.get()
        global triggerA
        global triggerB
        global triggerC
        triggerA=False
        triggerC=False
        triggerB=True
        return True    
    
def ReconocimientoA(variableRec):
    if variableRec==False:
        global nombrerostro
        nombrerostro=entryNombre.get()
        global triggerA
        global triggerB
        global triggerC
        triggerC=False
        triggerB=False
        triggerA=True
        return True  
##########################


        
#l-l-l-l-l PROGRAMA MAIN l-l-l-l-l-l-#     
show_frame(framelogin)     ## Mostramos el frame default (login)
frametop=tkinter.Canvas(ventana) ## Corresponde a la barra verde superior que dice "Saveface" 
frametop.config(width=2000,height=75) 
frametop.place(x=0,y=0) 
frametop.config(bg="#046b17") 
frametop.create_text(100, 40, fill="white",text="SaveFace",font=("Arial",24,'bold')) 
ventana.mainloop()
#l-l-l-l-l-l-l-l-l-l-l-l-l-l-#     



