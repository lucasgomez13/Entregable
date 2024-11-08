from abc import ABC , abstractmethod

class Misión(ABC):
    def __init__(self,nombre,rango,recompensa,completado=False):
        self.__nombre=nombre
        self.__rango=rango
        self.__recompensa=recompensa
        self.__completado=completado
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def rango(self):
        return self.__rango

    @rango.setter
    def rango(self, rango):
        self.__rango = rango
    
    
    @property
    def recompensa(self):
        return self.__recompensa

    @recompensa.setter
    def recompensa(self, recompensa):
        self.__recompensa = recompensa
    

    @property
    def completado(self):
        return self.__completado

    @completado.setter
    def completado(self, completado):
        self.__completado = completado
    
    
    