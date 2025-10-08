import re
import os 
import json
from helpers import capitalizar
errores = []

def crear_cuenta():
    new_acount = """
    __________________________________________
   |               CREAR CUENTA               |
    ------------------------------------------
    """
    print(new_acount)
    print("porfavor ingrese sus datos para continuar.")
    

    nombre = input("Nombre: ")
    nombre = capitalizar(nombre)
    if not nombre.isalpha():
        errores.append("Nombre no válido, solo se admiten carácteres alfabéticos.") 
        

    apellido = input("Apellido: ")
    apellido = capitalizar(apellido)
    if not apellido.isalpha():
        errores.append("Apellido no válido, solo se admiten carácteres alfabéticos.")


    email = input("Email: ")
    patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'#Esta expresión regular verifica que la cadena tenga una estructura básica del tipo usuario@dominio.extension
    if not re.match(patron_email, email):
        errores.append("Email no válido, no cumple con el formato establecido.")
    
    password = input("Password: ")
    if len(password) > 15 or len(password) < 8:
        errores.append("La contraseña debe tener entre 8 y 15 carácteres.")

    else:
        if not os.path.exists("usuarios.json"):
            with open("usuarios.json", "w") as archivo:
                json.dump({}, archivo) 
    
        with open("usuarios.json", "r") as archivo:
            usuarios_registrados = json.load(archivo)

       
            if email in usuarios_registrados:
                print("¡Ya existe una cuenta registrada con ese email!, inicie sesión.")
            else:
                usuarios_registrados[email] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "password": password
                }
        # Se agrega un nuevo perfil de usuario
                with open("usuarios.json", "w") as archivo:
                    json.dump(usuarios_registrados, archivo, indent = 4)
                    print("✅ Usuario registrado exitosamente.\n")
    
    

    if errores:
        print("❌ Errores encontrados:")
        for error in errores:
            print(f"- {error}")
        print("Corrija los errores e intente nuevamente.\n")
        return crear_cuenta()
    else:

        return nombre, apellido, email, password
