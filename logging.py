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

    errores = []

    email = input("Email: ")
    patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'#Esta expresión regular verifica que la cadena tenga una estructura básica del tipo usuario@dominio.extension
    if not re.match(patron_email, email):
        errores.append("Email no válido, no cumple con el formato válido.")

    password = input("Password: ")
    if len(password) > 15 or len(password) < 8:
        errores.append("La contraseña debe tener entre 8 y 15 carácteres.")

    if errores:
        print("❌ Errores encontrados:")
        for error in errores:
            print(f"- {error}")
        print("Corrija los errores e intente nuevamente.")
        return logging()
   
    # 🔹 Verificar que el usuario exista en la base de datos
    conn = sqlite3.connect("registro_users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT contraseña FROM usuarios WHERE email = ?", (email,))
    fila = cursor.fetchone()

    conn.close()

    if fila is None:
        print("⚠️ No existe ninguna cuenta registrada con ese email.\n")
        return logging()
    elif fila[0] != password:
        print("❌ Contraseña incorrecta.\n")
        return logging()
    else:
        print("✅ Inicio de sesión exitoso. ¡Bienvenido!\n")
        return email, password



