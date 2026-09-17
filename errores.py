'''try:
    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado es: {numero}")

except ValueError:
    print("Error debe ingresar un número válido: ") 

    '''
'''
#Ciclo infinito
while True:
    print("Hola Mundo ")

'''
'''
#ciclo condicion

edad=18
while edad >=18:

    try:
        edad = int(input("Ingrese su edad: "))
        print(f"Su edad es: {edad}")
    except ValueError:
        print("\nIngresar una edad válida:\n")    
print("\nMenor de edad saliendo del sistema\n")    
'''

'''
# Ejercicio 1: try / except básico
# Sin manejo de errores, ingresar "hola" en lugar de un número
# provocaría un ValueError y el programa se detendría.

try:
    numero = int(input("Ingrese un número entero: "))
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("Error: debe ingresar un número entero válido.")
    '''

'''
# Ejercicio 2: División segura con ZeroDivisionError
try:
    dividendo = float(input("Ingrese el dividendo: "))
    divisor   = float(input("Ingrese el divisor: "))
    resultado = dividendo / divisor
    print(f"Resultado: {dividendo} / {divisor} = {resultado}")
except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: ingrese únicamente valores numéricos.")
    '''
'''
# Ejercicio 3: else y finally
# else  → se ejecuta solo si NO ocurrió ninguna excepción
# finally → se ejecuta SIEMPRE, con o sin error

try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: la edad debe ser un número entero.")
else:
    if edad >= 18:
        print("Acceso permitido.")
    else:
        print("Acceso denegado: debe ser mayor de edad.")
finally:
    print("Verificación finalizada.")
    '''

'''
# Ejercicio 4: Solicitar un dato válido hasta que el usuario lo ingrese correctamente
while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        break   # sale del ciclo si el valor es válido
    except ValueError as e:
        print(f"Entrada inválida: {e}. Intente de nuevo.")

print(f"Nota registrada: {nota}")
'''

'''
# Ejercicio 5: raise — lanzar una excepción personalizada
def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)

try:
    n      = int(input("¿Cuántas notas va a ingresar? "))
    notas  = []
    for i in range(n):
        nota = float(input(f"  Nota {i + 1}: "))
        notas.append(nota)                          #lista de notas
    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error: {e}")
'''
'''
 #Solicitar al usuario dos numeros y un operador matematico
try:
    num1 = float(input("\nIngrese el primer número: "))
    num2 = float(input("\nIngrese el segundo número: "))
    operador = input("\nIngrese un operador (+, -, *, /): ")

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        resultado = num1 / num2
    else:
        raise ValueError("Operador inválido. Use +, -, *, o /.")

    print(f"\nTu Resultado es: {num1} {operador} {num2} = {resultado}\n")
except ValueError:
    print("Error: debe ingresar datos válidos.")
    while True:
            try:
                num1 = float(input("\nIngrese el primer número: "))
                num2 = float(input("\nIngrese el segundo número: "))
                operador = input("\nIngrese un operador (+, -, *, /): ")

                if operador == "+":
                    resultado = num1 + num2
                elif operador == "-":
                    resultado = num1 - num2
                elif operador == "*":
                    resultado = num1 * num2
                elif operador == "/":
                    if num2 == 0:
                        raise ZeroDivisionError("No se puede dividir entre cero.")
                    resultado = num1 / num2
                else:
                    raise ValueError("Operador inválido. Use +, -, *, o /.")

                print(f"Resultado: {num1} {operador} {num2} = {resultado}")
                break  # Salir del ciclo si todo es válido
            except ValueError:
                print("Error datos no válidos: ")
                '''
