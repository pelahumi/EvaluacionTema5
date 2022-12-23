from Ejercicios.Ejercicio1.calculos import calculos
from Ejercicios.Ejercicio2.contador import visitas
from Ejercicios.Ejercicio3.pruebas import *
from Ejercicios.Ejercicio4.reloj import *


def lanzador():
    opcion = int(input("Introduce el ejercicio que quieres ejecutar: "))
    
    if opcion == 1:
        calculos()
    
    elif opcion == 2:
        visitas()
    
    elif opcion == 3:
        prueba()

    elif opcion == 4:
        reloj()

lanzador()