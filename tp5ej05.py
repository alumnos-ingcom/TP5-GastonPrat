################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 05
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto

def inversion_mayusculas(texto):
    texto_modificado = ""
    for c in texto:
        if c.isspace():
            texto_modificado += " "
        elif c.isupper():
            texto_modificado += c.lower()
        elif c.islower():
            texto_modificado += c.upper()
        else:
            texto_modificado += c
    return texto_modificado


def prueba():
    print("Éste programa invertira las mayusculas y minusculas"
          " de la palabra o frase ingresada")
    texto = input("escriba una frase o palabra: ")
    texto_modificado = inversion_mayusculas(texto)
    print(f"su ingreso invertido es: {texto_modificado}")

if __name__ == "__main__":
    prueba()