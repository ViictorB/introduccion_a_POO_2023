# ***PRACTICA 2 BALMACEDA VICTOR (Ejercicio 2 - Clase Cuenta)***

class Cuenta:
    __nombre: str
    __dni: str
    __contraseña: str
    __saldo: float
    
    def __init__(self, nomb, dni, contra, saldo):
        self.__nombre = nomb
        self.__dni = dni
        self.__contraseña = contra
        self.__saldo = saldo
        
    def getNombre(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def getContraseña(self):
        return self.__contraseña
    
    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, nuevo):
        self.__saldo = nuevo