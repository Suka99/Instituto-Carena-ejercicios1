print("\n Guia 3 - Ejercicio 5 \n")

import random

cont1, cont2, = 0, 0
acum1, acum2, = 0, 0

for x in range(0,30):
    numero = random.randint(10,99)
    #print( x , "-" , numero)
    
    if numero % 2 == 0:
        cont1 += 1
        acum1 += numero
        print("*" , numero)
    
    else:
        cont2 += 1
        acum2 += numero
        print("#", numero)

print("Numeros pares contados: ", cont1 , "valores acumulados: ", acum1)
print("Numeros pares contados: ", cont2 , "valores acumulados: ", acum2)