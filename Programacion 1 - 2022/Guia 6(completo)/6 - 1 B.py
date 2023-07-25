import random

def minmax(lista, nombre):
    minimo = min(lista)
    maximo = max(lista)
    posmin = lista.index(minimo)
    posmax = lista.index(maximo)
    
    print(nombre, "Valor minimo: ",minimo ,"Posicion: ",posmin)
    print(nombre, "Valor maximo: ",maximo ,"Posicion: ",posmax)
    
V1 = random.sample(range(10,99),20)
V2 = []
V3 = []



for numero in V1:
    if numero % 2 == 0:
        V2.append(numero)
    else:
        V3.append(numero)
        
print("Lista V1" , V1)
print("Lista V2" , V2)
print("Lista V3" , V3)
print()

#Pone primero el llamado(lista), despues el (nombre) sino a la hora de ejecutar no queda claro en la terminal
minmax(V2,"V2")
minmax(V3,"V3")