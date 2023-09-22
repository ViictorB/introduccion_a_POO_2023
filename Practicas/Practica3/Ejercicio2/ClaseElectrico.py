# ***PRACTICA 3 BALMACEDA VICTOR (Ejercicio 2 - Subclase Calefaccion a Electricidad)***
import math
from ClaseCalefaccion import Calefaccion

class Electrico(Calefaccion):
    __potenciaMax: int
    
    def __init__(self, marca, modelo, potencia):
        super().__init__(marca,modelo)
        self.__potenciaMax = int(potencia)
        
    def calcularCosto(self, costo , cantidad): #Obtener Calculo para luego hacer el punto 3
        return (self.__potenciaMax / 1000) * cantidad * costo

    def mostrar(self, costo , cantidad): #lo hago aparte porque Cada funcion HACE UNA TAREA (mostrar)
        print("\n-Informacion de Calefaccion Electrica-")
        print("Marca: {} - Modelo: {}")
        print(f"El costo por kilowatt/h es de: ${(self.__potenciaMax / 1000) * cantidad * costo }\n")
        