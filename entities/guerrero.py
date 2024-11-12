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

    def calcular_rango(self):
        habilidad_total = self.puntos_habilidad + self.fuerza / 2
        if habilidad_total <= 20:
            return 1
        elif habilidad_total <= 40:
            return 2
        elif habilidad_total <= 60:
            return 3
        elif habilidad_total <= 80:
            return 4
        else:
            return 5

