nombre = "Samuel"
edad = 26

def saludar(nombre):

    print(f"Hola {nombre}")


class Usuario:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.premium = False

    def __repr__(self):
        return f"{self.nombre} {self.email} {self.premium}"
    
    def hacer_premium(self):
        self.premium = True


insertar_nombre = str(input("Introduce tu nombre: "))
insertar_email = str(input("Introduce tu email: "))

usuario = Usuario(insertar_nombre, insertar_email)
print(f"usuario estandard: {usuario}")
print(usuario.nombre)
print(usuario.email)
usuario.hacer_premium()
print(f"usuario premium: {usuario}")
