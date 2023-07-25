# Ejercicio 5:
# 1. A partir de un texto:
texto = "Bienvenidos a un texto para practicas de Diego Llanos"
# 2. Mostrar en pantalla la cadena completa.
print(texto)
print()
#vocales = ["a", "b", "c", "d", "e"]
#numeros = "1", "2", "3", "4", "5"

texto_modificado = " "
# 3. Encontrar las vocales y reemplazarlas según la siguiente lista (a - 1, e - 2, i - 3, o - 4, u - 5)
for caracter in texto:
    if caracter == "a":
        texto_modificado = texto_modificado + "1"
    elif caracter == "e":
        texto_modificado = texto_modificado + "2"
    elif caracter == "i":
        texto_modificado = texto_modificado + "3"
    elif caracter == "o":
        texto_modificado = texto_modificado + "4"
    elif caracter == "u":
        texto_modificado = texto_modificado + "5"
    else:
        texto_modificado = texto_modificado + caracter
        

# 4. Mostrar como queda la nueva cadena o la cadena original modificada.

print(texto_modificado)

# for caracter in cadena_original:
#     if caracter == caracter_a_reemplazar:
#         cadena_modificada += caracter_reemplazo
#     else:
#         cadena_modificada += caracter

# print(cadena_modificada)