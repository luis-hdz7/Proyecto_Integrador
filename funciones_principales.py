import re
from catalogos import catalogo_venta, catalogo_renta

#Compra y renta de Autos

#Saluda al usuario
def saludar(nombre, apellido):
    print(f"Hola {nombre} {apellido}, bienvenido al concesionario.\n")



def mostrar_menu():
    opciones = input("""Elige una opcion:
1. Comprar un auto
2. Rentar un auto
3. Salir
> """).strip()
    print("")
    return opciones


#Le muestra al usuario los auto disponibles en venta
def mostrar_auto_venta():
    print("🚗 Autos disponibles en venta:\n ")
    for nombre, datos in catalogo_venta.items():
        print(f"-{nombre}: Modelo: {datos['modelo']}, ${datos['precio']:,}")
        print("")
#Le muestra al usuario los auto disponibles en renta
def mostrar_auto_renta():
    print("🚗 Autos disponibles en renta:\n ")
    for nombre, datos in catalogo_renta.items():
        print(f"-{nombre}: Modelo: {datos['modelo']}, ${datos['precio']:.2f} (Día)")
        print("")

def buscar_auto_venta(nombre_auto):
    return catalogo_venta.get(nombre_auto, "No existe el modelo de automovil seleccionado")

def buscar_auto_renta(nombre_auto):
    return catalogo_renta.get(nombre_auto, "No existe el modelo de automovil seleccionado")

    
def metodo_pago():

    print("Metodos de pago validos:  Efectivo | Tarjeta | Transferencia")
#Comportamiento del código dependiendo del metodo de pago
    while True:
        metodo = input("Ingrese su metodo de pago: ").strip().capitalize()
        if metodo in ["Efectivo", "Tarjeta", "Transferencia"]:
            if metodo == "Efectivo":
                print("💵 Coloque el dinero")
                pago = input("> Coloque monto $: ")
                return {
                    "Metodo" : "Efectivo",
                    "Detalle" : "pago en efectivo",
                    "Monto" : pago
                }
            if metodo == "Tarjeta":
                print("💳 Ingrese su tarjeta:")
                tarjeta = input("> Número de tarjeta: ").strip()
                cvv = input("CVV: ").strip()
                return {
                    "Metodo" : "Tarjeta",
                    "Detalle" : "pago con tarjeta",
                    "Tarjeta" : tarjeta,
                    "CVV" : cvv 
                }
            if metodo == "Transferencia":
                print("🔁 Ingrese su número de cuenta:")
                cuenta = input("> Número de cuenta: ").strip()
                return {
                    "Metodo" : "Transferencia",
                    "Detalle" : "pago con transferencia",
                    "Cuenta" : cuenta
                }    
        else:
            print("❌ Opcion de pago no valida, intente nuevamente.")

    


