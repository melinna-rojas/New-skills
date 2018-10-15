#coding utf-8
#FACTORIAL DE UN numero
n = int(raw_input("Escriba n : "))
producto = 1
for fact in range(1,n+1):
    producto = producto * fact

print producto
