from abc import ABC , abstractmethod

class Misión(ABC):
    def __init__(self,nombre,rango,recompensa,completado):
        self.__nombre=nombre
        self.__rango=rango
        self.__recompensa=recompensa
        self.__completado=completado
    