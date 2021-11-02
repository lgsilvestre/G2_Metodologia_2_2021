# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:47:40 2021

@author: Matias
"""
import mediapipe as mp
from tkinter import *
from PIL import Image, ImageTk #pip install Pillow
import cv2 #pip install opencv-contrib-python
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk, Button
import tkinter
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle 
from mtcnn.mtcnn import MTCNN
#import numpy as np
import os
#import imutils
from os import remove
from os import path


def reconocimientoA(nombrePersona): 
    s = os.getcwd() ##Con esto obtenemos el directorio de la maquina 
    new_s = s.replace('\\','/')
    new_s = s.replace('Main','Guardar informacion de rostros')

    ##direccion= 'C:/Users/maxim/Documents/SaveFace/G2_Metodologia_2_2021/SaveFace/Guardar informacion de rostros'
    direccion = new_s
    nombreCara= nombrePersona
    direccionFinal = direccion + '/' + nombreCara
    if not os.path.exists(direccionFinal):
        print('Carpeta creada: ', direccionFinal)
        os.makedirs(direccionFinal) 
    face_detection= mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) 
    cap= cv2.VideoCapture(0)
    while True: 
     ret, im= cap.read()
     if not ret: 
          break 
     im2=cv2.cvtColor(im, cv2.COLOR_BGR2RGB) 
     results= face_detection.process(im2)       
     if results.detections: 
            for detection in results.detections: 
                mp.solutions.drawing_utils.draw_detection(im, detection) 
                cv2.imwrite(direccionFinal + '/rostro_{}.jpg'.format(nombreCara),im) 
     cv2.imshow('imagen',im) 
     if cv2.waitKey(1) == 27: 
            break 
    cap.release() 
    cv2.destroyAllWindows()

    
##reconocimientoA("Maxito")

def reconocimientoB(nombrePersona): ## podriamos pedirselo al usuario examinandolo (?)
    
    s = os.getcwd()

    new_s = s.replace('\\','/')
    new_s = s.replace('Main','Guardar informacion de rostros')

    ##direccion= 'C:/Users/maxim/Documents/SaveFace/G2_Metodologia_2_2021/SaveFace/Guardar informacion de rostros'
    direccion = new_s
    nombreCara= nombrePersona
    direccionFinal = direccion + '/' + nombreCara
    if not os.path.exists(direccionFinal):
        print('Carpeta creada: ', direccionFinal)
        os.makedirs(direccionFinal)
    faceClassif= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    while True:
        _,img=cap.read()
        gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        auxFrame= img.copy()
        faces= faceClassif.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), maxSize=(200,200))
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)
            cara= auxFrame[y:y+h,x:x+w]
            cara= cv2.resize(cara,(150,150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(direccionFinal + '/rostro_{}.jpg'.format(nombreCara),cara)
        cv2.imshow('img',img)
        k= cv2.waitKey(30)
        if k == 27: 
            break
    
    cap.release()   
    cv2.destroyAllWindows()

#reconocimientoB()# hay que pasar el nombre de la persona a la cual se le identifico el rostro


def reconocimientoC(nombrePersona):
    #captura de rostro
     s = os.getcwd()

     new_s = s.replace('\\','/')
     new_s = s.replace('Main','Guardar informacion de rostros')

     direccion = new_s
     nombreCara= nombrePersona
     direccionFinal = direccion + '/' + nombreCara
     if not os.path.exists(direccionFinal):
        print('Carpeta creada: ', direccionFinal)
        os.makedirs(direccionFinal)
     cap = cv2.VideoCapture(0)
     while(True):
         ret,frame = cap.read()
         cv2.imshow('Deteccion Facial',frame)
         if cv2.waitKey(1) == 27:
             break
     usuario_img = nombrePersona
     cv2.imwrite(usuario_img + ".jpg",frame)
     
     cap.release()
     cv2.destroyAllWindows()
         #nomreUsuario.delete(0, END) # se ocupa para limpiar la variable, posible utilizacion en pantalla.py
         
     def Identificar_cara(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range (len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]['box']
            x2, y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i+1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg, (150,200), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite(direccionFinal+'/rostro_{}.jpg'.format(nombreCara),cara_reg)
            
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()
     img= usuario_img+".jpg"
     pixeles= pyplot.imread(img)
     detector= MTCNN()
     
     caras= detector.detect_faces(pixeles)
     Identificar_cara(img,caras)
     s = os.getcwd()
     new_s = s.replace('\\','/')
     new_s = s.replace('\\','/')
     new_s= (new_s+'/{}.jpg'.format(nombreCara))
     

     if path.exists(new_s):
    
         remove(new_s)
         
#reconocimientoC("matias")
         
