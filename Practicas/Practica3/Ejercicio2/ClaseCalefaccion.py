# ***PRACTICA 3 BALMACEDA VICTOR (Ejercicio 2 - SuperClase Calefaccion)***

class Calefaccion:
    __marca: str
    __modelo: str
    
    def __init__(self, marca, modelo):
        self.__marca = str(marca)
        self.__modelo = str(modelo)
        
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    
    def calcularCosto(self):
        pass
    
    def mostrar(self):
        pass