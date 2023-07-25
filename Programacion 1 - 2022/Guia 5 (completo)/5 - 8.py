# Ejercicio 8:
from colorama import init,Fore
init(True)
# 1. A partir de un texto:
texto = "Bienvenidos a un texto para practicas de Diego Llanos"
# 2. Mostrar en pantalla la cadena completa.
print(texto)
print()
# 3. Imprimir el texto y remarcar los artículos (el, la, los, las, un, una, unos, unas) en otro color.
for vocal in texto:
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        print(Fore.BLUE + vocal, end="")
    else:
        print(vocal, end="")
    
print()