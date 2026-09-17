
nombre = "Fidely"
documento = "5251327"
direccion = "Medellin"
tiene_deudas= True

print(nombre)
print("concatenacion usando +")
print("=" *30)

print("Mi nombre es: "+ nombre + " y mi documento es:" +  str(documento))

print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

print(f"Mi nombre es: {nombre} y mi documento es: {documento}") #forma facil de concatenar variables y texto

print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)

print(f"""
    Nombre:         {nombre}
    Documento:      {documento}
    Dirección:      {direccion}
    ¿Tiene deudas?: {tiene_deudas}
""")

print("=" * 30)

print(f"""
Nombre:         {nombre}
Documento:      {documento}
Dirección:      {direccion}
¿Tiene deudas?: {tiene_deudas}
""")

print(f"\n Hola, {nombre}!")

print(f"Bienvenida {nombre} a Python.\n")