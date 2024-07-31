#Con args podemos hacer una funcion sin especificar los parametros de entrada

def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(1, 2, 3, 4, 5))

#Kwargs funciona igual pero con por ejemplo variables declaradas dentro

def inf_personal(**kwargs):
    nombre = kwargs.get("nombre", "anonimo")
    edad = kwargs.get("edad", "desconocida")
    peso = kwargs.get("peso", "desconocido")

     
    return f"Me llamo {nombre}, tengo {edad} años y peso {peso} kilos"
    

print(inf_personal(nombre = "samuel", edad = 26))



#o tambien directamente un diccionario


def inf_personal(**kwargs):
    nombre = kwargs.get("nombre", "anonimo")
    edad = kwargs.get("edad", "desconocida")
    peso = kwargs.get("peso", "desconocido")

     
    return f"Me llamo {nombre}, tengo {edad} años y peso {peso} kilos"
    

inf_dict = {"nombre": "samuel",
            "edad": 26}
print(inf_personal(**inf_dict)) #Importante incluir los dos asteriscos al incluir el diccionario como parametro