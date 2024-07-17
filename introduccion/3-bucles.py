#forma 1
numero_de_tabla = int(input("¿Que tabla quieres calcular?: "))
numero_maximo = int(input("¿Numero maximo de calculos?: "))

for i in range(0, numero_maximo + 1):
    print(f"{numero_de_tabla} x {i} = {numero_de_tabla * i}")
    

#Forma 2

numero_de_tabla = int(input("¿Que tabla quieres calcular?: "))
num = 0
for i in range(11):
    print(f"{numero_de_tabla} x {num} = {numero_de_tabla * num}")
    num = num + 1