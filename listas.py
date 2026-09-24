#listas

lista_nombres =[]

while True:
    variable_nombre = input("Ingrese un nombre: ")   
    if variable_nombre != "salir":
        lista_nombres.append(variable_nombre)   
    if variable_nombre == "salir":
      print("Nombres Guardados: ")
      print(lista_nombres)
      break


nombre =input("Ingrese nombre: ")
print(f"nombre en Mayuscula {nombre.upper()}")
print(f"Nombre en Minuscula {nombre.lower()}")

if nombre.lower()=='fide':
    print("Hola Fide")
else:
    print("Tu no eres Fide")
    

lista_perros =[]
lista_gatos =[]

while True:
    try:
        pregunta =int(input("""
        Seleccion Opcion:
        1: Registrar Perros
        2: Registar Gatos
        3: Mostrar Listado de Perros
        4: Mostrar Listado Gatos
        5: Salir
        
        """))
        #Validadr opcion
        if pregunta ==1:
            perro=input("\nCual es el nombre del perro: ")
            lista_perros.append(perro)

        elif pregunta ==2:
            gato=input("\nCual es el nombre del gato: ")
            lista_gatos.append(gato)

        elif pregunta ==3:
            print("\nLista de perros: ")   
            print(lista_perros)

        elif pregunta ==4:
            print("\nLista de Gatos: ")
            print(lista_gatos)

        elif pregunta ==5:
            print("\nSaliendo del Sistema")
            break
        else:
            print("\nOpcion Invalida")

    except ValueError:
        print("Ingrese una opcion valida")
    