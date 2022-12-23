import pickle
from os import open

class Personaje():
    def __init__(self, vida, ataque, defensa, alcance, nombre):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
        self.nombre = nombre
    
class Gestor():
    def __init__(self):
        self.personajes = []
        self.cargar_personajes()

    def añadir(self, personaje):
        self.personajes.append(personaje)
        self.guardar()
    
    def borrar(self, nombre):
        for i in self.personajes:
            if i.nombre == nombre:
                self.remove(i)
                self.guardar()
                print("{} ha sido eliminado".format(nombre))

    def mostrar(self):
        if len(self.personajes) == 0:
            print("Fichero vacio")
        else:
            for i in self.personajes:
                print(i.nombre)
        
    def guardar(self):
        fichero = open("gestor.pckl", "wb")
        pickle.dump(self.personajes, fichero)
        fichero.close()
    
    def cargar_personajes(self):
        fichero = open("personajes.pckl", "ab+")
        fichero.seek(0)
        
        self.personajes = pickle.load(fichero)
        fichero.close()
        print("Personaje cargado")
    

