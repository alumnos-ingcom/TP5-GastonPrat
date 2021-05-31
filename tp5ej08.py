################
# Gastón Emanuel Prat - @GastonPrat
# Trabajo Práctico N°5
# Ejercicio 07
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej01 import IngresoIncorrecto, ingreso_entero

def ingreso_entero_restringido(mensaje,minimo = 1, maximo = 40):
    rot = ingreso_entero(mensaje)
    if (rot >= minimo and rot <= maximo):
        return rot
        print(f"El numero ingresado {num} es correcto")
    else:
        raise IngresoIncorrecto("El nomero ingresado no pertenece "
                                f"al rango entre {maximo} y {minimo}")

def cifrado_cesar(texto, rot):
    encriptado = ""
    for c in texto:
        temp = ord(c)
        if temp >= ord("A") and temp <= ord("Z"):
            temp = temp + rot
            while temp > ord("Z"):
                temp = temp - 26
                
            encriptado += chr(temp)
        elif temp >= ord("a") and temp <= ord("z"):
            temp = temp + rot
            while temp > ord("z"):
                temp = temp - 26
                
            encriptado += chr(temp)
        elif temp >= ord("0") and temp <= ord("9"):
            temp = temp + rot
            while temp > ord("9"):
                temp = temp - 10
                
            encriptado += chr(temp)
        elif temp == ord(" "):
            encriptado += chr(temp)
    return encriptado
                
def decodificado_cesar(encriptado, rot):
    decodificado = ""
    for c in encriptado:
        temp = ord(c)
        if temp >= ord("A") and temp <= ord("Z"):
            temp = temp - rot
            while temp < ord("A"):
                temp = temp + 26
                
            decodificado += chr(temp)
        elif temp >= ord("a") and temp <= ord("z"):
            temp = temp - rot
            while temp < ord("a"):
                temp = temp + 26
                
            decodificado += chr(temp)
        elif temp >= ord("0") and temp <= ord("9"):
            temp = temp - rot
            while temp < ord("0"):
                temp = temp + 10
                
            decodificado += chr(temp)
        elif temp == ord(" "):
            decodificado += chr(temp)
    return decodificado
            

def prueba():
    print("El programa encriptara el texto ingresado"
          "segun el factor de rotacion que especifique")
    texto = input("Escriba el texto a encriptar: ")
    rot = ingreso_entero_restringido("Factor de rotación entre 1 y 40")
    encriptado = cifrado_cesar(texto, rot)
    print(f"su ingreso encriptado es: {encriptado}")
    decodificado = decodificado_cesar(encriptado, rot)
    print(f"su ingreso decodificado es: {decodificado}")
    

if __name__ == "__main__":
    prueba()