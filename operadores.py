
# ============================================================
# OPERADORES ARITMÉTICOS EN PYTHON
# ============================================================
numero1 = 20
numero2 = 4

suma           = numero1 + numero2   
resta          = numero1 - numero2   
multiplicacion = numero1 * numero2   
division       = numero1 / numero2   
division_entera= numero1 // numero2  
residuo        = numero1 % numero2   
potencia       = numero1 ** numero2  

print(f"""
Resultado de Operaciones Aritméticas:
suma:            {numero1} +  {numero2} = {suma}
resta:           {numero1} -  {numero2} = {resta}
multiplicacion:  {numero1} *  {numero2} = {multiplicacion}
division:        {numero1} /  {numero2} = {division:.4f}  
division_entera: {numero1} // {numero2} = {division_entera}
residuo:         {numero1} %  {numero2} = {residuo}
potencia:        {numero1} ** {numero2} = {potencia}
""")


# Ejercicio 1: Suma de dos números
print("\n SUMA DE NÚMERO")
print("*"*20)
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2   # Se calcula la suma

print(f"La suma es: {suma}")


# Ejercicio 2: Área de un rectángulo
print("\nEJERCICIO 2: ÁREA DE UN RECTÁNGULO")
print("*"*20)
base   = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

area = base * altura   # fórmula: base × altura

print(f"El área del rectángulo es: {area}")

# Ejercicio 3: Conversión de minutos a horas y minutos
print("\nEJERCICIO 3: CONVERSION MINUTOS ")
print("*"*20)
minutos_totales = int(input("Ingrese la cantidad de minutos: "))

horas   = minutos_totales // 60   # división entera → horas completas
minutos = minutos_totales % 60    # módulo → minutos restantes

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")

# Ejercicio 4: Cálculo del precio con descuento
print("\nEJERCICIO 4: PRECIO CON DESCUENTO")
print("*"*20)
precio    = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento / 100)   # valor que se descuenta
precio_final    = precio - valor_descuento      # precio con descuento

print(f"El precio final a pagar es: {precio_final}")

# Ejercicio 5: Intercambio de valores entre dos variables
print("\nEJERCICIO 5: INTERCAMBIO DE VALORES")
print("*"*20)
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

auxiliar = a   # guardar temporalmente el valor de a
a = b          # a toma el valor de b
b = auxiliar   # b toma el valor original de a

print(f"Después del intercambio: a = {a} , b = {b}")
