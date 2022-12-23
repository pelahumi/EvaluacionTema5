from Ejercicios.Ejercicio3.gestor import *

def prueba():
    caballero = Personaje(4, 2, 4, 2, "caballero")
    guerrero = Personaje(2, 4, 2, 4, "guerrero")
    arquero = Personaje(2, 4, 1, 8, "arquero")

    gestor = Gestor()

    gestor.añadir(caballero)
    gestor.añadir(guerrero)
    gestor.añadir(arquero)

    gestor.mostrar()

    gestor.borrar(arquero)

    gestor.mostrar()

