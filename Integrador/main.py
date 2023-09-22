from CajaAhorro import CajaAhorro
from PlazoFijo import PlazoFijo
#from Cuenta import Cuenta

def test():
    Cuenta1 = CajaAhorro("Victor Balmaceda", 7)
    Cuenta2 = PlazoFijo("Ana Martinez", 4, 5 , 10.5)
    Cuenta3 = CajaAhorro("Sofia Chavez", 8)
    Cuenta4 = PlazoFijo("Lionel Messi",10, 3, 10.00)
    
    Cuenta1.mostrar()
    Cuenta2.mostrar()
    Cuenta3.mostrar()
    print("\nMonto Total de Interes de la Cuenta 4, el Mejor del mundo ( {} ) es de: ${}".format(Cuenta4.getTitular(),Cuenta4.obtenerMontoTotal()))

if __name__ == "__main__":
    test()
    #Cuenta5 = Cuenta("Mario", 64)    No se puede crear un objeto de una clase padre(Super Clase) ya que es una clase abstracta

