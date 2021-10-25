# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:45:55 2021

@author: Matias
"""
archivo= open("Correos.txt")# el nombre del txt es archivo


#funcion
def verificarUsuario(usuario):
    linea = archivo.readlines()#
    while len(linea)>0:
        linea=archivo.readline()
        if(usuario==linea):
            return True
    return False   
        

def verificarContraseña(contraseña):
    linea = archivo.readlines()#
    while len(linea)>0:
        linea=archivo.readline()
        if(contraseña==linea):
            return True
    return False

archivo.close()# cerrar el archivo

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

