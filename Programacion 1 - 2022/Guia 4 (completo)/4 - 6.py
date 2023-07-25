# 6. Realizar un algoritmo que:
# a. Permite ingresar una serie de números enteros entre 100 y 500 inclusivos.
acum = cont = 0



while True:
    ingreso = int(input("Ingrese numeroos entre 100 y 500: "))
    # e. Salir con -1        
    if ingreso == -1:
        break
    
    if ingreso < 100 or ingreso > 500:
        print("Fuera de rango")
        continue
        
    acum += ingreso
    cont += 1
        

# b. Acumular los valores.
# c. Contar los valores.
# d. Sacar el promedio de los valores.
promedio = acum / cont

print("EL promedio es: " , promedio)
