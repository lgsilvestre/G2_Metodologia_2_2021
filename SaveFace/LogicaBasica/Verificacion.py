# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:45:55 2021

@author: Matias
"""

#funcion
import os

def verificarUsuario(usuario, contraseña):
    s = os.getcwd()
    new_s = s.replace('Graficas','LogicaBasica/usuarios.txt')    
    archivo= open(new_s)
    linea = archivo.readline()#
    while len(linea)>0:
        linea=linea.rstrip()
        Array=linea.split()
        if(usuario == Array[0]):
            if(contraseña == Array[1]):
                return True
        linea=archivo.readline()
    return False   
        

# cerrar el archivo

#para importar las funciones a otro fichero se utiliza " from funciones import verificarUsuario, verificarContraseña "

#print (archivo.read())

#linea = archivo.readlines()# leer una linea, y luego avanza
#print(linea) # mostrar por pantalla la linea

# un ciclo que termina cuando una linea está vacia ( que es 0)
#while len(linea)>0:
#    print(linea)# el print hace el salto de linea y se puede cambiar con (end =' ') despues de linea en el print
#    linea=archivo.readline()

#funciona mas directo con el for
#for linea in archivo:
#    print(linea, end=' ')
