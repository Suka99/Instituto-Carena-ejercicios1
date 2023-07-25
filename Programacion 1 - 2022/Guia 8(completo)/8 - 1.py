from colorama import init,Fore
init(True)
# 1. A partir de una cadena de texto iniciada en el código mostrar la cadena en color
# azul.
texto = "Texto con fines educativos para pruebas."


def mostrar_en_azul(texto):
    print(Fore.BLUE + texto)
    print()
    return
# 2. En el texto quitar los caracteres que no sean letras ni números, mostrar nuevamente
# el texto en blanco, utilizar la función Replacepara quitar.
def quitar_caracter(texto):
    nuevo_texto = " "
    for caracter in texto:
        if caracter.isspace() or caracter.isdigit() or caracter.isalpha():
            nuevo_texto += caracter
    return nuevo_texto
texto_nuevo = quitar_caracter(texto)
print(texto_nuevo)
# 3. Convertir el texto en un vector p() de palabras y mostrar todos los elementos y su
# posición en blanco.
def convertir_vector(texto):
    vector = texto.split()
    return vector

A = convertir_vector(texto_nuevo)
print(A)
# 4. Encontrar y mostrar el elemento menor, mayor y su posición en el vector p, inicializar
# menor con el primer elemento del vector y mayor con nada (“”).
def encontrar_mayor_menor(palabra):
    minimo = min(palabra, key=len)
    posmin = palabra.index(minimo)
    maximo = max(palabra, key=len)
    posmax = palabra.index(maximo)
    return minimo, posmin, maximo, posmax

# 5. Mostrar el vector con formato de texto en color blanco, una palabra al lado de la otra
# separa por un espacio.
def mostrar_vector(palabra):
    print(Fore.WHITE + ' '.join(palabra))
    print()
    return
# 6. Mostrar la palabra menor en rojo en cada aparición, contar cuantas apariciones
# tiene.
def mostrar_menor(palabra, menor, posmenor):
    contador=0
    for x in palabra:
        if x == menor:
            contador += 1
            print(Fore.RED + x, end=' ')
        else:
            print(Fore.WHITE + x, end=' ')
    print('\n', 'La palabra menor aparece {} veces'.format(contador))
    print()
    return
# 7. Mostrar la palabra mayor en verde en cada aparición, contar cuantas apariciones
# tiene.
def mostrar_mayor(palabra, mayor, posmayor):
    contador=0
    for x in palabra:
        if x == mayor:
            contador += 1
            print(Fore.GREEN + x, end=' ')
        else:
            print(Fore.WHITE + x, end=' ')
    print('\n', 'La palabra mayor aparece {} veces'.format(contador))
    print()
    return
# 8. Mostrar cuántas palabras menores y cuántas mayores se encontraron.
def contar_mayores_menores(palabra, menor, mayor):
    contador_menor=0
    contador_mayor=0
    for x in palabra:
        if x == menor:
            contador_menor += 1
        if x == mayor:
            contador_mayor += 1
    print('La palabra menor aparece {} veces'.format(contador_menor))
    print('La palabra mayor aparece {} veces'.format(contador_mayor))
    print()
    return

mostrar_en_azul(texto)

texto_nuevo = quitar_caracter(texto)
print(texto_nuevo)

v = convertir_vector(texto_nuevo)
print(v)

r = encontrar_mayor_menor(v)
print('El elemento menor es:', '"' + r[0] + '"', 'en la posición:', r[1])
print('El elemento mayor es:', '"' + r[2] + '"', 'en la posición:', r[3])
print()

#a1,a2,a3,a4 = encontrar_mayor_menor(v)
menor, posmenor, mayor, posmayor = encontrar_mayor_menor(v)

mostrar_vector(v)

mostrar_menor(v, r[0], r[1])

mostrar_mayor(v, r[2], r[3])

contar_mayores_menores(v, r[0], r[2])