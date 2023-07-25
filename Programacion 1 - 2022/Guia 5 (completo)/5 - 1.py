# Ejercicio 1:
# 1. A partir de una cadena de texto:
from colorama import init, Style, Fore, Cursor, Back
init(True)
texto = "Bienvenidos a un texto para practicas."
# 2. Mostrar en pantalla la cadena completa.
print(texto)
print()
# 3. Añadir una estructura de control while.
while True:
# 4. Solicitar al usuario ingrese una palabra a buscar en el texto.
    palabra = input("Ingrese una palabra a buscar en el texto: ")
# 5. Salir con enter o sea cuando palabra sea igual ‘’
    if palabra == "":
            break
# 6. Para buscar utilizar texto.find
    buscar = texto.find(palabra)
# 7. Si la búsqueda devuelve -1, mostrar el cartel “La palabra no se encuentra”
    if buscar == -1:
        print("La palabra no se encuentra")
# 8. Si la palabra se encuentra mostrar el texto con la palabra coloreada en rojo
    else:
        print(Back.WHITE + Fore.RED + palabra)
