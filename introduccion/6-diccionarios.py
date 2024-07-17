my_dict = {"nombre": "samuel", #claves y valores
           "edad": 26,
           "sexo": "femenino"}


print(my_dict["nombre"]) #Acceder al valor de una clave
print(my_dict["edad"])

my_dict["sexo"] = "masculino" #Modificamos el valor de una clave

print(my_dict["sexo"]) #Comprobamos el cambio 

my_dict["peso"] = 72.1 #añadimos un nuevo valor

print(my_dict) #comprobamos

my_dict.pop("nombre")  #Eliminamos un elemento
print(my_dict)

temp_dict = {}
for clave, valor in list(my_dict.items()):
    if clave == "sexo":
        temp_dict["nombre"] = "samuel" #Le meto el valor en la posicion inicial
    temp_dict[clave] = valor #Le meto los valores de mi my_dict
my_dict = temp_dict #Le asigno los valores a my_dict

print(f"Mi diccionario final es: {my_dict}")

print(my_dict["edad"] + 1) #operaciones (27)


for clave in my_dict:
    print(my_dict[clave]) #Para mostrar todos los valores de las claves

for clave, valor in my_dict.items(): #Para mostrar claves y valores
    print(clave, valor)