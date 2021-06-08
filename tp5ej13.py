################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 12
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto

def buscador_de_palabras(texto, busqueda, ignorar_mayusculas=True):
    if ignorar_mayusculas:
        texto = texto.lower()
    posicion = texto.find(busqueda)
    if posicion == -1:
        raise IngresoIncorrecto("Esa palabra no esta en el texto")
    return posicion, busqueda
    
    
def prueba():
    print("Este programa le indicará la posición de la palabra"
          " buscada en el texto")
    texto = ("La ley de Moore conocida en la actualidad"
    "fue una predicción realizada por el ingeniero Goordon"
    "Moore (Cofundador de INTEL) en 1965 la cual decía que"
    "la cantidad de transistores por unidad de superficies"
    "en los circuitos integrados se duplicaría cada año.")
    busqueda = input("¿que palabra busca? ")
    posicion, busqueda = buscador_de_palabras(texto, busqueda)
    print(f"La posicion de {busqueda} en el texto es {posicion}")
    
    
if __name__ == "__main__":
    prueba()