import time

class Personaje():
    def __init__(self, nombre: str, nivel: int = 1, experiencia: int = 0):
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia

    @property
    def estado(self):
        return (
            print(f'''
        ______________________________________________________________________   
        NOMBRE: {self.nombre}    NIVEL: {self.nivel}    EXPERIENCIA: {self.experiencia}'''))
    @estado.setter
    def estado(self, experiencia_adicional):
        experiencia_total = self.experiencia + (self.nivel - 1)* 100 + experiencia_adicional
        if experiencia_total < 0:
            experiencia_total = 0

        nivel = 1 + experiencia_total // 100
        if nivel < 1:
            self.nivel = 1
        else:
            self.nivel = nivel
        self.experiencia = experiencia_total % 100


    def __gt__(self, personaje):
        return self.nivel > personaje.nivel

    def __lt__(self, personaje):
        return self.nivel < personaje.nivel

    def __eq__(self, personaje):
        return self.nivel == personaje.nivel

    def probabilidad_de_ganar(self, orco):
        if self.nivel < orco.nivel:
            return 0.33  # 33% de probabilidad de ganar si el nivel del jugador es menor que el del orco
        elif self.nivel > orco.nivel:
            return 0.66  # 66% de probabilidad de ganar si el nivel del jugador es mayor que el del orco
        else:
            return 0.50  # 50% de probabilidad de ganar si el nivel del jugador es igual al del orco

    def enfrentamiento(self, orco):
        print(f'''
        ¡Oh no!, ¡Ha aparecido un Orco!
        Con tu nivel actual, tienes {self.probabilidad_de_ganar(orco)} de probabilidades de ganarle al Orco.
        Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
        Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.''')

        while True:
            opcion = input('''
            ¿Qué deseas hacer?
            1. Atacar
            2. Huir
            >''')
            if int(opcion) in [1, 2]:
                break
            else:
                print('''
            ¡Opcion Invalida!''')
            time.sleep(1)
        return opcion




