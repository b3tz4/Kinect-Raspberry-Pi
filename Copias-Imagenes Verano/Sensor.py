#Importar librerias
import cv2
import freenect
import numpy as np
import RPi.GPIO as tablero
import time

#Filtro de imagen difuminada y tipo de letra
difu = np.ones((5,5),np.float32)/25
font = cv2.FONT_ITALIC

#Trabajar con el número de pin y poner el pin 12 (especial para PWM) en modo de salida
tablero.setmode(tablero.BOARD)
tablero.setup(12,tablero.OUT)


#Definición de funciones
#Sacar la imagen normal del video
def get_video():
    array,_ = freenect.sync_get_video(0, freenect.VIDEO_RGB)
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array
 
#Mostrar la imagen de profundidad
def get_depth():
    array,_ = freenect.sync_get_depth(0,freenect.DEPTH_11BIT)
    array = array.astype(np.uint8)
    return array

#Obtener distancia promedio de toda la imagenm, de la región central y del pixel de en medio
def get_mean_distance_mks():
    array,_ = freenect.sync_get_depth(0,freenect.DEPTH_MM)
    suma = []
    #Distancia del pixel de en medio y promedio, ignorando lo que esté marque distancia 0
    bina = array[240][320]/1000
    for x in range (225,255):
        for y in range (305,335):
            suma.append(array[x][y])
    cuadro = np.nanmean(suma)/1000
    dpromedio = np.nanmean(array)/1000
    return dpromedio, cuadro, bina

#Se obtiene el contorno de una imàgen: Se copia la imagen, se le aplican los filtros adecuados, se obtienen sus contornos y èstos contornos se dibujan en la
#imagen original
def contor_thresh(imagen):
    wea = imagen.copy()
    ima = cv2.filter2D(wea,-1,difu)
    imgray = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,128,0)
    ima2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(wea,contours, -1, (255,255,0), 2)
    return wea

def contor_sobelx(imagen):
    weaa = imagen.copy()
    wea = cv2.filter2D(weaa,-1,difu)
    ima = cv2.Sobel(wea,cv2.CV_64F,1,0,ksize=5)
    ima = ima.astype(np.uint8)
    imgray = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    ima2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(weaa,contours, -1, (255,255,0), 1)
    return weaa

def contor_lapla(imagen):
    weaa = imagen.copy()
    wea = cv2.filter2D(weaa,-1,difu)
    ima = cv2.Laplacian(wea, cv2.CV_64F)
    ima = ima.astype(np.uint8)
    imgray = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#0 en el ultimo argumento
    ima2, contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(weaa,contours, -1, (255,255,0), 1)
    return weaa

#Este es el filtro que mejores resultados dió
def contor_canny(imagen):
    weaa = imagen.copy()
    wea = cv2.filter2D(weaa,-1,difu)
    ima = cv2.Canny(wea,100,200)
    ima = ima.astype(np.uint8)
    ret,thresh = cv2.threshold(ima,127,255,0)
    ima2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(weaa,contours, -1, (255,255,0), 2)
    return weaa

if __name__ == "__main__":
    while 1:
       
        #Obtener imagen RGB
        frame = get_video()

        """IMPORTANTE: Tratar de no usar las funciones de get_depth y get_mean_distance al mismo tiempo, los datos que tienen vienen de las mismas càmaras y
        alentan mucho el funcionamiento"""

        #Conseguir imagen de profundidad y mostrarla
        """depth = get_depth()
        cv2.imshow('Depth image',depth)"""

        #Conseguir distancia en metros y convertir estos datos en string
        distancia, cuad, bina = get_mean_distance_mks()
        BinD = 'Dist a pix central: '+ str(bina)+' Metros'
        StrD = str(cuad)+' Metros'

        #Dibuja cuadro donde se está tomando la distancia promedio
        fondo= np.ones((200,600,3),np.uint8) 
        cv2.putText(fondo,BinD,(10,60), font, 1,(219,169,1),1,cv2.LINE_AA)
        cv2.putText(fondo,'Distancia central promedio',(10,110), font, 1,(0,191,255),1,cv2.LINE_AA)
        cv2.putText(fondo,StrD,(10,160), font, 1,(0,191,255),1,cv2.LINE_AA)

        #Muestra cuadro con valores de distancia del pixel de en medio 
        #cv2.imshow('Distancia',fondo)

        #Cambia imagen a imagen difuminada y la muestra
        """dst = cv2.GaussianBlur(frame,(9,9),0)
        cv2.imshow('Difuminada', dst)"""


        #Cambia a imagen con filtro laplaciano y laplaciano difuminado y los muestra
        """laplacian = cv2.Laplacian(frame, cv2.CV_64F)
        dlapla = cv2.GaussianBlur(laplacian,(9,9),0)
        
        cv2.imshow('Filtro Laplaciano', laplacian)
        cv2.imshow('Laplaciano difuminado', dlapla)"""
        
        #Saca la imagen con su contorno para diferentes formatos y les dibuja cuadro donde se toma la distancia, muestra las imagenes con contornos
        #Tratar de solo usar uno a la vez

        contorno = contor_thresh(frame)
        cv2.rectangle(contorno,(295,215),(345,265),(0,0,255),2)
        cv2.imshow('Contorno sin filtro',contorno)
        
        sob = contor_sobelx(frame)
        cv2.rectangle(sob,(295,215),(345,265),(0,0,255),2)
        cv2.imshow('Contorno sobelx',sob)
        
        LA = contor_lapla(frame)
        cv2.rectangle(LA,(295,215),(345,265),(0,0,255),2)
        cv2.imshow('Contorno laplaciano',LA)
        
        can= contor_canny(frame)
        cv2.rectangle(can,(295,215),(345,265),(0,0,255),2)
        cv2.imshow('Contorno canny',can)


        #Dibuja rectàngulo en imagen 
        cv2.rectangle(frame,(295,215),(345,265),(0,0,255),2)
        
        #Muestra la imagen
        #cv2.imshow('Imagen',frame)

        #Señal al dron: Prendido cuando puede avanzar, apagado cuando no (Enable a distancia igual o mayor de .5 metros
        if (cuad) >= .5:
            tablero.output(12,tablero.HIGH)
        else:
            tablero.output(12,tablero.LOW)

        #Sal del ciclo apretando la tecla 'Esc' y guarda las imagenes en la carpeta
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            cv2.imwrite('Imagen.png',frame)
            #Limpia el tablero    
            tablero.output(12, tablero.LOW)
            tablero.cleanup()
            break

    #Acaba el programa
    cv2.destroyAllWindows()


