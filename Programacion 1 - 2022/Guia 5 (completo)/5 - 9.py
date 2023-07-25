# Ejercicio 9:
from colorama import init, Fore
init(True)
# 1. A partir de un texto:
texto = "Bienvenidos a un texto para practicas de Diego Llanos"
# 2. Mostrar en pantalla la cadena completa.
print(texto)
print()
# 3. Imprimir el texto con las vocales coloreadas según la siguiente tabla:
for vocal in texto:
    if vocal == "a":
        print(Fore.BLUE + vocal, end="")
    elif vocal == "e":
        print(Fore.CYAN + vocal, end="")
    elif vocal == "i":
        print(Fore.GREEN + vocal, end="")
    elif vocal == "o":
        print(Fore.MAGENTA + vocal, end="")
    elif vocal == "u":
        print(Fore.RED + vocal, end="")
    else:
        print(vocal, end="")