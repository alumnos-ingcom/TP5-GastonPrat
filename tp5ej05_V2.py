################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 05 V2
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto

def inversion_mayusculas(texto):
    texto_modificado = ""
    for c in texto:
        if ord(c) == 32:
            texto_modificado += " "
        elif ord(c) >= ord("A") and ord(c) <= ord("Z"):
            temp = ord(c)
            temp = temp + 32
            temp = chr(temp)
            texto_modificado += temp
        elif ord(c) >= ord("a") and ord(c) <= ord("z"):
            temp = ord(c)
            temp = temp - 32
            temp = chr(temp)
            texto_modificado += temp
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