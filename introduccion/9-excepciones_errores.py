#errores excepciones




try:
    menu = int(input("Ingrese una opcion valida: "))
    print(f"Ha ingresado la opcion {menu}")

   
except ValueError as error:
    print(f"{menu} no es una opcion valida, error: {error}")