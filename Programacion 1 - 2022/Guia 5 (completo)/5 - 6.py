# Ejercicio 6:
from colorama import init, Fore , Back
init(True)
# 1. A partir de un texto:
texto = "Bienvenidos a un texto para practicas de Diego Llanos"
# 2. Mostrar en pantalla la cadena completa.
print(texto)
print()
#vocales = "a" , "e" , "i" , "o" , "u"
# 3. Encontrar y colorear todas las vocales en rojo.
# Para el desarrollo de este ejercicio recomiendo ir imprimiendo letra por letra dentro de un bucle for.
for vocal in texto:
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        print(Back.WHITE + Fore.RED + vocal, end="")
    else:
        print(vocal, end="")

print()