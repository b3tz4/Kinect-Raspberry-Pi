import numpy as np
import cv2

fondo= np.ones((200,600,3),np.uint8)
font = cv2.FONT_ITALIC
i = 2236
a = str(i)
if __name__ == "__main__":
    while 1:
        #Orden: Archivo imagen, texto, coordenadas, font, multiplicacion tamaño, color rgb, grosor, tipo linea
              cv2.putText(fondo,a,(10,60), font, 1,(255,0,255),1,cv2.LINE_AA)
              cv2.imshow('Distancia',fondo)
              if cv2.waitKey(5) & 0xFF == 27:
                    break
    cv2.destroyAllWindows()
    
