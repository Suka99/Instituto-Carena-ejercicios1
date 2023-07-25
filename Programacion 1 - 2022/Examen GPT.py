import random

# 1
def insertar_valor(lista, valor):
    nueva_lista = []
    valor_insertado = False
    for elemento in lista:
        if not valor_insertado and elemento > valor:
            nueva_lista.append(valor)
            valor_insertado = True
        nueva_lista.append(elemento)
    if not valor_insertado:
        nueva_lista.append(valor)
    return nueva_lista

# 2
def obtener_listas(lista):
    lista_menor = []  # Creación de una lista vacía para almacenar los elementos menores al promedio.
    lista_mayor = []  # Creación de otra lista vacía para almacenar los elementos mayores o iguales al promedio.

    # Cálculo del promedio de los elementos en la lista utilizando la función sum() y len().
    promedio = sum(lista) / len(lista)

    # Iteración sobre cada elemento en la lista.
    for x in lista:
        # Si el elemento es menor al promedio, se añade a la lista_menor.
        if x < promedio:
            lista_menor.append(x)
        # Si el elemento es mayor o igual al promedio, se añade a la lista_mayor.
        else:
            lista_mayor.append(x)

    # Se retorna las listas lista_menor y lista_mayor como una tupla.
    return lista_menor, lista_mayor


# 3
lista1 = [random.randint(10, 99) for _ in range(10)]
lista1.sort()

print("lista1:", lista1)

# 4
lista2 = insertar_valor(lista1, 35)
print("lista2:", lista2)

# 5
lista3, lista4 = obtener_listas(lista1)
print("lista3 (menor):", lista3)
print("lista4 (mayor):", lista4)
