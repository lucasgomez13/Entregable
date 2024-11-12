from Aventurero import Aventureros
from Mascota import Mascota

class Ranger(Aventureros):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero,mascota=None):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__mascota=mascota


    @property
    def mascota(self):
        return self.__mascota

    def mascota(self, mascota):
        self.__mascota = mascota

    def calcular_rango(self):
        habilidad_total = self.puntos_habilidad + (self.mascota._puntos_habilidad() if self.mascota else 0)
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

    