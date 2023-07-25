# Ejercicio 11:
# 1. A partir de un texto:
texto = "Bienvenidos a un texto para practicas de Diego Llanos"
# 2. Mostrar en pantalla la cadena completa.
print(texto)
print()
# 3. Pasar el texto a un vector de palabras.
lista = texto.split()
nuevo_texto = " "
# 4. Recorrer el vector y encerrar entre paréntesis aquellas palabras que empiecen con una vocal minúsculas, mayúscula o acentuada.
letras = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']
for palabra in lista:
    if palabra.lower(0) in letras:
        nuevo_texto += "(" + palabra + ")"
    else:
        nuevo_texto += palabra + " "
        
# 6. Imprimir el nuevo texto.
#nuevo_texto = " ".join(lista)
print(nuevo_texto)