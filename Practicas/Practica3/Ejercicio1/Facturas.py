# ***PRACTICA 3 BALMACEDA VICTOR (Ejercicio 1 - Subclase Facturas)***

from Ferreteria import Ferreteria

class Facturas(Ferreteria):
    __numeroFactura: int
    __monto: float
    
    def __init__(self, num, monto):
        self.__numeroFactura = int(num)
        self.__monto = float(monto)
        
    def imprimir(self):
        print("      FACTURA     ")
        super().imprimir()
        print(f"Numero de Factura: {self.__numeroFactura}  Monto: ${self.__monto}")
        
        