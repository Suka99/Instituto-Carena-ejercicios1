# Ejercicio 4:
from colorama import init, Fore, Back
init(True)
# 1. A partir de un texto:
texto = "Bienvenidos a un texto para practicas de Diego Llanos"
# 2. Mostrar en pantalla la cadena completa..
print(texto)
print()

lista = {'el': 0, 'la': 0, 'los': 0, 'las': 0, 'un': 0, 'una': 0, 'unos': 0, 'unas': 0}
# 3. Encontrar cada unos de los artículos de la lista (el, la, los, las, un, una, unos, unas) e imprimir el artículo y la posición dentro de la cadena de cada aparición.
for palabra in texto:
    indice = 0
    while True:
        buscar = texto.find(" " + palabra + " ", indice)

        if buscar == -1:

# 4. Contar y mostrar cuantos artículos de cada uno se encontraron.
            if indice == 0:
                print("La palabra", Back.WHITE + Fore.RED + " " + palabra +" ", "no se encuentra")
        else:
            print("Se encontro", Back.WHITE + Fore.RED + ' ' + palabra + ' ', 'en la posición', buscar)
            lista[palabra] += 1
            indice = buscar + 1
print()

for clave, valor in lista.items():
    print("Cantidad de aparicioones de la plabra", clave, valor)

