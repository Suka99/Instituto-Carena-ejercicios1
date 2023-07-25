import random
# 1. Generar una lista V1 de 20 elementos enteros de hasta 2 dígitos.
V1 = random.sample(range(10,99),20)
print("Lista V1", V1)
V2 = []
V3 = []
# 2. Obtener una lista V2 a partir del lista V1 con los elementos divisibles por 2.
for numero in V1:
    if numero % 2 == 0:
        V2.append(numero)
# 3. Obtener una lista V3 a partir de la lista V1 con los elementos no divisibles por 2.
    else:
        V3.append(numero)

print("Lista V2", V2)
print("Lista V3", V3)
# 4. Calcular el mayor, menor elemento y sus posiciones de la lista V2.
maximo = max(V2)
minimo = min(V2)
max_posicion = V2.index(maximo)
min_posicion = V2.index(minimo)

print("\nLista V2")
print("Minimo:", minimo, "posicion:", min_posicion)
print("Maximo:", maximo, "posicion:", max_posicion)
# 5. Calcular el mayor, menor elemento y sus posiciones de la lista V3.
maximo = max(V3)
minimo = min(V3)
max_posicion = V3.index(maximo)
min_posicion = V3.index(minimo)

print("\nLista V3")
print("Minimo:", minimo, "posicion:", min_posicion)
print("Maximo:", maximo, "posicion:", max_posicion)
# 6. Mostrar los resultados.
