"""
Escribir una función para invertir una cadena: Pueden pedirte que escribas una función que tome una cadena de caracteres como entrada y 
devuelva la cadena invertida, para evaluar tu comprensión de las secuencias y las operaciones de strings en Python."""

"""def cadena():
    cadena = str(input("Escribe una frase: "))
    list(cadena)
    print(cadena[::-1])

cadena()
"""

"""
Calcular numeros pares de una lista: Este es un clásico para comprobar si entiendes los conceptos de listas. 
Puedes ser solicitado a implementar una función que calcule el resto de un número dado."""
"""
def pares():
    lista_numeros = []
    numero = int(input("Introduce un numero: "))
    for numero in range(0, numero):
        if numero % 2 == 0:
            lista_numeros.append(numero)
    print(lista_numeros)

pares()
"""

"""
Buscar elementos duplicados en una lista: Este problema puede ayudar al entrevistador a entender cómo manejas las estructuras de datos como listas y sets.
 El ejercicio podría ser encontrar todos los elementos duplicados en una lista dada."""
"""
from collections import Counter
def duplicados(lista_numeros):
    conteo = Counter(lista_numeros) #crea un diccionario con clave valor donde la clave es el numero y el valor las veces que se repite
    duplicados = [num for num, cnt in conteo.items() if cnt > 1]
    print(f"Los números duplicados son: {duplicados}")

cantidad = int(input("¿Cuántos números quieres introducir? "))
lista_numeros = []
for numero in range(cantidad):
    numero = int(input(f"Introduce el número {numero}: "))
    lista_numeros.append(numero)

duplicados(lista_numeros)
"""

"""
Sumar todos los números en una cadena: Se te podría pedir que escribas un programa que extraiga todos los números de una cadena y sume sus valores. 
Esto prueba tu habilidad para manipular cadenas y realizar operaciones matemáticas básicas."""
"""
def suma_num(lista_num):
    print(f"La suma de {lista_num} es {sum(lista_num)}")

lista_num = int(input("¿Cuantos numeros quieres introducir?"))
lista_numeros = []
for numero in range(1, lista_num +1):
    intro_num = int(input(f"Introduce el numero {numero}: "))
    lista_numeros.append(intro_num)
print(f"Esta es la lista de numeros: {lista_numeros}")
print(lista_numeros)
suma_num(lista_numeros)
"""


"""
Contar las ocurrencias de cada carácter en una cadena: Este ejercicio es útil para evaluar tu manejo de diccionarios en Python, 
pidiéndote que cuentes y almacenes la frecuencia de cada carácter en una cadena."""
"""
from collections import Counter

lista = ["platano", "manzana", "naranja", "manzana", "naranja", "manzana", "naranja", "platano"]
conteo_frutas = Counter(lista) #crea un diccionaro
lista_aux = [num for num , cnt in conteo_frutas.items() if cnt >1]

print(f"El diccionario es {conteo_frutas}")
print(f"La lista es {lista_aux}")
"""


"""
Encontrar el número mayor y menor en una lista: Este tipo de pregunta evalúa tu habilidad para iterar a través de listas y comparar elementos, 
fundamental para operaciones más complejas en análisis de datos o algoritmos."""

"""
#Encontrar el número mayor y menor en una lista: Este tipo de pregunta evalúa tu habilidad para iterar a través de listas y comparar elementos, fundamental para operaciones más complejas en análisis de datos o algoritmos.
def max_min(lista_num):
    print(f"El maximo de {lista_num} es {max(lista_num)}")
    print(f"El minimo de {lista_num} es {min(lista_num)}")

lista_num = int(input("¿Cuantos numeros quieres introducir?"))
lista_numeros = []
for numero in range(1, lista_num +1):
    intro_num = int(input(f"Introduce el numero {numero}: "))
    lista_numeros.append(intro_num)
print(f"Esta es la lista de numeros: {lista_numeros}")
print(lista_numeros)

max_min(lista_numeros)

"""


"""
Ejemplo de un script para ejecutar pandas en la lectura de un CSV
"""

"""
import pandas as pd

archivo = pd.read_csv("ruta")
"""
"""

palabra = str(input("Introduce una palabra para comprobar si es palindromo: "))

if palabra == palabra[::-1]:
    print(f"La palabra {palabra} es palindromo")
else:
    print(f"La palabra {palabra} NO es palindromo")

"""
"""
Escribir un programa que imprima los números del 1 al 100.
Para los números que son múltiplos de 3, imprimir "Fizz" en lugar del número.
Para los números que son múltiplos de 5, imprimir "Buzz" en lugar del número.
Para los números que son múltiplos de ambos, 3 y 5, imprimir "FizzBuzz".
"""

"""
lista_num = []
for numero in range(1, 101):
    if numero %3 == 0 and numero %5 == 0:  #Tambien se puede poner 15
        lista_num.append("FizzBuzz")
    elif numero %3 ==0:
        lista_num.append("Fizz")
    elif numero %5 ==0:
        lista_num.append("Buzz")
    else:
        lista_num.append(numero)
print(lista_num)
"""

"""
frase1 = "samuel"
frase2 = "leumas"

frase1_list =list(frase1.strip())

frase2_list =list(frase2.strip())

conteo1 = {}
for letra in frase1_list:
    if letra not in conteo1:
        conteo1[letra] = 1
    else:
        conteo1[letra] += 1

conteo2 = {}
for letra in frase2_list:
    if letra not in conteo2:
        conteo2[letra] = 1
    else:
        conteo2[letra] += 1

if conteo1 == conteo2:
    print("Las palabras son anagramas")
else:
    print("Las palabras NO son anagramas")
"""
"""
Otra forma
from collections import Counter

frase1 = "samuel"
frase2 = "leumas"

conteo1 = Counter(frase1)
conteo2 = Counter(frase2)

if conteo1 == conteo2:
    print("Las palabras son anagramas")
else:
    print("Las palabras NO son anagramas")
"""

"""
#Problema: Dado un array que contiene números de 1 a n con uno que falta, encuentra el número faltante.

lista_num = []

for numero in range(1, 21):
    lista_num.append(numero)

lista_num.remove(15)

lista_num.remove(16)

faltantes = []
conteo = 1
for numero in range(1, len(lista_num) +1):
    if numero not in lista_num:
        faltantes.append(numero)
print(faltantes)
"""
"""
def factorial(num):

    inicio = 1

    for num in range(inicio, num +1):
        
        inicio = inicio * num
    
    print(f"El factorial de {num} es : {inicio}")



numero = int(input("Introduce un numero para calcular su factorial: "))
factorial(numero)

"""