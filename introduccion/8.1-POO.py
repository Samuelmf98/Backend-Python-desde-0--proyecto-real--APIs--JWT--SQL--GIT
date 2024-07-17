class Usuario:

    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.premium = False
    
    def __repr__(self):
        return f"{self.nombre}, {self.apellido}, {self.edad}, {self.sexo}, {self.premium}"


    def __del__(self):
        print("Objeto borrado")


    def convertir_premium(self):
        self.premium = True

    def mirar_peliculas(self):
        if self.premium:
            print("El usuario puede ver las peliculas")
        else:
            print("El usuario no es premium")
    
    @staticmethod
    def usuario_mayor(edad): #No le pasamos self porque no tenemos objeto creado
        return edad >= 18
         

usuario = Usuario("samuel", "marcos", 26, "hombre")

print(f"El usuario es: {usuario}") #Aqui premium es False
print(f"El usuario premium es: {usuario.premium}") #False

usuario.mirar_peliculas() #aqui no puede ver las peliculas porque aun no es premium
usuario.convertir_premium() #Llamamos al metodo premium para hacerlo True

print(f"El usuario es: {usuario}") #Aqui premium es True
print(f"El usuario premium es: {usuario.premium}") #True

usuario.mirar_peliculas() #Aqui ya puede ver las peliculas porque ya es premium

#del usuario para eliminarlo

print(Usuario.usuario_mayor(14)) #Da false