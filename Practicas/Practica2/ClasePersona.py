# ***PRACTICA 2 BALMACEDA VICTOR (Ejercicio 1 - Modulo Clase)***

class Persona:
    __nombre: str
    __apellido: str
    __dni: str
    __motivo: str
    __obraSocial: bool
    
    def __init__(self, nomb, apell, dni, motivo, obra):
        self.__nombre = nomb
        self.__apellido = apell
        self.__dni = dni
        self.__motivo = motivo
        self.__obraSocial = obra
        
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDni(self):
        return self.__dni
    
    def getMotivo(self):
        return self.__motivo
        
    def getObraSocial(self):
        return self.__obraSocial
    
