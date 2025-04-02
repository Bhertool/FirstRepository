#Generar la serie para n numeros, matris que dibuja una piramide
n = int(input("ingrese n impar: "))

f = 0
izq = 0
der = 0
k = 1

for i in range(1,n+1):
    if i % 2 == 1:
        f = f + 1
        izq=f
        der=f

if n % 2 == 1:
    for l in range(1,f+1):
        k = 1
        for c in range(1,n+1):
            if c < izq:
                print(" ",end="")
            else:
                if c > der:
                    print(" ", end="")
                else:
                    print(k,end="")
                    if c < f:
                        k = k+1
                    else:
                        k = k-1

        print()
        izq=izq-1
        der=der+1
else:
    print("n deve ser impar")
        
