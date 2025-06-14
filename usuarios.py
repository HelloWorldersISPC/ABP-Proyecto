import hashlib    #Cifrar contraseñas con hash seguro (SHA-256)
import re         #Para asegurarse de que el usuario ingrese un email válido como usuario@dominio.com

def solicitar_rol(): # esta es para para poder ediar el rol del usuario desde el menu administrador 
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
    print(f"Usuario {nombre} registrado.")
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

def lista_usuarios(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("\nLista de usuarios:")
    for usuario in usuarios:
        print(f"ID: {usuario['id_usuario']}, \nEmail: {usuario['email']}, \nNombre: {usuario['nombre']}, \nRol: {usuario['rol']}")

def editar_rol_usuario(usuarios):
    lista_usuarios(usuarios)
    email_editar = input("\nIngresa el Email de usuario a editar: ").strip().lower()
    
    for usuario in usuarios:
        if usuario["email"] == email_editar:
            nuevo_rol = solicitar_rol()
            usuario["rol"] = nuevo_rol
            print(f"Rol del usuario {usuario['nombre']} actualizado a {nuevo_rol}.")
            return
    
    print("Usuario no encontrado.")
    
def ver_mi_perfil(usuario_actual):
    if usuario_actual:
        print("\n--- Mis Datos ---")
        print(f"Nombre: {usuario_actual['nombre']}")
        print(f"Email: {usuario_actual['email']}")
        print(f"Rol: {usuario_actual['rol']}")
    else:
        print("No has iniciado sesión.")


