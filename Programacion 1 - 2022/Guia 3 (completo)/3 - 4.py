print("\n Guia 3 - Ejercicio 4 \n")

cont1,cont2 = 0, 0
acum1, acum2 = 0, 0
contador = 0

while True:
 
    numero = int(input("Ingrese 12 numeros entre 1 y 100: "))

    if numero == -1:
        break
    
    if numero < 1 or numero > 100:
        print("Valor fuera de rango")
        continue
    
    contador += 1
    
    if numero % 2 == 0:
        cont1 += 1
        acum1 += numero
        
    else:
        cont2 += 1
        acum2 += numero
    

print("Valores ingresados: " , contador)
print("Numeros contados divisibles por 2: ", cont1, "Numeros acumuladores: " ,acum1,)
print("Numeros contados no divisibles por 2: ", cont2, "Numeros acumuladores: " ,acum2,)

# d. Contar y acumular los divisibles por 2. (número % 2)
# e. Contar y acumular los no divisibles por 2. (else)
# f. Mostrar los resultados en caso de completar la lista
# g. En caso de no completar la lista mostrar el mensaje “No ha completado la lista de 12 números”.1