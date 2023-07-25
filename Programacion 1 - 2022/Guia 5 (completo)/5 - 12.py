# Ejercicio 12:
from colorama import init, Fore
init(True)
# 1. A partir de un texto:
texto = "Bienvenidos a un texto para practicas de Diego Llanos" \
    'De acuerdo con Van Rossum, Python simplemente utiliza demasiada memoria y energía del ' \
    'hardware, por lo que el no le ve futuro en la creación de sitios web, además de los servicios ' \
    'Back End y su uso en WebAssembly, explicó el portal ZDNet. «Las personas que han logrado usar ' \
    'CPython en una tableta Android o iOS han encontrado que necesita demasiados recursos», resaltó ' \
    'el programador.'
# 2. Mostrar en pantalla la cadena completa.
print(texto)
print()
# 3. Pasar el texto a un vector v.
vector = texto.split()
print(vector)
acentos='áéíóú'
contador = 0
# 4. Contar e Imprimir nuevamente el texto coloreando las palabras con acento ortográfico.
for palabra in vector:
    flag=False

    for letra in palabra:
        if letra.lower() in acentos:
            contador += 1
            flag=True
            break

    if flag:
        print(Fore.RED + palabra, end=' ' )
    else:
        print(palabra, end=' ')

# 5. Mostrar el resultado del contador.
print("Contador: ", contador)