def decorar_funcion(funcion):
    def wrapper(*args, **kwargs):
        funcion(*args, **kwargs)
        print("Como estas?")
    return wrapper

@decorar_funcion #Al poner eso y seguidamente definir una funcion, lo que realmente sucede es que llamamos a wrapper y luego a la funcion saludar.
def saludar():
    print("Hola")

#saludar()

#La idea de todo esto es poder ejecutar funciones solo si cumple x condiciones, por ejemplo que el usuario tenga permisos


def role_necesitado(roles):
    def decorator(funcion):
        def wrapper(*args, **kwargs):
            perfil = {
                "role": "admin"
            }
            if perfil["role"] in roles:
                return funcion(*args, **kwargs)
            else:
                print("Rol no permitido para ser saludado")
        return wrapper
    return decorator



@role_necesitado(roles = ["admin", "cliente"])
def saludar_con_permiso(nombre):
    print(f"Hola como estas {nombre}")


saludar_con_permiso("samuel")


