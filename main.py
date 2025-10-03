from contratos import contrato_compra, contrato_renta
from catalogos import catalogo_venta, catalogo_renta
from funciones_principales import  saludar, mostrar_auto_venta, mostrar_auto_renta, buscar_auto_venta, buscar_auto_renta, metodo_pago, mostrar_menu
from logging import logging
from crear_cuenta import crear_cuenta
from menu_logging import menu_logging

def menu_principal():
    concesonario = """  
        -------------------------------------------  
        |       CONCESIONARIO LEÓN MOTORS         |  
        -------------------------------------------

    """ 
    print(concesonario)

    nombre, apellido, email, password = menu_logging()
    email, password = logging()
    saludar(nombre, apellido)

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            mostrar_auto_venta()
            nombre_auto = input("Ingrese el nombre del modelo de automovil: ").strip()
            auto = buscar_auto_venta(nombre_auto)
            if isinstance(auto, dict): 
                metodo = metodo_pago()
                contrato_compra("Concesionario León Motors", f"{nombre} {apellido}", auto, auto['precio'], metodo)
            else: 
                print("❌ Auto no encontrado, intente nuevamente.")
        
        elif opcion == "2":
            mostrar_auto_renta()
            nombre_auto = input("Ingrese el nombre del modelo de automovil: ").strip()
            auto = buscar_auto_renta(nombre_auto)
            if isinstance(auto, dict):
                try: 
                    dias = int(input("Ingrese el número de días de renta: "))
                    metodo = metodo_pago()
                    contrato_renta("Concesionario León Motors", f"{nombre} {apellido}", auto, dias, metodo)
                except ValueError:
                    print("❌ Número de días no definido (solo números enteros), intente nuevamente.")
            else:
                print("❌ Auto no encontrado, intente nuevamente.")
        elif opcion == "3":
            print("👋 Gracias por visitar nuestro Concesionario, Hasta pronto!")
            break

        else: 
            print("❌ Opción no valida, intente con 1, 2 o 3.")

            

menu_principal()