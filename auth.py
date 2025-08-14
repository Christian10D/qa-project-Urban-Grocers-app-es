import json
import os

USER_FILE = "user.json"

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r")as f:
        return json.load(f)

def save_users(users):
        with open(USER_FILE, "w")as f:
            json.dump(users, f)

def registrer(username, password):
    users=load_users()
    if username in users()
        return "Usuario ya registrado"
    users[username]=password
    save_users(users)
    return "Registro completado"

def login(username, password):
    save_users=load_users()
    if username not in users:
        return "usuario no encontrado"
    if users[username]!=password:
        return "contraseña incorrecta"
    return "inicio de sesion correcto"

def logout(username):
    return f"{username} ha cerrado sesion"
