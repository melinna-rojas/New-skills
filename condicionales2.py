#coding utf-8
#Verficar numeros primos
num1 = int(raw_input("Escriba el numero a verificar: "))
flag = False
divisor = 1
for i in range(2,num1):
    if(num1%i)==0:
        flag = True
    else:
        flag = False

if(flag):
    print("El numero es primo")
else:
    print("El numero NO es primo")
