from LogicaBasica.Verificacion import verificarUsuario,verificarCorreo, verificarCantidadAdmin
from DetecciónRostros.Detecciónderostros import reconocimientoA,reconocimientoB,reconocimientoC, RastreoActivoCamara
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
    framecamUser = tk.Frame(ventana,bg="white")
    framecamUser.config(height=1900,width=1900)
    framecamAdmin = tk.Frame(ventana,bg="white")
    framecamAdmin.config(height=1900,width=1900)
    frameforg = tk.Frame(ventana,bg="white")
    frameforg.config(height=1900,width=1900)
    frameAdmin = tk.Frame(ventana,bg="white")
    frameAdmin.config(height=1900,width=1900)
    framecamBuscar = tk.Frame(ventana,bg="white")
    framecamBuscar.config(height=1900,width=1900)
    framecamDetectar = tk.Frame(ventana,bg="white")
    framecamDetectar.config(height=1900,width=1900)
    
    #frame Buscar Admin
    framecam1Admin = tk.Frame(ventana,bg="white") 
    framecam1Admin.config(height=1900,width=1900)
    
    #frame Detectar Admin
    framecam2Admin = tk.Frame(ventana,bg="white")
    framecam2Admin.config(height=1900,width=1900)
    
    frameAdminEditar = tk.Frame(ventana,bg="white")
    frameAdminEditar.config(height=1900,width=1900)
    frameRastreoActivo= tk.Frame(ventana,bg="white")
    frameRastreoActivo.config(height=1900,width=1900)
    frameAdminAdd= tk.Frame(ventana,bg="white")
    frameAdminAdd.config(height=1900,width=1900)
    for frame in (framelogin, framecamUser,framecamAdmin, frameforg,frameAdmin, framecamBuscar,framecamDetectar,framecam1Admin,framecam2Admin,frameAdminEditar,frameRastreoActivo,frameAdminAdd): #For para mostrar los frames
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
        
        AgregarUsuario= Button(Admin,text="Agregar Usuario",font=("Arial",16,'bold'),bg='#a8021e',fg='white',command=lambda:[GotoAñadir()])
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
        correoEntrada = editarUsuario2.get()
        if(correoEntrada!=None):
            if verificarCorreo(correoEntrada):
                contraseñaEntrada = editarContra2.get()
                if (messagebox.askyesno("Verificar Eliminación","¿Desea agregar a "+correoEntrada+" como Admin?")==True):
                    Lista.agregar(correoEntrada, contraseñaEntrada, "Admin")
                    probando=Lista.copiaratxt()
                    f = open (auxilioprueba,'w')
                    f.write(probando)
                    f.close()
                    Lista.imprimirlista()
                    show_frame(frameAdmin)
                    Actualizarpantalla()
                    editarUsuario.delete(0,END) 
                    editarContra.delete(0,END) 
                else:
                    Lista.agregar(correoEntrada, contraseñaEntrada, "User")
                    probando=Lista.copiaratxt()
                    f = open (auxilioprueba,'w')
                    f.write(probando)
                    f.close()
                    Lista.imprimirlista()
                    show_frame(frameAdmin)
                    Actualizarpantalla()
                    editarUsuario.delete(0,END) 
                    editarContra.delete(0,END) 
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
                            editarUsuario.delete(0,END) 
                            editarContra.delete(0,END) 
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
                            editarUsuario.delete(0,END) 
                            editarContra.delete(0,END) 
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
                            editarUsuario.delete(0,END) 
                            editarContra.delete(0,END) 
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
                            editarUsuario.delete(0,END) 
                            editarContra.delete(0,END) 
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
     
    ActivarCamara = Button(RastreoActivo,text="Activar camara",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RastreoActivoCamara()]) ## Boton crear cuenta 
    ActivarCamara.place(x=500,y=650) 
    ActivarCamara.config(width="12") 
    ActivarCamara.configure(relief="solid") 
    ActivarCamara.config(bd=0.5) 
     
    btnregresar = Button(RastreoActivo,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoPrincipal()]) ## Boton crear cuenta 
    btnregresar.place(x=1150,y=650) 
    btnregresar.config(width="15") 
    btnregresar.configure(relief="solid") 
    btnregresar.config(bd=0.5)     
 
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
    btnedit1 = Button(frameAdminEditar,text="Cancelar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[FrameAdministrarEditar()]) ## Boton crear cuenta 
    btnedit1.place(x=850,y=700) 
    btnedit1.config(width="10",height="2") 
    btnedit1.configure(relief="solid") 
    btnedit1.config(bd=0.5) 
         
    ################### FRAME AÑADIR####################
    Adminañadir = tkinter.Canvas(frameAdminAdd) 
    Adminañadir.config(width=1425,height=720) 
    Adminañadir.config(bg="white") 
    Adminañadir.configure(relief="solid") 
    Adminañadir.place(x=50,y=100) 
    editarUsuario2 = ttk.Entry(Adminañadir)     
    editarUsuario2.place(x=550,y=300,width="350",height="50") 
    editarContra2 = ttk.Entry(Adminañadir)     
    editarContra2.place(x=550,y=450,width="350",height="50") 
    Adminañadir.create_text(740, 75, text="Introduzca el correo y contraseña",font=("Arial",24,'bold')) 
    Adminañadir.create_text(715, 275, text="Correo",font=("Arial",14,'bold')) 
    Adminañadir.create_text(715, 425, text="Contraseña",font=("Arial",14,'bold')) 
    btnedit3 = Button(frameAdminAdd,text="Aceptar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:(Agregar())) ## Boton crear cuenta 
    btnedit3.place(x=550,y=700) 
    btnedit3.config(width="10",height="2") 
    btnedit3.configure(relief="solid") 
    btnedit3.config(bd=0.5) 
    btnedit2 = Button(frameAdminAdd,text="Cancelar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[FrameAdministrarAdd()]) ## Boton crear cuenta 
    btnedit2.place(x=850,y=700) 
    btnedit2.config(width="10",height="2") 
    btnedit2.configure(relief="solid") 
    btnedit2.config(bd=0.5) 
         #########################################################
         
        
        
        
        

    #+++++++++++++++FRAME LOGIN+++++++++++++++++++++++++++++++#
    
    miframe=tkinter.Canvas(framelogin)
    miframe.config(width=740,height=620)
    miframe.config(bg="white")
    miframe.configure(relief="solid")
    miframe.config(bd=0.5)
    miframe.create_text(50, 50, text="Inicio",font=("Sitka Text",14))
    miframe.place(x=400,y=100)
          
    btn2 = Button(miframe,text="Ingresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[Login()])
    btn2.place(x=270,y=380)
    btn2.config(width="16")
    btn2.configure(relief="solid")
    btn2.config(bd=0.5)
            
    
    btncontra = Button(miframe,text="Olvidó su contraseña",font=("Sitka Text",14,'bold', "underline") , bg='white',fg='darkcyan',command=lambda:[Olvide()])
    btncontra.place(x=270,y=460)
    btncontra.config(width="16")
    btncontra.configure(relief="solid")
    btncontra.config(bd=0)
    
    
    
    btn3 = Button(miframe,text="Crear Cuenta",font=("Arial",14,'bold') , bg='#858282',fg='white',command=lambda:[Olvide()]) ## Boton crear cuenta
    btn3.place(x=270,y=550)
    btn3.config(width="16")
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
    miframeUser=tkinter.Canvas(framecamUser)
    miframeUser.config(width=840,height=420)
    miframeUser.config(bg="white")
    miframeUser.configure(relief="solid")
    miframeUser.config(bd=0.5)
    miframeUser.create_text(50, 50, text="Camara",font=("Arial",14))
    miframeUser.place(x=100,y=175)
    
    btnBuscarRostro = Button(framecamUser,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BuscarRostro()]) ## Boton crear cuenta
    btnBuscarRostro.place(x=1050,y=200)
    btnBuscarRostro.config(width="16")
    btnBuscarRostro.configure(relief="solid")
    btnBuscarRostro.config(bd=0.5)
    
    btnDetectarRostro = Button(framecamUser,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
    btnDetectarRostro .place(x=1050,y=320)
    btnDetectarRostro .config(width="16")
    btnDetectarRostro .configure(relief="solid")
    btnDetectarRostro .config(bd=0.5)
    
    
    labelEstadoCam = tk.Label(framecamUser, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    labelEstadoCam.place(x=100,y=100)
    
    
    
    global triggerA,triggerC,triggerB
    triggerA=False;
    triggerC=False;
    triggerB=False;
    
    comboReconocimientoUser= ttk.Combobox(framecamUser, font= ("Arial", 14, "bold"))
    comboReconocimientoUser['values']= ('Seleccionar Patron','Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboReconocimientoUser.place(x=1050,y=450)
    comboReconocimientoUser.config(width = "16")
    comboReconocimientoUser.current(0)
    
    btnAplicarPatronUser = Button(framecamUser,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerComboUser()]) ## Boton crear cuenta
    btnAplicarPatronUser.place(x=1050,y=560)
    btnAplicarPatronUser.config(width="16")
    btnAplicarPatronUser.configure(relief="solid")
    btnAplicarPatronUser.config(bd=0.5)
    
    btnRastreoActivo = Button(framecamUser,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BottonRastreoActivo()]) ## Boton crear cuenta
    btnRastreoActivo.place(x=600,y=120)
    btnRastreoActivo.config(width="16")
    btnRastreoActivo.configure(relief="solid")
    btnRastreoActivo.config(bd=0.5)
    
    
   
    def switchAdmin():
        global is_on
        global triggerA,triggerC,triggerB
        
        # Determine is on or off
        if is_on:
            on_button.config(image = off)
            on_button1.config(image = off)
            on_button2.config(image = off)
            labelEstadoCam.config(text = "Cámara apagada", bg="white",fg = "black",font = ("Arial", 14))
            is_on = False
        else:
           
            on_button.config(image = on)
            on_button1.config(image = on)
            on_button2.config(image = on)
            
            labelEstadoCam.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            labelEstadoCamAdmin.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            labelEstadoCamBuscar.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            labelEstadoCamBuscarAdmin.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            labelEstadoCamDetectar.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            labelEstadoCamDetectarAdmin.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            is_on = True
            switch2Admin()
  
    def switch2Admin():
        global triggerA,triggerC,triggerB
        nombrerostro=entryNombreDetectarAdmin.get()
        if(triggerC==True):
            reconocimientoC(nombrerostro)
 
        if(triggerB==True):
            reconocimientoB(nombrerostro)

        if(triggerA==True):
            reconocimientoA(nombrerostro)

    

    def switchUser():
        global is_on
        global triggerA,triggerC,triggerB
        
        # Determine is on or off
        if is_on:
            on_button.config(image = off)
            on_button1.config(image = off)
            on_button2.config(image = off)
            labelEstadoCam.config(text = "Cámara apagada", bg="white",fg = "black",font = ("Arial", 14))
            is_on = False
        else:
           
            on_button.config(image = on)
            on_button1.config(image = on)
            on_button2.config(image = on)
            
            labelEstadoCam.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            labelEstadoCamAdmin.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            labelEstadoCamBuscar.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            labelEstadoCamBuscarAdmin.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            labelEstadoCamDetectar.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            labelEstadoCamDetectarAdmin.config(text = "Cámara encendida", bg="white",fg = "green",font = ("Arial", 14))
            is_on = True
            switch2User()
  
    def switch2User():
        global triggerA,triggerC,triggerB
        nombrerostro=entryNombreDetectarUser.get()
        if(triggerC==True):
            reconocimientoC(nombrerostro)
 
        if(triggerB==True):
            reconocimientoB(nombrerostro)

        if(triggerA==True):
            reconocimientoA(nombrerostro)

    
#+++++++++++++++FRAME CAM ADMIN++++++++++++++++++++++++++++++++#  
    miframe2=tkinter.Canvas(framecamAdmin)
    miframe2.config(width=840,height=420)
    miframe2.config(bg="white")
    miframe2.configure(relief="solid")
    miframe2.config(bd=0.5)
    miframe2.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe2.place(x=50,y=100)
    
    btnBuscarRostroAdmin = Button(framecamAdmin,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BuscarRostroAdmin()()]) ## Boton crear cuenta
    btnBuscarRostroAdmin.place(x=1050,y=150)
    btnBuscarRostroAdmin.config(width="12")
    btnBuscarRostroAdmin.configure(relief="solid")
    btnBuscarRostroAdmin.config(bd=0.5)
    
    btnDetectarAdmin = Button(framecamAdmin,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostroAdmin()()]) ## Boton crear cuenta
    btnDetectarAdmin.place(x=1050,y=250)
    btnDetectarAdmin.config(width="12")
    btnDetectarAdmin.configure(relief="solid")
    btnDetectarAdmin.config(bd=0.5)
    
    btnAdministrar = Button(framecamAdmin,text="Administrar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[FrameAdministrar()()]) ## Boton crear cuenta
    btnAdministrar.place(x=1200,y=100)
    btnAdministrar.config(width="12")
    btnAdministrar.configure(relief="solid")
    btnAdministrar.config(bd=0.5)
    
    
    labelEstadoCamAdmin = tk.Label(framecamAdmin, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    labelEstadoCamAdmin.place(x=750,y=550)
    
     
    global triggerX,triggerZ,triggerY
    triggerX=False;
    triggerZ=False;
    triggerY=False;
    
    comboReconocimientoAdmin= ttk.Combobox(framecamAdmin)
    comboReconocimientoAdmin['values']= ('Seleccionar Patron','Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboReconocimientoAdmin.place(x=1050,y=350)
    comboReconocimientoAdmin.current(0)
    
    btnAplicarPatronAdmin = Button(framecamAdmin,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerComboAdmin()]) ## Boton crear cuenta
    btnAplicarPatronAdmin.place(x=1040,y=450)
    btnAplicarPatronAdmin.config(width="15")
    btnAplicarPatronAdmin.configure(relief="solid")
    btnAplicarPatronAdmin.config(bd=0.5)
    
    
    btnRastreoActivoAdmin = Button(framecamAdmin,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BottonRastreoActivo()]) ## Boton crear cuenta
    btnRastreoActivoAdmin.place(x=750,y=650)
    btnRastreoActivoAdmin.config(width="15")
    btnRastreoActivoAdmin.configure(relief="solid")
    btnRastreoActivoAdmin.config(bd=0.5)
    
   

    #+++++++++++++++FRAME Buscar Rostro User+++++++++++++++++++++++++++++++#  
    miframe3=tkinter.Canvas(framecamBuscar)
    miframe3.config(width=840,height=420)
    miframe3.config(bg="white")
    miframe3.configure(relief="solid")
    miframe3.config(bd=0.5)
    miframe3.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe3.place(x=100,y=175)
    
    botonBuscarRostro = Button(framecamBuscar,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#9A9797',fg='black') ## Boton crear cuenta
    botonBuscarRostro.place(x=1050,y=200)
    botonBuscarRostro.config(width="16")
    botonBuscarRostro.configure(relief="solid")
    botonBuscarRostro.config(bd=0.5)
    
    botonDetectarRostro = Button(framecamBuscar,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
    botonDetectarRostro.place(x=1050,y=270)
    botonDetectarRostro.config(width="16")
    botonDetectarRostro.configure(relief="solid")
    botonDetectarRostro.config(bd=0.5)
    
    my_label1 = tk.Label(framecamBuscar, text = "Seleccionar Modo",bg="white",fg = "black",font = ("Arial", 14, "bold"))
    my_label1.place(x=1060,y=150)
    
    comboBoxBuscarRostroUser = ttk.Combobox(framecamBuscar, font=("Arial", 14, "bold"))
    comboBoxBuscarRostroUser['values']= ('Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboBoxBuscarRostroUser.place(x=1050,y=340)
    comboBoxBuscarRostroUser.config(width = "16")
    comboBoxBuscarRostroUser.current(0)
    
    botonAplicPatronBuscarRostro = Button(framecamBuscar,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    botonAplicPatronBuscarRostro.place(x=1050,y=410)
    botonAplicPatronBuscarRostro.config(width="16")
    botonAplicPatronBuscarRostro.configure(relief="solid")
    botonAplicPatronBuscarRostro.config(bd=0.5)
    
    botonGuardarRostro = Button(framecamBuscar,text="Guardar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    botonGuardarRostro.place(x=1050,y=480)
    botonGuardarRostro.config(width="16")
    botonGuardarRostro.configure(relief="solid")
    botonGuardarRostro.config(bd=0.5)
    
    labelEstadoCamBuscar = tk.Label(framecamBuscar, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    labelEstadoCamBuscar.place(x=750,y=550)
    
    btnrastrearBuscarRostro = Button(framecamBuscar,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BottonRastreoActivo()]) ## Boton crear cuenta
    btnrastrearBuscarRostro.place(x=600,y=120)
    btnrastrearBuscarRostro.config(width="16")
    btnrastrearBuscarRostro.configure(relief="solid")
    btnrastrearBuscarRostro.config(bd=0.5)
    
    btnRegresarBuscarRostro = Button(framecamBuscar,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoPrincipal()]) ## Boton crear cuenta
    btnRegresarBuscarRostro.place(x=1050,y=570)
    btnRegresarBuscarRostro.config(width="16")
    btnRegresarBuscarRostro.configure(relief="solid")
    btnRegresarBuscarRostro.config(bd=0.5)
    
    
    
    
    
 #+++++++++++++++FRAME Buscar Rostro ADMIN+++++++++++++++++++++++++++++++#  
    miframe4=tkinter.Canvas(framecam1Admin)
    miframe4.config(width=840,height=420)
    miframe4.config(bg="white")
    miframe4.configure(relief="solid")
    miframe4.config(bd=0.5)
    miframe4.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe4.place(x=50,y=100)
    
    botonBuscarRostroAdmin = Button(framecam1Admin,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#9A9797',fg='black') ## Boton crear cuenta
    botonBuscarRostroAdmin.place(x=1000,y=150)
    botonBuscarRostroAdmin.config(width="12")
    botonBuscarRostroAdmin.configure(relief="solid")
    botonBuscarRostroAdmin.config(bd=0.5)
    
    botonDetectarRostroAdmin = Button(framecam1Admin,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostroAdmin()()]) ## Boton crear cuenta
    botonDetectarRostroAdmin.place(x=1000,y=250)
    botonDetectarRostroAdmin.config(width="12")
    botonDetectarRostroAdmin.configure(relief="solid")
    botonDetectarRostroAdmin.config(bd=0.5)
    
    my_label1 = tk.Label(framecam1Admin, text = "Seleccionar Modo",bg="white",fg = "black",font = ("Arial", 14))
    my_label1.place(x=1000,y=100)
    
    comboBoxBuscarRostroAdmin = ttk.Combobox(framecam1Admin)
    comboBoxBuscarRostroAdmin['values']= ('Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboBoxBuscarRostroAdmin.place(x=1000,y=350)
    comboBoxBuscarRostroAdmin.current(0)
    
    botonAplicPatronBuscarR = Button(framecam1Admin,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    botonAplicPatronBuscarR.place(x=1000,y=400)
    botonAplicPatronBuscarR.config(width="15")
    botonAplicPatronBuscarR.configure(relief="solid")
    botonAplicPatronBuscarR.config(bd=0.5)
    
    botonGuardarRostroAdmin = Button(framecam1Admin,text="Guardar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    botonGuardarRostroAdmin.place(x=1000,y=490)
    botonGuardarRostroAdmin.config(width="15")
    botonGuardarRostroAdmin.configure(relief="solid")
    botonGuardarRostroAdmin.config(bd=0.5)
    
    labelEstadoCamBuscarAdmin = tk.Label(framecam1Admin, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    labelEstadoCamBuscarAdmin.place(x=750,y=550)
    
    btnrastrearBuscarRostroAdmin = Button(framecam1Admin,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BottonRastreoActivo()]) ## Boton crear cuenta
    btnrastrearBuscarRostroAdmin.place(x=750,y=650)
    btnrastrearBuscarRostroAdmin.config(width="15")
    btnrastrearBuscarRostroAdmin.configure(relief="solid")
    btnrastrearBuscarRostroAdmin.config(bd=0.5)
    
    btnRegresarBuscarR = Button(framecam1Admin,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoAdmin1()()()]) ## Boton crear cuenta
    btnRegresarBuscarR.place(x=1150,y=650)
    btnRegresarBuscarR.config(width="15")
    btnRegresarBuscarR.configure(relief="solid")
    btnRegresarBuscarR.config(bd=0.5)
    
    
    
    
    

            


 #+++++++++++++++FRAME Detectar Rostro User+++++++++++++++++++++++++++++++#  
    miframe5=tkinter.Canvas(framecamDetectar)
    miframe5.config(width=840,height=420)
    miframe5.config(bg="white")
    miframe5.configure(relief="solid")
    miframe5.config(bd=0.5)
    miframe5.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe5.place(x=100,y=175)
   
    btnBuscarRostroUser = Button(framecamDetectar,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    btnBuscarRostroUser.place(x=1050,y=200)
    btnBuscarRostroUser.config(width="16")
    btnBuscarRostroUser.configure(relief="solid")
    btnBuscarRostroUser.config(bd=0.5)
    
    btnDetectarRostroUser = Button(framecamDetectar,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#9A9797',fg='black',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
    btnDetectarRostroUser.place(x=1050,y=270)
    btnDetectarRostroUser.config(width="16")
    btnDetectarRostroUser.configure(relief="solid")
    btnDetectarRostroUser.config(bd=0.5)
    
    my_label1 = tk.Label(framecamDetectar, text = "Seleccionar Modo",bg="white",fg = "black",font = ("Arial", 14, "bold"))
    my_label1.place(x=1060,y=150)
    
    comboBoxDetectarRostroUser = ttk.Combobox(framecamDetectar, font=("Arial", 14,"bold"))
    comboBoxDetectarRostroUser['values']= ('Seleccionar Patron','Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboBoxDetectarRostroUser.place(x=1050,y=340)
    comboBoxDetectarRostroUser.config(width= "16")
    comboBoxDetectarRostroUser.current(0)
    
    botonAplicarDetectarUser = Button(framecamDetectar,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerComboUser()]) ## Boton crear cuenta
    botonAplicarDetectarUser.place(x=1050,y=410)
    botonAplicarDetectarUser.config(width="16")
    botonAplicarDetectarUser.configure(relief="solid")
    botonAplicarDetectarUser.config(bd=0.5)
    
    botonGuardarRostroUser = Button(framecamDetectar,text="Guardar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[guardarRostro()]) ## Boton crear cuenta
    botonGuardarRostroUser.place(x=1050,y=480)
    botonGuardarRostroUser.config(width="16")
    botonGuardarRostroUser.configure(relief="solid")
    botonGuardarRostroUser.config(bd=0.5)
    
    labelEstadoCamDetectar = tk.Label(framecamDetectar, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    labelEstadoCamDetectar.place(x=750,y=550)
    
    botonRastreoActivoUser = Button(framecamDetectar,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BottonRastreoActivo()]) ## Boton crear cuenta
    botonRastreoActivoUser.place(x=600,y=120)
    botonRastreoActivoUser.config(width="16")
    botonRastreoActivoUser.configure(relief="solid")
    botonRastreoActivoUser.config(bd=0.5)
    
    botonRegresarDetectarUser = Button(framecamDetectar,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoPrincipal()]) ## Boton crear cuenta
    botonRegresarDetectarUser.place(x=1050,y=570)
    botonRegresarDetectarUser.config(width="16")
    botonRegresarDetectarUser.configure(relief="solid")
    botonRegresarDetectarUser.config(bd=0.5)
    
    
   
            
#+++++++++++++++FRAME Detectar Rostro ADMIN+++++++++++++++++++++++++++++++#  
    miframe4=tkinter.Canvas(framecam2Admin)
    miframe4.config(width=840,height=420)
    miframe4.config(bg="white")
    miframe4.configure(relief="solid")
    miframe4.config(bd=0.5)
    miframe4.create_text(50, 50, text="Camara",font=("Arial",14))
    miframe4.place(x=50,y=100)
   
    botonBuscarAdmin = Button(framecam2Admin,text="Buscar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white') ## Boton crear cuenta
    botonBuscarAdmin.place(x=1000,y=150)
    botonBuscarAdmin.config(width="12")
    botonBuscarAdmin.configure(relief="solid")
    botonBuscarAdmin.config(bd=0.5)
    
    botonDetectarAdmin = Button(framecam2Admin,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#9A9797',fg='black',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
    botonDetectarAdmin.place(x=1000,y=250)
    botonDetectarAdmin.config(width="12")
    botonDetectarAdmin.configure(relief="solid")
    botonDetectarAdmin.config(bd=0.5)
    
    my_label1 = tk.Label(framecam2Admin, text = "Seleccionar Modo",bg="white",fg = "black",font = ("Arial", 14))
    my_label1.place(x=1000,y=100)
    
    comboBoxDetectarRostroAdmin = ttk.Combobox(framecam2Admin)
    comboBoxDetectarRostroAdmin['values']= ('Seleccionar Patron','Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboBoxDetectarRostroAdmin.place(x=1000,y=350)
    comboBoxDetectarRostroAdmin.current(0)
    
    botonAplicarDetectarAdmin = Button(framecam2Admin,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerComboAdmin()]) ## Boton crear cuenta
    botonAplicarDetectarAdmin.place(x=1000,y=400)
    botonAplicarDetectarAdmin.config(width="15")
    botonAplicarDetectarAdmin.configure(relief="solid")
    botonAplicarDetectarAdmin.config(bd=0.5)
    
    btnDetectarRostroAdmin = Button(framecam2Admin,text="Guardar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[guardarRostro2()]) ## Boton crear cuenta
    btnDetectarRostroAdmin.place(x=1000,y=490)
    btnDetectarRostroAdmin.config(width="15")
    btnDetectarRostroAdmin.configure(relief="solid")
    btnDetectarRostroAdmin.config(bd=0.5)
    
    labelEstadoCamDetectarAdmin = tk.Label(framecam2Admin, text = "Cámara apagada",bg="white",fg = "black",font = ("Arial", 14))
    labelEstadoCamDetectarAdmin.place(x=750,y=550)
    
    botonRastreoActivoAdmin = Button(framecam2Admin,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BottonRastreoActivo()]) ## Boton crear cuenta
    botonRastreoActivoAdmin.place(x=750,y=650)
    botonRastreoActivoAdmin.config(width="15")
    botonRastreoActivoAdmin.configure(relief="solid")
    botonRastreoActivoAdmin.config(bd=0.5)
    
    botonRegresarDetectarAdmin = Button(framecam2Admin,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoAdmin1()()]) ## Boton crear cuenta
    botonRegresarDetectarAdmin.place(x=1150,y=650)
    botonRegresarDetectarAdmin.config(width="15")
    botonRegresarDetectarAdmin.configure(relief="solid")
    botonRegresarDetectarAdmin.config(bd=0.5)
    
    
    
    s = os.getcwd()
    new_s = s.replace('\\','/')
    new_s = s.replace('Main','Graficas')
    new_s1 = s.replace('\\','/')
    #new_s1 = s.replace('Main','Guardar informacion de rostros',entryNombre1.get())
    on = PhotoImage(file = new_s+"/on.png")
    off = PhotoImage(file = new_s+"/off.png")
    detectar = PhotoImage(file = new_s+"/imagenDetectar.png")
    buscar = PhotoImage(file = new_s+"/imagenBuscar.png")
    
    on_button = Button(framecamUser, image = off, bd = 0,command = switchUser)
    on_button.place(x=100,y=130)
    on_button1 = Button(framecamBuscar, image = off, bd = 0,command = switchUser)
    on_button1.place(x=100,y=130)
    on_button2 = Button(framecamDetectar, image = off, bd = 0,command = switchUser)
    on_button2.place(x=100,y=130)
    
    
    on_buttonA = Button(framecamAdmin, image = off, bd = 0,command = switchAdmin)
    on_buttonA.place(x=750,y=600)
    on_button1A = Button(framecam2Admin, image = off, bd = 0,command = switchAdmin)
    on_button1A.place(x=750,y=600)
    on_button2A = Button(framecam1Admin, image = off, bd = 0,command = switchAdmin)
    on_button2A.place(x=750,y=600)
    
    
    #Canvas detectar rostro USER
    CanvasDetectarUser = tkinter.Canvas(framecamDetectar)   
    CanvasDetectarUser.config(width=840,height=200)
    CanvasDetectarUser.configure(relief="solid")
    CanvasDetectarUser.place(x=100,y=600)
    CanvasDetectarUser.create_image(0,0, image=buscar, anchor="nw")
   
   
    #Canvas buscar rostro USER
    CanvasBuscarRostroUser = tkinter.Canvas(framecamBuscar)   
    CanvasBuscarRostroUser.config(width=840,height=200)
    CanvasBuscarRostroUser.configure(relief="solid")
    CanvasBuscarRostroUser.place(x=100,y=600)
    CanvasBuscarRostroUser.create_image(0,0, image=detectar, anchor="nw")
   
    entryNombreDetectarUser = ttk.Entry(framecamDetectar) ## Entrada de nombre
    entryNombreDetectarUser.place(x=360, y=640, width="450",height="25")
    labelnombreDetectarUser= Label(framecamDetectar,text="Nombre",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelnombreDetectarUser.place(x=360, y=620)
    
    entryDescripcionDetectarUser = ttk.Entry(framecamDetectar) ## Entrada de descripción
    entryDescripcionDetectarUser.place(x=360,y=700, width="450",height="25")
    entryDescripcionDetectarUser= Label(framecamDetectar,text="Descripción",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    entryDescripcionDetectarUser.place(x=360,y=680)
    
    entryFechaDetectarUser = ttk.Entry(framecamDetectar) ## Entrada de fecha
    entryFechaDetectarUser.place(x=360,y=760, width="450",height="25")
    labelFechaDetectarUser = Label(framecamDetectar,text="Fecha",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelFechaDetectarUser.place(x=360,y=740)
    
    
     #Canvas detectar rostro ADMIN
    CanvasDetectarAdmin = tkinter.Canvas(framecam2Admin)   
    CanvasDetectarAdmin.config(width=692,height=200)
    CanvasDetectarAdmin.configure(relief="solid")
    CanvasDetectarAdmin.place(x=50,y=530)
    CanvasDetectarAdmin.create_image(0,0, image=buscar, anchor="nw")
   
   
    #Canvas buscar rostro ADMIN
    CanvasBuscarRostroAdmin = tkinter.Canvas(framecam1Admin)   
    CanvasBuscarRostroAdmin.config(width=692,height=200)
    CanvasBuscarRostroAdmin.configure(relief="solid")
    CanvasBuscarRostroAdmin.place(x=50,y=530)
    CanvasBuscarRostroAdmin.create_image(0,0, image=detectar, anchor="nw")
   
    entryNombreDetectarAdmin= ttk.Entry(framecam2Admin) ## Entrada de nombre
    entryNombreDetectarAdmin.place(x=320, y=560, width="394",height="25")
    
    labelnombreDetectarAdmin= Label(framecam2Admin,text="Nombre",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelnombreDetectarAdmin.place(x=320,y=537)
    
    entryDescripcionDetectarAdmin = ttk.Entry(framecam2Admin) ## Entrada de nombre
    entryDescripcionDetectarAdmin.place(x=320, y=610, width="394",height="25")
    
    labelDescripcionDetectarAdmin= Label(framecam2Admin,text="Descripción",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelDescripcionDetectarAdmin.place(x=320,y=587)
    
    entryFechaDetectarAdmin = ttk.Entry(framecam2Admin) ## Entrada de nombre
    entryFechaDetectarAdmin.place(x=320, y=660, width="394",height="25")
    
    labelFechaDetectarAdmin = Label(framecam2Admin,text="Fecha",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelFechaDetectarAdmin.place(x=320,y=637)
    
    def guardarRostro():
        nombrerostro=entryNombreDetectarAdmin.get()
        descripcionrostro=entryDescripcionDetectarAdmin.get()
        fecharostro=entryFechaDetectarAdmin.get()
        pruebatxt = os.getcwd()
        auxilioprueba = pruebatxt.replace('Main','Guardar informacion de rostros/'+nombrerostro+'/Datos.txt') 
        probando=("Nombre:"+nombrerostro+"\nDescipción:"+descripcionrostro+"\nFecha:"+fecharostro+"\n")
        f = open (auxilioprueba,'w')
        f.write(probando)
        f.close()
        
        
    def guardarRostro2():
        nombrerostro=entryNombreDetectarUser.get()
        descripcionrostro=entryDescripcionDetectarUser.get()
        fecharostro=entryFechaDetectarUser.get()
        pruebatxt = os.getcwd()
        auxilioprueba = pruebatxt.replace('Main','Guardar informacion de rostros/'+nombrerostro+'/Datos.txt') 
        probando=("Nombre:"+nombrerostro+"\nDescipción:"+descripcionrostro+"\nFecha:"+fecharostro+"\n")
        f = open (auxilioprueba,'w')
        f.write(probando)
        f.close()
    # FUNCIONES             #
    #########################
    
    

    def obtenerComboAdmin():
        comparar=comboReconocimientoAdmin.get()
        compararDetectar=comboBoxDetectarRostroAdmin.get()
        global nombrerostro
        nombrerostro=entryNombreDetectarAdmin.get()
        global triggerA
        global triggerB
        global triggerC
        
        if(comparar =='Reconocimiento A' or compararDetectar == 'Reconocimiento A'):
            triggerC=False
            triggerB=False
            triggerA=True
            return True  
            print("si entra A")
        if(comparar =='Reconocimiento B' or compararDetectar == 'Reconocimiento B'):
            triggerA=False
            triggerC=False
            triggerB=True
            return True 
            print("si entra B")
        if(comparar =='Reconocimiento C' or compararDetectar == 'Reconocimiento C' ):
            triggerA=False
            triggerB=False
            triggerC=True
            return True
            print("si entra C")
            
    def obtenerComboUser():
        comparar1=comboReconocimientoUser.get()
        compararDetectarUser=comboBoxDetectarRostroUser.get()
        print(compararDetectarUser)
        global nombrerostro
        nombrerostro=entryNombreDetectarUser.get()
        global triggerA
        global triggerB
        global triggerC
        
        if(comparar1 =='Reconocimiento A' or compararDetectarUser == 'Reconocimiento A'):
            triggerC=False
            triggerB=False
            triggerA=True
            return True  
            
      
       
        if(comparar1 =='Reconocimiento B' or compararDetectarUser == 'Reconocimiento B'):
            triggerA=False
            triggerC=False
            triggerB=True
            return True 
            
      
        if(comparar1 =='Reconocimiento C' or compararDetectarUser == 'Reconocimiento C'):
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
            show_frame(framecamUser)
        else:
            print("Error en usuario o contraseña")
            
    def Regreso():
            show_frame(framecamUser)
            
    def RegresoAdmin():
            show_frame(framelogin)
   
    def RegresoAdmin1():
            show_frame(framecamAdmin)
    def GotoAñadir():
        show_frame(frameAdminAdd)
    def GotoEdit(): 
        if(opcion.get()!=0): 
            show_frame(frameAdminEditar)       
        else: 
            messagebox.showwarning("Error selección", "No ha seleccionado nada para poder editar")        
    def RegresoPrincipal():
            show_frame(framecamUser)
    
    def Olvide():
            show_frame(frameforg)
            
    def DetectarRostro():
        show_frame(framecamDetectar)
        
    def BuscarRostro():
        show_frame(framecamBuscar)
        
    def DetectarRostroAdmin():
        show_frame(framecam2Admin)
        
    def BuscarRostroAdmin():
        show_frame(framecam1Admin)

    def FrameAdministrarEditar():
        editarUsuario.delete(0,END) 
        editarContra.delete(0,END) 
        show_frame(frameAdmin) 
    def FrameAdministrarAdd():
        editarUsuario2.delete(0,END) 
        editarContra2.delete(0,END) 
        show_frame(frameAdmin) 

    def FrameAdministrar():
        show_frame(frameAdmin)
    
    def BottonRastreoActivo():
            show_frame(frameRastreoActivo)


    ##########################
    
    
            
    #l-l-l-l-l PROGRAMA MAIN l-l-l-l-l-l-#     
    show_frame(framecamUser)     ## Mostramos el frame default (login)
    frametop=tkinter.Canvas(ventana) ## Corresponde a la barra verde superior que dice "Saveface" 
    frametop.config(width=2000,height=75) 
    frametop.place(x=0,y=0) 
    frametop.config(bg="#23442B") 
    frametop.create_text(100, 40, fill="white",text="SaveFace",font=("Arial",24,'bold')) 
    ventana.mainloop()
    #l-l-l-l-l-l-l-l-l-l-l-l-l-l-#     



