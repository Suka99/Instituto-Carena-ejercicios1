cont1, cont2, cont3 = 0, 0, 0
# 1. Realizar un algoritmo para ingresar una serie de temperaturas decimales entre -20 y 50.
while True:
    tempetatura = float(input("Ingrese temperatura: "))
# 2. Salir con 100.
    if tempetatura == 100:
        break
# 3. Validar que los valores están entre -20 y 50.
    if tempetatura < -20 or tempetatura > 50:
        print("Tempetatura fuera de rango")
        continue
# 4. Contar y sacar el promedio de los valores bajo cero.
    if tempetatura > 0:
        cont1 += 1
        promedio1 = tempetatura / cont1
# 5. Contar y sacar el promedio de los valores sobre cero.
    if tempetatura < 0:
        cont2 += 1
        promedio2 = tempetatura / cont2
# 6. Contar cuántos valores ingresados son iguales a cero.
    if tempetatura == 0:
        cont3 += 1
# 7. Mostrar resultados.
print("Valores contados bajo 0: ", cont1, "Promedio: ", promedio1)
print("Valores contados sobre 0: ", cont2, "Promedio: ", promedio2)
print("Valores igual a 0: ", cont3)