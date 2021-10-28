# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:47:40 2021

@author: Matias
"""
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle 
from mtcnn.mtcnn import MTCNN
#import numpy as np
import os
#import imutils
import cv2

def reconocimientoA():
    #captura de rostro
    cap = cv2.VideoCapture(0) #seleccion de camara
    while(True):
        ret,frame=cap.read() # leemos el video
        cv2.imshow('Rostro',frame) #mostramos el video en pantalla
        if cv2.waitKey(1) == 27: # cuando se presiona " escape" se para el video
            break
    cv2.imwrite('Rostro.jpg',frame) #guardamos la ultima captura de video como imagen
    cap.release() # cerramos se tiene que cambiar por el boton 
    cv2.destroyAllWindows() #cerrar la ventana de la camara pero hay que cambiarlo al boton que apaga la camara
    
    def dibujo(img, lista_resultados):
        print(caras)
        # leemos la imagen con la libreria matplotlib
        imagen= pyplot.imread(img)
        #Ploteamos la imagen
        pyplot.imshow(imagen)
        #obtenemos los ejes polares para dibujar
        ax= pyplot.gca()
        #ploteamos los rectangulos con las coordenadas que nos entrega 'box'
        for result in lista_resultados:
            #obtenemos las coordenadas
            x, y, ancho, alto= result['box']
            #creamos el rectangulo
            rect=Rectangle((x,y), ancho, alto, fill= False, color= 'green')
            #Dibujamos la caja
            ax.add_patch(rect)
            #ahora vamos a dibujar los ojos, nariz y boca puntos clave del rostro
            for puntos, value in result['keypoints'].items():
                #creamos los circulos
                dot=Circle(value, radius= 4, color='green')
                ax.add_patch(dot)
#######################para exportar#################################################################
        #ahora vamos a exportar los pixeles que pertenecen a los rostros con el fin de usarlos en otro sistema
        for i in range(len(lista_resultados)):
            #obtenemos las coordenadas
            x1, y1, ancho1, alto1 = lista_resultados[i]['box']
            x2, y2 = x1 + ancho1, y1 + alto1
            #definimos el subplot
            pyplot.subplot(1, len(lista_resultados),i+1)
            pyplot.axis('off')
            #ploteamos las caras
            pyplot.imshow(imagen[y1:y2, x1:x2])
#####################################################################################################
        #ploteamos la imagen con el dibujo del rectangulo
        pyplot.show()
   #leemos la imagen con la libraria matplotlib
    img = 'Rostro.jpg'
    pixeles= pyplot.imread(img)
    
    #creamos el detector usando los valores predeterminados
    detector = MTCNN()
    
    #detectamos las caras en la imagen
    caras= detector.detect_faces(pixeles)
    
    #llama la funcion que ya se creo para dibujar los rectangulos
    dibujo(img, caras)

    
#reconocimientoA()

def reconocimientoB(nombrePersona):
    direccion= 'C:/Users/Matias/Documents/Repositorios/Proyecto Metodologia SaveFace/G2_Metodologia_2_2021/SaveFace/Guardar informacion de rostros'
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


def reconocimientoC(NombreUsuario):
     #captura de rostro
     cap = cv2.VideoCapture(0)
     while(True):
         ret,frame = cap.read()
         cv2.imshow('Deteccion Facial',frame)
         if cv2.waitKey(1) == 27:
             break
         usuario_img = NombreUsuario
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
                 cara_reg = cv2.resize(cara_reg, (150,150), interpolation = cv2.INTER_CUBIC)
                 cv2.imwrite(usuario_img+".jpg",cara_reg)
                 pyplot.imshow(data[y1:y2, x1:x2])
             pyplot.show()
         img= usuario_img+".jpg"
         pixeles= pyplot.imread(img)
         detector= MTCNN()
         caras= detector.detect_faces(pixeles)
         Identificar_cara(img,caras)
#reconocimientoC("matias")
         
#face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#cap = cv2.VideoCapture(0)
#while True:
#        _, img=cap.read()
#        gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#        faces= face_cascade.detectMultiScale(gray, 1.1, 4)
#        for(x, y, w, h)in faces:
#            cv2.rectangle(img, (x, y),(x+w, y+h), (255, 0, 0), 2)
#        cv2.imshow('img', img)
#        k= cv2.waitKey(30)
#        if k == 27:
#            break
#cap.release()
#cv2.destroyAllWindows()# para cerrar todas las ventanas de camara
