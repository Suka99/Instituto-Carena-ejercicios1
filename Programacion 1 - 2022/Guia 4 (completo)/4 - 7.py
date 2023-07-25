# 7. Realizar un algoritmo que:
import random
# a. Generar una lista al azar de 20 números enteros de hasta 2 dígitos.
for i in range(0,20):
    elementos = random.randint(10,99)
    print(i , "-" , elementos)
    
    if elementos != nuevosElementos:
        nuevosElementos = random.randint(10,99)
        print( i , "-" , nuevosElementos)
# b. Obtener una segunda lista con los elementos no repetidos de la primera lista.
# c. Mostrar la lista original.
print(i , "-" , elementos)
# d. Mostrar la nueva lista.
print( i , "-" , nuevosElementos)