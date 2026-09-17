'''
# Ejercicio 1 nombre y mayoria de edad
var_nombre = input("Por favor ingrese su nombre: ")
var_edad = int(input("Ingrese su edad: "))
if var_edad >= 18:
    print(f"{var_nombre} usted es mayor de edad.")
elif var_edad < 0.0:
    print(f"Error. Edad inválida {var_edad} Debe ser un número positivo.")
elif var_edad < 18:
    print(f"{var_nombre} usted es menor de edad, te faltan {18 - var_edad} años para ser mayor de edad.")
else:
    print(f"{var_nombre} usted es menor de edad.") 
'''
'''
# Ejercicio 2 nombre y calificación
var_nombre = input("Por favor ingrese nombre del estudiante: ")
var_calificacion = float(input("Ingrese su calificación final en una escala (0.0 a 5.0): "))

if var_calificacion > 5.0:
    print("Calificación inválida. Debe estar entre 0.0 y 5.0")
elif var_calificacion < 0.0:
    print("Calificación inválida. Debe estar entre 0.0 y 5.0")
elif var_calificacion >= 4.5:
    print(f"{var_nombre} Aprobado!tiene un desempeño excelente.")
elif var_calificacion >= 3.5:
    print(f"{var_nombre} Aprobado!tiene un desempeño bueno.")
elif var_calificacion >= 3.0:
    print(f"{var_nombre} Aprobado! tiene un desempeño aceptable.")
else:
    print(f"{var_nombre} Reprobado! tiene un desempeño insuficiente.")
'''
'''
# Ejercicio 3 nombre valor de compra y descuento
var_nombre = input("Nombre del cliente: ")
var_valor_compra = float(input("Valor de la compra: "))

if var_valor_compra <= 0:
    print(f"{var_valor_compra} error es un valor inválido.")
elif var_valor_compra > 100000 and var_valor_compra <= 299999:
    var_descuento1 = 0.1
    var_valor_final = var_valor_compra - (var_valor_compra * var_descuento1)
    print(f"{var_valor_compra} tiene un descuento del 10%. Total a Pagar: ${var_valor_final:.0f}")
elif var_valor_compra >= 300000 and var_valor_compra <= 499999:
    var_descuento2 = 0.15
    var_valor_final = var_valor_compra - (var_valor_compra * var_descuento2)
    print(f"{var_valor_compra} tiene un descuento del 15%. Total a Pagar: ${var_valor_final:.0f}")
elif var_valor_compra >= 500000:
    var_descuento3 = 0.2
    var_valor_final = var_valor_compra - (var_valor_compra * var_descuento3)
    print(f"{var_valor_compra} tiene un descuento del 20%. Total a Pagar: ${var_valor_final:.0f}")
else:
    print(f"{var_valor_compra} no aplica para un descuento. Total a Pagar: ${var_valor_compra:.2f}")
'''
'''
# Ejercicio 4: temperatura

var_ciudad = input("Ingrese nombre de Ciudad: ")
var_temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

if var_temperatura < 10:
    print(f"{var_ciudad} Temperatura MUY FRIA {var_temperatura}°C, recomendamos abrigarse bien.")
elif var_temperatura  < 17:
    print(f"{var_ciudad} Temperatura FRIA {var_temperatura}°C, recomendamos abrigarse.")
elif var_temperatura  < 25:
    print(f"{var_ciudad} Temperatura TEMPLADA,{var_temperatura}°C")
elif var_temperatura  < 32:
    print(f"{var_ciudad} Temperatura CALIENTE {var_temperatura}°C")
else:
    print(f"{var_ciudad} Temperatura MUY CALIENTE {var_temperatura}°C")
'''

# Ejercicio 5: empleado y salario

var_nombre = input("Ingrese nombre del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))

salario = valor_hora * horas_trabajadas
var_seguridad = salario * 0.08 


if horas_trabajadas < 0 or valor_hora < 0:
    print("Error: Las horas trabajadas y el valor por hora deben ser números positivos.")

elif horas_trabajadas <= 160:

    salario_neto = salario - var_seguridad
    print(f""" === RESUMEN DE PAGO SALARIO ===
    -Salario: {salario} 
    -Seguridad social {var_seguridad} 
    -Salario neto es: {salario_neto}
    """)

elif horas_trabajadas > 160:

    horas_extras = horas_trabajadas - 160
    valor_horas_extras= (horas_extras* valor_hora )* 1.25
    salario_neto = (valor_hora * horas_trabajadas) + valor_horas_extras - var_seguridad

    print (f""" == RESUMEN DE PAGO SALARIO ==
    -Horas extras {horas_extras} Valor Horas Extras {valor_horas_extras}
    -Salario basico: {salario}
    -seguridad social {var_seguridad} 
    -salario total {salario_neto} 

""")