print("\n Guia 3 - Ejercicio 2 \n")

import random

cont1, cont2, cont3 = 0 , 0 , 0
acum1, acum2, acum3 = 0 , 0 , 0

for x in range(0,30):
    numero = random.randint(100,999)
    print(x , "-" , numero)
    
    if numero >= 0 and numero <= 300:
        cont1 += 1
        acum1 += numero
        
    if numero >= 301 and numero <= 600:
        cont2 += 1
        acum2 += numero
    
    if numero >= 601 and numero <= 1000:
        cont3 += 1
        acum3 += numero
        
print("Valores entre 0 y 300: " , cont1 , " Acumulados: " , acum1 , "\n")

print("Valores entre 301 y 600: " , cont2 , " Acumulados: " , acum2 , "\n")

print("Valores entre 601 y 1000: " , cont3 , " Acumulados: " , acum3 , "\n")

print("Fin del Programa")
        

#2. Genera una serie de 30 números al azar de hasta 3 dígitos.
#b. Generar números aleatorios entre 0 y 999 (random.randint(0, 999).
#c. Contar y acumular los valores entre 0 y 300 inclusivos.
#d. Contar y acumular los valores entre 301 y 600 inclusivos.
#e. Contar y acumular los valores entre 601 y 1000 inclusivos.
#f. Mostrar los resultados.
