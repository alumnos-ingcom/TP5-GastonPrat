################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 10
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto, ingreso_entero

def numero_a_binario(numero):
    binario = ""
    if numero > 1:
        while numero > 1:
            valor_bin = int(numero % 2)
            numero = int(numero / 2)
            valor_bin = str(valor_bin)
            binario += valor_bin
        binario += "1"
    elif numero == 1:
        binario += "1"
    elif numero == 0:
        binario += "0"

    else:
        raise IngresoIncorrecto("El número debe ser mayor a cero")
    binario = binario[::-1]
    return binario

def prueba():
    print("Este programa transformara su número en Binario")
    numero = ingreso_entero("Escriba un número entero positivo")
    binario = numero_a_binario(numero)
    print(f"su número {numero} es {binario} en Binario")
    
if __name__ == "__main__":
    prueba()