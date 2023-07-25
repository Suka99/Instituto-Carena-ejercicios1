#1
def insertar_valor(lista, valor):
    nueva_lista = []
    valor_insertado = False
    
    for elemento in lista:
        if not valor_insertado and valor < elemento:
            nueva_lista.append(valor)
            valor_insertado = True
        nueva_lista.append(elemento)
    
    if not valor_insertado:
        nueva_lista.append(valor)
    
    return nueva_lista

# lista_ordenada = [1, 3, 5, 7, 9]
# valor_a_insertar = 4

# nueva_lista = insertar_valor(lista_ordenada, valor_a_insertar)
# print(nueva_lista)  # Salida: [1, 3, 4, 5, 7, 9]

#2
def obtener_listas(lista):
    lista_menor = []  # Crear una lista vacía para almacenar los valores menores que el promedio.
    lista_mayor = []  # Crear una lista vacía para almacenar los valores mayores o iguales que el promedio.
    promedio = sum(lista) / len(lista)  # Calcular el promedio de la lista.

    for x in lista:
        if x < promedio:
            lista_menor.append(x)  # Agregar el valor a lista_menor si es menor que el promedio.
        else:
            lista_mayor.append(x)  # Agregar el valor a lista_mayor si es mayor o igual que el promedio.

    return lista_menor, lista_mayor  # Retornar lista_menor y lista_mayor como una tupla.
