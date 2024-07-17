from modelos import Peliculas, Catalogo
from sql import agregar_pelicula_sql, obtener_peliculas_sql
from time import sleep

def agregar_pelicula():

    nombre = str(input("Introduce el nombre de la pelicula: "))
    duracion = int(input("Introduce su duracion en minutos: "))
    genero = str(input("Introduce el genero de la pelicula: "))
    sleep(1)

    pelicula = Peliculas(nombre, duracion, genero)

    agregar_pelicula_sql(pelicula)

catalogo = Catalogo("Peliculas de ciencia ficcion")

#Esta funcion coge todos los registros de la base de datos y los guarda en una lista
def obtener_peliculas():
    peliculas = obtener_peliculas_sql()
    for pelicula in peliculas:
        guardar_pelicula = Peliculas(pelicula[1], pelicula[2], pelicula[3])
        catalogo.peliculas.append(guardar_pelicula)
    for pelicula in catalogo.peliculas:
        print(f"""\

        Nombre de la pelicula: {pelicula.nombre}
        Duracion de la pelicula : {pelicula.duracion}
        Genero de la pelicula: {pelicula.genero}
""")

