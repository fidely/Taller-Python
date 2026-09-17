#ciclos Repetitivos

#ciclo For = Repite por cantidad de veces
for i in range(10):  #no puede haber espacios entre range y el parentesis
    print(f"  {i} - Hola Mundo ") # i es una variable 

#configurar el rango de inicio y fin
for i in range(1, 11): #inicio en 5 y finaliza en 10
    print(f"  {i} - Hola Mundo ")

#ciclo While = Repite intervalos de tiempo
for i in range(2,12,2): #inicio en 0 y finaliza en 10 con incremento de 2
    print(f"  {i} - Hola Mundo ")

# de 5 a 100 con incremento de 5
for i in range(0, 101, 5):
    print(f"  {i} - Hola Mundo ")

#Ejecicio 1: adivina el numero secreto:

import random
import re

numero_secreto = random.randint(1,10)
intentos = 3

for i in range(intentos): #tienes tres intentos
    numero = int(input("\n Adivina el número secreto (entre 1 y 10): "))
    
    if numero == numero_secreto:
        print("\n ¡Felicidades! Adivinaste el número secreto. \n")
        break
    else:
        intentos_restantes = intentos - (i+1) 
        print(f"\n X Número incorrecto. Te quedan {intentos_restantes} intentos.\n ")
        if intentos_restantes == 0:
            print(f"el numero secreto era: {numero_secreto} ")

# Ejercicio 1: Mostrar la tabla de multiplicar de un número
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):          # recorre los valores del 1 al 10
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 2: Sumar los primeros n números naturales
n = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma = suma + i

print(f"La suma de los primeros {n} números naturales es: {suma}")