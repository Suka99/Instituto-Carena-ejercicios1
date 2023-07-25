#1 A partir de un texto:
texto = 'El mercado laboral actual conlleva a que los profesionales relacionados con la ' \
    'tecnología deban sortear distintos escenarios en los que Python aparece como una de ' \
    'las herramientas más utilizada (si no es la más popular) por distintos motivos. ' \
    'Es un lenguaje de programación interpretado, no compilado; es decir que no se necesita ' \
    'un complicado proceso de compilación, lo que lo hace más práctico y simple de aplicar, ' \
    'aunque un poco menos eficiente que los lenguajes compilados.'

#2 Mostrar en pantalla la cadena completa.
print(texto)

#3 Pasar el texto a un vector de palabras.
lista = texto.split()
texto_nuevo = ''

#4 Recorrer el vector y encerrar entre paréntesis aquellas palabras que empiecen
#  con una vocal minúsculas, mayúscula o acentuada.
letras = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']

for x, y in enumerate(lista):
    if y[0: 1].lower() in letras:
        lista[x] = '(' + y + ')'

    #Armar o concatenar el vector en otra variable String como por ejemplo nuevotexto.
    #Imprimir el nuevo texto.
    #texto_nuevo = texto_nuevo + lista[i] + ' '

# Se utiliza ' ' como separador para unir cada elemento de la lista.
texto_nuevo = ' '.join(lista)

print()
print(texto_nuevo)