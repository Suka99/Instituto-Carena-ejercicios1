# Generar lista:
import random
cont = 0
acum = 0
# a. Generar una lista de 20 números enteros al azar de 3 dígitos.
for i in range(0,20):
    numero = random.randint(100,999)
    
    if numero > 300 and numero < 700:
        cont += 1
        acum += 1
# b. Mostrar los números mayores a 300 y menores a 700 inclusivos.        
        print(i,"-", numero)

# c. Acumular los números del rango.
# d. Contar los números del rango
print("rango acumulado: ", acum , "rango contado: ", cont)