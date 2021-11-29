# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:45:55 2021

@author: Matias
"""

#funcion
import os

def verificarUsuario(usuario, contraseña):
    s = os.getcwd()
    new_s = s.replace('Main','LogicaBasica/usuarios.txt')    
    archivo= open(new_s)
    linea = archivo.readline()#
    while len(linea)>0:
        linea=linea.rstrip()
        Array=linea.split()
        if(usuario == Array[0]):
            if(contraseña == Array[1]):
                if('Admin'== Array[2]):
                    return 'Admin'
                elif('User' == Array[2]):
                    return 'User'
        linea=archivo.readline()
    return 'Error'   
        

def verificarCorreo(Correo):
    signos = ['.','_','-']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    dominios = ['gmail', 'hotmail', 'live']
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    mayusculas = []
    extenciones = ['com','cl']
    
    for x in minusculas:
        mayusculas.append(x.upper())
    
    if Correo.find('@') != -1:
        nuevo_email = Correo.split('@')
        usuario = nuevo_email[0]
        resto = nuevo_email[1]
        continuacion = resto.split('.')
        dominio = continuacion[0]
        terminacion = continuacion[1]
        for x in usuario:
            if x in signos or x in numeros or x in minusculas or x in mayusculas:
                if dominio in dominios:
                    if terminacion in extenciones:
                        return True
                    else:
                        return True
                else:
                    return True
            else:
                return False
    else:
        return False
    
    return False