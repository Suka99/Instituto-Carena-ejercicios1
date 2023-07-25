def conteo(lista,variable):
    contador=0
    for x in lista:
        if variable.lower() == x.lower():
            contador+=1
    print("La palabra", variable, "aparece", contador)

texto = 'Una cadena de bloques, conocida en inglés como blockchain, es una '\
'etiqueta que a través de una estructura de datos cuya información se agrupa '\
'en conjuntos (bloques) a los que se les añade metainformaciones relativas a '\
'otro bloque de la cadena anterior en una línea temporal para hacer un '\
'seguimiento seguro a través de grandes cálculos criptográficos. Este/ párrafo '\
'(es) para ver el- -funcionamiento *del algo-ritmo (reconocer, arenera, salas, '\
'radar, ojo, ana, ala, seres)'

print(texto)
print()

lista1 = texto.split()
print("Lista 1:", lista1)
print()

lista2 = []

for palabra in lista1:
    limpia = ''
    for caracter in palabra:
        if not caracter == ',' and not caracter == ')':
            limpia += caracter

    if limpia != '':
        lista2.append(limpia)
        
print("Lista 2:", lista2)
print()

lista3=[x for x in lista2 if x ==x[::-1]]

print("Lista 3", lista3)
print()

while True:
    palabra = input("Ingrese la palabra que busca: ")
    if palabra == "":
        break
    else:
        conteo(lista3, palabra)
        
lista4 = lista3
lista4.sort()
print("Lista 4", lista4)