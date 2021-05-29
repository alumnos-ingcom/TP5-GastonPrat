################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 01
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    pass

def ingreso_entero(mensaje):
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero

def par_impar(numero):
    numero = str(numero)
    primer_cifra = numero[-1]    
    primer_cifra = int(primer_cifra)
    while primer_cifra > 0:
        primer_cifra = primer_cifra-2
    if primer_cifra == 0:
        resultado = True
    else:
        resultado = False
    return resultado

def prueba():
    print("Esto le dira si su numero es PAR o IMPAR")
    numero = ingreso_entero("Ingresa un número entero")
    resultado = par_impar(numero)
    if resultado:
        print(resultado)
        print(f"Su numero es PAR")
    else:
        print(resultado)
        print(f"Su numero es IMPAR")
    

if __name__ == "__main__":
    prueba()
