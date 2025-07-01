from auth import registrer, login, logout

def mostrar_menu():
    print("\n--MENU--")
    print("1.-Registrarse")
    print("2.-Iniciar sesion")
    print("2.-Salir")

    def main():
        usuario_actual= None

        while True:
            mostrar_menu()
            opcion=input("elige una opcion: ")

            if opcion=="1":
                user=input("Nombre de usuario: ")
                pwd = input("contraseña: ")
                print(registrer(user,pwd))

            elif opcion=="2":
                if usuario_actual:
                    print(f"Ya has iniciado sesion como {usuario actual}")
                else:
                    user=input("Nombre de usuario: ")
                    pwd = input("contraseña: ")
                    resultado=login(user, pwd)
                    print(resultado)
                    if resultado == "inicio de sesion correcto":
                        usuario_actual=user

            elif opcion =="3":
                if usuario_actual:
                    print(logout(usuario_actual))
                    print("hasta luego")
                    break

                else:
                    print("opcion invalida")
                if __name__ == "__main__":
                main()
