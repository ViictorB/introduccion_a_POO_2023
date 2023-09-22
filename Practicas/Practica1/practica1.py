# ***PRACTICA 1 BALMACEDA VICTOR***

#------Punto 1-------

class Persona:
    nombre: str
    apellido: str
    dni: str
    telefono: str
    edad: int
    
    def __init__(self, nom, ape, dni, tel, edad): 
        self.nombre = nom
        self.apellido = ape
        self.dni = dni
        self.telefono = tel
        self.edad = edad
        
    def mostrar_cartel (self):
        
        if self.edad > 17:
            print(f"{self.nombre} {self.apellido} es mayor de edad")
            print(f"Tiene {self.edad} años y su telefono es: {self.telefono}")
            
            
#------Punto 2-------

class Factura:
    monto: float
    pagado: bool
    
    def __init__(self, monto, pagado):
        self.monto = monto
        self.pagado = pagado
        
    def verificar(self):
        if self.pagado:
            print("Factura pagada!")
        else:
            print("Ingrese el monto a pagar: (${})".format(self.monto))
            nuevo_monto = float(input("-> "))
            if nuevo_monto == self.monto:
                self.pagado = not self.pagado
                print("Factura pagada exitosamente!")
            elif nuevo_monto > self.monto:
                self.pagado = not self.pagado
                print("Factura pagada exitosamente!")
                print("Vuelto a dar: ${}".format(nuevo_monto - self.monto ))
            else:
                print("Error")
            
            
#------Punto 3-------            

class ViajeroFrecuente:
    num_viajero: int
    dni: str
    nombre: str
    apellido: str
    millas_acum: int
    
    def __init__(self, num, dni, nomb, apell, millas): #punto a
        self.num_viajero = num
        self.dni = dni
        self.nombre = nomb
        self.apellido = apell
        self.millas_acum = millas
         
    def CantidadTotalMillas(self): #punto b
        print(self.millas_acum)
        
    def AcumularMillas(self, millas): #punto c
        self.millas_acum += millas
        print("Millas en total: {}".format(self.millas_acum)) #punto d
        
    def CanjearMillas(self, millas):
        if self.millas_acum >= millas:
            self.millas_acum -= millas
            print("Millas restantes: {}".format(self.millas_acum))
        else:
            print("Error. No es posible canjear esa cantidad de millas.")
        

        