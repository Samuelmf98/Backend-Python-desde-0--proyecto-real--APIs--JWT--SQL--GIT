"""
Hacer un programa que le pida al usuario que ingrese su edad y su sexo,
si el usuario es mayor de edad y ademas es menor de 65 años le debe permitir
al usuario quedarse en el programa, en caso
contrario el programa debe deternese. Si es sexo es masculino que el programa
salude al usuario como un caballero y si el sexo es femino que el programa salude al
usuario como una dama
-Para que el usuario ingrese su sexo hacer un menu con condiciones.
"""

edad = int(input("Introduce tu edad: "))
sexo = str(input("""Introduce tu sexo: 
[1] Para hombre
[2] Para mujer
>>>"""))

if edad >= 18 and edad <=65:
    if sexo == str(1):
        print(f"Buenas tardes señor de {edad} años")
    elif sexo == str(2):
        print(f"Buenas tardes señora de {edad} años")
    else:
       
        print("No se ha identificado el sexo. \nPor favor, introduce un numero valido.")
        exit()
else:
    print("No puedes quedarte en el programa.\nTienes que tener entre 18 y 65 años")
    exit()