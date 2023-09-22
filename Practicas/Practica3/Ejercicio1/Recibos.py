# ***PRACTICA 3 BALMACEDA VICTOR (Ejercicio 1 - Subclase Recibos)***

from Ferreteria import Ferreteria

class Recibos(Ferreteria):
    __numeroRecibo: int
    __monto: float
    
    def __init__(self, num, monto):
        self.__numeroRecibo = int(num)
        self.__monto = float(monto)
        
    def imprimir(self):
        print("      RECIBO     ")
        super().imprimir()
        print(f"Numero de Recibo: {self.__numeroRecibo}  Monto: ${self.__monto}")
        
