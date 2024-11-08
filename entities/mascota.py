class Mascota:
    def __init__(self, nombre, puntos_habilidad):
        self.__nombre = nombre  
        self.__puntos_habilidad = puntos_habilidad  

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad
    
    @puntos_habilidad.setter
    def puntos_habilidad(self,puntos_habilidad):
        self.__puntos_habilidad=puntos_habilidad
