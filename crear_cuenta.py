import re
import os 
import sqlite3
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
    patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron_email, email):
        errores.append("Email no válido, no cumple con el formato establecido.")
    
    password = input("Password: ")
    if len(password) > 15 or len(password) < 8:
        errores.append("La contraseña debe tener entre 8 y 15 carácteres.")
    

    if errores:
        print("❌ Errores encontrados:")
        for error in errores:
            print(f"- {error}")
        print("Corrija los errores e intente nuevamente.\n")
        return crear_cuenta()
    else:
        agregar_usuario(nombre, apellido, email, password)
        return nombre, apellido, email, password


def agregar_usuario(nombre, apellido, email, contraseña):
    conn = sqlite3.connect('registro_users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO usuarios (nombre, apellido, email, contraseña)
            VALUES (?, ?, ?, ?)
        ''', (nombre, apellido, email, contraseña))
        conn.commit()
        print("✅ Usuario agregado correctamente")
    except sqlite3.IntegrityError:
        print("⚠️ El email ya está registrado, inicia sesión o cambia el email")
    finally:
        conn.close()
