def minmax(lista, nombre):
    minimo = min(lista)
    maximo = max(lista)
    posmin = lista.index(minimo)
    posmax = lista.index(maximo)
    
    print(nombre, "Valor minimo: ",minimo ,"Posicion: ",posmin)
    print(nombre, "Valor maximo: ",maximo ,"Posicion: ",posmax)
    