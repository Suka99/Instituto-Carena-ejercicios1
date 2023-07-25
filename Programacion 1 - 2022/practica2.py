def limpiar_palabras(lista):
    for indice, palabra in enumerate(lista):
        palabra1 =""
        for x in palabra1:
            if x.isalnum():
                palabra1 +=x
                lista[indice] = palabra1
                return lista