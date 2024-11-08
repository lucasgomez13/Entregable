from clases.Aventurero import Aventureros

class Ranger(Aventureros):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero,mascota=None):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__mascota=mascota

    