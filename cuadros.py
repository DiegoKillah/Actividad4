#Escribe un programa que solicite al usuario ingresar un número entero positivo. Luego, el programa debe imprimir los cuadrados de todos los números desde 1 hasta ese número
#Diego Alejandro Salcido Pérez 
#29/07/26

n = int(input("Numero positivo: "))
i = 1

while True:
    print(i ** 2)
    i += 1

    if i > n:
        break

print("Secuencia de cuadros hasta", n)
