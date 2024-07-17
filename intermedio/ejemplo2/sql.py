import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

database = os.environ[  "DATABASE_PELICULAS"]

def conectar_db():

    conexion = sqlite3.connect(database)
    cursor = conexion.cursor()
    return conexion, cursor

def crear_tabla_si_no_existe():

    try:
        conexion, cursor = conectar_db()
        cursor.execute("""SELECT 1 FROM sqlite_master WHERE type='table' AND name='peliculas'""")
        datos_tabla = cursor.fetchone()

        if datos_tabla:
            print("La tabla ya existe")
        else:
            print("Creando tabla")

            sql = """CREATE TABLE IF NOT EXISTS peliculas
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT, 
            duracion INTEGER, 
            genero TEXT, 
            timestamp DATETIME);"""

            cursor.execute(sql)
            conexion.commit()
            print("La tabla ha sido creada")
    except Exception as e:
        print("Error al crear la tabla:",e)
    finally:
        cursor.close()
        conexion.close()

def agregar_pelicula_sql(pelicula):

    conexion, cursor = conectar_db()

    pelicula = (
        pelicula.nombre,
        pelicula.duracion,
        pelicula.genero
    )

    sql = """
    INSERT INTO peliculas (nombre, duracion, genero, timestamp)
    VALUES (?, ?, ?, datetime('now'));
    """
    cursor.execute(sql, (pelicula))
    conexion.commit()

    cursor.execute("""SELECT *
                   FROM peliculas
                   WHERE  nombre = ?
                   AND duracion = ?
                   AND genero = ?""", (pelicula))
    datos_insertados =  cursor.fetchall()

    if not datos_insertados:
        print("No se ha insertado la pelicula")
    else:
        print("La pelicula se han insertado:")
        for pelicula in datos_insertados:
            print(pelicula)

    cursor.close()
    conexion.close()

def obtener_peliculas_sql():
    conexion, cursor = conectar_db()

    sql = "SELECT * FROM peliculas"

    cursor.execute(sql)
    peliculas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return peliculas

