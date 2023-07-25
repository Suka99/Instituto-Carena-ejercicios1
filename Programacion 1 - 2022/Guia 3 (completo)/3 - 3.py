print("\n Guia 3 - Ejercicio 3 \n")

cont1, cont2 = 0, 0
acum1, acum2 = 0, 0

while True:
    
    numero = int(input("Ingrese una serie de numeros entre 1 y 999: "))
    if numero == 0:
            break
        
    if numero < 1 or numero > 999: 
            print("Valor fuera de rango")
            continue
            
    if numero <= 500:
        cont1 += 1
        acum1 += 1
        
    if numero > 500:
        cont2 += 1
        acum2 += 1


print("Numeros contados menores o igual a 500: " , cont1 , " acumulados: " , acum1)
print("Numeros contados mayores o igual a 500: " , cont2 , " acumulados: " , acum2)