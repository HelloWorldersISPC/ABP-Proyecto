from usuarios import registrar_usuario, iniciar_sesion
from menu import ejecutar_menu

def iniciar_aplicacion():
    usuarios = []
    dispositivos = []
    usuario_actual = None

    while usuario_actual is None:
        print("\n--- Bienvenido a SmartHome Solutions ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario_actual = registrar_usuario(usuarios)
        elif opcion == "2":
            usuario_actual = iniciar_sesion(usuarios)
        elif opcion == "3":
            print("¡Hasta luego!")
            return
        else:
            print("Opción inválida. Intente de nuevo.")

    ejecutar_menu(usuarios, dispositivos, usuario_actual)
