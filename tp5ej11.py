################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 11
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto, ingreso_entero
from random import randint

def promedio_movil_simple(valores):
    if valores < 3:
        raise IngresoIncorrecto("Tienen que ser 3 valores o mas")
    lista1 = []
    lista_promedio = []
    for i in range (valores):
        lista1.append(randint(1, 100))
    valor = 0
    while valor < (valores-2):
        uno = lista1[valor]
        dos = lista1[valor+1]
        tres = lista1[valor+2]
        valor = valor + 1
        promedio = (uno+dos+tres)/3
        lista_promedio.append(round(promedio, 1))
    return lista1, lista_promedio

def prueba():
    print("Aquí se mostrara una lista con su promedio móvil en 3 valores")
    valores = ingreso_entero("Ingresar cuantos valores desea promediar,"
                             " deben ser 3 o mas")
    lista1, lista_promedio = promedio_movil_simple(valores)
    print("Valores a promediar:")
    print(lista1)
    print("Promedios moviles:")
    print(lista_promedio)
    
if __name__ == "__main__":
    prueba()
    