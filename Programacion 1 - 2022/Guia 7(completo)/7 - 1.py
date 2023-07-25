from colorama import init, Fore
# 1. A partir de una cadena de texto iniciada en el código, mostrar la cadena en color azul.
texto = 'De acuerdo con Van Rossum, Python simplemente utiliza demasiada memoria y energía del ' \
    'hardware, por lo que el no le ve futuro en la creación de sitios web, además de los servicios ' \
    'Back End y su uso en WebAssembly, explicó el portal ZDNet. «Las personas que han logrado usar ' \
    'CPython en una tableta Android o iOS han encontrado que necesita demasiados recursos», resaltó ' \
    'el programador.'

print(Fore.BLUE + texto)
# 2. Crear un nuevo_texto con los caracteres que sean solo letras y espacios, mostrar nuevo_texto en color blanco (aplicar join combinado con sintaxis por comprensión para filtrar o filter).
nuevo_texto = ""
acentos= "ÁÉÍÓÚ"
for caracter in texto:
    if (caracter.upper() >= 'A' and caracter.upper() <= 'Z') or caracter.isspace() or caracter.upper() in acentos:
        nuevo_texto += caracter

print('\n', nuevo_texto, '\n')
# 3. Convertir el texto en una lista de palabras y mostrar todos los elementos y suposición en color blanco (enumerate).
palabras = nuevo_texto.split()
for X in range(len(palabras)):
    print(X, palabras[X]) #encapsular entre parentesis rectos para que muestre palabra por palabra, sino aparece el texto completo con posiciones diff
# print(Fore.WHITE, palabras)
# 4. Encontrar y mostrar el elemento menor, mayor y su posición en la lista de palabras (min, max e index, min y max deben proporcionar el argumento key = len paracomparar cadenas).
menor = palabras[0]
for x, palabra in enumerate(palabras):
    if len(palabra) < len(menor):
        menor = palabra
        posmenor = x

mayor = ''
for x, palabra in enumerate(palabras):
    if len(palabra) > len(mayor):
        mayor = palabra
        posmayor = x

print()
print('Palabra de menor longitud', menor, ', posición', posmenor)
print('Palabra de mayor longitud', mayor, ', posición', posmayor)
# 5. Mostrar la lista con formato de texto en color blanco, una palabra al lado de la otra separada por un espacio (join).
print('\n', ' '.join(palabras), '\n')
# 6. Mostrar la palabra menor en rojo en cada aparición, contar cuantas apariciones tiene.
# 7. Mostrar la palabra mayor en verde en cada aparición, contar cuantas apariciones tiene.
conmenor = 0
conmayor = 0

for palabra in palabras:
    if palabra == menor:
        print(Fore.RED + palabra, end=' ')
        conmenor += 1
    elif palabra == mayor:
        print(Fore.GREEN + palabra, end=' ')
        conmayor += 1
    else:
        print(palabra, end=' ')
# 8. Mostrar cuántas palabras menores y cuántas mayores se encontraron.
print()
print('\nLa palabra menor', menor, 'aparece', conmenor, 'veces')
print('La palabra mayor', mayor, 'aparece', conmayor, 'veces')