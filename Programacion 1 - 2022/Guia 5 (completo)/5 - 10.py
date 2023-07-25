# Ejercicio 10:
# 1. A partir de un texto.
texto = "Bienvenidos a un texto para practicas de Diego Llanos"
# 2. Mostrar en pantalla la cadena completa.
print(texto)
print()
# 3. Imprimir nuevamente el texto pero con los artículos (el, la, los, las, un, una, unos, unas) encerrados entre asteriscos (ej: *el*)
# (Trabajarlo con una lista)
lista = texto.split()
articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas"]

for vocal in lista:
    if vocal.lower() in articulos:
        print("*" + vocal + "*", end=" ")
    else:
        print(vocal, end=" ")