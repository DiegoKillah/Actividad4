# Script genra un numero aleatorio entre 1 y 100 y el usuario tiene que adivinarlo //Diego Alejandro Salcido Pérez
# 29/07/26



"""
en lo personal agregaria esta version para que tenga un intermedio ya que con el programa planteado no es que haya un intermedio si el numero es 10 pero colocamos 8 
aun asi colocara que estamos muy lejos, con esta nueva version es un poco mas intuitivo para el usuario si esta mas o menos cerca del numero secreto.
import random

secreto = random(1, 100)

while True:
    intento = int(input("Adivina (1-100): "))

    if intento < secreto:
        if secreto - intento <= 5:
            print("Muy cerca, pero un poco más alto.")
        else:
            print("Demasiado bajo.")

    elif intento > secreto:
        if intento - secreto <= 5:
            print("Muy cerca, pero un poco más bajo.")
        else:
            print("Demasiado alto.")

    else:
        print("¡Correcto! Era", secreto)
        break

print("Juego terminado. El número era", secreto)
"""

import random

secreto = random.randint(1, 100)

while True:
    intento = int(input("Adivina (1-100): "))

    if intento < secreto:
        print("Demasiado bajo")

    elif intento > secreto:
        print("Demasiado alto")

    else:
        print("¡Correcto! Era", secreto)
        break

print("Juego terminado. El número era", secreto)
