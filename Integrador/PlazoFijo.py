from Cuenta import Cuenta

class PlazoFijo(Cuenta):
    __plazo: int
    __interes: float
    
    def __init__(self,titular,cant,plazo,interes):
        super().__init__(titular, cant)
        self.__plazo = int(plazo)
        self.__interes = float(interes)
        
    def obtenerMontoTotal(self):
        return super().getCantidad() * self.__interes / 100    
        
    def mostrar(self):
       super().mostrar()
       print("Plazo: {}  Interes: ${}".format(self.__plazo, self.__interes))
       print(f"**********MONTO TOTAL DE INTERES: ${super().getCantidad() * self.__interes / 100}")
       