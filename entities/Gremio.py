from Misiones import Misión
from Aventurero import Aventureros
from Guerrero import Guerrero
from Mago import Mago
from Ranger import Ranger
from Mascota import Mascota
class Gremio:
    def __init__(self):
        self.__aventureros=[]
        self.__misiones=[]

    def registrar_mision(self):
        
        nombre_mision = input("Ingrese el nombre para la misión: ")
        if not nombre_mision:
            print("Por favor, ingrese un nombre válido. El nombre no puede estar vacío.")
            return
        
        try:
            rango = int(input("Ingrese el rango de la misión (1-5): "))
            if rango < 1 or rango > 5:
                print("El rango debe estar entre 1 y 5.")
                return
        except ValueError:
            print("El rango debe ser un número entero entre 1 y 5.")
            return

        try:
            recompensa = float(input("Ingrese la recompensa para la misión: "))
            if recompensa <= 0:
                print("La recompensa debe ser un valor positivo.")
                return
        except ValueError:
            print("La recompensa debe ser un número válido.")
            return
      
        tipo_mision = input("¿Es una misión individual o grupal? individual/grupal  ")
        if tipo_mision not in ["individual", "grupal"]:
            print("Por favor, ingrese  individual o grupal .")
            return
        
        
        if tipo_mision == "grupal":
            try:
                min_miembros = int(input("Ingrese la cantidad mínima de miembros requeridos para la misión grupal: "))
                if min_miembros < 1:
                    print("La cantidad mínima de miembros debe ser al menos 1.")
                    return
            except ValueError:
                print("La cantidad mínima de miembros debe ser un número entero.")
                return
        else:
            min_miembros = 0  




        
    def realizar_mision(self):
        mision_id = int(input("Ingrese el ID de la misión a realizar: "))
        mision = self.__misiones[mision_id]
        aventureros_participantes = []

        while True:
            aventurero_id = int(input("Ingrese el ID del aventurero para la misión: "))
            aventurero = next((a for a in self.__aventureros if a.id == aventurero_id), None)
            if aventurero:
                aventureros_participantes.append(aventurero)
            else:
                print("Aventurero no encontrado.")
                continue

            otro = input("¿Registrar otro aventurero? (S/N): ").lower()
            if otro != 's':
                break

        
        for aventurero in aventureros_participantes:
            if Aventureros.calcular_rango() < Misión.rango():
                print(f"Aventurero {Aventureros.nombre()} no tiene el rango suficiente para la misión.")
                return

        
        recompensa_total = Misión.recompensa()
        recompensa_por_aventurero = recompensa_total / len(aventureros_participantes)

        for aventurero in aventureros_participantes:
            Aventureros.dinero(Aventureros.dinero() + recompensa_por_aventurero)

        Misión.completado(True)
        print(f"Misión completada con éxito! Recompensa de {recompensa_por_aventurero} por aventurero.")

        


        
