################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 04
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import ingreso_entero, IngresoIncorrecto

def numeros_perfectos(numero):
    if numero > 0:
        resultado = 0
        for divisor in range(1, numero):
            resto = numero % divisor
            if resto == 0:
                resultado = resultado + divisor
            
        return resultado
    else:
        raise IngresoIncorrecto("El numero debe ser mayor a 0")


def prueba():
    print("El programa le dira si escribió un Número Perfecto")
    numero = ingreso_entero("Ingresa un número entero positivo")
    resultado = numeros_perfectos(numero)
    if resultado == numero:
        print(f"{numero} es un NÚMERO PERFECTO")
    else:
        print(f"{numero} no es NÚMERO PERFECTO")

if __name__ == "__main__":
    prueba()

