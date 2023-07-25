import random

def insertar_valor(lista, valor):
    # Inserta el parámetro valor en nueva lista en la posición que corresponde a su orden.
    nueva_lista = []
    # insertado es u na variable para poner en True cuando se el momento de insertar valor.
    insertado = False
    # Bucle for para recorrer lista.
    for x in lista:
        # Si insertado es False y además x es mayor que valor, entonces es el momento de
        # insertar valor.
        if not insertado and x >= valor:
            # Añade valor a nueva_lista.
            nueva_lista.append(valor)
            # Pone insertado en False para que no se vuelva a insertar.
            insertado = True
        # Añade x al final de nueva_lista.
        nueva_lista.append(x)
    # Retorna nueva_lista.
    return nueva_lista

def obtener_listas(lista):
    # Obtiene dos listas, una con los menores al promedio y otra con los mayores o igual al promedio.
    # Incializa la lista de menores.
    lista_menor = []
    # Inicializa la lista de mayores.
    lista_mayor = []
    # Inicializa el promedio obenteniendo la suma de valores dividio la cantidad de valores.
    promedio = sum(lista) / len(lista)
    # Recorre la lista
    for x in lista:
        if x < promedio:
            # Si el valor de x es menor que promedio, entonces añade x en lista_menor.
            lista_menor.append(x)
        else:
            lista_mayor.append(x)
    return lista_menor, lista_mayor

# Genera una lista al azar entre 10 y 100 no inclusivo de 10 elementos.
lista1 = random.sample(range(10, 100), 10)
# Ordena lista1.
lista1.sort()
# Muestra lista1 y su contenido.
print('lista1:', lista1)
# Guarda en lista2 lo que devuelve el llamado de insertar_valor con los parámetros
# lista1 y el valor 35.
lista2 = insertar_valor(lista1, 35)
# Muestra lista2 y sus valores.
print('lista2:', lista2)
# Obtiene lista3 y lista4 como resultado de la llamada a obtener_listas con el
# parámetro lista1
lista3, lista4 = obtener_listas(lista1)
# Muestra lista3 y lista4 con sus respectivos valores.
print('lista3:', lista3)
print('lista4:', lista4)