#Generar la serie para n numeros impares, matris que dibuja una piramide invertida
n = int(input("ingrese el valor de n numero positivo impar: "))

f = 0
izq = 2
der = n-1
izqu = 0
dere = 0

for i in range(1,n+1):
    if i % 2 == 1:
        f = f + 1
        izqu = f
        dere = f
print()
if n % 2 == 1 and n > 0:
    for l in range(1,f+1):
        for c in range(1,n+1):
            if c < izqu:
                print(" ",end="")
            else:
                if c > dere:
                    print(" ", end="")
                else:
                    print("*",end="")
        print()
        izqu=izqu-1
        dere=dere+1

    for l in range(1,f+1):
        for c in range(1,n+1):
            if c < izq:
                print(" ",end="")
            else:
                if c > der:
                    print(" ", end="")
                else:
                    print("*",end="")
        print()
        izq=izq+1
        der=der-1
else:
    print("n deve ser impar y positivo")
        
