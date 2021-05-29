################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 03
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import ingreso_entero, IngresoIncorrecto

def tribonacci(numero):
    lista_trib = [1, 1, 1]
    if numero > 3:        
        for i in range(numero-3):
            primero = lista_trib[-1]
            segundo = lista_trib[-2]
            tercero = lista_trib[-3]
            resultado = primero + segundo + tercero
            lista_trib.append(resultado)
    elif numero == 3:
        return lista_trib
    else:
        raise IngresoIncorrecto("se requiere un valor mayor a 3")
    return lista_trib


def prueba():
    print("Este programa la cantidad de números que pida"
          "de la sucesión TRIBONACCI")
    numero = ingreso_entero("Ingrese un número entero mayor a 3")
    lista_trib = tribonacci(numero)
    for item in(lista_trib):
        print(item)
    


if __name__ == "__main__":
    prueba()
