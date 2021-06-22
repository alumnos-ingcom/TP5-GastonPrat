################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 13
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto

def buscador_de_palabras(texto, busqueda, ignorar_mayusculas=True):
    if ignorar_mayusculas:
        texto = texto.lower()
    n_texto = len(texto)
    n_busqueda = len(busqueda)
    n = 0
    caracter = 0
    comparador = []
    pila = []
    ubicacion = []
    for i in busqueda:
        comparador.append(i)
    while caracter < n_busqueda:
        i = busqueda[caracter]
        for c in range(n, n_texto):
            c = texto[n]
            if i == c:
                pila.append(c)
                ubicacion.append(n)
                caracter += 1
                n += 1
                if pila == comparador:
                    igualdad = True
                    return igualdad, ubicacion
                break
            else:
                pila.clear()
                ubicacion.clear()
                caracter = 0
                n += 1
                break
        if n == n_texto:
            break
    igualdad = False
    return igualdad, ubicacion
                

    
def prueba():
    print("Este programa le indicará la posición de la palabra"
          " buscada en el texto")
    texto = (
'''La ley de Moore conocida en la actualidad fue una predicción realizada por el ingeniero
Goordon Moore (Cofundador de INTEL) en 1965 la cual decía que la cantidad de
transistores por unidad de superficies en los circuitos integrados se duplicaría cada año,
tiempo después, en 1975, Gordon desestimo esto y cambio su predicción afirmando que
la capacidad de integración no se duplicaría cada un año, sino que sería cada 24 meses.
Para que esto sea posible es necesario reducir el tamaño de los transistores ya que, de lo
contrario, no podríamos meter el doble de cantidad donde no hay espacio.'''
            )
    busqueda = input("¿que palabra busca? ")
    igualdad, ubicacion = buscador_de_palabras(texto, busqueda)
    if igualdad:
        print(f"La posicion de {busqueda} en el texto es {ubicacion.pop(0)}")
    else :
        print("La palabra buscada no esta en el texto")
        
if __name__ == "__main__":
    prueba()