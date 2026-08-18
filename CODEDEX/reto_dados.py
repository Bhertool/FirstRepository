#Crea un juego donde uno adivine el valor total después de tirar un par de dados una vez.
import random

dice1 = random.randint(1, 6)#dado 1
dice2 = random.randint(1, 6)#dado 2
total = dice1 + dice2 #suma de los dados
answer = ""

while total != answer: #mientras la suma de los dados no sea igual a la respuesta
    answer = int(input("¿Cuál es el total de los dados? "))
    if answer == total:
        print("¡Correcto!")
    else:
        print("Incorrecto. Intenta de nuevo.")