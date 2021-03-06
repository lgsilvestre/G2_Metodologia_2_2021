# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:46:54 2021

@author: Matias
"""

class User:
    def __init__(self, correo = None,contraseña= None, tipousuario = None,next = None):
        self.correo = correo
        self.contraseña=contraseña
        self.tipousuario=tipousuario
        self.next = next
        
        
        
class ListaUser: 
    def __init__(self):
        self.head = None        
    # Método para verificar si la estructura de datos esta vacia
    def estavacio(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def agregar(self, correo,contraseña,tipousuario):
        if not self.head:
            self.head = User(correo=correo,contraseña=contraseña,tipousuario=tipousuario)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = User(correo=correo,contraseña=contraseña,tipousuario=tipousuario)
        # Método para imprimir la lista de nodos
    def imprimirlista( self ):
        User = self.head
        while User != None:
            print(User.correo+" "+User.contraseña+" "+User.tipousuario+"\n")
            User = User.next
    def copiaratxt( self ):
        stringtxt=""
        User = self.head
        while User != None:
            stringtxt=stringtxt+(User.correo+" "+User.contraseña+" "+User.tipousuario+"\n")
            User = User.next
        return stringtxt 
     # Método para eleminar nodos
    def eliminar(self, correo):
        curr = self.head
        prev = None
        while curr and curr.correo != correo:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
            
