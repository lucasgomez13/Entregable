from  Aventurero import Aventureros

class Mago(Aventureros):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero,mana):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__mana=mana

    
    @property
    def mana(self):
        return self.__mana
    
    mana.setter
    def mana(self,mana):
        self.__mana=mana
    
    def calcular_rango(self):
        habilidad_total = self.puntos_habilidad + self.mana / 10
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
