################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 12
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto, ingreso_entero

def comparar_listas(lista1, lista2):
    resultado = True
    for item in lista1:
        for c in lista2:
            if item == c:
                lista2.pop()
    if len(lista2) == 0:
        resultado = True
    else:
        resultado = False
    return resultado


def prueba():
    lista1 = []
    lista2 = []
    print("Este programa le dira si dos listas tienen los mismos valores")
    valores = ingreso_entero("¿cuantos valores tendra cada lista?")
    print(f"Ingresar {valores} valores de la primer lista:")
    for i in range(valores):
        numero = ingreso_entero("Escribaun número")
        lista1.append(numero)
    print("Este programa le dira si dos listas tienen los mismos valores")
    print(f"Ingresar {valores} valores de la segunda lista:")
    for i in range(valores):
        numero = ingreso_entero("Escribaun número")
        lista2.append(numero)
    resultado = comparar_listas(lista1, lista2)
    print(f"¿son iguales? --- {resultado}")
    
if __name__ == "__main__":
    prueba()
    