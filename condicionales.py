"""
#solicitar el nombre de usuario
var_nombre = input("Ingrese su nombre: ")

#Solicitar edad del usuario.
var_edad =int(input("Ingrese su edad: "))

#Condicional para determinar si el usuario es mayor de edad o no.
if var_edad >= 18:
    print(f"{var_nombre} usted es mayor de edad.")
else:
    print(f"{var_nombre} usted es menor de edad.")
    """
""""
# Ejercicio 1: número positivo, negativo o cero
input("\n EJERCICIO 1: NÚMERO POSITIVO, NEGATIVO O CERO") 
numero = float(input("\n Por favor Ingrese un número: "))

if numero > 0:
    print(f"{numero} es un número positivo")
elif numero < 0:
    print(f"{numero} es un número negativo")
else:
    print("El número es cero")

# Ejercicio 2: Verificar si es mayor o menor de edad
input("\n EJERCICIO 2: VERIFICAR SI ES MAYOR O MENOR DE EDAD \n")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Ejercicio 3: número par o impar
input("\nEJERCICIO 3: NÚMERO PAR O IMPAR \n")
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:      # si el residuo es 0 → es par
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

    """
"""
# Ejercicio 4: nota académica
input("\n EJERCICIO 4: CLASIFICAR UNA NOTA ACADEMICA \n")
nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))

if nota > 5.0:
    print("Nota inválida. Debe estar entre 0.0 y 5.0")
elif nota >= 4.5:
    print("Desempeño superior")
elif nota >= 3.5:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
elif nota < 0.0:
    print("Nota inválida. Debe estar entre 0.0 y 5.0")
else:
    print("Desempeño bajo")
    """

'''
# Ejercicio 5: Determinar el mayor de tres números
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

print(f"El mayor de los tres números es: {mayor}")
'''