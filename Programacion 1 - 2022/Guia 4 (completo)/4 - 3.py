# Generar lista
import random
# a. Generar una lista de 20 números enteros al azar de 3 dígitos.
for i in range(0,20):
    num = random.randint(100,999)
# b. Mostrar toda lista.
# c. Marcar con * (asterisco) los divisibles por 2.
    if num % 2 == 0:
        print("*", i ,"-", num)
# d. Marcar con # (numeral) los divisibles por 3.
    elif  num % 3 == 0:
        print("#", i ,"-", num)
# e. Marcar con $ (peso) los divisible por 4.
    elif num % 4 == 0:
        print("$", i ,"-", num)
# f. Marcar con & (per se and per sand – por sí mismo) los divisibles por 5.
    elif num % 5 == 0:
        print("&", i ,"-", num)
    else:
        print(" ", i ,"-", num)