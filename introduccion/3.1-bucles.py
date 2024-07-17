contador = 1
while contador <= 5:
    print(contador)
    contador += 1

for numero in range(1, 10):
    if numero % 2 == 0:
        continue  # Salta los números pares
    print(numero)

for numero in range(1, 10):
    if numero == 5:
        break  # Detiene el bucle cuando numero es 5
    print(numero)    