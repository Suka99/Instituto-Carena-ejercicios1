print("Guia 4 - Ejercicio 1")
print()
cont1, cont2 = 0, 0

# 2. De un grupo de n notas de calificación de alumnos ingresadas por teclado:
while True:
    calificacion = int(input("Ingrese de un grupo de n notas de calificación"))
# a. Salir con -1.
    if calificacion == -1:
        break
# b. Ingresar valores enteros entre 1 y 10.
    if calificacion < 1 or calificacion > 10:
        print("Sea serio compa")
# b. Contar cuantas notas son menores a 7.
    if calificacion < 7:
        cont1 += 1
#c. Sacar el promedio de notas menores a 7
        promedio1 = calificacion / cont1

# d. Contar cuantas notas son mayores o iguales a 7
    if calificacion > 7:
        cont2 += 1
# e. Sacar el promedio de notas mayores o iguales a 7.
        promedio2 = calificacion / cont2

# f. Mostrar los resultados de la cantidad de notas y los promedios.
print("Cantidad de notas menores a 7: " , cont1 , "Promedio de nota: " , promedio1)
print("Cantidad de notas mayores a 7: " , cont2 , "Promedio de nota: " , promedio2)