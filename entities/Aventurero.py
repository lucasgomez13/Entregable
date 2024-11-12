from abc import ABC,abstractmethod

class Aventureros(ABC):
    def __init__(self,nombre,id,puntos_habilidad,experiencia,dinero):
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__experiencia = experiencia
        self.__dinero = dinero

    
    @property
    def nombre(self):
        return self.__nombre
    
    nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    
    @property
    def id(self):
        return self.__id
    
    id.setter
    def id(self,id):
        self.__id=id

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad
    
    puntos_habilidad.setter
    def puntos_habilidad(self,puntos_habilidad):
        self.__puntos_habilidad=puntos_habilidad

    
    @property
    def experiencia(self):
        return self.__experiencia
    
    experiencia.setter
    def experiencia(self,experiencia):
        self.__experiencia=experiencia

    @property
    def dinero(self):
        return self.__dinero
    
    dinero.setter
    def dinero(self,dinero):
        self.__dinero=dinero
    
    @abstractmethod
    def calcular_rango(self):
        pass
    
    