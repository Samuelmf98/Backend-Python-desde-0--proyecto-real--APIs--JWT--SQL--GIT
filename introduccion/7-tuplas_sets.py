"""Una tupla no puede modificarse, 
se tienen que convertir a listas y luego de nuevo a tuplas
"""

tupla = (100, "hello", ["nombre", "edad", {"hello": "hello"}])

#tupla[0] = 200  #Esto da error, porque no se puede modificar

tupla = list(tupla) #pasarla a lista
tupla[0] = 200  #Realizar modificaciones
tupla = tuple(tupla) #volver a convertir en tupla

print(tupla)

lista_modificar = tupla[2] #Creamos una lista y accedemos al elemento 2 de la tupla
lista_modificar[0] = "name" #dentro de ["nombre", "edad", {"hello": "hello"}] accedemos al primero
print(lista_modificar)
print(tupla)

lista_modificar1 = tupla[2][2] #Cambiar el valor del dicconario que esta en la posicion 2 de la tupla y a su vez en la posicion 2 tambien
lista_modificar1["hello"] = "hola"

print(tupla)


my_set = {20, 21, 21, 21, 21, 21, 22, 22,22, 22} #como diccionario pero sin tener clave valor. Si hay repetidos los trata como uno solo.
print(my_set) #La salida es solo 20, 21, 22

#Eliminar duplicados de una lista con set
list_set = [20, 21, 21, 21, 21, 21, 22, 22,22, 22]

list_set = set(list_set)

list_set =list(list_set)
print(f"Mi lista final es: {list_set}") #La salida es solo 20, 21, 22