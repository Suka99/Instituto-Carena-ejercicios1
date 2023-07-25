# 1. Inicializar 2 matrices v1 y v2 de 5 x 5 con valores enteros de hasta 2 dígitos.
# 2. Cargar las listas con números al azar con dos for anidados para filas y columnas.
# 3. Mostrar por separado cada lista con dos for, usar print(‘{:>2}’.format(v1[f][c])).
import random

# 1. Inicializar las matrices v1 y v2
v1 = [[0 for _ in range(5)] for _ in range(5)]
v2 = [[0 for _ in range(5)] for _ in range(5)]

# 2. Cargar las listas con números al azar
for f in range(5):
    for c in range(5):
        v1[f][c] = random.randint(0, 99)
        v2[f][c] = random.randint(0, 99)

# 3. Mostrar la matriz v1
print("Matriz v1:")
for f in range(5):
    for c in range(5):
        print('{:>2}'.format(v1[f][c]), end=' ')
    print()

# 4. Mostrar la matriz v2
print("\nMatriz v2:")
for f in range(5):
    for c in range(5):
        print('{:>2}'.format(v2[f][c]), end=' ')
    print()
