nombre = "Samuel"
edad = 26
sexo = "masculino"
soltero = False
independizado = True

if nombre != "Julian":
    print("El nombre es incorrecto")
else:
    print("El nombre es correcto")


if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Eres mayo de edad")
else:
    print("Eres menor de edad")


if sexo == "Femenino":
    print("No eres masculino")
else:
    print("Eres masculino")

if soltero is False and independizado is True:
    print("No estas soltero y estas independizado")
elif soltero is False or independizado is True:
    print("Solo necesito que se cumpla una condicion")


if not independizado:
    print("independizate!")