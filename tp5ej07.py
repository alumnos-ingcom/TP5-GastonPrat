################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 07
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto

def ingreso_float(mensaje):
    ingreso = input(mensaje + " #")
    try:
        real = float(ingreso)
    except ValueError as err:
        print("Eso no era un Número, intenta nuevamente")
        return prueba()
    return real

def distacia_numeros(numero1, numero2):
    if numero1 > numero2:
        distancia = numero1 - numero2
    else:
        distancia = numero2 - numero1
    if distancia < 0:
        distancia = (distancia+distancia) + distancia
    return distancia
            

def prueba():
    print("El programa le devolvera la distancia"
          " entre dos numeros reales")
    numero1 = ingreso_float("ingrese un número")
    numero2 = ingreso_float("ingrese otro número")
    distancia = distacia_numeros(numero1, numero2)
    print(f"La distancia entre {numero1} y {numero2} es: {distancia}")
    

if __name__ == "__main__":
    prueba()
