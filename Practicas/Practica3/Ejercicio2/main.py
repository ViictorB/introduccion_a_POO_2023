# ***PRACTICA 3 BALMACEDA VICTOR (Ejercicio 2 - Subclase Main)***

from ClaseElectrico import Electrico
from ClaseGas import Gas

if __name__ == "__main__":
    
    print("Cargar Datos de Calefaccion Electrica:") #Punto a
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    potenciaMax = input("Ingrese la potencia maxima: ")
    CalefacionElectrica = Electrico(marca, modelo, potenciaMax)
    costo_kilowats = int(input("Ingrese el costo por hora por kilowatts: "))
    cantidad_estimada = int(input("Ingrese la cantidad estimada por kilowatts: "))
    CalefacionElectrica.mostrar(costo_kilowats,cantidad_estimada)
    
    print("Cargar Datos de Calefaccion a Gas Natural:") #Punto b
    marca_gas = input("Ingrese la marca: ")
    modelo_gas = input("Ingrese el modelo: ")
    matricula = input("Ingrese la matricula: ")
    calorias = input("Ingrese las calorias: ")
    CalefacionGas = Gas(marca_gas, modelo_gas, matricula, calorias)
    costo_gas = int(input("Ingrese el costo por metro cubico de gas: "))
    cantidad_m3 = int(input("Ingrese estimada por metros cubicos: "))
    CalefacionGas.mostrar(costo_gas, cantidad_m3)
    
    CostoTotalGas = CalefacionGas.calcularCosto(costo_gas, cantidad_m3) #Punto c
    CostoTotalElectrico = CalefacionElectrica.calcularCosto(costo_kilowats, cantidad_estimada)
    if CostoTotalGas > CostoTotalElectrico:
        print("Es mas factible comprar la Calefaccion a Gas Natural en este caso")
    elif CostoTotalGas < CostoTotalElectrico:
        print("Es mas factible comprar la Calefaccion Electrica en este caso")
    else:
        print("Ambas Calefacciones son factibles")
    
    
    
    