import hashlib    #Cifrar contraseñas con hash seguro (SHA-256)
import re         #Para asegurarse de que el usuario ingrese un email válido como usuario@dominio.com

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
