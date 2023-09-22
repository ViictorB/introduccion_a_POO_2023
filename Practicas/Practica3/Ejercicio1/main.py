# ***PRACTICA 3 BALMACEDA VICTOR (Ejercicio 1 - Main)***

from Facturas import Facturas
from Recibos import Recibos

def mostrarMenu():
    print("-----------------------")
    print("1 - Emitir Factura")
    print("2 - Emitir Recibo")
    print("0 - Salir")
    print("-----------------------")


def menu():
    mostrarMenu()
    op = int(input("Ingrese una opcion-> "))
    while op != 0:
        if op == 1:
            numero = int(input("Ingrese el numero de factura: "))
            monto = float(input("Ingrese el monto: "))
            factura = Facturas(numero, monto)
            factura.imprimir()
        elif op == 2:
            numero = int(input("Ingrese el numero de recibo: "))
            monto = float(input("Ingrese el monto: "))
            recibo = Recibos(numero,monto)
            recibo.imprimir()
        else:
            print("Error")
            
        mostrarMenu()
        op = int(input("Ingrese una nueva opcion-> "))
        
            
if __name__ == "__main__":
    menu()