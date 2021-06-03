################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 12
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto, ingreso_entero
from random import randint

def comparar_listas(lista1, lista2):
    resultado = True
    for item in lista1:
        if item == lista2[0]:
            resultado = True
        elif item == lista2[1]:
            resultado = True
        elif item == lista2[2]:
            resultado = True
        elif item == lista2[3]:
            resultado = True
        else:
            resultado = False
            break
    return resultado


def prueba():
    lista1 = []
    lista2 = []
    print("Este programa le dira si dos listas tienen los mismos valores")
    print("Ingresar 4 valores de la primer lista:")
    for i in range(4):
        numero = ingreso_entero("Escribaun número")
        lista1.append(numero)
    print("Este programa le dira si dos listas tienen los mismos valores")
    print("Ingresar 4 valores de la segunda lista:")
    for i in range(4):
        numero = ingreso_entero("Escribaun número")
        lista2.append(numero)
    resultado = comparar_listas(lista1, lista2)
    print(f"¿son iguales? --- {resultado}")
    
if __name__ == "__main__":
    prueba()
    