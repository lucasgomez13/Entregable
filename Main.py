from entities.Gremio import Gremio
from entities.Aventurero import Aventurero
from entities.Guerrero import Guerrero
from entities.Mago import Mago
from entities.Mascota import Mascota
from entities.Ranger import Ranger 
from entities.Mision import Mision

if __name__ == "__main__":
    gremio = Gremio()
    print("Bienvenido al Simulador de Gremio de Aventureros!")
    gremio.menu_principal()
