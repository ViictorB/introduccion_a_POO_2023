# ***PRACTICA 3 BALMACEDA VICTOR (Ejercicio 1 - Super Clase)***

class Ferreteria:
    __nombre = "El Cosito S.A"
    __cuit = "30-456-456-8"
    
    def __init__(self):
        pass
    
    def imprimir(self):
        print(f"***  {self.__nombre}  ***")
        print(f"CUIL: {self.__cuit}")