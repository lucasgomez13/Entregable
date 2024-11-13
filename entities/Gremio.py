from Mision import Mision
from Aventurero import Aventureros
from Guerrero import Guerrero
from Mago import Mago
from Ranger import Ranger
from Mascota import Mascota

class Gremio:
    def __init__(self):
        self.__aventureros = []
        self.__misiones = []

    def registrar_aventurero(self):
        try:
            nombre = input("Ingrese el nombre del aventurero: ")
            id = int(input("Ingrese el ID del aventurero: "))
            if any(aventurero.id == id for aventurero in self.__aventureros):
                print("ID usado, favor, ingresar un nuevo ID")
                return

            habilidad = int(input("Ingrese los puntos de habilidad (1-100): "))
            if habilidad < 1 or habilidad > 100:
                print("Puntos de habilidad deben ser entre 1 y 100.")
                return

            experiencia = int(input("Ingrese los puntos de experiencia: "))
            dinero = float(input("Ingrese la cantidad de dinero: "))

            print("Elija la clase del aventurero:")
            print("1. Guerrero")
            print("2. Mago")
            print("3. Ranger")
            clase_opcion = int(input("Ingrese el número de la clase (1-3): "))

            if clase_opcion == 1:
                fuerza = int(input("Ingrese la fuerza (1-100): "))
                if fuerza < 1 or fuerza > 100:
                    print("Fuerza debe estar entre 1 y 100.")
                    return
                nuevo_aventurero = Guerrero(nombre, id, habilidad, experiencia, dinero, fuerza)
            elif clase_opcion == 2:
                mana = int(input("Ingrese el mana (1-1000): "))
                if mana < 1 or mana > 1000:
                    print("Mana debe estar entre 1 y 1000.")
                    return
                nuevo_aventurero = Mago(nombre, id, habilidad, experiencia, dinero, mana)
            elif clase_opcion == 3:
                mascota_nombre = input("Ingrese el nombre de la mascota: ")
                mascota_habilidad = int(input("Ingrese los puntos de habilidad de la mascota (1-50): "))
                if mascota_habilidad < 1 or mascota_habilidad > 50:
                    print("Los puntos de habilidad de la mascota deben ser entre 1 y 50.")
                    return
                mascota = Mascota(mascota_nombre, mascota_habilidad)
                nuevo_aventurero = Ranger(nombre, id, habilidad, experiencia, dinero, mascota)
            else:
                print("Clase no válida.")
                return

            self.__aventureros.append(nuevo_aventurero)
            print(f"Aventurero {nombre} registrado con éxito!")
        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")

    def registrar_mision(self):
        try:
            nombre_mision = input("Ingrese el nombre para la misión: ")
            if not nombre_mision:
                print("Por favor, ingrese un nombre válido. El nombre no puede estar vacío.")
                return

            rango = int(input("Ingrese el rango de la misión (1-5): "))
            if rango < 1 or rango > 5:
                print("El rango debe estar entre 1 y 5.")
                return
            
            recompensa = float(input("Ingrese la recompensa para la misión: "))
            if recompensa <= 0:
                print("La recompensa debe ser un valor positivo.")
                return

            es_grupal = input("¿Es misión grupal? (S/N): ").strip().lower()
            if es_grupal == 's':
                min_miembros = int(input("Ingrese la cantidad mínima de miembros requeridos para la misión grupal: "))
                if min_miembros < 1:
                    print("La cantidad mínima de miembros debe ser al menos 1.")
                    return
            elif es_grupal == 'n':
                min_miembros = 0
            else:
                print("Entrada no válida. Por favor, ingrese 'S' o 'N'.")
                return

            nueva_mision = Mision(nombre_mision, rango, recompensa, 'grupal' if es_grupal == 's' else 'individual', min_miembros)
            self.__misiones.append(nueva_mision)
            print(f"Misión {nombre_mision} registrada con éxito!")
        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")

    def realizar_mision(self):
        try:
            nombre_mision = input("Ingrese el nombre de la misión a realizar: ")
            mision = next((m for m in self.__misiones if m.nombre == nombre_mision), None)
            if not mision:
                print("Misión no encontrada.")
                return

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
                if aventurero.calcular_rango() < mision.rango:
                    print(f"Aventurero {aventurero.nombre} no tiene el rango suficiente para la misión.")
                    return

            recompensa_total = mision.recompensa
            recompensa_por_aventurero = recompensa_total / len(aventureros_participantes)

            for aventurero in aventureros_participantes:
                aventurero.dinero += recompensa_por_aventurero
                aventurero.experiencia += mision.rango

            mision.completado = True
            print(f"Misión completada con éxito! Recompensa de {recompensa_por_aventurero} por aventurero.")
        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")

    def ver_top_10_aventureros(self):
        misiones_por_aventurero = {aventurero: 0 for aventurero in self.__aventureros}

        for mision in self.__misiones:
            if mision.completado:
                for aventurero in mision.aventureros_participantes:
                    misiones_por_aventurero[aventurero] += 1

        top_aventureros = sorted(misiones_por_aventurero.items(), key=lambda x: (-x[1], x[0].nombre))

        print("Top 10 Aventureros con Más Misiones Resueltas:")
        for i, (aventurero, misiones) in enumerate(top_aventureros[:10], start=1):
            print(f"{i}. {aventurero.nombre} - {misiones} misiones resueltas")

    def ver_top_10_aventureros_por_habilidad(self):
        def calcular_habilidad_total(aventurero):
            if isinstance(aventurero, Guerrero):
                return aventurero.habilidad + aventurero.fuerza / 2
            elif isinstance(aventurero, Mago):
                return aventurero.habilidad + aventurero.mana / 10
            elif isinstance(aventurero, Ranger):
                return aventurero.habilidad + (aventurero.mascota.habilidad if aventurero.mascota else 0)
            return aventurero.habilidad

        aventureros_habilidad = [(aventurero, calcular_habilidad_total(aventurero)) for aventurero in self.__aventureros]
        top_aventureros = sorted(aventureros_habilidad, key=lambda x: (-x[1], -x[0].experiencia))

        print("Top 10 Aventureros por Mayor Habilidad:")
        for i, (aventurero, habilidad_total) in enumerate(top_aventureros[:10], start=1):
            print(f"{i}. {aventurero.nombre} - Habilidad Total: {habilidad_total}")

    def ver_top_5_misiones_por_recompensa(self):
        top_misiones = sorted(self.__misiones, key=lambda m: (-m.recompensa, m.nombre))

        print("Top 5 Misiones con Mayor Recompensa:")
        for i, mision in enumerate(top_misiones[:5], start=1):
            print(f"{i}. {mision.nombre} - Recompensa: {mision.recompensa}")

    def menu_principal(self):
        while True:
            print("\nMenú Principal:")
            print("1. Registrar Aventurero")
            print("2. Registrar Misión")
            print("3. Realizar Misión")
            print("4. Otras Consultas (Submenú)")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.registrar_aventurero()
            elif opcion == '2':
                self.registrar_mision()
            elif opcion == '3':
                self.realizar_mision()
            elif opcion == '4':
                self.menu_otros()
            elif opcion == '5':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def menu_otros(self):
        while True:
            print("\nSubmenú de Otras Consultas:")
            print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
            print("2. Ver Top 10 Aventureros con Mayor Habilidad")
            print("3. Ver Top 5 Misiones con Mayor Recompensa")
            print("4. Ver Aventureros por Tipo")
            print("5. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.ver_top_10_aventureros()
            elif opcion == '2':
                self.ver_top_10_aventureros_por_habilidad()
            elif opcion == '3':
                self.ver_top_5_misiones_por_recompensa()
            elif opcion == '4':
                self.ver_aventureros_por_tipo()
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def ver_aventureros_por_tipo(self):
        print("\nAventureros por Tipo:")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Ranger")
        print("4. Volver al Submenú de Otras Consultas")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            guerreros = sorted([a for a in self.__aventureros if isinstance(a, Guerrero)], key=lambda x: x.nombre)
            print("Guerreros:")
            for guerrero in guerreros:
                print(f"{guerrero.nombre}")
        elif opcion == '2':
            magos = sorted([a for a in self.__aventureros if isinstance(a, Mago)], key=lambda x: x.nombre)
            print("Magos:")
            for mago in magos:
                print(f"{mago.nombre}")
        elif opcion == '3':
            rangers = sorted([a for a in self.__aventureros if isinstance(a, Ranger)], key=lambda x: x.nombre)
            print("Rangers:")
            for ranger in rangers:
                print(f"{ranger.nombre}")
        elif opcion == '4':
            return
        else:
            print("Opción no válida. Por favor, intente de nuevo.")