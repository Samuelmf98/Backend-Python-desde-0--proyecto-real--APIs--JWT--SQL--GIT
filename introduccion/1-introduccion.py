# Imprimir datos
print("Hello World")

#Variables
nombre = "Samuel"
edad = 26
peso = 72.1

#Forma 1
print("nombre es de tipo {}, edad es de tipo {} y peso es de tipo {}".format(type(nombre), type(edad), type(peso)))

#Forma 2
print(f"nombre es de tipo {type(nombre)}, edad es de tipo {type(edad)} y peso es de tipo {type(peso)}")

language = "python"

language_slice = language[1:3] #yt
print(language_slice)

language_slice = language[2:6] #thon
print(language_slice)

language_slice = language[1:] #ython
print(language_slice)

language_slice = language[:-2] #pyth
print(language_slice)

language_slice = language[::-1] #nohtyp
print(language_slice)

language_slice = language[0:6:2] #pto
'''primero coge todo del 0 al 6, es decir, python
Luego coge los valores cada 2 posiciones, es decir, p t o
'''
print(language_slice)

