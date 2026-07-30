#Scrip cuenta cuantas veces aparece la letra a en palabra ingresada por el usuario //Diego Alejandro Salcido Pérez
# 29/07/26


palabra = input("Ingrese una palabra: ").lower()

contador = 0

for letra in palabra:
    if letra == 'a':
        contador += 1

print("La letra 'a' aparece", contador, "veces")
