#Este codigo dibuja un corazón con asteriscos (*) en la consola.
#Nos basamos en la idea de dibujar dos pirámides y una pirámide invertida.
n = int(input("ingrese el valor de (n) numero positivo impar mayor a 15 para dibujar un corazón: "))

f = 0
izq = 1
der = n-2
k = n // 2
izqu = k // 2
dere = k // 2

for i in range(1,n+1):
    if i % 2 == 1:
        f = f + 1


print()
if n % 2 == 1: #Verificacion para que n siempre sea impar y mayor a 15.
    if  n > 15:
        #Parte superior de la figura.
        #Dos pirámides seguidas
        for i in range(1,k//2+1):
            for c in range(1,k+1):
                if c < izqu:
                    print(" ",end="")
                else:
                    if c > dere:
                        print(" ", end="")
                    else:
                        print("*",end="")
            print(" ",end="")  # Espacio entre pirámides
            for c in range(1,k+1):
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
#Pirámide invertida, parte inferior de la figura .
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
        print("(n) deve ser positivo mayo a 15.")
else:
    print("(n) deve ser impar.")

#Punto clave para entender y mover las figuras son los espacios en blanco.
#por ejemplo, " " y " " caombian todo, al igual que "*" y " *", le da un cambio total a la orientación

#triangulo hacia la izquierda
limit = 1
for i in range(1,25):
    for j in range(1,25):
        if limit < j:
            print(" ", end="")
        else:
            print("* ", end="")
    limit += 1
    print()

#Piramide invertida.
print("\n")
limit = 1
for i in range(1,25):
    for j in range(1,25):
        if limit < j:
            print("* ", end="")
        else:
            print(" ", end="")
    limit += 1
    print()

#Triangulo hacia la izquierda invertido.
print("\n")
limit = 24
for i in range(1,25):
    for j in range(1,25):
        if limit < j:
            print(" ", end="")
        else:
            print("* ", end="")
    limit -= 1
    print()

#Piramide.
print("\n")
limit = 24
for i in range(1,25):
    for j in range(1,25):
        if limit < j:
            print("* ", end="")
        else:
            print(" ", end="")
    limit -= 1
    print()

#Diamante o Rombo.
print("\n")
limit = 24
for i in range(1,25):
    for j in range(1,25):
        if limit < j:
            print("* ", end="")
        else:
            print(" ", end="")
    limit -= 1
    print()
limit = 1
for i in range(1,25):
    for j in range(1,25):
        if limit < j:
            print("* ", end="")
        else:
            print(" ", end="")
    limit += 1
    print()

#Triangulo hacia la derecha.
print("\n")
limit = 24
for i in range(1,25):
    for j in range(1,25):
        if limit > j:
            print("  ", end="")
        else:
            print(" *", end="")
    limit -= 1
    print()

#Triangulo hacia la derecha invertido.
print("\n")
limit = 1
for i in range(1,25):
    for j in range(1,25):
        if limit < j:
            print(" *", end="")
        else:
            print("  ", end="")
    limit += 1
    print()

#Generar la serie para n numeros impares, matris que dibuja un rombo con el centro vacio.
n = int(input("ingrese el valor de (n) numero entero positivo impar para dibujar un rombo vacio: "))

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
if n % 2 == 1:
    if  n > 0:
        for l in range(1,f+1):
            for c in range(1,n+1):
                if c < izqu:
                    print(" ",end="")
                else:
                    if c > dere:
                        print(" ", end="")
                    else:
                        if c == izqu:
                            print("*",end="")
                        else:
                            if c == dere:
                                print("*",end="")
                            else:
                                print(" ",end="")
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
                        if c == izq:
                            print("*",end="")
                        else:
                            if c == der:
                                print("*",end="")
                            else:
                                print(" ",end="")
            print()
            izq=izq+1
            der=der-1
    else:
        print("(n) deve ser positivo.")
else:
    print("(n) deve ser impar.")


#Este codigo dibuja la silueta de un corazón con asteriscos (*) en la consola.
n = int(input("ingrese el valor de (n) numero positivo impar mayor a 15 para dibujar un corazón: "))

f = 0
izq = 1
der = n-2
k = n // 2
izqu = k // 2
dere = k // 2
for i in range(1,n+1):
    if i % 2 == 1:
        f = f + 1


print()
if n % 2 == 1:
    if  n > 15:
        #Parte superior de la figura.
        #Dos pirámides seguidas
        for i in range(1,k//2+1):
            for c in range(1,k+1):
                if c < izqu:
                    print(" ",end="")
                else:
                    if c > dere:
                        print(" ", end="")
                    else:
                        if c == izqu:
                            print("*",end="")
                        else:
                            if c == dere:
                                print("*",end="")
                            else:
                                print(" ",end="")
            print(" ",end="")  # Espacio entre pirámides
            for c in range(1,k+1):
                if c < izqu:
                    print(" ",end="")
                else:
                    if c > dere:
                        print(" ", end="")
                    else:
                        if c == izqu:
                            print("*",end="")
                        else:
                            if c == dere:
                                print("*",end="")
                            else:
                                print(" ",end="")
            print()
            izqu=izqu-1
            dere=dere+1
#Pirámide invertida, parte inferior de la figura .
        for l in range(1,f+1):
            for c in range(1,n+1):
                if c < izq:
                    print(" ",end="")
                else:
                    if c > der:
                        print(" ", end="")
                    else:
                        if c == izq:
                            print("*",end="")
                        else:
                            if c == der:
                                print("*",end="")
                            else:
                                print(" ",end="")
            print()
            izq=izq+1
            der=der-1
    else:
        print("(n) deve ser positivo mayo a 15.")
else:
    print("(n) deve ser impar.")
