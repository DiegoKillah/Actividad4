#Script Multiplos de 3 y 5 //Diego Alejandro Salcido Pérez
# 29/07/26
#Script pide algun numero entre 1 al 100 para despues imprimir los numeros que son divisibles entre estos

print("Numeros divisibles por 3 y 5 del 1 al 100")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i,  end=" ")
print()
