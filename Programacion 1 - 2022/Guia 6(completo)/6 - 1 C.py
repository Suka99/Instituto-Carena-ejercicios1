import random

V1 = random.sample(range(10,99),20)
V2 = [numero for numero in V1 if numero % 2 == 0]
V3 = [numero for numero in V1 if numero % 2 != 0]

print("Lista V1", V1)
print("Lista V2", V2)
print("Lista V3", V3)
print()
minimo = min(V2)
maximo = max(V2)
minpos = V2.index(minimo)
maxpos = V2.index(maximo)

print("Lista V2")
print("Minimo: ", minimo,"Posicion: ", minpos)
print("Maximo: ", maximo,"Posicion: ", maxpos)

minimo = min(V3)
maximo = max(V3)
minpos = V3.index(minimo)
maxpos = V3.index(maximo)

print()
print("Lista V3")
print("Minimo: ", minimo,"Posicion: ", minpos)
print("Maximo: ", maximo,"Posicion: ", maxpos)
