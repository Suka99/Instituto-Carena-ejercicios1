import os

texto = "Bienvenidos a un texto para practicas de Diego Llanos"

# Mostrar la cadena completa
print(texto)
print()

# Cambiar la configuración de la pantalla a 40 columnas y el número de filas necesarias
os.system('mode 40,60')

# Imprimir el texto en pantalla con 40 columnas y el número de filas necesarias
filas = len(texto) // 40 + 1
for i in range(filas):
    inicio = i * 40
    fin = inicio + 40
    print(texto[inicio:fin])
