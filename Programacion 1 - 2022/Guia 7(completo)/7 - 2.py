import random

def mostrar(nombre,lista):
    print()
    print(nombre, lista)
    for posicion, numero in enumerate(lista):
        print(f"Posicion: {posicion} - {numero}")

def menor_mayor(lista):
    menor = min(lista)
    mayor = max(lista)
    promedio = sum(lista) / len(lista)
    resultado = f"El numero menor es: {menor} el numero mayor es: {mayor} y su promedio es: {promedio}"
    print(resultado)
# 1. Generar una lista de 30 elementos enteros al azar entre 50 y 250 inclusivos y
# guardarlos en una lista v1 (random.sample).
V1 = random.sample(range(50, 250), 30)
# 2. Hacer una copia en una segunda lista v2 con los valores del primero que se
# encuentren entre 75 y 225 (aplicar sintaxis por comprensión).
V2 = [numero for numero in V1 if numero >= 75 and numero <= 225]
# 3. Crear una función para mostrar todos los elementos de una lista cualquiera y su
# posición, llamarla desde el main para mostrar v1 y v2.
mostrar("lista V1", V1)
menor_mayor(V1)
mostrar("Lista V2", V2)
menor_mayor(V2)
# 4. Crear una función para encontrar el mayor, menor y el promedio de un lista
# cualquiera, llamar desde el main para mostrar los resultados de v1 y v2.