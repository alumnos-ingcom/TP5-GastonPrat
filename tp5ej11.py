################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 11
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto, ingreso_entero
from random import randint

def promedio_movil_simple(ventana, lista1):
    if ventana > len(lista1):
        raise IngresoIncorrecto("La cantidad de valores a "
                                "promediar debe ser igual o menor "
                                "a la cantidad de valores en la lista")
    lista_promedio = []
    for n in range(len(lista1)-(ventana-1)):
        contador = n - 1
        sumador = 0
        vuelta = 0
        while vuelta < ventana:
            sumador = sumador + lista1[contador+1]
            vuelta = vuelta + 1
            contador = contador +1
        sumador = sumador / ventana
        sumador = round(sumador, 1)
        lista_promedio.append(sumador)
    return lista1, lista_promedio

def prueba():
    print("Aquí se mostrara una lista con su promedio móvil")
    lista1 = []
    for i in range (15):
        lista1.append(randint(1, 100))
    ventana = ingreso_entero("¿Cuantos valores desea promediar?")
    lista1, lista_promedio = promedio_movil_simple(ventana, lista1)
    print("Valores a promediar:")
    print(lista1)
    print("Promedios moviles:")
    print(lista_promedio)
    
if __name__ == "__main__":
    prueba()
    