#Encapsulamiento

class Curso:

    __titulo = "Curso Python"
    __duracion = 120


    def __adquirir_curso(self):
        print("Has adquitido el curso") #Metodo privado 


    def get_adquirir_curso(self):
        return self.__adquirir_curso() #Metodo publico para accedr al metodo privado
        
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo): #Para modificar el atributo privado
        self.__titulo = titulo
        
curso = Curso()
curso.get_adquirir_curso() #Acceder a metodo sin print
print(curso.get_titulo()) #Aceeder aa tributos con print

curso.set_titulo("Curso Java")  #Modificamos el atributo privado
print(curso.get_titulo())