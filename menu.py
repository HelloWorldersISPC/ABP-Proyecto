from dispositivos import (
    listar_dispositivos,
    agregar_dispositivo,
    eliminar_dispositivo,
    usar_dispositivo
)
from usuarios import registrar_usuario, iniciar_sesion, lista_usuarios,editar_rol_usuario
from escenarios import (
    escenarios,
    usar_escenario,
    agregar_escenario,
    escenarios_predefinidos
)


usuarios = [{
        "id_usuario": 1,
        "email": 'admin@admin.com',
        "contrasena_hash": 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', # password: 123
        "nombre": 'admin 1',
        "rol": "administrador",
    }]
dispositivos = []


def menu_administrador(dispositivos, escenarios, rol_actual="admin"):
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Listar dispositivos")
        print("2. Agregar dispositivo")
        print("3. Eliminar dispositivo")
        print("4. Usar y configurar dispositivo")
        print("5. Escenarios")
        print("6. Agregar Escenario")
        print("7. Listar usuarios")
        print("8. Cambiar rol de usuario")
        print("0. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listar_dispositivos(dispositivos)
        elif opcion == '2':
            agregar_dispositivo(dispositivos, rol_actual, escenarios)
        elif opcion == '3':
            eliminar_dispositivo(dispositivos)
        elif opcion == '4':
            usar_dispositivo(dispositivos)
        elif opcion == '5':
            usar_escenario(escenarios, dispositivos)
        elif opcion == '6':
            agregar_escenario(escenarios)
        elif opcion == '7':
            lista_usuarios(usuarios)
        elif opcion == '8':
            editar_rol_usuario(usuarios)
        elif opcion == '0':
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")

def menu_invitado(dispositivos, escenarios, rol_actual="invitado"):
    while True:
        print("\n--- Menú Invitado ---")
        print("1. Listar dispositivos")
        print("2. Usar y configurar dispositivo")
        print("3. Escenarios")
        print("4. Datos personales")
        print("0. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listar_dispositivos(dispositivos)
        elif opcion == '2':
            usar_dispositivo(dispositivos)
        elif opcion == '3':
            usar_escenario(escenarios, dispositivos)
        elif opcion == '4':
            continue  
        elif opcion == '0':
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")

def ejecutar_menu():

    escenarios.clear()
    escenarios.extend(escenarios_predefinidos)

    while True:
        print("\n--- SmartHome Solutions ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario(usuarios)
        elif opcion == '2':
            usuario = iniciar_sesion(usuarios)
            if usuario:
                if usuario["rol"] == "administrador":
                    menu_administrador(dispositivos, escenarios, rol_actual="admin")
                elif usuario["rol"] == "invitado":
                    menu_invitado(dispositivos, escenarios, rol_actual="invitado")
        elif opcion == '3':
            print("Gracias por usar SmartHome Solutions. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


