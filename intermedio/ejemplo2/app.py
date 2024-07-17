import sqlite3
from dotenv import load_dotenv
import os
from sql import crear_tabla_si_no_existe
from time import sleep
from funciones import agregar_pelicula, obtener_peliculas


load_dotenv()
database = os.environ[  "DATABASE_PELICULAS"]

#Creamos la tabla peliculas
crear_tabla_si_no_existe()

while True:

    try:
        print("***Bienvenido a tu Catalogo***")
        sleep(1)
        menu = int(input("""

    [1] Para agregar una nueva pelicula
    [2] Para obtener peliculas
    [0] Para salir del Catalogo
    >>>"""))
        if menu == 1:
            agregar_pelicula()
        elif menu ==2:
            obtener_peliculas()
        elif menu == 0:
            print("Saliendo del programa...")
            exit()
        else:
            print("Ingrese una opcion correcta")
    except ValueError as error:
        print(f"Ingrese una opcion correcta, {error}")