print("Guia 4 - Ejercicio 1")
print()
cont1, cont2, cont3 = 0, 0, 0

# 1. Realizar un algoritmo para ingresar una serie de temperaturas decimales entre -20 y 50.
while True:
    temperatura = float(input("Ingrese temperatura: "))
# a. Salir con 100.
    if temperatura == 100:
        break
# b. Validar que los valores estén entre -20 y 50.
    if temperatura < -20 or temperatura > 50:
        print("Moriste crack")
        continue
# c. Contar y sacar el promedio de los valores bajo cero.
    if temperatura < 0:
        cont1 += 1
        prom1 = temperatura / cont1
# d. Contar y sacar el promedio de los valores sobre cero.
    if temperatura > 0:
        cont2 += 1
        prom2 = temperatura / cont2
# e. Contar cuántos valores ingresados son iguales a cero.
    if temperatura == 0:
        cont3 += 1
# f. Mostrar resultados.
print("Valores contados: " , cont1, "Promedio de los valores bajo cero: " , prom1)
print("Valores contados: " , cont2, "Promedio de los valores sobre cero: " , prom2)
print("Valores contados iguales a cero: " , cont3)