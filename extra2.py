#coding utf-8
#lista = [1,2,3,4,5,6,7]
cantidad = int(raw_input("Cuantos datos tendra tu lista: "))
lista = []
for m in range(0,cantidad):
    lista[m]=int(raw_input("Digite numero: "))

suma = 0
contador = 0
for i in lista:
    suma = suma+i
    contador = contador+1

promedio = suma /contador
print(promedio)
