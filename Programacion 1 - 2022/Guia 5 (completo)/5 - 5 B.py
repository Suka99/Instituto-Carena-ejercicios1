texto = "Este es un texto de ejemplo. Bienvenidos a un texto para practicas de Diego Llanos"

# Mostrar la cadena completa
print("Cadena completa:")
print(texto)

# Reemplazar las vocales según la lista dada
vocales = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}

nueva_cadena = ""
for caracter in texto:
    if caracter.lower() in vocales:
        nueva_cadena += vocales[caracter.lower()]
    else:
        nueva_cadena += caracter

# Mostrar la nueva cadena o la cadena original modificada
print("\nCadena modificada:")
print(nueva_cadena)
