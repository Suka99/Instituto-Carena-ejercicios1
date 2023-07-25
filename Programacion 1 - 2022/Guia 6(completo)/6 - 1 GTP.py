import random

# Generar una lista V1 de 20 elementos enteros de hasta 2 dígitos
V1 = [random.randint(1, 99) for _ in range(20)]

# Obtener una lista V2 con los elementos divisibles por 2
V2 = [num for num in V1 if num % 2 == 0]

# Obtener una lista V3 con los elementos no divisibles por 2
V3 = [num for num in V1 if num % 2 != 0]

# Calcular el mayor, menor elemento y sus posiciones de la lista V2
max_V2 = max(V2)
min_V2 = min(V2)
max_pos_V2 = V2.index(max_V2)
min_pos_V2 = V2.index(min_V2)

# Calcular el mayor, menor elemento y sus posiciones de la lista V3
max_V3 = max(V3)
min_V3 = min(V3)
max_pos_V3 = V3.index(max_V3)
min_pos_V3 = V3.index(min_V3)

# Mostrar los resultados
print("Lista V1:", V1)
print("Lista V2:", V2)
print("Lista V3:", V3)
print("Mayor elemento de V2:", max_V2)
print("Menor elemento de V2:", min_V2)
print("Posición del mayor elemento en V2:", max_pos_V2)
print("Posición del menor elemento en V2:", min_pos_V2)
print("Mayor elemento de V3:", max_V3)
print("Menor elemento de V3:", min_V3)
print("Posición del mayor elemento en V3:", max_pos_V3)
print("Posición del menor elemento en V3:", min_pos_V3)
