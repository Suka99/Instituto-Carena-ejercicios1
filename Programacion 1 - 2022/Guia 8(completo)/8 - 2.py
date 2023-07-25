import random

# 1. Generar una lista de 30 elementos enteros al azar entre 50 y 250 inclusivos y
# guardarlos en un vector v1().
V1 = random.sample(range(50,250),30)
# print("Lista V1",V1)

# 2. Hacer una copia en un segundo vector v2() con los valores del primero que se
# encuentren entre 75 y 225.
V2 = [numero for numero in V1 if numero >= 75 and numero <= 225]
# print("Lista V2",V2)

# 3. Crear una subrutina o procedimiento para mostrar todos los elementos de un vector
# cualquiera y su posición, llamarla desde el main para mostrar v1 y v2.
def mostrar_lista(lista):
    for indice, valor in enumerate(lista):
        print(indice, ":", valor, end=" ")

mostrar_lista(V1)
print()
mostrar_lista(V2)
print()
# 4. Crear una subrutina para encontrar el mayor, menor y el promedio de un vector
# cualquiera, llamar desde el main para mostrar los resultados de v1() y v2().
def mayor_menor_promedio(lista):
    maximo = max(lista)
    minimo = min(lista)
    promedio = sum(lista) / len(lista)
    return minimo, maximo, promedio


mayor, menor, promedio = mayor_menor_promedio(V1)
print()
print("Mayor: " , mayor, "Menor: ", menor, "Promedio: ", promedio)

mayor, menor, promedio = mayor_menor_promedio(V2)
print()
print("Mayor: " , mayor, "Menor: ", menor, "Promedio: ", promedio)