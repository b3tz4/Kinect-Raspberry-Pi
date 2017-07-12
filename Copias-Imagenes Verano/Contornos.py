import numpy as np
import cv2

im = cv2.imread('foto.png')
ima = im.copy()
imgray = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
ima2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(ima,contours, -1, (255,0,0), 1)

if __name__ == "__main__":
    while 1:

        cv2.imshow('No contornos', im)
        cv2.imshow('Contornos', ima)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            cv2.imwrite('Contornos.png',ima)
            break
    #Acaba el programa
    cv2.destroyAllWindows()
