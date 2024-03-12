import random
import time
import sys
import os
from personaje import *

os_sys = 'cls' if sys.platform == 'win32' else 'clear'
os.system(os_sys)

nombre = input('''
¡Bienvenido a Gran Fantasía Orco Slayer 3!
Por favor indique nombre de su personaje:
>''')

personaje_1 = Personaje(nombre)
personaje_1.estado
personaje_2 = Personaje('Orcoco')
time.sleep(2)
os.system(os_sys)
print('Loading ...')
time.sleep(2)
os.system(os_sys)

while True:
    opcion = personaje_1.enfrentamiento(personaje_2)
    aleatorio = random.random()
    if int(opcion) == 2:
         print ('Soldado que arranca sirve para otra batalla...')
         time.sleep(2)
         break
    else :

        if aleatorio > personaje_1.probabilidad_de_ganar(personaje_2):
            time.sleep(2)
            print('''
¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!
''')
            personaje_1.estado = 50
            personaje_2.estado = -30
            time.sleep(2)
            os.system(os_sys)
            personaje_1.estado
            personaje_2.estado
            time.sleep(2)
            os.system(os_sys)

        else:
            time.sleep(2)
            print('''
¡Oh no! ¡El orco te ha ganado!
¡Has perdido 30 puntos de experiencia!
            ''')
            personaje_1.estado = -30
            personaje_2.estado = 50
            time.sleep(2)
            os.system(os_sys)
            personaje_1.estado
            personaje_2.estado
            time.sleep(2)
            os.system(os_sys)

