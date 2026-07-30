# Scipt que soicitda numeros enteros y comenta cuantos digitos tiene  // Diego Alejandro Salcido Pérez
# 29/07/26

num = int(input("Número entero: "))

if num == 0:
    digitos = 1
else:
    digitos = 0

    if num < 0:
        num = abs(num)

    while num > 0:
        num //= 10
        digitos += 1

print("El número tiene", digitos, "dígitos")
