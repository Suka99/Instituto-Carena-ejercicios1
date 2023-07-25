 #Desarrollar un algoritmo para permitir el ingreso de una serie de números enteros, hasta que el usuario ingrese el número 0, determinar cuál es el mayor.
#a. Muestre un mensaje de presentación.
#b. Iniciar una variable mayor en cero para obtener el mayor propiamente.
#c. Hacer un bucle while que permita ingresar una serie de números enteros.
#d. Dentro del bucle solicitar el ingreso de un valor entero para a.
#e. Verificar si el número ingresado es cero para encontrar la salida de bucle con break.
#f. Verificar si a es mayor que mayor y copiar a en mayor si es verdadero.
#g. Por la línea siguiente fuera del bucle mostrar un mensaje y el mayor.
print("\n================================================")
print("Programa 5 de la guia 2")
print("================================================")


mayor = 0

while True:
    a = int(input("Ingrese numero entero para a: "))
    if a == 0:
        break
    if a > mayor:
        mayor = a
        
print("El numero mayor es: ",mayor)
