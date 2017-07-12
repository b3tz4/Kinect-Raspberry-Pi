#Librerías del GPIO de la raspberry pi3
import RPi.GPIO as tablero
import time

#Trabajar con el número de pin y poner el pin 12 (especial para PWM) en modo de salida
tablero.setmode(tablero.BOARD)
tablero.setup(12, tablero.OUT)

#Porcentaje de ciclo de trabajo y frecuencia en hertz a la cual trabajar, tiempo en segundos
ciclo = 0
tiempo =.02
count = 1

#Va elevando cada tiempo el ciclo de trabajo
while (ciclo<100):
   
    print ("Es el ciclo número: ", count," ciclo de trabajo: ", ciclo, "%")
    ciclo = ciclo+.5
    count = count+1
    tablero.output(12, tablero.HIGH)
    THigh = ciclo*tiempo/100
    time.sleep(THigh)
    tablero.output(12, tablero.LOW)
    time.sleep(tiempo-THigh)

#Al llegar al cien porciento se queda prendido el tiempo en segundos especificado
tablero.output(12, tablero.HIGH)
time.sleep(4)

#Regresa el valor a 0 de ciclo de trabajo
while (ciclo> 0):
    print ("Es el ciclo número: ", count," ciclo de trabajo: ", ciclo, "%")
    ciclo = ciclo-.5
    count = count+1
    tablero.output(12, tablero.HIGH)
    THigh = ciclo*tiempo/100
    time.sleep(THigh)
    tablero.output(12, tablero.LOW)
    time.sleep(tiempo-THigh)
    
#Apaga led
tablero.output(12, tablero.LOW)
tablero.cleanup()

