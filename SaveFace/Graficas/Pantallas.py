
from tkinter import ttk, Button
import tkinter

from LogicaBasica.Verificacion import verificarUsuario, verificarContraseña

#import cv2

ventana =tkinter.Tk()   #Creacion de ventana
ventana.title("SaveFace")
ventana.config(bg="white")
frametop=tkinter.Canvas() ## Frametop corresponde la barra verde superior que dice "Saveface"
frametop.config(width=2000,height=75)
frametop.place(x=0,y=0)
frametop.config(bg="#046b17")
frametop.create_text(100, 40, fill="white",text="SaveFace",font=("Arial",24,'bold'))

miframe=tkinter.Canvas(ventana,width="800",height="600") ## Corresponde al frame de logeo
miframe.pack(padx=400, pady=120)
miframe.config(width="800",height="600")
miframe.config(bg="white")
miframe.configure(relief="solid")
miframe.config(bd=0.5)
miframe.create_text(50, 50, text="Inicio",font=("Arial",14))

btn2 = Button(text="Ingresar",font=("Arial",14,'bold'),bg='#a8021e',fg='white',command=lambda:[Login()]) ##Boton ingresar
btn2.place(x=680,y=450)
btn2.config(width="12")
btn2.configure(relief="solid")
btn2.config(bd=0.5)

btn3 = Button(text="Crear Cuenta",font=("Arial",14,'bold') , bg='#858282',fg='white') ## Boton crear cuenta
btn3.place(x=680,y=650)
btn3.config(width="12")
btn3.configure(relief="solid")
btn3.config(bd=0.5)
miframe.create_text(155, 110, text="Correo Electrónico",font=("Arial",14)) ##Se crea un texto desde miframe
entry = ttk.Entry(miframe) ## Entrada de correo
entry.place(x=75, y=130,width="600",height="40")

entry2 = ttk.Entry(miframe) ## Entrada de contraseña
entry2.place(x=75, y=260,width="600",height="40")
miframe.create_text(125, 240, text="Contraseña",font=("Arial",14))



def Login():
    usuario=entry.get()
    contraseña=entry2.get()
    if(verificarUsuario(usuario)== True and verificarContraseña(contraseña) == True):
            print("Login Succesfull")
    else:
            print("Usuario o contraseña incorrecta")



ventana.mainloop()  #Bucle infinito de la ventana para que se ejecute todo el rato

