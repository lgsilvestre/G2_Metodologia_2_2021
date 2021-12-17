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
global tipoUsuario
tipoUsuario=" "

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
    
    #------- Frame Usuario --------#
    framecamUser = tk.Frame(ventana,bg="white")
    framecamUser.config(height=1900,width=1900)
    
    #-----------Frame Administrador ------------#
    framecamAdmin = tk.Frame(ventana,bg="white")
    framecamAdmin.config(height=1900,width=1900)
    
    #------ Frame Olvidó Contraseña -------#
    frameforg = tk.Frame(ventana,bg="white")
    frameforg.config(height=1900,width=1900)
    
    # Frame Administrar(Agregar, editar, eliminar usuarios)#
    frameAdmin = tk.Frame(ventana,bg="white")
    frameAdmin.config(height=1900,width=1900)
    
    ## FRAME DETECTAR ROSTRO DEFINITIVO####
    DetectFace = tk.Frame(ventana,bg="white")
    DetectFace.config(height=1900,width=1900)
    
    frameAdminEditar = tk.Frame(ventana,bg="white")
    frameAdminEditar.config(height=1900,width=1900)
    
    frameAdminAdd= tk.Frame(ventana,bg="white")
    frameAdminAdd.config(height=1900,width=1900)
    
    frameRastreoActivo= tk.Frame(ventana,bg="white")
    frameRastreoActivo.config(height=1900,width=1900)
    
    frameRastreoActivoAdmin= tk.Frame(ventana,bg="white")
    frameRastreoActivoAdmin.config(height=1900,width=1900)
    
    for frame in (framelogin, framecamUser,framecamAdmin,DetectFace, frameforg,frameAdmin, frameAdminEditar,frameAdminAdd,frameRastreoActivo,frameRastreoActivoAdmin): #For para mostrar los frames
        frame.grid(row=0,column=0,sticky='nsew')

    #NO ELIMINAR
    #-----------------RadiobuttonBox----------------#
    opcion= IntVar()

    #NO ELIMINAR
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
    #NO ELIMINAR
    #------------Actualizar Pantalla----------------#
    def Actualizarpantalla():
        Admin = tkinter.Canvas(frameAdmin)
        Admin.config(width=1425,height=720)
        Admin.config(bg="white")
        Admin.configure(relief="solid")
        Admin.place(x=50,y=100)
        
        Admin.create_text(740, 75, text="Administrar",font=("Arial",36,'bold'))
        
        
        #-------------------Button-------------------#
        RegresarPrincipal= Button(Admin,text="Regresar",font=("Arial",20,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoAdmin()])
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
          
    #NO ELIMINAR
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
        
    #----------------Funciones de Admin-------------#
    #NO ELIMINAR
    #----------------Agregar Usuario----------------#
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
                    editarUsuario2.delete(0,END) 
                    editarContra2.delete(0,END)
                  
                else:
                    Lista.agregar(correoEntrada, contraseñaEntrada, "User")
                    probando=Lista.copiaratxt()
                    f = open (auxilioprueba,'w')
                    f.write(probando)
                    f.close()
                    Lista.imprimirlista()
                    show_frame(frameAdmin)
                    Actualizarpantalla() 
                    editarUsuario2.delete(0,END) 
                    editarContra2.delete(0,END)
                  
            else:
                messagebox.showwarning("Error Correo", "El correo "+correoEntrada+" no es valido")
    
    #NO ELIMINAR
    #----------------Editar Usuario-----------------#
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
        
     #NO ELIMINAR   
    #--------------Eliminar Usuario-----------------#
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
    
        
    #NO ELIMINAR
    #------------Frame Rastreo Activo--------------# 
    RastreoActivo = tkinter.Canvas(frameRastreoActivo) 
    RastreoActivo.config(width=1425,height=720) 
    RastreoActivo.config(bg="white") 
    RastreoActivo.configure(relief="solid") 
    RastreoActivo.place(x=50,y=100) 
     
    ActivarCamara = Button(RastreoActivo,text="Activar camara",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RastreoActivoCamara()]) ## Boton crear cuenta 
    ActivarCamara.place(x=600,y=550) 
    ActivarCamara.config(width="16") 
    ActivarCamara.configure(relief="solid") 
    ActivarCamara.config(bd=0.5) 
     
    btnregresar = Button(RastreoActivo,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoDeRastreoActivo()]) ## Boton crear cuenta 
    btnregresar.place(x=1150,y=650) 
    btnregresar.config(width="15") 
    btnregresar.configure(relief="solid") 
    btnregresar.config(bd=0.5)     
    
      
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
    Admineditar.create_text(760, 100, text="para editar un usuario",font=("Arial",24,'bold')) 
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
    Adminañadir.create_text(760, 100, text="para agregar un usuario",font=("Arial",24,'bold'))
    Adminañadir.create_text(715, 275, text="Correo",font=("Arial",14,'bold')) 
    Adminañadir.create_text(715, 425, text="Contraseña",font=("Arial",14,'bold')) 
    
    btnedit3 = Button(frameAdminAdd,text="Aceptar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[Agregar()]) ## Boton crear cuenta 
    btnedit3.place(x=550,y=700) 
    btnedit3.config(width="10",height="2") 
    btnedit3.configure(relief="solid") 
    btnedit3.config(bd=0.5) 
    
    btnedit2 = Button(frameAdminAdd,text="Cancelar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[FrameAdministrarAdd()]) ## Boton crear cuenta 
    btnedit2.place(x=850,y=700) 
    btnedit2.config(width="10",height="2") 
    btnedit2.configure(relief="solid") 
    btnedit2.config(bd=0.5) 
         

    #----------------Frame Login--------------------# 
    miframe=tkinter.Canvas(framelogin)
    miframe.config(width=740,height=620)
    miframe.config(bg="white")
    miframe.configure(relief="solid")
    miframe.config(bd=0.5)
    miframe.create_text(50, 50, text="Inicio",font=("Sitka Text",14))
    miframe.place(x=400,y=100)
          
    btnIngresar = Button(miframe,text="Ingresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[Login()])
    btnIngresar.place(x=270,y=380)
    btnIngresar.config(width="16")
    btnIngresar.configure(relief="solid")
    btnIngresar.config(bd=0.5)
            
    btnOlvidar = Button(miframe,text="Olvidó su contraseña",font=("Sitka Text",14,'bold', "underline") , bg='white',fg='darkcyan',command=lambda:[Olvide()])
    btnOlvidar.place(x=270,y=460)
    btnOlvidar.config(width="16")
    btnOlvidar.configure(relief="solid")
    btnOlvidar.config(bd=0)
    
    btnCrear = Button(miframe,text="Crear Cuenta",font=("Arial",14,'bold') , bg='#858282',fg='white',command=lambda:[Olvide()]) ## Boton crear cuenta
    btnCrear.place(x=270,y=550)
    btnCrear.config(width="16")
    btnCrear.configure(relief="solid")
    btnCrear.config(bd=0.5)
    
    miframe.create_text(155, 110, text="Correo Electrónico",font=("Sitka Text",14)) ##Se crea un texto desde miframe
    miframe.create_text(125, 240, text="Contraseña",font=("Sitka Text",14))
    
    EntradaUsuario = ttk.Entry(miframe) ## Entrada de correo
    EntradaUsuario.place(x=75, y=130,width="600",height="40")
    
    EntradaContraseña = ttk.Entry(miframe) ## Entrada de contraseña
    EntradaContraseña.place(x=75, y=260,width="600",height="40")
    EntradaContraseña.config(show="*")
    
    miframe.create_line(20,80,730,80,fill="darkcyan")
    miframe.create_line(20,510,730,510,fill="darkcyan")
   
    
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
   
    RastreoActivo = tkinter.Canvas(framecamUser) 
    RastreoActivo.config(width=500,height=300) 
    RastreoActivo.config(bg="white") 
    RastreoActivo.configure(relief="solid") 
    RastreoActivo.place(x=25, y=90)     
   
    labelUser = tk.Label(framecamUser, text = "Seleccionar acción deseada ",bg="white",fg = "black",font = ("Arial", 16, "bold"))
    labelUser.place(x=130,y=150) 
   
    btnDetectarRostro = Button(framecamUser,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
    btnDetectarRostro .place(x=50,y=250)
    btnDetectarRostro .config(width="16")
    btnDetectarRostro .configure(relief="solid")
    btnDetectarRostro .config(bd=0.5)
    
    btnRastreoActivo = Button(framecamUser,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BottonRastreoActivo()]) ## Boton crear cuenta
    btnRastreoActivo.place(x=300,y=250)
    btnRastreoActivo.config(width="16")
    btnRastreoActivo.configure(relief="solid")
    btnRastreoActivo.config(bd=0.5)


#+++++++++++++++FRAME CAM ADMIN++++++++++++++++++++++++++++++++#  
    miframe2=tkinter.Canvas(framecamAdmin)
    miframe2.config(width=500,height=300)
    miframe2.config(bg="white")
    miframe2.configure(relief="solid")
    miframe2.place(x=25, y=90)
    
    labelAdmin = tk.Label(framecamAdmin, text = "Seleccionar acción deseada ",bg="white",fg = "black",font = ("Arial", 16, "bold"))
    labelAdmin.place(x=130,y=150)
    
    
    btnDetectarAdmin = Button(framecamAdmin,text="Detectar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[DetectarRostro()]) ## Boton crear cuenta
    btnDetectarAdmin.place(x=50,y=250)
    btnDetectarAdmin.config(width="16")
    btnDetectarAdmin.configure(relief="solid")
    btnDetectarAdmin.config(bd=0.5)
    
    
    btnRastreoActivoAdmin = Button(framecamAdmin,text="Rastreo Activo",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[BottonRastreoActivo()]) ## Boton crear cuenta
    btnRastreoActivoAdmin.place(x=300,y=250)
    btnRastreoActivoAdmin.config(width="16")
    btnRastreoActivoAdmin.configure(relief="solid")
    btnRastreoActivoAdmin.config(bd=0.5)
    
    
    btnAdministrar = Button(framecamAdmin,text="Administrar Usuarios",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[FrameAdministrar()]) ## Boton crear cuenta
    btnAdministrar.place(x=160,y=320)
    btnAdministrar.config(width="18")
    btnAdministrar.configure(relief="solid")
    btnAdministrar.config(bd=0.5)
    
    
    
 #+++++++++++++++FRAME Detectar Rostro FINAL NO BORRAR+++++++++++++++++++++++++++++++#  
     #NO ELIMINAR
    s = os.getcwd()
    new_s = s.replace('\\','/')
    new_s = s.replace('Main','Graficas')
    new_s1 = s.replace('\\','/')
    #new_s1 = s.replace('Main','Guardar informacion de rostros',entryNombre1.get())
    on = PhotoImage(file = new_s+"/on.png")
    off = PhotoImage(file = new_s+"/off.png")
    detectar = PhotoImage(file = new_s+"/imagenDetectar.png")
    buscar = PhotoImage(file = new_s+"/imagenBuscar.png")
    on_button2 = Button(DetectFace, image = off, bd = 0,command = lambda:[switchUser()])
    on_button2.place(x=575,y=230)
    entryNombreDetectarFinal = ttk.Entry(DetectFace) ## Entrada de nombre
    entryNombreDetectarFinal.place(x=360, y=440, width="350",height="30")
    labelnombreDetectarFinal= Label(DetectFace,text="Nombre",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelnombreDetectarFinal.place(x=360, y=420)
   
    labelEstadoCamDetectar = tk.Label(DetectFace, text = "Encender Cámara",bg="white",fg = "black",font = ("Arial", 14,"bold"))
    labelEstadoCamDetectar.place(x=550,y=170)
    labelinstructivo= Label(DetectFace,text="Para Buscar y Guardar un rostro es necesario seleccionar",font=("Arial",14,'bold'))
    labelinstructivo.place(x=880, y=160)
    labelinstructivo2= Label(DetectFace,text=" un patrón, luego, aplicar el patrón y encender",font=("Arial",14,'bold'))
    labelinstructivo2.place(x=880, y=200)
    labelinstructivo3= Label(DetectFace,text="la cámara (Tocar el botón Off/On). Al momento de ",font=("Arial",14,'bold'))
    labelinstructivo3.place(x=880, y=240)
    labelinstructivo4= Label(DetectFace,text="hacer click en el botón se abrirá una ventana y",font=("Arial",14,'bold'))
    labelinstructivo4.place(x=880, y=280)
    labelinstructivo6= Label(DetectFace,text="sacar la fotografía con la tecla escape.",font=("Arial",14,'bold'))
    labelinstructivo6.place(x=880, y=320)
    labelinstructivo5= Label(DetectFace,text="Para guardar el rostro es necesario rellenar la",font=("Arial",14,'bold'))
    labelinstructivo5.place(x=880, y=400)
    labelinstructivo7= Label(DetectFace,text="información del recuadro rojo y luego pulsar Guardar rostro.",font=("Arial",14,'bold'))
    labelinstructivo7.place(x=880, y=440)
    labelinstructivo8= Label(DetectFace,text="Para repetir el proceso hay que accionar nuevamente el",font=("Arial",14,'bold'))
    labelinstructivo8.place(x=880, y=520)
    labelinstructivo9= Label(DetectFace,text="Botón Off/On, apagarlo y volverlo a encender respectivamente.",font=("Arial",14,'bold'))
    labelinstructivo9.place(x=880, y=560)
    labelinstructivo0= Label(DetectFace,text="Para cambiar patrón basta con seleccionar uno nuevo y aplicarlo.",font=("Arial",14,'bold'))
    labelinstructivo0.place(x=880, y=660)
    
    comboBoxDetectarRostroFinal = ttk.Combobox(DetectFace, font=("Arial", 14,"bold"))
    comboBoxDetectarRostroFinal['values']= ('Seleccionar Patron','Reconocimiento A','Reconocimiento B','Reconocimiento C')
    comboBoxDetectarRostroFinal.place(x=120,y=170)
    comboBoxDetectarRostroFinal.config(width= "16")
    comboBoxDetectarRostroFinal.current(0)
    
    botonAplicarDetectarFinal = Button(DetectFace,text="Aplicar patrón",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[obtenerCombo()]) ## Boton crear cuenta
    botonAplicarDetectarFinal.place(x=120,y=230)
    botonAplicarDetectarFinal.config(width="16")
    botonAplicarDetectarFinal.configure(relief="solid")
    botonAplicarDetectarFinal.config(bd=0.5)
    
    botonGuardarRostroFinal = Button(DetectFace,text="Guardar Rostro",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[guardarRostro()]) ## Boton crear cuenta
    botonGuardarRostroFinal.place(x=320,y=600)
    botonGuardarRostroFinal.config(width="20",height="2")
    botonGuardarRostroFinal.configure(relief="solid")
    botonGuardarRostroFinal.config(bd=0.5)

    botonRegresarDetectarFinal = Button(DetectFace,text="Regresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[RegresoPantallaPrincipal()]) ## Boton crear cuenta
    botonRegresarDetectarFinal.place(x=345,y=700)
    botonRegresarDetectarFinal.config(width="16",height="2")
    botonRegresarDetectarFinal.configure(relief="solid")
    botonRegresarDetectarFinal.config(bd=0.5)
    

   #NO ELIMINAR
    #Canvas para mostrar Nombre Descripcion Fecha
    CanvasBuscarRostroFinal = tkinter.Canvas(DetectFace)   
    CanvasBuscarRostroFinal.config(width=750,height=200)
    CanvasBuscarRostroFinal.configure(relief="solid")
    CanvasBuscarRostroFinal.place(x=100,y=350)
    CanvasBuscarRostroFinal.create_image(0,0, image=buscar, anchor="nw")
   ## CanvasBuscarRostroFinal.create_image(0,0, image=pruebademiniatura, anchor="nw")
   #NO ELIMINAR
    entryNombreDetectarFinal = ttk.Entry(DetectFace) ## Entrada de nombre
    entryNombreDetectarFinal.place(x=360, y=380, width="350",height="30")
    labelnombreDetectarFinal= Label(DetectFace,text="Nombre",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelnombreDetectarFinal.place(x=360, y=360)
    
    entryDescripcionDetectarFinal = ttk.Entry(DetectFace) ## Entrada de descripción
    entryDescripcionDetectarFinal.place(x=360,y=440, width="350",height="30")
    labelDescripcionDetectarFinal= Label(DetectFace,text="Descripción",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelDescripcionDetectarFinal.place(x=360,y=420)
    
    entryFechaDetectarFinal = ttk.Entry(DetectFace) ## Entrada de fecha
    entryFechaDetectarFinal.place(x=360,y=500, width="350",height="30")
    labelFechaDetectarFinal = Label(DetectFace,text="Fecha",font=("Arial",10,'bold'),background='#a8021e',foreground="white")
    labelFechaDetectarFinal.place(x=360,y=480)
   
 #++++++++++++++++++++++++++++++++++++++++++++++#     
   
        
    #--------------FUNCIONES--------------#
    
       
    ##NO ELIMINAR
    def guardarRostro():
        nombrerostro=entryNombreDetectarFinal.get()
        descripcionrostro=entryDescripcionDetectarFinal.get()
        fecharostro=entryFechaDetectarFinal.get()
        pruebatxt = os.getcwd()
        new_s = pruebatxt.replace('\\','/')
        new_s = pruebatxt.replace('Main','Guardar informacion de rostros')
        auxilioprueba = new_s.replace('Main','Guardar informacion de rostros/'+nombrerostro+'/Datos.txt') 
        auxilioprueba = pruebatxt.replace('Main','Guardar informacion de rostros/'+nombrerostro+'/Datos.txt') 
        print("Directorio Guardar Rostro 1", auxilioprueba)
        probando=("Nombre:"+nombrerostro+"\nDescipción:"+descripcionrostro+"\nFecha:"+fecharostro+"\n")
        f = open (auxilioprueba,'w')
        f.write(probando)
        f.close()
        
        
    
    ##NO ELIMINAR
    def switchUser():
        global is_on
        global triggerA,triggerC,triggerB
        
        # Determine is on or off
        if is_on:
            on_button2.config(image = off)
            is_on = False
        else:
           
            on_button2.config(image = on)
            is_on = True
            switch2User()
     
    ##NO ELIMINAR
    def switch2User():
        global triggerA,triggerC,triggerB
        nombrerostro=entryNombreDetectarFinal.get()
        if(triggerC==True):
            reconocimientoC(nombrerostro)
 
        if(triggerB==True):
            reconocimientoB(nombrerostro)

        if(triggerA==True):
            reconocimientoA(nombrerostro)
        
    ##NO ELIMINAR       
    def obtenerCombo():
        comparar=comboBoxDetectarRostroFinal.get()
        global nombrerostro
        nombrerostro=entryNombreDetectarFinal.get()
        global triggerA
        global triggerB
        global triggerC
        
        if(comparar =='Reconocimiento A'):
            triggerC=False
            triggerB=False
            triggerA=True
            return True  
        
        if(comparar == 'Reconocimiento B'):
            triggerA=False
            triggerC=False
            triggerB=True
            return True 
      
        if(comparar == 'Reconocimiento C'):
            triggerA=False
            triggerB=False
            triggerC=True
            return True
    
    #NO ELIMINAR
    def Login():
        usuario=EntradaUsuario.get()
        contraseña=EntradaContraseña.get()
        resultado=verificarUsuario(usuario,contraseña)
        global tipoUsuario
        tipoUsuario=resultado
        if(resultado == 'Admin'):
            print("Ingreso como Admin")
            show_frame(framecamAdmin)
        elif(resultado =='User'):
            print("Ingreso como User")
            show_frame(framecamUser)
        else:
            print("Error en usuario o contraseña")
            
    def RegresoDeRastreoActivo():
        if(tipoUsuario=='User'):
            show_frame(framecamUser)
        elif(tipoUsuario=='Admin'):
            show_frame(framecamAdmin)
    
    def RegresoPantallaPrincipal():
        if(tipoUsuario=='User'):
            show_frame(framecamUser)
        elif(tipoUsuario=='Admin'):
            show_frame(framecamAdmin)
    
    def RegresoAdmin():
        show_frame(framecamAdmin)
        
    def Regreso():
        show_frame(framelogin)
    #NO ELIMINAR      
    def GotoAñadir():
        show_frame(frameAdminAdd)
        
    #NO ELIMINAR    
    def GotoEdit(): 
        if(opcion.get()!=0): 
            show_frame(frameAdminEditar)       
        else: 
            messagebox.showwarning("Error selección", "No ha seleccionado nada para poder editar")        
    
    #NO ELIMINAR       
    def Olvide():
        show_frame(frameforg)
            
    def DetectarRostro():
        show_frame(DetectFace)
        
    #NO ELIMINAR
    def FrameAdministrarEditar():
        show_frame(frameAdmin)
        
    #NO ELIMINAR    
    def FrameAdministrarAdd():
        show_frame(frameAdmin) 
        
    #NO ELIMINAR
    def FrameAdministrar():
        show_frame(frameAdmin)
        
    #NO ELIMINAR
    def BottonRastreoActivo():
        show_frame(frameRastreoActivo)
 
    ##########################
    
       
    #l-l-l-l-l PROGRAMA MAIN l-l-l-l-l-l-#     
    show_frame(frameRastreoActivo)     ## Mostramos el frame default (login)
    frametop=tkinter.Canvas(ventana) ## Corresponde a la barra verde superior que dice "Saveface" 
    frametop.config(width=2000,height=75) 
    frametop.place(x=0,y=0) 
    frametop.config(bg="#23442B") 
    frametop.create_text(100, 40, fill="white",text="SaveFace",font=("Arial",24,'bold')) 
    ventana.mainloop()
    #l-l-l-l-l-l-l-l-l-l-l-l-l-l-#     



