#Script Calcula el factorial de un número ingresado por el usuario //Diego Alejandro Salcido Pérez
# 29/07/26


num =  int(input("Número para factorial: "))
factorial = 1
if num < 0:
    print("Error: Factorial no definido para números negativos.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es: {factorial}")
