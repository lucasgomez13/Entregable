from Aventurero import Aventureros

class Ranger(Aventureros):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero,mascota=None):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__mascota=mascota

    @property
    def mascota(self):
        return self.__mascota
    
    mascota.setter
    def mascota(self,mascota):
        self.__mascota=mascota
        

    