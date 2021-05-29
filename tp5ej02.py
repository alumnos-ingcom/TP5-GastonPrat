################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 02
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import ingreso_entero, IngresoIncorrecto

def fibonacci(numero):
    primero = 0
    segundo = 1
    lista_fib = [0, 1]
    if numero > 2:        
        for i in range(numero-1):
            resultado = primero + segundo
            primero = segundo
            segundo = resultado
            lista_fib.append(resultado)
    elif numero == 2:
        return lista_fib
    else:
        raise IngresoIncorrecto("se requiere un valor mayor a 2")
    return lista_fib


def prueba():
    print("Este programa la cantidad de números que pida"
          "de la sucesión FIBONACCI")
    numero = ingreso_entero("Ingrese un número entero mayor a 2")
    lista_fib = fibonacci(numero)
    for item in(lista_fib):
        print(item)
    


if __name__ == "__main__":
    prueba()
