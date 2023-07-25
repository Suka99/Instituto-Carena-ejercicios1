print("\n================================")
print("Programa 2: Mayor de 2 numeros o igual")
print("================================")

a = int(input("ingrese el valor para A: "))
b = int(input("ingrese el valor para B: "))

if a == b:
    print("Los numeros son iguales: \n",a,"es igual a", b)
elif a > b:
    print("A =",a,"es mayor a B =",b)
else:
    print("B =",b,"es mayor al A =",a)
    
print("\n Fin del programa")