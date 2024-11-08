from Aventurero import Aventureros

class Guerrero(Aventureros):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero,fuerza):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__fuerza=fuerza

    @property
    def fuerza(self):
        return self.__fuerza
    
    fuerza.setter
    def fuerza(self,fuerza):
        self.__fuerza=fuerza

