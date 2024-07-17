#ficheros
def leer_fichero():

    nombre = open("nombre.txt", "r")#lo abrimos
    dato = nombre.read() #leemos
    nombre.close() #cerramos
    print(dato) #imprimimos

leer_fichero()

nombre = open("nombre.txt", "w") #modo write, sobreescribe

dato = "Mi nombre NO es Samuel"
nombre.write(dato)
nombre.close()
print(nombre)

leer_fichero()

nombre = open("nombre.txt", "a") #modo agregar sin eliminar existente
dato = " y esta es una nueva linea"
nombre.write(dato)
nombre.close()

leer_fichero()


#Para crear un nuevo archivo

archivo = open("prueba.txt", "w")  #abre el mismo que cierra (archivo)
nuevo_dato = "Esto es una prueba"
archivo.write(nuevo_dato)
archivo.close()

nuevo_archivo = open("prueba.txt", "r") 
nuevo_archivo1 = nuevo_archivo.read()
nuevo_archivo.close()
print(nuevo_archivo1) #hacemps print del que lee (nuevo_archivo1)

leer_fichero()