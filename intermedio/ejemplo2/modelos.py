class Peliculas:

    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

class Catalogo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []

