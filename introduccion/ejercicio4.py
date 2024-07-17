"""Problema: Diseña una clase Vehículo que tenga atributos básicos como marca, 
modelo, y año, y métodos para iniciar el vehículo y detenerlo. 
Extiende esta clase para crear subclases específicas como Automóvil y
 Motocicleta, 
que tengan características propias."""

"""

class Vehiculo():


    def __init__(self, marca, modelo, año):

        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __repr__(self):
        return f"{self.marca}, {self.modelo}, {self.año}"

    def arrancar_vehiculo(self):
        print("EL vehiculo se ha arrancado")

    def detener_vehiculo(self):
        print("EL vehiculo se ha detenido")

class Motocicleta(Vehiculo):

    caballito = None
    num_ruedas = None

        
    def caballito(self):
        print("La motocicleta puede hacer el caballito")


class Automovil(Vehiculo):

    caballito = None
    num_ruedas = None



vehiculo = Vehiculo("Audi", "A6", "2012")
print(vehiculo)

motocicleta = Motocicleta("Kawasaki", "X", "2015")
motocicleta.caballito = "sí"
motocicleta.num_ruedas = 2
print(f"La motocicleta es de la marca {motocicleta.marca}, modelo {motocicleta.modelo} \n del año {motocicleta.año}, {motocicleta.caballito} hace el caballito \n y tiene {motocicleta.num_ruedas} ruedas")


automovil = Automovil("Ford", "Focus", 2009)
automovil.caballito = "no"
automovil.num_ruedas = 4
print(f"El automovil es de la marca {automovil.marca}, modelo {automovil.modelo} \n del año {automovil.año}, {automovil.caballito} hace el caballito \n y tiene {automovil.num_ruedas} ruedas")
"""
"""
#otra forma

from typing import Any


class Vehiculo():


    def __init__(self, marca, modelo, año):

        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __repr__(self):
        return f"{self.marca}, {self.modelo}, {self.año}"

    def arrancar_vehiculo(self):
        print("EL vehiculo se ha arrancado")

    def detener_vehiculo(self):
        print("EL vehiculo se ha detenido")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, caballito, num_ruedas):
        super().__init__(marca, modelo, año)
        self.num_ruedas = num_ruedas
        self.caballito = caballito
    
    def hacer_caballito(self):
        print("La moticicleta hace el caballito")


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, caballito, num_ruedas):
        super().__init__(marca, modelo, año)
        self.num_ruedas = num_ruedas
        self.caballito = caballito


vehiculo = Vehiculo("Audi", "A6", "2012")
print(vehiculo)

motocicleta = Motocicleta("Kawasaki", "X", "2015", "si",2)
print(f"La motocicleta es de la marca {motocicleta.marca}, modelo {motocicleta.modelo} \n del año {motocicleta.año}, {motocicleta.caballito} hace el caballito \n y tiene {motocicleta.num_ruedas} ruedas")


automovil = Automovil("Ford", "Focus", 2009, "no", 4)
automovil.num_ruedas = 4
print(f"El automovil es de la marca {automovil.marca}, modelo {automovil.modelo} \n del año {automovil.año}, {automovil.caballito} hace el caballito \n y tiene {automovil.num_ruedas} ruedas")

"""
"""

2. Implementación de un Sistema de Gestión de Biblioteca
Problema: Crea un conjunto de clases para gestionar una biblioteca que pueda manejar libros, revistas y periódicos. Debes incluir clases para los elementos, los usuarios de la biblioteca, y el personal. Implementa métodos para añadir elementos, prestarlos a usuarios, y devolverlos.

Objetivos:

Utilizar la encapsulación para proteger y mantener el estado interno de los objetos.
Implementar la herencia para compartir comportamientos entre clases relacionadas.

"""



"""
3. Simulación de una Cuenta Bancaria
Problema: Diseña una clase CuentaBancaria que permita a los usuarios depositar y retirar dinero, además de ver el saldo actual. Extiende esta clase para crear tipos específicos de cuentas como CuentaDeAhorros y CuentaCorriente, donde la CuentaDeAhorros podría generar interés.

Objetivos:

Mostrar el uso de métodos y atributos protegidos o privados.
Explorar cómo diferentes tipos de cuentas pueden modificar o ampliar el comportamiento básico de la cuenta.
4. Sistema de Calificaciones de Estudiantes
Problema: Crea clases para manejar un sistema de calificaciones de estudiantes. Debes incluir al menos clases para Estudiante, Curso, y Profesor. Los estudiantes deben poder inscribirse en cursos, y los profesores deben poder asignar calificaciones.

Objetivos:

Implementar asociaciones entre clases.
Gestionar listas de estudiantes y cursos para simular la inscripción y la asignación de calificaciones."""

"""

class CuentaBancaria():

    def __init__(self, nombre, apellido, entidad, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.entidad =entidad
        self.saldo = saldo

    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"Se han ingresado {cantidad}€. El saldo total es {self.saldo}€")
    
    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}€. El saldo total es de {self.saldo}€")
        else:
            print("No hay saldo suficiente.")



class CuentaAhorros(CuentaBancaria):

    def __init__(self, nombre, apellido, entidad, saldo, interes):
        super().__init__(nombre, apellido, entidad, saldo)
        self.interes = interes


    def __repr__(self):
        return f"{self.nombre} {self.apellido} {self.entidad} {self.saldo} {self.interes}"


class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre, apellido, entidad, saldo, interes):
        super().__init__(nombre, apellido, entidad, saldo)
        self.interes = interes

    def __repr__(self):
        return f"{self.nombre} {self.apellido} {self.entidad} {self.saldo} {self.interes}"
    
    def intereses(self):
        print(f"Esta cuenta no tiene intereses")


cuentas = []

def registrar_cuenta(cuenta):
    cuentas.append(cuenta) 
    print(f"Cuenta registrada {cuenta}")






cuenta_ahorros = CuentaAhorros("Samuel", "Marcos", "Imagin", 10, 10)
cuenta_corriente = CuentaCorriente("Samuel", "Marcos", "Imagin", 5, 0)

registrar_cuenta(cuenta_ahorros)
registrar_cuenta(cuenta_corriente)

ingresar_ahorros = cuenta_ahorros.ingresar_dinero(10)
ingresar_corriente = cuenta_corriente.ingresar_dinero(5)

#retirar_ahorros = cuenta_ahorros.retirar_dinero(10)
#retirar_ahorros = cuenta_corriente.retirar_dinero(5)

for cuenta in cuentas:
    print(cuenta)
    
"""


"""
class Menu:
    def __init__(self, plato):
        self.plato = plato

    def __repr__(self):
        return f"{self.plato}"
    
class Pedido(Menu):
    def __init__(self, plato, nombre_cliente, num_platos, num_mesa):
        super().__init__(plato)
        self.nombre_cliente = nombre_cliente
        self.num_platos = num_platos
        self.num_mesa = num_mesa

    def mostrar_pedido(self):
        return f"{self.nombre_cliente} {self.num_platos} {self.num_mesa} {self.plato}"
    

    def factura_total(self):
        return f"La factura para el cliente {self.nombre_cliente} de la mesa {self.num_mesa} es de {int(self.num_platos) * 10}€"



lista_comensales = []

while True:
    import random
    pedir_nombre = input("Por favor, introduzca su nombre: ")
    pedir_plato = input("Por favor, digame qué desea pedir: ") 
    pedir_num_platos = input("¿Cuantos platos deseas pedir?") 
    pedir_mesa = random.randint(1, 100)
    

    pedido = Pedido(pedir_plato, pedir_nombre, pedir_num_platos, pedir_mesa)
    pedido_info = pedido.mostrar_pedido()
    pedido_factura = pedido.factura_total()
    comensal_info = pedido_info + " | " + pedido_factura
    print(f"Se ha realizado el siguiente pedido: {pedido.mostrar_pedido()}")


    lista_comensales.append(comensal_info)


    seguir_añadiendo = input("¿Desea añadir mas comensales?")
    if seguir_añadiendo.lower() != "si":
        for comensal in lista_comensales:
            print(comensal)
        break
"""
"""

class Juego:

    def __init__(self, nombre_jugador1, nombre_jugador2, personaje1, personaje2):

        self.nombre_jugador1 = nombre_jugador1
        self.nombre_jugador2 = nombre_jugador2
        self.personaje1 = personaje1
        self.personaje2 = personaje2

    def __repr__(self):
        return f"{self.nombre_jugador1} {self.nombre_jugador2} {self.personaje1} {self.personaje2}"
    

class Personajes(Juego):
    
    def __init__(self, nombre_jugador1, nombre_jugador2, personaje1, personaje2, tipo_personaje1, tipo_personaje2):
        super().__init__(nombre_jugador1, nombre_jugador2, personaje1, personaje2)
        self.tipo_personaje1 = tipo_personaje1
        self.tipo_personaje2 = tipo_personaje2

    def seleccion_personaje(self):

        return f"El jugador {self.nombre_jugador1} ha elegido el personaje {self.personaje1} de tipo {self.tipo_personaje1} y el jugador {self.nombre_jugador2} ha elegido el pesonaje {self.personaje2} de tipo {self.tipo_personaje2}"



lista_tipos = ["luchador", "arquero", "mago"]


primer_jugador =input("Introduce tu nombre del jugador 1: ")
segundo_jugador = input("Introduce el nombre del jugador 2: ")
primer_personaje =input(f"Introduce el nombre del personaje para el jugador {primer_jugador}: ")
segundo_personaje = input(f"Introduce el nombre del personaje para el jugador {segundo_jugador}: ")

personajes_actuales = {"primer_jugador": primer_jugador,
                           "segundo_jugador": segundo_jugador,
                           "primer_personaje": primer_personaje,
                           "segundo_personaje": segundo_personaje}


while True: 
    tipo_primer_personaje = input(f"Elige el tipo para el personaje {personajes_actuales['primer_personaje']} entre los siguientes tipos {lista_tipos}: ")
    tipo_segundo_personaje = input(f"Elige el tipo para el personaje {personajes_actuales['segundo_personaje']} entre los siguientes tipos {lista_tipos}: ")

    if tipo_primer_personaje in lista_tipos and tipo_segundo_personaje in lista_tipos:
        personajes_actuales["tipo_primer_personaje"] = tipo_primer_personaje
        personajes_actuales["tipo_segundo_personaje"] = tipo_segundo_personaje
        break
    else:
        personajes_actuales["tipo_primer_personaje"] = tipo_primer_personaje
        personajes_actuales["tipo_segundo_personaje"] = tipo_segundo_personaje
        print("No has elegido un tipo de la lista")

print(f"Esta es la composicion actual de personajes: {personajes_actuales}")


personajes = Personajes(personajes_actuales) 
elegir_personaje = personajes.eleccion_personaje()

"""