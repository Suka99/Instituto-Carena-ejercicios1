# 1. A partir de una cadena de texto texto1 inicializada en el código, convertir en un
# vector p() de palabras y mostrar.
texto = 'De acuerdo con Van Rossum, Python simplemente utiliza demasiada memoria y energía del ' \
    'hardware, por lo que el no le ve futuro en la creación de sitios web, además de los servicios ' \
    'Back End y su uso en WebAssembly, explicó el portal ZDNet. «Las personas que han logrado usar ' \
    'CPython en una tableta Android o iOS han encontrado que necesita demasiados recursos», resaltó ' \
    'el programador.'

palabras = texto.split()
print(palabras)
print()
# 2. Mostrar el elemento menor (en cantidad de caracteres), mayor (en cantidad de
# caracteres) y su posición del vector p().
def cantidad_caracteres(palabra):
    menor = min(palabra, key=len)
    posmin = palabra.index(menor)
    mayor = max(palabra, key=len)
    posmax = palabra.index(mayor)
    
    print(f"Palabra menor: {menor} Posicion: {posmin} ")
    print(f"Palabra mayor: {mayor} Posicion: {posmax} ")

cantidad_caracteres(palabras)
print()
# 3. Concatenar los elementos en una nueva cadena texto2 pero en sentido inverso, es
# decir donde el primer elemento sea el último elemento de p() y mostrar al finalizar.
texto2 = ' '.join(palabras[::-1])
print(texto2)
# 4. Crear un procedimiento para mostrar el vector p(), llamar desde main