################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 14
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto, ingreso_entero

def numero_capicua(numero):
    numero = str(numero)
    invertido = numero[::-1]
    if numero == invertido:
        capicua = True
    else:
        capicua = False
    return capicua, numero
    
def prueba():
    print("Este programa le indicará si el numero ingresado es capicúa")
    numero = ingreso_entero("Ingrese otro Número Entero")
    capicua, numero = numero_capicua(numero)
    if capicua:
        print(f"El número {numero} es Capicúa")
    else:
        print(f"{numero} no es un número Capicúa")
    
if __name__ == "__main__":
    prueba()
