import re
from helpers import capitalizar
import sqlite3

def logging():
    logger = """
    __________________________________________
   |              INICIAR SESIÓN              |
    ------------------------------------------
    """
    print(logger)

    while True:  # 🔁 bucle controlado (no recursivo)
        errores = []

        email = input("Email:\n> ")
        patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron_email, email):
            errores.append("Email no válido, no cumple con el formato válido.")

        password = input("Password:\n> ")
        if len(password) > 15 or len(password) < 8:
            errores.append("La contraseña debe tener entre 8 y 15 carácteres.")

        if errores:
            print("❌ Errores encontrados:")
            for error in errores:
                print(f"- {error}")
            print("Corrija los errores e intente nuevamente.\n")
            continue  # 🔁 vuelve al inicio del bucle

        # 🔹 Verificar que el usuario exista en la base de datos
        conn = sqlite3.connect("registro_users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT nombre, apellido, email, contraseña FROM usuarios WHERE email = ?", (email,))
        fila = cursor.fetchone()
        conn.close()

        if fila is None:
            print("⚠️ No existe ninguna cuenta registrada con ese email.\n")
            continue  # 🔁 vuelve a pedir datos
        elif fila[3] != password:
            print("❌ Contraseña incorrecta.\n")
            continue  # 🔁 vuelve a pedir datos
        else:
            nombre, apellido, email, contraseña = fila
            print(f"✅ Inicio de sesión exitoso. ¡Bienvenido {nombre}!\n")
            return nombre, apellido, email, contraseña




