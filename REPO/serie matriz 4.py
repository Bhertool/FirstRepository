#Generar la serie para n numeros impares, matris que dibuja una piramide invertida
n = int(input("ingrese n impar: "))

f = 0
izq = 1
der = n

for i in range(1,n+1):
    if i % 2 == 1:
        f = f + 1

if n % 2 == 1:
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
    print("n deve ser impar")
        
