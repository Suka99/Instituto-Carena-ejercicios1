temperatura_alta = []
temperatura_baja = []
while True:
    Ingresar = int(input("Ingrese la temperatura: "))
    
    if Ingresar == 60:
        print("Se murio")
        break
    if  60 < Ingresar or Ingresar <-25:
        print("Temperatura no valida")
        continue
    
    if 0< Ingresar < 30:
        temperatura_alta.append(Ingresar)
    if 0> Ingresar >-25:
        temperatura_baja.append(Ingresar)
        
print(f"Temperatura Alta: {temperatura_alta} Temperatura Baja: {temperatura_baja}")

def Promedio(lista):
    suma=sum(lista)
    promedio= suma / len(lista)
    return promedio

def promedio2(lista):
    acum=0
    cont=len(lista)
    for x in lista:
        acum+=x
    promedio=acum/cont
    return promedio

print(Promedio(temperatura_alta))
print(Promedio(temperatura_baja))