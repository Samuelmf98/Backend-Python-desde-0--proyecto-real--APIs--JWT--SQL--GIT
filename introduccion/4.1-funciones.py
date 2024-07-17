def sumar(num1, num2):
    return f"{num1} mas {num2} es igual a {num1 + num2}"

def restar(num1, num2):
    return f"{num1} menos {num2} es igual a {num1 - num2}"


def multiplicar(num1, num2):
    return f"{num1} multiplicado por {num2} es igual a {num1 * num2}"


def dividir(num1, num2):
    return f"{num1} dividido entre {num2} es igual a {num1 / num2}"

def calculadora():
    while True:
        opcion = int(input("""Introduce una opcion: 
                                    [1] sumar
                                    [2] restar
                                    [3] multiplicar
                                    [4] dividir
                                    >>>"""))
        if opcion >= 1 and opcion <= 4:
        
            primer_numero = int(input("Introduce el primer numero: "))
            segundo_numero = int(input("Introduce el segundo numero: "))


            if opcion == 1:
                print(sumar(primer_numero, segundo_numero))
            elif opcion == 2:
                print(restar(primer_numero, segundo_numero))
            elif opcion == 3:
                print(multiplicar(primer_numero, segundo_numero))
            elif opcion == 4:
                print(dividir(primer_numero, segundo_numero))
        
        else:
            print("Por favor introduzca un numero valido")

        repeticion = str(input("¿Quieres seguir calculando? (si/no): ")).lower()
        if repeticion != "si":
            print("Hasta pronto!")
            break
    
calculadora()

