# ***PRACTICA 3 BALMACEDA VICTOR (Ejercicio 2 - Subclase Calefaccion a GAS NATURAL)***

from ClaseCalefaccion import Calefaccion

class Gas(Calefaccion):
    __matricula: str
    __calorias: float
    
    def __init__(self, marca, modelo, matricula, calorias):
        super().__init__(marca,modelo)
        self.__matricula = str(matricula)
        self.__calorias = float(calorias) 
         
    def calcularCosto(self, costo , cantidad): #Obtener Calculo para luego hacer el punto 3
        return self.__calorias * cantidad * costo
        
    def mostrar(self, costo , cantidad): #lo hago aparte porque Cada funcion HACE UNA TAREA (mostrar)
        print("\n-Informacion de Calefaccion a Gas Natural-")
        print("Marca: {} - Modelo: {}")
        print(f"El costo por metro cubico es de: ${self.__calorias * cantidad * costo }\n")
    