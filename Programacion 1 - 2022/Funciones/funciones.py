#Funcion de saludo
def saludo():
    nombre = input("Ingresa tu nombre: ")
    print("Bienvenido: " + nombre)

# saludo()


# Suma simple
def suma(a,b):
    a = int(input("Ingrese valor: "))
    b = int(input("Ingrese valor: "))
    
    resultado = a + b
    return resultado

#Recuerda lo de abajo no lo entendiste muy bien. xd
# resultado_total = suma(0,0)
# print("Resultado: " , resultado_total) Comentado para crear otras funciones.

def sumadelista(lista):
    return sum(lista)

# numero = [1,6,8,10]
# print("Resultado: " , sumadelista(numero))

def quitar_caracter(texto):
    nuevo_texto = " "
    for caracter in texto:
        if caracter.isalpha() or caracter.isdigit() or caracter.isspace():
            nuevo_texto += caracter
    return nuevo_texto

#Texto_nuevo = quitar_caracter(texto) --> En "Texto" agrega lo que quieres seleccionar.
#print(texto_nuevo)
#####################################################

def minmax(lista, nombre):
    minimo = min(lista)
    maximo = max(lista)
    posmin = lista.index(minimo)
    posmax = lista.index(maximo)
    
    print(nombre, "Valor minimo: ",minimo ,"Posicion: ",posmin)
    print(nombre, "Valor maximo: ",maximo ,"Posicion: ",posmax)

#####################################################
def mostrar_lista(lista):
    for indice, valor in enumerate(lista):
        print(indice, ":", valor, end=" - ")

#mostrar_lista(V1)

def mayor_menor_promedio(lista):
    maximo = max(lista)
    minimo = min(lista)
    promedio = sum(lista) / len(lista)
    return minimo, maximo, promedio


# mayor, menor, promedio = mayor_menor_promedio(X)
# print()
# print("Mayor: " , mayor, "Menor: ", menor, "Promedio: ", promedio)


#Busca la palabra con menor y mayor caracteres y su posicion
def cantidad_caracteres(palabra):
    menor = min(palabra, key=len)
    posmin = palabra.index(menor)
    mayor = max(palabra, key=len)
    posmax = palabra.index(mayor)
    
    print(f"Palabra menor: {menor} Posicion: {posmin} ")
    print(f"Palabra mayor: {mayor} Posicion: {posmax} ")

#cantidad_caracteres(X)

def obtener_pares_impares(lista):
    lista_par=[]
    lista_impar=[]

    for x in lista:
        if x % 2 == 0:
            lista_par.append(x)
        else:
            lista_impar.append(x)

    return lista_par, lista_impar

def invertir_lista(lista):
    lista_invertida = []

    #range(start, stop, step)
    for x in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[x])

    return lista_invertida

# lista1=random.sample(range(10, 100), 20)
# print('lista1:', lista1)

# lista2, lista3 = obtener_pares_impares(lista1)
# print('lista2:', lista2)
# print('lista3:', lista3)

# lista4=invertir_lista(lista1)
# print('lista4:', lista4)
