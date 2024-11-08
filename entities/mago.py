from  clases.Aventurero import Aventureros

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
    
