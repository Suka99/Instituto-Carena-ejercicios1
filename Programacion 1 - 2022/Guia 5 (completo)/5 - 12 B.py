import re
from collections import Counter

# Paso 1: Obtener el texto
texto = 'El mercado laboral actual conlleva a que los profesionales relacionados con la ' \
    'tecnología deban sortear distintos escenarios en los que Python aparece como una de ' \
    'las herramientas más utilizada (si no es la más popular) por distintos motivos. ' \
    'Es un lenguaje de programación interpretado, no compilado; es decir que no se necesita ' \
    'un complicado proceso de compilación, lo que lo hace más práctico y simple de aplicar, ' \
    'aunque un poco menos eficiente que los lenguajes compilados.'

# Paso 2: Mostrar la cadena completa
print("Cadena completa:")
print(texto)

# Paso 3: Convertir el texto en un vector
v = re.findall(r'\w+', texto.lower())

# Paso 4: Contar e imprimir nuevamente el texto con palabras acentuadas
contador = Counter(v)
texto_con_acentos = re.sub(r'(\w*[áéíóúÁÉÍÓÚ]\w*)', r'\033[91m\1\033[0m', texto)
print("Texto con palabras acentuadas:")
print(texto_con_acentos)

# Paso 5: Mostrar el resultado del contador
print("Resultado del contador:")
for palabra, conteo in contador.items():
    print(f"{palabra}: {conteo}")
