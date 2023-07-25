#1
def fusionar_listas_ordenadas(lista1, lista2):
    resultado = []
    i, j = 0, 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])

    return resultado

lista1 = [1, 2, 3] # cadenas ordenas
lista2 = [2, 4, 6]
resultado = fusionar_listas_ordenadas(lista1, lista2)
print(resultado)  # salida [1 ,2 ,2 ,3 ,4, 6]

# si pongo una cadena no ordenada [2, 4, 0] se rompe :c
def cadena_palabras(cadena):
    
    palabras = cadena.split()
    contador = 0
    
    for palabra in palabras:
        if len(palabra) > 5:
            contador += 1

    return contador

# Ejemplo de uso:
texto = "Hola manolo queri chocolate."
resultado = cadena_palabras(texto)
print(resultado) # Tiene que salir con mas de 5 letras [Manolo y chocolate]