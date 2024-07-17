class Catalogo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = [] #no la metemos arriba porque luego cuando creewmos el objetonno quiero que me pida meter [] como arguemnto

    

class Peliculas:

    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __repr__(self):
        return f"{self.nombre}, {self.duracion}, {self.genero}" #Aqui si quiero que me imprima la pelicula
    

catalogo = Catalogo("catalogo_de_terror") #Creamos objetos de ambas clases, aqui hubiera puesto [] como segundo argumento pero no lo puse arriba
pelicula = Peliculas("Insidius", 120, "terror")

print(catalogo.peliculas) #Aqui esta lista esta vacia
catalogo.peliculas.append(pelicula) #le meto el objeto pelicula dentro del otro objeto (en su lista)
print(catalogo.peliculas) #Ya esta llena la lista.

#Vamos a acceder al objeto catalogo, a su atributo peliculas, y dentro de esta lista tenemos otro objeto
#Accedemos al elemento 0, el cual es la lista que hemos introducido, y luego a sus atributos.
print(catalogo.peliculas[0].nombre) 
print(catalogo.peliculas[0].duracion) 
print(catalogo.peliculas[0].genero) 


#Creemos otro objeto de catalogo

pelicula1 = Peliculas("Anabelle", 200, "terror")

catalogo.peliculas.append(pelicula1)
print(catalogo.peliculas)

print(catalogo.peliculas[1]) #Aqui accedemos a la lista 2
print(catalogo.peliculas[1].nombre)
