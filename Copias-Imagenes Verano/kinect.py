#Importar librerias
import cv2
import freenect
import matplotlib
import numpy as np
import frame_convert2 as fc
from math import tan


#Sacar la imagen normal del video

def get_video():
    array,_ = freenect.sync_get_video(0, freenect.VIDEO_IR_8BIT)
    #Poner freenect.VIDEO_RGB para imagen normal y descomentar la linea de abajo
    #array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array
 
#Sacar la imagen de profundidad
# Global porque necesitamos que el valor se conserve
def get_depth():
    array,_ = freenect.sync_get_depth(0,freenect.DEPTH_11BIT)
    global distancia
    global distancia2
    global dpromedio
    global promedio
    global bina
    
    #global arraydistancias
    #global arraydistancias2
    bina = array[240][320]
    we = np.mean(array)
    promedio = int(we)
    distancia = .1236*tan(array[240][320]/2845.5+1.1863)
    distancia2 = 100/(-0.00307 * array[240][320] + 3.33)
    dpromedio = 100/(-0.00307 * int(we) + 3.33)
    #arraydistancias=[]
    #arraydistancias=[]
    #Calculo distancia promedio
    """for x in range (240,250):
        for y in range (320,330):
            j = .1236*tan(array[x][y]/2845.5+1.1863)
            arraydistancias[x][y] = j"""
    array = array.astype(np.uint8)
    return array

#Filtro de imagen difuminada
kernel = np.ones((5,5),np.float32)/25

distancias1= []
distancias2= []
if __name__ == "__main__":
    while 1:
       
        #Obtener imagen
        frame = get_video()

        #Cambia imagen a imagen difuminada
        #dst = cv2.filter2D(frame,-1,kernel)

        #Cambia a imagen con filtro laplaciano
        #laplacian = cv2.Laplacian(frame, cv2.CV_64F)

        #Conseguir imagen de profundidad
        depth = get_depth()
        #Información de los pixeles y la imagen

        """a = depth.shape
        e = depth.size
        i = depth.itemsize
        o = depth.dtype
        print('Dimensiones array: ',a)
        print('NumPixeles array: ',e)
        print('Tamaño en bytes por pixel:', i)
        print('Tipos: ',o)"""
        
        #Valores numèricos de 11 bits
        if (distancia>0 and distancia2>0):
            print('Distancia del pixel (240,320) en metros: ',distancia)
            distancias1.append(distancia)
            print('Distancia del pixel (240,320) en metros: ',distancia2/100)
            distancias2.append(distancia2/100)
            print('Valor del pixel de en medio bin: ', bina)
            print('Distancia promedio de imagen en metros: ', dpromedio)
            print('Distancia promedio de imagen en metros: ', promedio)
        #binar = bin(distancia)[2:]
        #print('Valor binario (240,320): ', binar)
        
        #Muestra las imagenes correspondientes
        #cv2.imshow('Imagen',frame)
        #cv2.imshow('Filtrada', laplacian)
        #cv2.imshow('Filtrada', dst)
        #depth = depth.astype(np.uint8)
        cv2.imshow('Depth image',depth)
        #depth2 = fc.pretty_depth(depth)
        #cv2.imshow('DepthMod', depth2)
        
 
        #Sal del ciclo apretando la tecla 'Esc' y guarda las imagenes en la carpeta
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            """for x in range (0,100):
                print ('\n')
                for y in range (0,101):
                    a = depth[x][y]
                    if a!=255:
                        print(x,',',y,':', depth[x][y])"""
            cv2.imwrite('foto.png',frame)
            cv2.imwrite('laplaciana.png', depth)
            break
    cv2.destroyAllWindows()

print('Distancias')
"""print (distancias1)
print (distancias2)"""
