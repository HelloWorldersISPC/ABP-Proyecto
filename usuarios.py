import hashlib    #Cifrar contraseñas con hash seguro (SHA-256)
import re         #Para asegurarse de que el usuario ingrese un email válido como usuario@dominio.com

def solicitar_rol():
    print("Seleccione rol:")
    print("1. Administrador")
    print("2. Invitado")
    rol_opcion = input("Ingrese opción (1-2): ")
    roles = {"1": "administrador", "2": "invitado"}
    return roles.get(rol_opcion, "invitado")

def es_email_valido(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email)

def registrar_usuario(usuarios):
    while True:
        email = input("Ingrese email: ").strip().lower()

        if not es_email_valido(email):
            print("Error: El email no tiene un formato válido (ejemplo: usuario@dominio.com).")
            continuar = input("¿Desea intentar registrarse de nuevo? (s/n):")
            if continuar != 's':
                return None
            continue

        if any(u['email'] == email for u in usuarios):
            print("Error: El email ya está registrado.")
            return None

        break

    nombre = input("Ingrese nombre: ").strip()
    contrasena = input("Ingrese contraseña: ").strip()
    contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()

    id_usuario = len(usuarios) + 1
    usuario = {
        "id_usuario": id_usuario,
        "email": email,
        "contrasena_hash": contrasena_hash,
        "nombre": nombre,
        "rol": "invitado",
    }
    usuarios.append(usuario)
    print(f"Usuario {nombre} registrado con rol '{rol}'.")
    return usuario

def iniciar_sesion(usuarios):
    email = input("Email: ").strip().lower()
    contrasena = input("Contraseña: ").strip()
    contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()

    for usuario in usuarios:
        if usuario["email"] == email and usuario["contrasena_hash"] == contrasena_hash:
            print(f"¡Inicio de sesión exitoso! Bienvenido/a {usuario['nombre']}")
            return usuario
    print("Email o contraseña incorrectos.")
    return None
if __name__ == "__main__":
    # Define las credenciales del usuario administrador
    ADMIN_EMAIL = "admin@example.com"
    ADMIN_PASSWORD = "admin123" # ¡En un entorno real, esto no estaría hardcodeado y se gestionaría de forma más segura!
    ADMIN_NAME = "Administrador"
    ADMIN_ROLE = "administrador"

    # Calcula el hash de la contraseña del administrador
    admin_password_hash = hashlib.sha256(ADMIN_PASSWORD.encode()).hexdigest()

    # Crea el usuario administrador
    usuario_admin = {
        "id_usuario": 1, # Se le asigna el primer ID
        "email": ADMIN_EMAIL,
        "contrasena_hash": admin_password_hash,
        "nombre": ADMIN_NAME,
        "rol": ADMIN_ROLE
    }

    # Inicializa la lista de usuarios con el usuario administrador
    usuarios = [usuario_admin]
    print(f"Usuario administrador '{ADMIN_NAME}' precargado.")

    # --- Ejemplo de uso del sistema ---
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario(usuarios)
        elif opcion == '2':
            usuario_actual = iniciar_sesion(usuarios)
            if usuario_actual:
                print(f"Usuario logueado: {usuario_actual['email']} con rol {usuario_actual['rol']}")
                # Aquí podrías añadir lógica para diferentes roles
                if usuario_actual['rol'] == 'administrador':
                    print("Acceso a funciones de administrador.")
                else:
                    print("Acceso a funciones de invitado.")
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
   
