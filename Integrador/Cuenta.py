import abc
from abc import ABC


class Cuenta(ABC):
    __titular: str
    __cantidad: int
    
    def __init__(self, titular, cantidad):
        self.__titular = str(titular)
        self.__cantidad = int(cantidad)
        
    def getTitular(self):
        return self.__titular
    def getCantidad(self):
        return self.__cantidad

    @abc.abstractmethod
    def mostrar(self):
        print("****************************************")
        print(f"Nombre del Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")