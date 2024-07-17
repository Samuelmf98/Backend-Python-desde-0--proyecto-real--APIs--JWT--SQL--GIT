import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

database = os.environ["DATABASE_PRUEBA"] #esto es interesante hacerlo cuando hay contraseñas


def crear_tabla_if_not_exists():
        
        conexion = sqlite3.connect(database)
        
        try:
        
            cursor = conexion.cursor()

            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='usuarios';"
            )
            table_exists = cursor.fetchone()

            if not table_exists:
                print("Creando tabla...")
                cursor.execute(
                    """
                    CREATE TABLE usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        apellido TEXT,
                        telefono INTEGER,
                        created_date DATETIME
                    );
                """
                )
                conexion.commit()

                print("La tabla usuarios ha sido creada")

            else:
                print("La tabla ya existe")

        except Exception as e:
            print("Error al crear la tabla:", e)
        finally:
            cursor.close()
            conexion.close()