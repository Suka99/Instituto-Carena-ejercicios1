print("Guia 3 Ejercicio 1. \n")


import random

contadorpor2, contadorpor3, contadorpor4, contadorpor5 = 0,0,0,0
acumulador2, acumulador3 ,acumulador4 ,acumulador5 = 0, 0, 0, 0

for x in range(0,20):
    numero = random.randint(100,999)
    print(x, numero)
    
    if numero % 2 == 0:
        contadorpor2 += 1
        acumulador2 += numero
    
    if numero % 3 == 0:
        contadorpor3 += 1
        acumulador3 += numero
    
    if numero % 4 == 0:
        contadorpor4 += 1
        acumulador4 += numero
    
    if numero % 5 == 0:
        contadorpor5 += 1
        acumulador5 += numero

print("\n")
print("Divisioves por 2: " , contadorpor2 , " Valores acumulados " , acumulador2)
print("Divisioves por 3: " , contadorpor3 , " Valores acumulados " , acumulador3)
print("Divisioves por 4: " , contadorpor4 , " Valores acumulados " , acumulador4)
print("Divisioves por 5: " , contadorpor5 , " Valores acumulados " , acumulador5)

print("\n")
print("Fin del Programa")