# Ejercicio 3:
from colorama import init, Fore
# 1. A partir de un texto:
texto = "Bienvenidos a un texto para practicas de Diego Llanos"
# 2. Mostrar en pantalla la cadena completa..
print(texto)
print()
# 3. Pasar el texto a un lista.
lista = texto.split()
print(lista)
# 4. Recorrer el vector.
for palabra in lista:
# 5. Determinar si el elemento o palabra es uno de artículos (el, la, los, las, un, una, unos, unas).
    if palabra == 'el' or palabra == 'la' or palabra == 'los' or palabra == 'las' \
    or palabra == 'un' or palabra == 'una' or palabra == 'unos' or palabra == 'unas':
# 6. Las palabras que no son artículos de la lista mostrarlas en color blanco y a los artículos en color rojo, deben formar un párrafo.

        print(Fore.RED + palabra," ", end="")
    else:
        print(palabra," ", end="")
    