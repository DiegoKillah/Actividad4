#Scipt genera si es una vocal o una consonante el programa termina cunado el usuario ingresa un espacio //Diego Alejandro Salcido Pérez
# 29/07/26


while True:
    letra = input("Ingrese letra (espacio termina): ")

    if letra == " ":
        break

    letra = letra.lower()

    if letra in "aeiou":
        print("Vocal")
    else:
        print("No vocal")

print("Programa finalizado")
