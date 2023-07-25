# 4. Generar lista:
import random
mayor1 = mayor2 = 0
menor1 = menor2 = 999

# a. Generar una lista de 20 números enteros al azar de 3 dígitos.
for i in range(0,20):
    num = random.randint(100,999)
# b. Encontrar el mayor entre los menores a 500.
    if num < 500:
        if num > mayor1:
            mayor1 = num

    if num > 500:
        if num > menor1:
            menor1 = num
# c. Encontrar el menor entre los menores a 500.
    if num < menor2:
        if num > mayor2:
            mayor2 = num
# d. Encontrar el mayor entre los mayores a 500.
    if num > mayor2:
        if num < menor2:
           menor2 = num
    
    if num > 500:
        if num < menor2:
            menor2 = num
           
print("El numero mayor en los menores a 500: ", mayor1)
print("El numero menor en los menores a 500: ", menor1)
print("El numero mayor en los mayores a 500: ", mayor2)
print("El numero menor en los mayores a 500: ", menor2)