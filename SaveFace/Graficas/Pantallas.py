from LogicaBasica.Verificacion import verificarUsuario,verificarCorreo, verificarCantidadAdmin
from DetecciónRostros.Detecciónderostros import reconocimientoA,reconocimientoB,reconocimientoC
from LogicaBasica.Usuario import User,ListaUser
from tkinter import *
from PIL import Image, ImageTk #pip install Pillow
from tkinter.ttk import Label
import tkinter as tk
from tkinter import ttk, Button, Checkbutton, IntVar, simpledialog, Radiobutton, messagebox
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
    framecamAdmin = tk.Frame(ventana,bg="white")
    framecamAdmin.config(height=1900,width=1900)
    frameforg = tk.Frame(ventana,bg="white")
    frameforg.config(height=1900,width=1900)
    frameAdmin = tk.Frame(ventana,bg="white")
    frameAdmin.config(height=1900,width=1900)
    framecam1 = tk.Frame(ventana,bg="white")
    framecam1.config(height=1900,width=1900)
    framecam2 = tk.Frame(ventana,bg="white")
    framecam2.config(height=1900,width=1900)
    framecam1Admin = tk.Frame(ventana,bg="white")
    framecam1Admin.config(height=1900,width=1900)
    framecam2Admin = tk.Frame(ventana,bg="white")
    framecam2Admin.config(height=1900,width=1900)
    frameAdminEditar = tk.Frame(ventana,bg="white")
    frameAdminEditar.config(height=1900,width=1900)
    frameRastreoActivo= tk.Frame(ventana,bg="white")
    frameRastreoActivo.config(height=1900,width=1900)
    
    for frame in (framelogin, framecam,framecamAdmin, frameforg,frameAdmin, framecam1,framecam2,framecam1Admin,framecam2Admin,frameAdminEditar,frameRastreoActivo): #For para mostrar los frames
        frame.grid(row=0,column=0,sticky='nsew')
    #-----------------------------------------------#
        

    
    #-----------------RadiobuttonBox----------------#
    opcion= IntVar()
    #-----------------------------------------------#

    
    #------------------Lista de usuarios-------------#
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
    #-----------------------------------------------#
    
    #------------Actualizar Pantalla----------------#
    def Actualizarpantalla():
        Admin = tkinter.Canvas(frameAdmin)
        Admin.config(width=1425,height=720)
        Admin.config(bg="white")
        Admin.configure(relief="solid")
        Admin.place(x=50,y=100)
        
        Admin.create_text(740, 75, text="Administrar",font=("Arial",36,'bold'))
        
        
        #-------------------Button-------------------#
        RegresarPrincipal= Button(Admin,text="Regresar",font=("Arial",20,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoAdmin1()()])
        RegresarPrincipal.place(x=650,y=625)
        RegresarPrincipal.config(width="12")
        RegresarPrincipal.configure(relief="solid")
        RegresarPrincipal.config(bd=0.5)
        
        AgregarUsuario= Button(Admin,text="Agregar Usuario",font=("Arial",16,'bold'),bg='#a8021e',fg='white',command=lambda:[Agregar()])
        AgregarUsuario.place(x=1100,y=175)
        AgregarUsuario.config(width="14")
        AgregarUsuario.configure(relief="solid")
        AgregarUsuario.config(bd=0.5)
        
        EditarUsuario= Button(Admin,text="Editar Usuario",font=("Arial",16,'bold'),bg='#a8021e',fg='white',command=lambda:[GotoEdit()])
        EditarUsuario.place(x=1100,y=325)
        EditarUsuario.config(width="14")
        EditarUsuario.configure(relief="solid")
        EditarUsuario.config(bd=0.5)
        
        ElimininarUsuario= Button(Admin,text="Eliminar Usuario",font=("Arial",16,'bold'),bg='#a8021e',fg='white',command=lambda:[EliminarU()])
        ElimininarUsuario.place(x=1100,y=475)
        ElimininarUsuario.config(width="14")
        ElimininarUsuario.configure(relief="solid")
        ElimininarUsuario.config(bd=0.5)
        #-----------------------------------------------#
        
        ListaCorreo=" "
        ListaContraseña=" "
        ListaRol=" "
        cont=1
        
        #---------------Leer Archivo txt-----------------#
        s = os.getcwd()
        new_s = s.replace('Main','LogicaBasica/usuarios.txt')    
        archivo= open(new_s)
        linea = archivo.readline()#
        
        #-------------RadiobuttonBox Relleno-------------#
        while len(linea)>0:
            if(cont==1):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(cont)
                checkusuario1= Radiobutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, value=1)
                checkusuario1.place(x=245,y=140)
                
            if(cont==2):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(cont)
                checkusuario2= Radiobutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, value=2)
                checkusuario2.place(x=245,y=190)
            
            if(cont==3):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(cont)
                checkusuario3= Radiobutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, value=3)
                checkusuario3.place(x=245,y=240)
            
            if(cont==4):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(cont)
                checkusuario4= Radiobutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, value=4)
                checkusuario4.place(x=245,y=290)
            
            if(cont==5):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(cont)
                checkusuario5= Radiobutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, value=5)
                checkusuario5.place(x=245,y=340)
            
            if(cont==6):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(cont)
                checkusuario6= Radiobutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, value=6)
                checkusuario6.place(x=245,y=390)
           
            if(cont==7):
               ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(cont)
               checkusuario7= Radiobutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, value=7)
               checkusuario7.place(x=245,y=440)
            
            if(cont==8):
               ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(cont)
               checkusuario8= Radiobutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, value=8)
               checkusuario8.place(x=245,y=490)
           
            if(cont==9):
               ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(cont)
               checkusuario9= Radiobutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, value=9)
               checkusuario9.place(x=245,y=540)
           
            if(cont==10):
               ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(cont)
               checkusuario10= Radiobutton(Admin, text="CORREO: "+ListaCorreo+" CONTRASEÑA: "+ListaContraseña+" ROL: "+ListaRol, font=("arial",14,'bold'), variable=opcion, value=10)
               checkusuario10.place(x=245,y=590)

            cont=cont+1
            linea=archivo.readline()
    #-----------------------------------------------#
    #-----------------------------------------------#            
    
    #-----------Rellenar lista con el txt-----------#
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
    #-----------------------------------------------#        
            
    Actualizarpantalla()    

    global Lista
    Lista = ListaUser()
    Completartxt()
        

    
    def Agregar():
        pruebatxt = os.getcwd()
        auxilioprueba = pruebatxt.replace('Main','LogicaBasica/usuarios.txt') 
        correoEntrada = simpledialog.askstring("Agregar Usuario","Introduzca el nombre de usuario.")
        if(correoEntrada!=None):
            if verificarCorreo(correoEntrada):
                contraseñaEntrada = simpledialog.askstring("Agregar Contraseña","Introduzca la contraseña.")
                if (messagebox.askyesno("Verificar Eliminación","¿Desea agregar a "+correoEntrada+" como Admin?")==True):
                    Lista.agregar(correoEntrada, contraseñaEntrada, "Admin")
                    probando=Lista.copiaratxt()
                    f = open (auxilioprueba,'w')
                    f.write(probando)
                    f.close()
                    Lista.imprimirlista()
                    Actualizarpantalla()
                else:
                    Lista.agregar(correoEntrada, contraseñaEntrada, "User")
                    probando=Lista.copiaratxt()
                    f = open (auxilioprueba,'w')
                    f.write(probando)
                    f.close()
                    Lista.imprimirlista()
                    Actualizarpantalla()
            else:
                messagebox.showwarning("Error Correo", "El correo "+correoEntrada+" no es valido")
       
    
    def EditarU():
        if(opcion.get()!=0):
            ListaCorreo=" "
            ListaContraseña=" "
            ListaRol=" "
            if(opcion.get()==1):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(1)
                opcion.set(0)
            elif(opcion.get()==2):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(2)
                opcion.set(0)
            elif(opcion.get()==3):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(3)
                opcion.set(0)
            elif(opcion.get()==4):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(4)
                opcion.set(0)
            elif(opcion.get()==5):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(5)
                opcion.set(0)
            elif(opcion.get()==6):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(6)
                opcion.set(0)
            elif(opcion.get()==7):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(7)
                opcion.set(0)
            elif(opcion.get()==8):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(8)
                opcion.set(0)
            elif(opcion.get()==9):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(9)
                opcion.set(0)
            elif(opcion.get()==10):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(10)
                opcion.set(0)

            correoEntrada = editarUsuario.get()
            
            if(correoEntrada!=None):
                if(verificarCorreo(correoEntrada)):
                    contraseñaEntrada = editarContra.get()
                    if("Admin"==ListaRol):
                        if (messagebox.askyesno("Verificación cambio de rol","¿Desea que "+correoEntrada+" siga como Admin?")==True):
                            Lista.agregar(correoEntrada, contraseñaEntrada, ListaRol)
                            Lista.eliminar(ListaCorreo)
                            pruebatxt = os.getcwd()
                            auxilioprueba = pruebatxt.replace('Main','LogicaBasica/usuarios.txt')
                            probando=Lista.copiaratxt()
                            f = open (auxilioprueba,'w')
                            f.write(probando)
                            f.close()
                            show_frame(frameAdmin)
                            Actualizarpantalla()
                        else:
                            Lista.agregar(correoEntrada, contraseñaEntrada, "User")
                            Lista.eliminar(ListaCorreo)
                            pruebatxt = os.getcwd()
                            auxilioprueba = pruebatxt.replace('Main','LogicaBasica/usuarios.txt')
                            probando=Lista.copiaratxt()
                            f = open (auxilioprueba,'w')
                            f.write(probando)
                            f.close()
                            show_frame(frameAdmin)
                            Actualizarpantalla()
                    else:
                        if (messagebox.askyesno("Verificación cambio de rol","¿Desea que "+correoEntrada+" sea Admin?")==True):
                            Lista.agregar(correoEntrada, contraseñaEntrada, "Admin")
                            Lista.eliminar(ListaCorreo)
                            pruebatxt = os.getcwd()
                            auxilioprueba = pruebatxt.replace('Main','LogicaBasica/usuarios.txt')
                            probando=Lista.copiaratxt()
                            f = open (auxilioprueba,'w')
                            f.write(probando)
                            f.close()
                            show_frame(frameAdmin)
                            Actualizarpantalla()
                        else:
                            Lista.agregar(correoEntrada, contraseñaEntrada, ListaRol)
                            Lista.eliminar(ListaCorreo)
                            pruebatxt = os.getcwd()
                            auxilioprueba = pruebatxt.replace('Main','LogicaBasica/usuarios.txt')
                            probando=Lista.copiaratxt()
                            f = open (auxilioprueba,'w')
                            f.write(probando)
                            f.close()
                            show_frame(frameAdmin)
                            Actualizarpantalla()
                else:
                    messagebox.showwarning("Error Correo", "El correo "+correoEntrada+" no es valido")
        else:
            messagebox.showwarning("Error selección", "No ha seleccionado nada para poder editar")
        
        
        

    def EliminarU():
        if(opcion.get()!=0):
            ListaCorreo=" "
            ListaContraseña=" "
            ListaRol=" "
            if(opcion.get()==1):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(1)
                opcion.set(0)
            elif(opcion.get()==2):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(2)
                opcion.set(0)
            elif(opcion.get()==3):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(3)
                opcion.set(0)
            elif(opcion.get()==4):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(4)
                opcion.set(0)
            elif(opcion.get()==5):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(5)
                opcion.set(0)
            elif(opcion.get()==6):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(6)
                opcion.set(0)
            elif(opcion.get()==7):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(7)
                opcion.set(0)
            elif(opcion.get()==8):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(8)
                opcion.set(0)
            elif(opcion.get()==9):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(9)
                opcion.set(0)
            elif(opcion.get()==10):
                ListaCorreo,ListaContraseña,ListaRol=RellenadoLista(10)
                opcion.set(0)
                
            if((True==verificarCantidadAdmin()) or (False==verificarCantidadAdmin() and ListaRol != "Admin")):
                if (messagebox.askyesno("Verificar Eliminación","¿Seguro/a que quiere eliminar el correro "+ListaCorreo+" ?")==True):
                    Lista.eliminar(ListaCorreo)
                    pruebatxt = os.getcwd()
                    auxilioprueba = pruebatxt.replace('Main','LogicaBasica/usuarios.txt')
                    probando=Lista.copiaratxt()
                    f = open (auxilioprueba,'w')
                    f.write(probando)
                    f.close()
                    Actualizarpantalla()
            else:
                messagebox.showwarning("Error eliminacion", "No es posible eliminar el ultimo Admin")
            
        else:
            messagebox.showwarning("Error selección", "No ha seleccionado nada para poder eliminar")  
    
        
    
    #------------Frame Rastreo Activo--------------#
    RastreoActivo = tkinter.Canvas(frameRastreoActivo)
    RastreoActivo.config(width=1425,height=720)
    RastreoActivo.config(bg="white")
    RastreoActivo.configure(relief="solid")
    RastreoActivo.place(x=50,y=100)

    #-----------------------------------------------#
    
    
    
    

    
    #*******************FIN FRAME ADMIN *************************    
    ################ FRAME ADMIN EDITAR####################
        
    Admineditar = tkinter.Canvas(frameAdminEditar)
    Admineditar.config(width=1425,height=720)
    Admineditar.config(bg="white")
    Admineditar.configure(relief="solid")
    Admineditar.place(x=50,y=100)
    editarUsuario = ttk.Entry(Admineditar)    
    editarUsuario.place(x=550,y=300,width="350",height="50")
    editarContra = ttk.Entry(Admineditar)    
    editarContra.place(x=550,y=450,width="350",height="50")
    Admineditar.create_text(740, 75, text="Introduzca el nuevo correo y contraseña",font=("Arial",24,'bold'))
    Admineditar.create_text(715, 275, text="Correo",font=("Arial",14,'bold'))
    Admineditar.create_text(715, 425, text="Contraseña",font=("Arial",14,'bold'))
    btnedit = Button(frameAdminEditar,text="Aceptar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[EditarU()]) ## Boton crear cuenta
    btnedit.place(x=550,y=700)
    btnedit.config(width="10",height="2")
    btnedit.configure(relief="solid")
    btnedit.config(bd=0.5)
    btnedit1 = Button(frameAdminEditar,text="Cancelar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[FrameAdministrar()]) ## Boton crear cuenta
    btnedit1.place(x=850,y=700)
    btnedit1.config(width="10",height="2")
    btnedit1.configure(relief="solid")
    btnedit1.config(bd=0.5)
        
        
        
        
        
        

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
    
    
   #+++++++++++++++FRAME CAM USER++++++++++++++++++++++++++++++++#  
    miframe1=tkinter.Canvas(framecam)
    miframe1.config(width=840,height=420)
    miframe1.config(bg="white")
    miframe1.configure(relief="solid")
    miframe1.config(bd=0.5)
    miframe1.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe1.place(x=50,y=100)
    
    btncam = Button(framecam,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BuscarRostro()]) ## Boton crear cuenta
    btncam.place(x=1050,y=150)
    btncam.config(width="12")
    btncam.configure(relief="solid")
    btncam.config(bd=0.5)
    
    btncam1 = Button(framecam,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
    btncam1.place(x=1050,y=250)
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
    comboReconocimiento.place(x=1050,y=350)
    comboReconocimiento.current(0)
    btncombo = Button(framecam,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo()]) ## Boton crear cuenta
    btncombo.place(x=1040,y=450)
    btncombo.config(width="15")
    btncombo.configure(relief="solid")
    btncombo.config(bd=0.5)
    labelnombre= Label(framecam,text="Introduzca el nombre del rostro en pantalla",font=("Arial",10,'bold'))
    labelnombre.place(x=1050,y=700)
    entryNombre = ttk.Entry(framecam) ## Entrada de nombre
    entryNombre.place(x=1050, y=720,width="200",height="40")
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

    
   
#+++++++++++++++FRAME CAM ADMIN++++++++++++++++++++++++++++++++#  
    miframe3=tkinter.Canvas(framecamAdmin)
    miframe3.config(width=840,height=420)
    miframe3.config(bg="white")
    miframe3.configure(relief="solid")
    miframe3.config(bd=0.5)
    miframe3.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe3.place(x=50,y=100)
    
    btncam3 = Button(framecamAdmin,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BuscarRostroAdmin()()]) ## Boton crear cuenta
    btncam3.place(x=1050,y=150)
    btncam3.config(width="12")
    btncam3.configure(relief="solid")
    btncam3.config(bd=0.5)
    
    btncam1 = Button(framecamAdmin,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostroAdmin()()]) ## Boton crear cuenta
    btncam1.place(x=1050,y=250)
    btncam1.config(width="12")
    btncam1.configure(relief="solid")
    btncam1.config(bd=0.5)
    
    btncamAdmin = Button(framecamAdmin,text="Administrar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[FrameAdministrar()()]) ## Boton crear cuenta
    btncamAdmin.place(x=1200,y=100)
    btncamAdmin.config(width="12")
    btncamAdmin.configure(relief="solid")
    btncamAdmin.config(bd=0.5)
    
    
    my_label = tk.Label(framecamAdmin, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    my_label.place(x=750,y=550)
    # Define Our Images
    # Create A Button
    global triggerX,triggerZ,triggerY
    triggerX=False;
    triggerZ=False;
    triggerY=False;
    comboReconocimiento= ttk.Combobox(framecamAdmin)
    comboReconocimiento['values']= ('Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboReconocimiento.place(x=1050,y=350)
    comboReconocimiento.current(0)
    btncombo = Button(framecamAdmin,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo()]) ## Boton crear cuenta
    btncombo.place(x=1040,y=450)
    btncombo.config(width="15")
    btncombo.configure(relief="solid")
    btncombo.config(bd=0.5)
    labelnombre= Label(framecamAdmin,text="Introduzca el nombre del rostro en pantalla",font=("Arial",10,'bold'))
    labelnombre.place(x=1050,y=700)
    entryNombre = ttk.Entry(framecamAdmin) ## Entrada de nombre
    entryNombre.place(x=1050, y=720,width="200",height="40")
    nombrerostro="Hola"
    btnrastrear = Button(framecamAdmin,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo()]) ## Boton crear cuenta
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
        global triggerX,triggerZ,triggerY
        nombrerostro=entryNombre.get()
        if(triggerZ==True):
            reconocimientoC(nombrerostro)
 
        if(triggerY==True):
            reconocimientoB(nombrerostro)

        if(triggerX==True):
            reconocimientoA(nombrerostro)

    
   

    #+++++++++++++++FRAME Buscar Rostro+++++++++++++++++++++++++++++++#  
    miframe2=tkinter.Canvas(framecam1)
    miframe2.config(width=840,height=420)
    miframe2.config(bg="white")
    miframe2.configure(relief="solid")
    miframe2.config(bd=0.5)
    miframe2.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe2.place(x=50,y=100)
    
    btncam3 = Button(framecam1,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#9A9797',fg='black') ## Boton crear cuenta
    btncam3.place(x=1000,y=150)
    btncam3.config(width="12")
    btncam3.configure(relief="solid")
    btncam3.config(bd=0.5)
    
    btncam4 = Button(framecam1,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
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

            
 #+++++++++++++++FRAME Buscar Rostro ADMIN+++++++++++++++++++++++++++++++#  
    miframe4=tkinter.Canvas(framecam1Admin)
    miframe4.config(width=840,height=420)
    miframe4.config(bg="white")
    miframe4.configure(relief="solid")
    miframe4.config(bd=0.5)
    miframe4.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe4.place(x=50,y=100)
    
    btncam3 = Button(framecam1Admin,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#9A9797',fg='black') ## Boton crear cuenta
    btncam3.place(x=1000,y=150)
    btncam3.config(width="12")
    btncam3.configure(relief="solid")
    btncam3.config(bd=0.5)
    
    btncam4 = Button(framecam1Admin,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostroAdmin()()]) ## Boton crear cuenta
    btncam4.place(x=1000,y=250)
    btncam4.config(width="12")
    btncam4.configure(relief="solid")
    btncam4.config(bd=0.5)
    
    my_label1 = tk.Label(framecam1Admin, text = "Seleccionar Modo",bg="white",fg = "black",font = ("Arial", 14))
    my_label1.place(x=1000,y=100)
    
    comboReconocimiento1 = ttk.Combobox(framecam1Admin)
    comboReconocimiento1['values']= ('Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboReconocimiento1.place(x=1000,y=350)
    comboReconocimiento1.current(0)
    btncombo1 = Button(framecam1Admin,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo1()]) ## Boton crear cuenta
    btncombo1.place(x=1000,y=400)
    btncombo1.config(width="15")
    btncombo1.configure(relief="solid")
    btncombo1.config(bd=0.5)
    
    btncombo2 = Button(framecam1Admin,text="Guardar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    btncombo2.place(x=1000,y=490)
    btncombo2.config(width="15")
    btncombo2.configure(relief="solid")
    btncombo2.config(bd=0.5)
    
    my_label3 = tk.Label(framecam1Admin, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    my_label3.place(x=750,y=550)
    
    btnrastrear1 = Button(framecam1Admin,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo()]) ## Boton crear cuenta
    btnrastrear1.place(x=750,y=650)
    btnrastrear1.config(width="15")
    btnrastrear1.configure(relief="solid")
    btnrastrear1.config(bd=0.5)
    
    btnregresar = Button(framecam1Admin,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoAdmin1()()()]) ## Boton crear cuenta
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

            


 #+++++++++++++++FRAME Detectar Rostro+++++++++++++++++++++++++++++++#  
    miframe3=tkinter.Canvas(framecam2)
    miframe3.config(width=840,height=420)
    miframe3.config(bg="white")
    miframe3.configure(relief="solid")
    miframe3.config(bd=0.5)
    miframe3.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe3.place(x=50,y=100)
   
    btncam4 = Button(framecam2,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    btncam4.place(x=1000,y=150)
    btncam4.config(width="12")
    btncam4.configure(relief="solid")
    btncam4.config(bd=0.5)
    
    btncam4 = Button(framecam2,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#9A9797',fg='black',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
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
    
    btncombo4 = Button(framecam2,text="Guardar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[guardarRostro()]) ## Boton crear cuenta
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
        nombrerostro=entryNombre1.get()
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
        nombrerostro=entryNombre1.get()
      
        
        if(triggerC==True):
            reconocimientoC(nombrerostro)
 
        if(triggerB==True):
            reconocimientoB(nombrerostro)

        if(triggerA==True):
            reconocimientoA(nombrerostro)
               
            
#+++++++++++++++FRAME Detectar Rostro ADMIN+++++++++++++++++++++++++++++++#  
    miframe4=tkinter.Canvas(framecam2Admin)
    miframe4.config(width=840,height=420)
    miframe4.config(bg="white")
    miframe4.configure(relief="solid")
    miframe4.config(bd=0.5)
    miframe4.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe4.place(x=50,y=100)
   
    btncam5 = Button(framecam2Admin,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    btncam5.place(x=1000,y=150)
    btncam5.config(width="12")
    btncam5.configure(relief="solid")
    btncam5.config(bd=0.5)
    
    btncam4 = Button(framecam2Admin,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#9A9797',fg='black',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
    btncam4.place(x=1000,y=250)
    btncam4.config(width="12")
    btncam4.configure(relief="solid")
    btncam4.config(bd=0.5)
    
    my_label1 = tk.Label(framecam2Admin, text = "Seleccionar Modo",bg="white",fg = "black",font = ("Arial", 14))
    my_label1.place(x=1000,y=100)
    
    comboReconocimiento1 = ttk.Combobox(framecam2Admin)
    comboReconocimiento1['values']= ('Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboReconocimiento1.place(x=1000,y=350)
    comboReconocimiento1.current(0)
    btncombo3 = Button(framecam2Admin,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo1()]) ## Boton crear cuenta
    btncombo3.place(x=1000,y=400)
    btncombo3.config(width="15")
    btncombo3.configure(relief="solid")
    btncombo3.config(bd=0.5)
    
    btncombo4 = Button(framecam2Admin,text="Guardar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[guardarRostro2()]) ## Boton crear cuenta
    btncombo4.place(x=1000,y=490)
    btncombo4.config(width="15")
    btncombo4.configure(relief="solid")
    btncombo4.config(bd=0.5)
    
    my_label3 = tk.Label(framecam2Admin, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    my_label3.place(x=750,y=550)
    
    btnrastrear1 = Button(framecam2Admin,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo()]) ## Boton crear cuenta
    btnrastrear1.place(x=750,y=650)
    btnrastrear1.config(width="15")
    btnrastrear1.configure(relief="solid")
    btnrastrear1.config(bd=0.5)
    
    btnregresar = Button(framecam2Admin,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoAdmin1()()]) ## Boton crear cuenta
    btnregresar.place(x=1150,y=650)
    btnregresar.config(width="15")
    btnregresar.configure(relief="solid")
    btnregresar.config(bd=0.5)
    
    
    def switch1():
        global is_on
        global triggerX,triggerZtriggerY
        nombrerostro=entryNombre2.get()
        # Determine is on or off
        if is_on:
            on_button1A.config(image = off)
            my_label3.config(text = "Cámara apagada", bg="white",fg = "black",font = ("Arial", 14))
            is_on = False
        else:
           
            on_button1A.config(image = on)
            my_label3.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            is_on = True
            switch2a()
            
            
    def switch2a():
        global triggerA,triggerB,triggerC
        nombrerostro=entryNombre2.get()
      
        
        if(triggerC==True):
            reconocimientoC(nombrerostro)
 
        if(triggerB==True):
            reconocimientoB(nombrerostro)

        if(triggerA==True):
            reconocimientoA(nombrerostro)
               
            
    
    
    s = os.getcwd()
    new_s = s.replace('\\','/')
    new_s = s.replace('Main','Graficas')
    new_s1 = s.replace('\\','/')
    #new_s1 = s.replace('Main','Guardar informacion de rostros',entryNombre1.get())
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
    
    
    on_buttonA = Button(framecamAdmin, image = off, bd = 0,command = switch)
    on_buttonA.place(x=750,y=600)
    on_button1A = Button(framecam2Admin, image = off, bd = 0,command = switch1)
    on_button1A.place(x=750,y=600)
    on_button2A = Button(framecam1Admin, image = off, bd = 0,command = switch1)
    on_button2A.place(x=750,y=600)
    
    
    #Canvas detectar rostro USER
    C = tkinter.Canvas(framecam2)   
    C.config(width=692,height=200)
    C.configure(relief="solid")
    C.place(x=50,y=530)
    C.create_image(0,0, image=buscar, anchor="nw")
   
   
    #Canvas buscar rostro USER
    C2 = tkinter.Canvas(framecam1)   
    C2.config(width=692,height=200)
    C2.configure(relief="solid")
    C2.place(x=50,y=530)
    C2.create_image(0,0, image=detectar, anchor="nw")
   
    entryNombre1 = ttk.Entry(framecam2) ## Entrada de nombre
    entryNombre1.place(x=320, y=560, width="394",height="25")
    labelnombre1= Label(framecam2,text="Nombre",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelnombre1.place(x=320,y=537)
    entryDescripcion = ttk.Entry(framecam2) ## Entrada de nombre
    entryDescripcion.place(x=320, y=610, width="394",height="25")
    labelDescripcion= Label(framecam2,text="Descripción",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelDescripcion.place(x=320,y=587)
    entryFecha = ttk.Entry(framecam2) ## Entrada de nombre
    entryFecha.place(x=320, y=660, width="394",height="25")
    labelFecha= Label(framecam2,text="Fecha",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelFecha.place(x=320,y=637)
    
    
     #Canvas detectar rostro ADMIN
    C1 = tkinter.Canvas(framecam2Admin)   
    C1.config(width=692,height=200)
    C1.configure(relief="solid")
    C1.place(x=50,y=530)
    C1.create_image(0,0, image=buscar, anchor="nw")
   
   
    #Canvas buscar rostro ADMIN
    C3 = tkinter.Canvas(framecam1Admin)   
    C3.config(width=692,height=200)
    C3.configure(relief="solid")
    C3.place(x=50,y=530)
    C3.create_image(0,0, image=detectar, anchor="nw")
   
    entryNombre2 = ttk.Entry(framecam2Admin) ## Entrada de nombre
    entryNombre2.place(x=320, y=560, width="394",height="25")
    labelnombre2= Label(framecam2Admin,text="Nombre",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelnombre2.place(x=320,y=537)
    entryDescripcion2 = ttk.Entry(framecam2Admin) ## Entrada de nombre
    entryDescripcion2.place(x=320, y=610, width="394",height="25")
    labelDescripcion2= Label(framecam2Admin,text="Descripción",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelDescripcion2.place(x=320,y=587)
    entryFecha2 = ttk.Entry(framecam2Admin) ## Entrada de nombre
    entryFecha2.place(x=320, y=660, width="394",height="25")
    labelFecha2= Label(framecam2Admin,text="Fecha",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelFecha2.place(x=320,y=637)
    
    def guardarRostro():
        nombrerostro=entryNombre1.get()
        descripcionrostro=entryDescripcion.get()
        fecharostro=entryFecha.get()
        pruebatxt = os.getcwd()
        auxilioprueba = pruebatxt.replace('Main','Guardar informacion de rostros/'+nombrerostro+'/Datos.txt') 
        probando=("Nombre:"+nombrerostro+"\nDescipción:"+descripcionrostro+"\nFecha:"+fecharostro+"\n")
        f = open (auxilioprueba,'w')
        f.write(probando)
        f.close()
        
        
    def guardarRostro2():
        nombrerostro=entryNombre2.get()
        descripcionrostro=entryDescripcion2.get()
        fecharostro=entryFecha2.get()
        pruebatxt = os.getcwd()
        auxilioprueba = pruebatxt.replace('Main','Guardar informacion de rostros/'+nombrerostro+'/Datos.txt') 
        probando=("Nombre:"+nombrerostro+"\nDescipción:"+descripcionrostro+"\nFecha:"+fecharostro+"\n")
        f = open (auxilioprueba,'w')
        f.write(probando)
        f.close()
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
            show_frame(framecamAdmin)
        elif(resultado =='User'):
            print("Ingreso como User")
            show_frame(framecam)
        else:
            print("Error en usuario o contraseña")
            
    def Regreso():
            show_frame(framecam)
            
    def RegresoAdmin():
            show_frame(framelogin)
   
    def RegresoAdmin1():
            show_frame(framecamAdmin)
    def GotoEdit():
            show_frame(frameAdminEditar)        
    def RegresoPrincipal():
            show_frame(framecam)
    
    def Olvide():
            show_frame(frameforg)
            
    def DetectarRostro():
        show_frame(framecam2)
        
    def BuscarRostro():
        show_frame(framecam1)
        
    def DetectarRostroAdmin():
        show_frame(framecam2Admin)
        
    def BuscarRostroAdmin():
        show_frame(framecam1Admin)

    def FrameAdministrar():
        show_frame(frameAdmin)

    ##########################
    
    
            
    #l-l-l-l-l PROGRAMA MAIN l-l-l-l-l-l-#     
    show_frame(frameAdmin)     ## Mostramos el frame default (login)
    frametop=tkinter.Canvas(ventana) ## Corresponde a la barra verde superior que dice "Saveface" 
    frametop.config(width=2000,height=75) 
    frametop.place(x=0,y=0) 
    frametop.config(bg="#23442B") 
    frametop.create_text(100, 40, fill="white",text="SaveFace",font=("Arial",24,'bold')) 
    ventana.mainloop()
    #l-l-l-l-l-l-l-l-l-l-l-l-l-l-#     



