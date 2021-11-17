
from LogicaBasica.Verificacion import verificarUsuario
from DetecciónRostros.Detecciónderostros import reconocimientoA,reconocimientoB,reconocimientoC
from tkinter import *
from PIL import Image, ImageTk #pip install Pillow
from tkinter.ttk import Label
import tkinter as tk
from tkinter import ttk, Button, Checkbutton, IntVar
import tkinter
import os
from os import remove
from os import path




global is_on
is_on=False
global triggerA,triggerC,triggerB
triggerA=False;
triggerC=False;
triggerB=False;



def Pantalla():
    global is_on
    is_on=False
    
    def show_frame(frame):
        frame.tkraise()
        frametop=tkinter.Canvas(ventana) ## Frametop corresponde la barra verde superior que dice "Saveface" 
        frametop.config(width=2000,height=75) 
        frametop.place(x=0,y=0) 
        frametop.config(bg="#23442B") 
        frametop.create_text(100, 40, fill="white",text="SaveFace",font=("Arial",24,'bold')) 
    
        
    ventana =tkinter.Tk()   #Creacion de ventana 
    ventana.title("SaveFace") #Titulo de ventana
    ventana.config(bg="white") #Fondo blanco
    ventana.state('zoomed')
    ventana.resizable(False, False)
    ventana.geometry('1200x780')  #
    
    
    
    #---------- Declaracion de frames a usar -------#
    framelogin = tk.Frame(ventana,bg="white")
    framelogin.config(height=1900,width=1900)
    framecam = tk.Frame(ventana,bg="white")
    framecam.config(height=1900,width=1900)
    frameforg = tk.Frame(ventana,bg="white")
    frameforg.config(height=1900,width=1900)
    frameAdmin = tk.Frame(ventana,bg="white")
    frameAdmin.config(height=1900,width=1900)
    
    for frame in (framelogin, framecam, frameforg,frameAdmin): #For para mostrar los frames
        frame.grid(row=0,column=0,sticky='nsew')
        
        
    #-----------------------------------------------#
        
    #****************FRAME ADMIN*********************************
    Admin = tkinter.Canvas(frameAdmin)
    Admin.config(width=1425,height=720)
    Admin.config(bg="white")
    Admin.configure(relief="solid")
    Admin.place(x=50,y=100)
    
    Admin.create_text(740, 75, text="Administrar",font=("Arial",36,'bold'))
    RegresarPrincipal= Button(Admin,text="Regresar",font=("Arial",20,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoPrincipal()])
    RegresarPrincipal.place(x=650,y=625)
    RegresarPrincipal.config(width="12")
    RegresarPrincipal.configure(relief="solid")
    RegresarPrincipal.config(bd=0.5)
    
    
    RegresarPrincipal= Button(Admin,text="Agregar Usuario",font=("Arial",16,'bold'),bg='#a8021e',fg='white',command=lambda:[AñadirU()])
    RegresarPrincipal.place(x=1100,y=175)
    RegresarPrincipal.config(width="14")
    RegresarPrincipal.configure(relief="solid")
    RegresarPrincipal.config(bd=0.5)
    
    RegresarPrincipal= Button(Admin,text="Editar Usuario",font=("Arial",16,'bold'),bg='#a8021e',fg='white',command=lambda:[EditarU()])
    RegresarPrincipal.place(x=1100,y=325)
    RegresarPrincipal.config(width="14")
    RegresarPrincipal.configure(relief="solid")
    RegresarPrincipal.config(bd=0.5)
    
    RegresarPrincipal= Button(Admin,text="Eliminar Usuario",font=("Arial",16,'bold'),bg='#a8021e',fg='white',command=lambda:[EliminarU()])
    RegresarPrincipal.place(x=1100,y=475)
    RegresarPrincipal.config(width="14")
    RegresarPrincipal.configure(relief="solid")
    RegresarPrincipal.config(bd=0.5)
   
    opcion= IntVar()
    opcion2= IntVar()
    opcion3= IntVar()
    checkusuario1= Checkbutton(Admin, text="CORREO: maximiliano.maure@gmail.com  CONTRASEÑA: Leona123  ROL: Admin", font=("arial",14,'bold'), variable=opcion, onvalue=1, offvalue=0)
    checkusuario1.place(x=300,y=190)
    
    checkusuario2= Checkbutton(Admin, text="CORREO: cristian.fuentes@gmail.com  CONTRASEÑA: Perla123  ROL: Admin", font=("arial",14,'bold'), variable=opcion2, onvalue=1, offvalue=0)
    checkusuario2.place(x=300,y=240)
    
    checkusuario3= Checkbutton(Admin, text="CORREO: matias.olave@gmail.com  CONTRASEÑA: Tonca123  ROL: User", font=("arial",14,'bold'), variable=opcion3, onvalue=1, offvalue=0)
    checkusuario3.place(x=300,y=290)
        
    checkusuario4= Checkbutton(Admin, text="CORREO: CONTRASEÑA: ROL:", font=("arial",14,'bold'), variable=opcion, onvalue=1, offvalue=0)
    checkusuario4.place(x=300,y=340)
    
    checkusuario5= Checkbutton(Admin, text="CORREO: CONTRASEÑA: ROL", font=("arial",14,'bold'), variable=opcion, onvalue=1, offvalue=0)
    checkusuario5.place(x=300,y=390)
    
    checkusuario6= Checkbutton(Admin, text="CORREO: CONTRASEÑA: ROL:", font=("arial",14,'bold'), variable=opcion, onvalue=1, offvalue=0)
    checkusuario6.place(x=300,y=440)
    
    checkusuario7= Checkbutton(Admin, text="CORREO: CONTRASEÑA: ROL:", font=("arial",14,'bold'), variable=opcion, onvalue=1, offvalue=0)
    checkusuario7.place(x=300,y=490)
    #************************************************************    
        
    #+++++++++++++++FRAME LOGIN+++++++++++++++++++++++++++++++#
    
    miframe=tkinter.Canvas(framelogin)
    miframe.config(width=740,height=620)
    miframe.config(bg="white")
    miframe.configure(relief="solid")
    miframe.config(bd=0.5)
    miframe.create_text(50, 50, text="Inicio",font=("Sitka Text",14))
    miframe.place(x=400,y=100)
          
    btn2 = Button(miframe,text="Ingresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[Login()])
    btn2.place(x=280,y=350)
    btn2.config(width="12")
    btn2.configure(relief="solid")
    btn2.config(bd=0.5)
            
    
    btncontra = Button(miframe,text="Olvidó su contraseña",font=("Sitka Text",14,'bold') , bg='white',fg='darkcyan',command=lambda:[Olvide()])
    btncontra.place(x=260,y=460)
    btncontra.config(width="16")
    btncontra.configure(relief="solid")
    btncontra.config(bd=0)
    
    
    
    btn3 = Button(miframe,text="Crear Cuenta",font=("Arial",14,'bold') , bg='#858282',fg='white',command=lambda:[Olvide()]) ## Boton crear cuenta
    btn3.place(x=280,y=550)
    btn3.config(width="12")
    btn3.configure(relief="solid")
    btn3.config(bd=0.5)
    miframe.create_text(155, 110, text="Correo Electrónico",font=("Sitka Text",14)) ##Se crea un texto desde miframe
    entry = ttk.Entry(miframe) ## Entrada de correo
    entry.place(x=75, y=130,width="600",height="40")
    
    entry2 = ttk.Entry(miframe) ## Entrada de contraseña
    entry2.place(x=75, y=260,width="600",height="40")
    
    miframe.create_text(125, 240, text="Contraseña",font=("Sitka Text",14))
    
    miframe.create_line(20,80,730,80,fill="darkcyan")
    miframe.create_line(20,510,730,510,fill="darkcyan")
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 
    #+++++++++++++++++++++FRAME OLVIDE CONTRASEÑA CREAR CUENTA++++++++++++++++++++++# 
    
    
    anuncio=tkinter.Canvas(frameforg)
    anuncio.config(width=1240,height=620)
    anuncio.config(bg="white")
    anuncio.configure(relief="solid")
    anuncio.config(bd=0.5)
    anuncio.create_text(620, 150, text="Para crear una cuenta o si olvidó su contraseña",font=("Arial",36,'bold'))
    anuncio.create_text(620, 200, text="envie un mensaje a SaveFace@gmail.com ",font=("Arial",36,'bold'))
    anuncio.create_text(620, 250, text="con los datos de correo y contraseña ",font=("Arial",36,'bold'))
    anuncio.place(x=150,y=100)
    boto= Button(anuncio,text="Regresar",font=("Arial",20,'bold'),bg='#a8021e',fg='white',command=lambda:[Regreso()])
    boto.place(x=500,y=400)
    boto.config(width="12")
    boto.configure(relief="solid")
    boto.config(bd=0.5)
    
    
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
    global triggerA,triggerC,triggerB
    triggerA=False;
    triggerC=False;
    triggerB=False;
    comboReconocimiento= ttk.Combobox(framecam)
    comboReconocimiento['values']= ('Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboReconocimiento.place(x=1000,y=350)
    comboReconocimiento.current(0)
    btncombo = Button(framecam,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo()]) ## Boton crear cuenta
    btncombo.place(x=1000,y=400)
    btncombo.config(width="15")
    btncombo.configure(relief="solid")
    btncombo.config(bd=0.5)
    labelnombre= Label(framecam,text="Introduzca el nombre del rostro en pantalla",font=("Arial",10,'bold'))
    labelnombre.place(x=1000,y=600)
    entryNombre = ttk.Entry(framecam) ## Entrada de nombre
    entryNombre.place(x=1000, y=620,width="200",height="40")
    nombrerostro="Hola"
    btnrastrear = Button(framecam,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo()]) ## Boton crear cuenta
    btnrastrear.place(x=750,y=650)
    btnrastrear.config(width="15")
    btnrastrear.configure(relief="solid")
    btnrastrear.config(bd=0.5)
    def switch():
        global is_on
        global triggerA,triggerC,triggerB
        nombrerostro=entryNombre.get()
        # Determine is on or off
        if is_on:
            on_button.config(image = off)
            my_label.config(text = "Cámara apagada", bg="white",fg = "black",font = ("Arial", 14))
            is_on = False
        else:
           
            on_button.config(image = on)
            my_label.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            is_on = True
            switch2()
  
    def switch2():
        global triggerA,triggerC,triggerB
        nombrerostro=entryNombre.get()
        if(triggerC==True):
            reconocimientoC(nombrerostro)
 
        if(triggerB==True):
            reconocimientoB(nombrerostro)

        if(triggerA==True):
            reconocimientoA(nombrerostro)

    
    s = os.getcwd()
    new_s = s.replace('\\','/')
    new_s = s.replace('Main','Graficas')
    on = PhotoImage(file = new_s+"/on.png")
    off = PhotoImage(file = new_s+"/off.png")
    on_button = Button(framecam, image = off, bd = 0,command = switch)
    on_button.place(x=750,y=600)

     
    
    # FUNCIONES             #
    #########################
    def obtenerCombo():
        comparar=comboReconocimiento.get()
        global nombrerostro
        nombrerostro=entryNombre.get()
        global triggerA
        global triggerB
        global triggerC
        if(comparar =='Reconocimiento A'):
            triggerC=False
            triggerB=False
            triggerA=True
            return True  
        if(comparar =='Reconocimiento B'):
            triggerA=False
            triggerC=False
            triggerB=True
            return True 
        if(comparar =='Reconocimiento C'):
            triggerA=False
            triggerB=False
            triggerC=True
            return True
        
            
        
    def Login():
        usuario=entry.get()
        contraseña=entry2.get()
        resultado=verificarUsuario(usuario,contraseña)
        if(resultado == 'Admin'):
            print("Ingreso como Admin")
            show_frame(framecam)
        elif(resultado =='User'):
            print("Ingreso como User")
            show_frame(framecam)
        else:
            print("Error en usuario o contraseña")
            
    def Regreso():
            show_frame(framelogin)
            
    def RegresoPrincipal():
            show_frame(framecam)
    
    def Olvide():
            show_frame(frameforg)
            
    def AñadirU():
        print("Añadir Usuario")
        
    def EditarU():
        print("Editar Usuario")
        
    def EliminarU():
        print("Eliminar Usuario")
        

    ##########################
    
    
            
    #l-l-l-l-l PROGRAMA MAIN l-l-l-l-l-l-#     
    show_frame(framecam)     ## Mostramos el frame default (login)
    frametop=tkinter.Canvas(ventana) ## Corresponde a la barra verde superior que dice "Saveface" 
    frametop.config(width=2000,height=75) 
    frametop.place(x=0,y=0) 
    frametop.config(bg="#23442B") 
    frametop.create_text(100, 40, fill="white",text="SaveFace",font=("Arial",24,'bold')) 
    ventana.mainloop()
    #l-l-l-l-l-l-l-l-l-l-l-l-l-l-#     



