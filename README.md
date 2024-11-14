//Primer intento de mejorar Readme

# Bienvenido a nuestro Gremio de Aventureros!

Este proyecto se trata de un gremio de aventureros al estilo de Dungeons & Dragons, en el mismo aplicamos lo aprendido sobre Programación Orientada a Objetos (POO), siendo nuestro proyecto final(Programación 1) de la Universidad de Montevideo. Este proyecto permite gestionar un gremio de aventureros, consultar información sobre el mismo.

## Simulador de Gremio de Aventureros

Este proyecto es un simulador de gremio de aventureros al estilo de Dungeons & Dragons. Utilizando Programación Orientada a Objetos (POO) en Python, se ha desarrollado una aplicación interactiva en la terminal que permite gestionar un gremio de aventureros, consultar información sobre el mismo, así como registrar y completar misiones. Fue creado por Augusto Calastretti y Lucas Gómez.

## Uso de la Aplicación
                 
- [Manejo de la aplicación](#manejo-de-la-aplicación) 
- [Modelado (UML)](https://github.com/lucasgomez13/Entregable/README.md)
- [Características y Funcionalidades](#características-y-funcionalidades)

### Manejo de la Aplicación

El manejo de la aplicación permite realizar diversas acciones para gestionar los aventureros y misiones del gremio. Las principales funcionalidades incluyen la creación de aventureros, registro de misiones y asignación de estas a los aventureros.

### Características y Funcionalidades

- **Registrar Aventureros**: Crear aventureros de las clases Guerrero, Mago, o Ranger, cada uno con atributos específicos (fuerza para guerreros, mana para magos, y mascota opcional para rangers).
- **Registrar Misiones**: Definir misiones que pueden ser individuales o grupales, cada una con atributos como nombre, rango, recompensa, y estado de completado.
- **Asignar Misiones**: Los aventureros pueden realizar misiones, ganando experiencia y recompensas. Se valida el rango de la misión y el aventurero.
- **Consultas**:
  - Ver los top 10 aventureros con más misiones completadas o mayor habilidad.
  - Listar las misiones con las mayores recompensas.
  - Filtrar aventureros por tipo (Guerrero, Mago, o Ranger).

### Instalación

Clona este repositorio en tu máquina local:

-Utilizar bash.
-git clone https://github.com/lucasgomez13/Entregable/.git.
-cd Entregable.
-python3 main.py.
