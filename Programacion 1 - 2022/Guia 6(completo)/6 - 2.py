import random
from minmax import minmax
# 1. Generar una lista de 20 elementos enteros al azar de hasta dos dígitos.
lista1 = random.sample(range(10,99),20)
print("Lista 1", lista1)
# 2. Calcular el menor, mayor elemento y sus posiciones de los primeros 10.
lista2 = lista1[0:10]
print("Lista 2", lista2)
# 3. Calcular el mayor, menor elemento y sus posiciones de los segundos 10.
lista3 = lista1[10:20]
print("Lista 3", lista3)
# 4. Mostrar resultados
print()
minmax(lista2,"lista2")
print()
minmax(lista3,"lista3")