def mostrar(nombre):
    print(nombre)
# 1. A partir de una cadena de texto inicializada en el código, convertir a una lista p de palabras y mostrar.
texto = "Texto con fines educativos para pruebas."
palabras = texto.split()
print(palabras)
# 2. Mostrar el elemento menor (en cantidad de caracteres), mayor (en cantidad de caracteres) y 
# su posición en la lista p (aplicar min y max con el parámetro key = len) ejemplo: menor = min(palabras, key = len).
menor = min(palabras, key = len)
mayor = max(palabras, key = len)
menorposicion = palabras.index(menor)
mayorposicion = palabras.index(mayor)
print(f"Palabra menor: {menor} y su posicion: {menorposicion}")
print(f"Palabra mayor: {mayor} y su posicion: {mayorposicion}")
# 3. Concatenar los elementos de la lista en una nueva cadena nuevo_texto pero en sentido inverso, es decir donde el primer elemento sea el último elemento de p 
# y mostrar al finalizar (aplicar join con for reversed).

nuevo_texto = " ".join(texto for texto in reversed(palabras))
# 4. Crear una función para mostrar la lista p, llamar desde main.

mostrar(nuevo_texto)