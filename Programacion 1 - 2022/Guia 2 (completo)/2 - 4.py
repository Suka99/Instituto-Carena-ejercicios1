print("\n================================")
print("Programa 1: Mayor de 2 numeros")
print("================================")

a = int(input("ingrese el valor para A: "))
b = int(input("ingrese el valor para B: "))
c = int(input("ingrese el valor para C: "))

if a == b and a == c:
    print("Los valores son iguales")
elif a > b and a > c:
    print("A =",a,"es mayor a B =",b ,"y C =",c)
elif b > a and b > c:
    print("B =",b,"es mayor al A =",a,"y C =",c)
else:
    print("C =",c,"es mayor al a =",a, "y B =",b)
    
print("\n Fin del programa")