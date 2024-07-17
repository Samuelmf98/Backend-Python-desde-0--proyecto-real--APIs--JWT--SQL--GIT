#Polimorfismo

class Arma:

    def __init__(self, balas, peso):
        self.balas = balas
        self.peso = peso 

    def disparar(self): #Esta clase es importante sino las demas de disparar no funcionaran

        print("El arma dispara") 


class Pistola(Arma): #hereda atributos de Arma

    def disparar(self):
        print("El arma dispara lento") #cada una tiene una velocidad
 
 
class Ametralladora(Arma): #hereda atributos de Arma
    def disparar(self):
        print("El arma dispara rapido") #cada una tiene una velocidad


arma = Arma(10, 3)
arma.disparar()

pistola = Pistola(12, 5)
pistola.disparar()

ametralladora =Ametralladora(100, 40)
ametralladora.disparar()