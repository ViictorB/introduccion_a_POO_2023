# ***PRACTICA 2 BALMACEDA VICTOR (Ejercicio 2 - Main)***

from ClaseCuenta import Cuenta

def generarCuenta(lista):
    print("-------Generar Cuenta-------")
    nombre  = str(input("Ingrese su Nombre Completo: "))
    dni = str(input("Ingrese su Dni: "))
    contraseña = str(input("Ingrese su contraseña: "))
    nuevaCuenta = Cuenta(nombre, dni, contraseña, 0)
    lista.append(nuevaCuenta)
    print("Cuenta creada con exito!")
    
def depositarDinero(lista):
    print("-------Depositar Dinero-------")
    dni = str(input("Ingrese su Dni: "))
    contraseña = str(input("Ingrese su Contraseña"))
    bandera = True
    for usuario in lista:
        if usuario.getDni() == dni and usuario.getContraseña() == contraseña:
            bandera = False
            saldo = float(input("ingrese el saldo a depositar: "))
            usuario.setSaldo(saldo)
            print("Dinero Depositado en su cuenta con exito!")
            
    if bandera:
        print("Error!. Nombre o Contraseña Incorrecta!")
    
        
def verificarSaldo(lista):
    print("-------Verificar Saldo-------")
    dni = str(input("Ingrese su Dni: "))
    bandera = True
    for usuario in lista:
        if dni == usuario.getDni():
            print("Su saldo es de: ${}".format(usuario.getSaldo()))
            bandera = False
    if bandera:
        print("Dni Incorrecto")
    
        
if __name__ == "__main__":
    Usuarios = []  #Genero una lista para tener varias cuentas de banco
    generarCuenta(Usuarios) #genero la primera cuenta
    depositarDinero(Usuarios) # funcion que me permite depositar dinero a cualquier usuario de la lista
    verificarSaldo(Usuarios) # funcion que me permite verificar el saldo con su dni 
