# Ejercicio 2:
from colorama import init, Fore, Back
init(True)

# 1. A partir de una cadena de texto:
texto = "Bienvenidos a un texto para practicas de Diego Llanos."
# 2. Mostrarlo en pantalla la cadena completa.
print(texto)
print()
# 3. Pasar el texto a una lista de palabras.
lista = texto.split()
print(lista)
# 4. Recorrer la lista con la instrucción for palabra in lista.
for palabra in lista:
    letra = palabra[0:1]

# 5. Determinar si la palabra o elemento comienza en mayúscula.
    if (letra >= 'A' and letra <= 'Z') or (letra >= 'Á' and letra <= 'Ú'):
        # 6. Si empieza con mayúscula imprimir en color rojo sino imprimir en blanco, deben formar un párrafo.
        print(Fore.RED + palabra + ' ', end='')

    else:
        print(palabra + ' ', end='')