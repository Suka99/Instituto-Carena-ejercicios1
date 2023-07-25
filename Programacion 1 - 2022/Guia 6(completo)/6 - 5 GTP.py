# Paso 1: Permitir el ingreso de nombres
nombres = []
nombre = input("Ingrese un nombre (Presione Enter para salir): ")

# Paso 2: Salir con Enter
while nombre != "":
    nombres.append(nombre)
    nombre = input("Ingrese un nombre (Presione Enter para salir): ")

# Paso 3: Ordenar alfabéticamente sin utilizar sort
n = len(nombres)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if nombres[j] > nombres[j + 1]:
            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

# Paso 4: Mostrar todos los elementos
print("Nombres ordenados alfabéticamente:")
for nombre in nombres:
    print(nombre)
