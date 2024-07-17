#Herencias

class Animal:


    def __init__(self, edad, num_patas, alimentacion):
        self.edad = edad
        self.num_patas = num_patas
        self.alimentacion = alimentacion

    def caminar(self): #Estos metodos los compartirá perro mas adelante
        print("El animal camina")

    def correr(self):
        print("El animal corre")

    
class Perro(Animal):

    raza = None
    ladrido = None
    pelaje = None

    def ladrar(self):
        print("El perro ladra")

    def muerde(self):
        print("El perro muerde")

perro = Perro(5, 4, "carnivoro") #Hereda los atributos de la clase padre Animal
perro.raza = "caniche" #Estos 3 no estan en la clase padre sino que son propios de la clase perro
perro.ladrido = "fuerte"
perro.pelaje = "Blanco"

print(perro.edad)
print(perro.num_patas)
print(perro.alimentacion)

print(perro.raza)
print(perro.ladrido)
print(perro.pelaje)
