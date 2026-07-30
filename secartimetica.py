#Script Secuencia Aritmética //Diego Alejandro Salcido Pérez
# 29/07/26

inicio = int(input("Primer número: "))
diferencia = int(input("Diferencia: "))
limite = int(input("Límite máximo: "))

num = inicio

while True:
    print(num, end=" ")
    num += diferencia

    if num > limite:
        break

print("\nSecuencia aritmética desde", inicio, "hasta", limite)
