from logging import logging
from crear_cuenta import crear_cuenta

def menu_logging():

    print("¿Ya tienes una cuenta con nosotros?, inicia sesión o registrate a continuación.")
    print("1. Iniciar sesión")
    print("2. Registrarse")

    opcion = input("Elige una de las opciones: ")
    if opcion == "1":    
        return logging()
    if opcion == "2":
        return crear_cuenta()
    else:
        print("Opción no valida, intente con 1 o 2.\n")
        return menu_logging()
