import sqlite3
from crear_tabla import crear_tabla_if_not_exists
from dotenv import load_dotenv
import os

load_dotenv()

database = os.environ["DATABASE_PRUEBA"] #esto es interesante hacerlo cuando hay contraseñas


crear_tabla_if_not_exists()


def insertar_datos():

    conexion = sqlite3.connect(database)
    cursor = conexion.cursor()

    try:
        nombre = str(input("Introduce el nombre: "))
        apellido = str(input("Introduce el apellido: "))
        telefono = int(input("Introduce el telefono: "))

        #En otros SQL se pueden poner como %s
        insert = """INSERT INTO usuarios (nombre, apellido, telefono, created_date)
                VALUES(?, ?, ?, datetime('now'))"""

        cursor.execute(insert, (nombre, apellido, telefono))
        conexion.commit()
        print("Se han insertado los datos")

        #Comprobar que se han insertado datos
        cursor.execute("""SELECT * FROM usuarios
                            WHERE nombre = ?
                            AND apellido = ?
                            AND telefono = ?""",
                            (nombre, apellido, telefono))
        datos_introducidos = cursor.fetchall()
        if not datos_introducidos:
            print("No se han introducido los datos")
        else:
            for usuario in datos_introducidos:
                print(f"Se han introducido los datos {usuario}")

    except:
        print("Error al insertar los datos")

    finally:
        cursor.close()
        conexion.close()

insertar_datos()
    
    

