################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 06
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto

def parentesis_balanceado(cadena, abre="[", cierra="]"):
    pila = []
    for c in cadena:
        if c == abre:
            pila.append(c)
        elif c == cierra:
            if len(pila) == 0:
                balanceado = False
            else:
                pila.pop()
    if len(pila) == 0:
        balanceado = True
    else:
        balanceado = False
    return balanceado
            
def prueba():
    print("Este programa le dira si los"
          "parentesis estan Balanceados")
    cadena = input("escriba una cadena con parentesis: ")
    balanceado = parentesis_balanceado(cadena)
    if balanceado:
        print("La cadena con parentesis está balanceada")
    else:
        print("La cadena no está balanceada")

if __name__ == "__main__":
    prueba()