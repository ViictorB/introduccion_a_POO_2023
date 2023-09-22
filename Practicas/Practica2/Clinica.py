# ***PRACTICA 2 BALMACEDA VICTOR (Ejercicio 1 - Main)***
from ClasePersona import Persona

def realizarChequeo(persona):
    if persona.getObraSocial():
        print("La persona {} DNI {} posee Obra social".format(persona.getNombre(), persona.getDni()))
    else:
        print("La persona {} DNI {} NO posse obra social".format(persona.getNombre(), persona.getDni()))


if __name__ == "__main__":
    
    p1 = Persona("Juan", "Diaz" , "41778568" , "Dolor de cabeza" , True)
    p2 = Persona("Matilda", "Mercado", "43898712" , "Dolor Estomacal" , False)
    p3 = Persona("Ana", "Chavez", "37555111", "Hipertension Alta", False)
    p4 = Persona("Armando" , "Paredes" , "27777888", "Dureza de hombro" , True)
    p5 = Persona("Nicolas", "Figueroa" , "30111325", "Dolor de cabeza muy intenso", True)
    
    realizarChequeo(p1)
    realizarChequeo(p2)
    realizarChequeo(p3)
    realizarChequeo(p4)
    realizarChequeo(p5)