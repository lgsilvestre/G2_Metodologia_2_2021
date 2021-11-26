from LogicaBasica.Verificacion import verificarUsuario
from DetecciónRostros.Detecciónderostros import reconocimientoA,reconocimientoB,reconocimientoC
from LogicaBasica.Usuario import User,Listauser
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
    framecam1 = tk.Frame(ventana,bg="white")
    framecam1.config(height=1900,width=1900)
    framecam2 = tk.Frame(ventana,bg="white")
    framecam2.config(height=1900,width=1900)
    
    for frame in (framelogin, framecam, frameforg,frameAdmin, framecam1,framecam2): #For para mostrar los frames
        frame.grid(row=0,column=0,sticky='nsew')
        
        
    #-----------------------------------------------#
        
    #****************FRAME ADMIN*********************************
    Admin = tkinter.Canvas(frameAdmin)
 
    
    
    ###############################           ChecktBox        ###############################################
    opcion= IntVar()
    opcion2= IntVar()
    opcion3= IntVar()
    opcion4= IntVar()
    opcion5= IntVar()
    opcion6= IntVar()
    opcion7= IntVar()
    opcion8= IntVar()
    opcion9= IntVar()
    opcion10= IntVar()
    
    def RellenadoLista(contador):
        aux=0
        s = os.getcwd()
        new_s = s.replace('Main','LogicaBasica/usuarios.txt')    
        archivo= open(new_s)
        linea = archivo.readline()
        while len(linea)>0:
            aux=aux+1
            linea=linea.rstrip()
            Array=linea.split()
            if(aux==contador):
                correo = Array[0]
                contraseña = Array[1]
                rol= Array[2]
                return correo, contraseña,rol
            linea=archivo.readline()
        return " ", " ", " "  
    

    
    def Actualizarpantalla():
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
        
        RegresarPrincipal= Button(Admin,text="Agregar Usuario",font=("Arial",16,'bold'),bg='#a8021e',fg='white',command=lambda:[Agregar()])
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
        
        contador=1
        ListaCorreo=" "
        ListaContraseña=" "
        ListaRol=" "
        
        ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(contador)
        contador=contador+1
        
        checkusuario1= Checkbutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, onvalue=1, offvalue=0)
        checkusuario1.place(x=245,y=140)
        
        ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(contador)
        contador=contador+1
        
        checkusuario2= Checkbutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion2, onvalue=1, offvalue=0)
        checkusuario2.place(x=245,y=190)
        
        ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(contador)
        contador=contador+1
       
        checkusuario3= Checkbutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion3, onvalue=1, offvalue=0)
        checkusuario3.place(x=245,y=240)
        
        ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(contador)
        contador=contador+1
        
        checkusuario4= Checkbutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion4, onvalue=1, offvalue=0)
        checkusuario4.place(x=245,y=290)
        
        ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(contador)
        contador=contador+1
        
        checkusuario5= Checkbutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion5, onvalue=1, offvalue=0)
        checkusuario5.place(x=245,y=340)
        
        ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(contador)
        contador=contador+1
        
        checkusuario6= Checkbutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion6, onvalue=1, offvalue=0)
        checkusuario6.place(x=245,y=390)
        
        ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(contador)
        contador=contador+1
        
        checkusuario7= Checkbutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion7, onvalue=1, offvalue=0)
        checkusuario7.place(x=245,y=440)
        
        ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(contador)
        contador=contador+1
        
        checkusuario8= Checkbutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion8, onvalue=1, offvalue=0)
        checkusuario8.place(x=245,y=490)
        
        ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(contador)
        contador=contador+1
        
        checkusuario9= Checkbutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion9, onvalue=1, offvalue=0)
        checkusuario9.place(x=245,y=540)
        
        ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(contador)
        contador=contador+1
        
        checkusuario10= Checkbutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion10, onvalue=1, offvalue=0)
        checkusuario10.place(x=245,y=590)
        contador=1
        
    
    Actualizarpantalla()    
        
    
    def Completartxt():
        aux=0
        s = os.getcwd()
        new_s = s.replace('Main','LogicaBasica/usuarios.txt')    
        archivo= open(new_s)
        linea = archivo.readline()
        while len(linea)>0:
            aux=aux+1
            linea=linea.rstrip()
            Array=linea.split()
            Lista.agregar(Array[0], Array[1], Array[2])
            linea=archivo.readline()
        
    global Lista
    Lista = Listauser()
    Completartxt()
    Lista.imprimirlista()    
    
    def Agregar():
        global Lista
        pruebatxt = os.getcwd()
        auxilioprueba = pruebatxt.replace('Main','LogicaBasica/usuarios.txt')    
        answer = simpledialog.askstring("Agregar Usuario","Introduzca el nombre de usuario.")
        answer2 = simpledialog.askstring("Agregar Contraseña","Introduzca la contraseña.")
        Lista.agregar(answer, answer2, "User")
        probando=Lista.copiaratxt()
        f = open (auxilioprueba,'w')
        f.write(probando)
        f.close()
        Lista.imprimirlista()
        Actualizarpantalla()
       
    
    def EditarU():
        print("Editar Usuario")
        ListaCorreo=" "
        ListaContraseña=" "
        ListaRol=" "
        if(opcion.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(1)
        elif(opcion2.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(2)
        elif(opcion3.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(3)
        elif(opcion4.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(4)
        elif(opcion5.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(5)
        elif(opcion6.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(6)
        elif(opcion7.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(7)
        elif(opcion8.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(8)
        elif(opcion9.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(9)
        elif(opcion10.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(10)
        print(ListaCorreo)
        answer = simpledialog.askstring("Editar Usuario","Introduzca el nuevo correo.")
        answer2 = simpledialog.askstring("Editar Usuario","Introduzca la nueva contraseña.")
        Lista.agregar(answer, answer2, ListaRol)
        Lista.eliminar(ListaCorreo)
        pruebatxt = os.getcwd()
        auxilioprueba = pruebatxt.replace('Main','LogicaBasica/usuarios.txt')
        probando=Lista.copiaratxt()
        f = open (auxilioprueba,'w')
        f.write(probando)
        f.close()
        Actualizarpantalla()
        
        
        
        
        
    def EliminarU():
        print("Eliminar Usuario")
        ListaCorreo=" "
        ListaContraseña=" "
        ListaRol=" "
        if(opcion.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(1)
        elif(opcion2.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(2)
        elif(opcion3.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(3)
        elif(opcion4.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(4)
        elif(opcion5.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(5)
        elif(opcion6.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(6)
        elif(opcion7.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(7)
        elif(opcion8.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(8)
        elif(opcion9.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(9)
        elif(opcion10.get()==1):
            ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(10)
        Lista.eliminar(ListaCorreo)
        pruebatxt = os.getcwd()
        auxilioprueba = pruebatxt.replace('Main','LogicaBasica/usuarios.txt')
        probando=Lista.copiaratxt()
        f = open (auxilioprueba,'w')
        f.write(probando)
        f.close()
        Actualizarpantalla()
        
    
        
    
    #*******************FIN FRAME ADMIN *************************    
        
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
    
    btncam = Button(framecam,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BuscarRostro()]) ## Boton crear cuenta
    btncam.place(x=1000,y=150)
    btncam.config(width="12")
    btncam.configure(relief="solid")
    btncam.config(bd=0.5)
    
    btncam1 = Button(framecam,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
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

    
   

    #+++++++++++++++FRAME Detectar Rostro+++++++++++++++++++++++++++++++#  
    miframe2=tkinter.Canvas(framecam1)
    miframe2.config(width=840,height=420)
    miframe2.config(bg="white")
    miframe2.configure(relief="solid")
    miframe2.config(bd=0.5)
    miframe2.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe2.place(x=50,y=100)
    
    btncam3 = Button(framecam1,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    btncam3.place(x=1000,y=150)
    btncam3.config(width="12")
    btncam3.configure(relief="solid")
    btncam3.config(bd=0.5)
    
    btncam4 = Button(framecam1,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#9A9797',fg='black',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
    btncam4.place(x=1000,y=250)
    btncam4.config(width="12")
    btncam4.configure(relief="solid")
    btncam4.config(bd=0.5)
    
    my_label1 = tk.Label(framecam1, text = "Seleccionar Modo",bg="white",fg = "black",font = ("Arial", 14))
    my_label1.place(x=1000,y=100)
    
    comboReconocimiento1 = ttk.Combobox(framecam1)
    comboReconocimiento1['values']= ('Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboReconocimiento1.place(x=1000,y=350)
    comboReconocimiento1.current(0)
    btncombo1 = Button(framecam1,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo1()]) ## Boton crear cuenta
    btncombo1.place(x=1000,y=400)
    btncombo1.config(width="15")
    btncombo1.configure(relief="solid")
    btncombo1.config(bd=0.5)
    
    btncombo2 = Button(framecam1,text="Guardar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    btncombo2.place(x=1000,y=490)
    btncombo2.config(width="15")
    btncombo2.configure(relief="solid")
    btncombo2.config(bd=0.5)
    
    my_label3 = tk.Label(framecam1, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    my_label3.place(x=750,y=550)
    
    btnrastrear1 = Button(framecam1,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo()]) ## Boton crear cuenta
    btnrastrear1.place(x=750,y=650)
    btnrastrear1.config(width="15")
    btnrastrear1.configure(relief="solid")
    btnrastrear1.config(bd=0.5)
    
    btnregresar = Button(framecam1,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoPrincipal()]) ## Boton crear cuenta
    btnregresar.place(x=1150,y=650)
    btnregresar.config(width="15")
    btnregresar.configure(relief="solid")
    btnregresar.config(bd=0.5)
    
    
    
    def switch1():
        global is_on
        global triggerX,triggerZtriggerY
        nombrerostro=entryNombre.get()
        # Determine is on or off
        if is_on:
            on_button1.config(image = off)
            my_label3.config(text = "Cámara apagada", bg="white",fg = "black",font = ("Arial", 14))
            is_on = False
        else:
           
            on_button1.config(image = on)
            my_label3.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            is_on = True
            switch2a()
            
            
    def switch2a():
        global triggerA,triggerB,triggerC
        nombrerostro=entryNombre.get()
      
        
        if(triggerC==True):
            reconocimientoC(nombrerostro)
 
        if(triggerB==True):
            reconocimientoB(nombrerostro)

        if(triggerA==True):
            reconocimientoA(nombrerostro)

            

 #+++++++++++++++FRAME Buscar Rostro+++++++++++++++++++++++++++++++#  
    miframe3=tkinter.Canvas(framecam2)
    miframe3.config(width=840,height=420)
    miframe3.config(bg="white")
    miframe3.configure(relief="solid")
    miframe3.config(bd=0.5)
    miframe3.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe3.place(x=50,y=100)
    
    btncam4 = Button(framecam2,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#9A9797',fg='black') ## Boton crear cuenta
    btncam4.place(x=1000,y=150)
    btncam4.config(width="12")
    btncam4.configure(relief="solid")
    btncam4.config(bd=0.5)
    
    btncam4 = Button(framecam2,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
    btncam4.place(x=1000,y=250)
    btncam4.config(width="12")
    btncam4.configure(relief="solid")
    btncam4.config(bd=0.5)
    
    my_label1 = tk.Label(framecam2, text = "Seleccionar Modo",bg="white",fg = "black",font = ("Arial", 14))
    my_label1.place(x=1000,y=100)
    
    comboReconocimiento1 = ttk.Combobox(framecam2)
    comboReconocimiento1['values']= ('Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboReconocimiento1.place(x=1000,y=350)
    comboReconocimiento1.current(0)
    btncombo3 = Button(framecam2,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo1()]) ## Boton crear cuenta
    btncombo3.place(x=1000,y=400)
    btncombo3.config(width="15")
    btncombo3.configure(relief="solid")
    btncombo3.config(bd=0.5)
    
    btncombo4 = Button(framecam2,text="Guardar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    btncombo4.place(x=1000,y=490)
    btncombo4.config(width="15")
    btncombo4.configure(relief="solid")
    btncombo4.config(bd=0.5)
    
    my_label3 = tk.Label(framecam2, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    my_label3.place(x=750,y=550)
    
    btnrastrear1 = Button(framecam2,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo()]) ## Boton crear cuenta
    btnrastrear1.place(x=750,y=650)
    btnrastrear1.config(width="15")
    btnrastrear1.configure(relief="solid")
    btnrastrear1.config(bd=0.5)
    
    btnregresar = Button(framecam2,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoPrincipal()]) ## Boton crear cuenta
    btnregresar.place(x=1150,y=650)
    btnregresar.config(width="15")
    btnregresar.configure(relief="solid")
    btnregresar.config(bd=0.5)
    
    
    def switch1():
        global is_on
        global triggerX,triggerZtriggerY
        nombrerostro=entryNombre.get()
        # Determine is on or off
        if is_on:
            on_button2.config(image = off)
            my_label3.config(text = "Cámara apagada", bg="white",fg = "black",font = ("Arial", 14))
            is_on = False
        else:
           
            on_button2.config(image = on)
            my_label3.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            is_on = True
            switch2a()
            
            
    def switch2a():
        global triggerA,triggerB,triggerC
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
    detectar = PhotoImage(file = new_s+"/detectar.png")
    buscar = PhotoImage(file = new_s+"/buscar.png")
    on_button = Button(framecam, image = off, bd = 0,command = switch)
    on_button.place(x=750,y=600)
    on_button1 = Button(framecam1, image = off, bd = 0,command = switch1)
    on_button1.place(x=750,y=600)
    on_button2 = Button(framecam2, image = off, bd = 0,command = switch1)
    on_button2.place(x=750,y=600)
    on_button3 = Button(framecam2, image = detectar, bd = 0)
    on_button3.place(x=50,y=530)
    on_button4 = Button(framecam1, image = buscar, bd = 0)
    on_button4.place(x=50,y=530)
    
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
    
    def obtenerCombo1():
        comparar1=comboReconocimiento1.get()
        global nombrerostro
        nombrerostro=entryNombre.get()
        global triggerA
        global triggerB
        global triggerC
        if(comparar1 =='Reconocimiento A'):
            triggerC=False
            triggerB=False
            triggerA=True
            return True  
        if(comparar1 =='Reconocimiento B'):
            triggerA=False
            triggerC=False
            triggerB=True
            return True 
        if(comparar1 =='Reconocimiento C'):
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
            
            
    def DetectarRostro():
        show_frame(framecam1)
        
    def BuscarRostro():
        show_frame(framecam2)


    ##########################
    
    
            
    #l-l-l-l-l PROGRAMA MAIN l-l-l-l-l-l-#     
    show_frame(framelogin)     ## Mostramos el frame default (login)
    frametop=tkinter.Canvas(ventana) ## Corresponde a la barra verde superior que dice "Saveface" 
    frametop.config(width=2000,height=75) 
    frametop.place(x=0,y=0) 
    frametop.config(bg="#23442B") 
    frametop.create_text(100, 40, fill="white",text="SaveFace",font=("Arial",24,'bold')) 
    ventana.mainloop()
    #l-l-l-l-l-l-l-l-l-l-l-l-l-l-#     



