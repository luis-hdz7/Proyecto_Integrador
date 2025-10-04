from  datetime import datetime
#Contrato en caso de que el usuario decida comprar un auto
def contrato_compra(nombre_vendedor, nombre_comprador, auto, precio, metodo_pago ):
    fecha_emision = datetime.now().strftime("%d/%m/%Y a las %H:%M horas")
    #datetime.now() devuelve la hora y fecha al momento de ejecución
    # strftime(...) → da formato a esa fecha y hora en forma de texto
    print("\n📄 Generando contrato de compraventa del auto..\n ")

    
    contrato = f"""
    ------------------------------------------------
                 CONTRATO DE COMPRAVENTA 
                 DE VEHICULO USADO
    ------------------------------------------------
    
    COMPRADOR:
    nombre: {nombre_comprador}

    VENDEDOR:
    nombre: {nombre_vendedor}

    VEHICULO:
    marca: {auto['marca']}
    modelo: {auto['modelo']}
    precio: ${precio:.2f}

    METODO DE PAGO:
    Método: {metodo_pago['Metodo']}
    Detalle: {metodo_pago['Detalle']}
    ________________________________________________
    """
    if metodo_pago['Metodo'] == "Efectivo":
        contrato += f"Monto: ${metodo_pago['Monto']}\n"

    elif metodo_pago['Metodo'] == "Tarjeta":
        contrato += f"Tarjeta: {metodo_pago['Tarjeta']}\nCVV: {metodo_pago['CVV']}\n"

    elif metodo_pago['Metodo'] == "Transferencia":
        contrato += f"Cuenta: {metodo_pago['Cuenta']}\n"

    contrato += f"""
    --------------------------------------------------
    DECLARACIONES:
    - El vendedor declara ser el legítimo propietario del vehículo y que se encuentra libre de gravámenes, multas o reportes de robo.
    - El comprador acepta las condiciones del vehículo en el estado actual.
    - Ambas partes acuerdan formalizar la transacción en los términos aquí descritos.

    FECHA DE EMISIÓN: {fecha_emision}

    FIRMA DEL VENDEDOR: _________________

    FIRMA DEL COMPRADOR: _________________

    ------------------------------------------------
    """

    print(contrato)
    return contrato

#Contrato en caso de que el usuario decida comprar un auto
def contrato_renta(nombre_proveedor, nombre_cliente, auto, dias, metodo_pago ):
    
    precio_dia = auto['precio']
    total = precio_dia * dias
    fecha_emision = datetime.now().strftime("%d/%m/%Y a las %H:%M horas")
    #datetime.now() devuelve la hora y fecha al momento de ejecución
    # strftime(...) → da formato a esa fecha y hora en forma de texto
    print("\n📄 Generando contrato de renta del auto..\n ")



    contrato = f"""
    ------------------------------------------------
                   CONTRATO DE RENTA 
                   DE VEHICULO 
    ------------------------------------------------

    CLIENTE:
    nombre: {nombre_cliente}

    PROVEEDOR:
    nombre: {nombre_proveedor}

    VEHICULO:
    marca: {auto['marca']}
    modelo: {auto['modelo']}
    precio por día: ${auto['precio']:.2f}
    dias de renta: {dias}
    TOTAL A PAGAR: ${total:.2f}

    METODO DE PAGO:
    Método: {metodo_pago['Metodo']}
    Detalle: {metodo_pago['Detalle']}
    
    """
    if metodo_pago['Metodo'] == "Efectivo":
        contrato += f"Monto: ${metodo_pago['Monto']}\n"

    elif metodo_pago['Metodo'] == "Tarjeta":
        contrato += f"Tarjeta: {metodo_pago['Tarjeta']}\nCVV: {metodo_pago['CVV']}\n"

    elif metodo_pago['Metodo'] == "Transferencia":
        contrato += f"Cuenta: {metodo_pago['Cuenta']}\n"

    contrato += f"""
    ________________________________________________

    DECLARACIONES:
    - El cliente debe entregar el vehículo en buen estado mecánico y estético.
    - Si se devuelve despúes de la fecha establecida, pueden presentarse cargos adicionales.
    - Solo se permite conducir a la persona autorizada en el contrato.
    - El vehículo no debe de usarse para cometer actos de violencia o crimen.
    - El cliente es responsable de cualquier daño, pérdida o multa mientras dure el tiempo de renta.
    - PROHIBICIONES:
        ● No se permite fumar dentro del vehículo.
        ● No se permite modificar o alterar el vehículo.
        ● No se permite subarrendar el vehículo.

    FECHA DE EMISIÓN: {fecha_emision}

    FIRMA DEL VENDEDOR: _________________

    FIRMA DEL COMPRADOR: _________________

    ------------------------------------------------
    """
    print(contrato)
    return contrato


