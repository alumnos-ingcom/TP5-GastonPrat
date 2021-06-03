################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 09
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto
from time import time

def factoriones_funcion(limite):
    factoriones = []
    for numero in range(1, limite+1):
        numero = str(numero)
        factoriales_del_numero = []
        for n in numero:
            n = int(n)
            factoriales_del_numero.append(n)
        solucion = 0
        for f in factoriales_del_numero:
            resultado = 1
            while f > 0:
                resultado = resultado * f
                f = f -1
            solucion = solucion + resultado
        numero = int(numero)
        if solucion == numero:
            factoriones.append(numero)
    return factoriones
    
def prueba():
    tiempo = time()
    print("Este programa retornara una lista con los")
    print("Factoriones menores a 1.999.999")
    factoriones = factoriones_funcion(limite=1499999)
    for item in factoriones:
        print(item)
    print(f"se tardo {round(time()-tiempo, 1)} "
          "segundos en llegar al resultado")
    
if __name__ == "__main__":
    prueba()