lista_vacia = []

lista_nombres = ["samuel", "guillermo", "pablo"]
print(lista_nombres)

lista_nombres.remove("samuel") #elimina el elemento introducido. Sino el primero.
print(lista_nombres)

lista_nombres.append("samuel") #añade un elememto introducido al final de la lista
print(lista_nombres)

lista_numeros = [26, 25, 24]
print(lista_numeros)

lista_numeros.pop() #elimina el ultimo elemento
print(lista_numeros)

lista_numeros.append(24)

print(len(lista_numeros)) #tamaño lista

print(lista_nombres[1]) #accede al elemento del indice 1

lista_nombres.pop() #eliminamos samuel que se encuentra al final
print(lista_nombres)

lista_nombres.insert(0, "samuel") #añade un elemento en un lugar en especifico
print(lista_nombres)

lista_nombres.reverse() #invierte el orden
print(lista_nombres)

lista_nombres.reverse()
print(lista_nombres)

print(max(lista_numeros)) #devuelve el numero maximo de la lista
print(min(lista_numeros)) #devuelve el numero minimo de la lista

print(lista_numeros)
print(lista_nombres)

lista_nombres.extend(lista_numeros) #añade a la primera lista los elemntos de la segunda
print(lista_nombres)


for numero in lista_numeros:

    lista_nombres.remove(numero)
print(lista_nombres)

#meter en una lista solo los numeros pares desde 0 a 100
lista_pares= []
for numero in range(100):
    if numero % 2 == 0:
        lista_pares.append(numero)
print(lista_pares)

#En una sola linea
lista_impares = [numero for numero in range(100) if numero % 2 !=0]
print(lista_impares)