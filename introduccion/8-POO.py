class Coche:

    def __init__(self, marca, color, num_ruedas, veloc_max): #def __init__ es el contructor
        self.marca = marca #El self se sustituye luego automaticamente por el nombre del objeto al hacer print
        self.color = color
        self.num_ruedas = num_ruedas
        self.veloc_max = veloc_max
        self.marca_preestablecida = {"alta_gama":"audi",
                                     "baja_gama": "toyota"}



    def __str__(self):
        return f"{self.marca}, {self.color}, {self.num_ruedas}, {self.veloc_max}"
    

    def acelerar(self): #Metodo
        print(f"El coche  acelera hasta {self.veloc_max} km")

    def frenar(self):   #Metodo
        print("El coche ha frenado")



maquina = Coche("Ford", "blanco", 4, 320) #Crear una instancia

huracan = Coche("Ford", "rojo", 3, 200)

print(maquina.color)
print(huracan.color)
maquina.acelerar()
maquina.frenar()
print(maquina.marca_preestablecida["alta_gama"])
"""Por ejemplo las persona tienen sus atributos como por ejemplo color de ojos,
, altura, peso y luego y luego los metodos que son las acciones como dormir, correr, saltar"""