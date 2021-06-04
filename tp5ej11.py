################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 11
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto, ingreso_entero
from random import randint

def promedio_movil_simple(ventana):
    if ventana > 10:
        raise IngresoIncorrecto("Ingrese un valor de 10 o menor")
    lista1 = []
    lista_promedio = []
    for i in range (15):
        lista1.append(randint(1, 100))
    for n in range(16-ventana):
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
    ventana = ingreso_entero("¿Cuantos valores derea promediar?")
    lista1, lista_promedio = promedio_movil_simple(ventana)
    print("Valores a promediar:")
    print(lista1)
    print("Promedios moviles:")
    print(lista_promedio)
    
if __name__ == "__main__":
    prueba()
    