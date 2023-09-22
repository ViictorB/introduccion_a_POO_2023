from Cuenta import Cuenta

class CajaAhorro(Cuenta):
    
    def __init__(self,titular,cant):
        super().__init__(titular, cant)
        
    def mostrar(self):
       super().mostrar()
       print("****************************************")
