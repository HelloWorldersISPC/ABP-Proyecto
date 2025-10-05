from usuarios import *
import re
class SistemaUsuarios:
    def __init__(self):
        self.__usuarios = []
        self.__next_id = 1
        
        admin = Usuario(
            id_usuario=self.__next_id,
            email="admin@smarthome.com",
            nombre="Administrador",
            contrasena="admin123",
            rol="administrador"
        )
        self.__usuarios.append(admin)
        self.__next_id += 1

    @staticmethod
    def es_email_valido(email):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, email)

    def registrar_usuario(self, email, nombre, contrasena):
        if not self.es_email_valido(email):
            print("Error: El email no tiene un formato válido.")
            return None
        if any(u.get_email() == email for u in self.__usuarios):
            print("Error: El email ya está registrado.")
            return None

        usuario = Usuario(self.__next_id, email, nombre, contrasena)
        self.__usuarios.append(usuario)
        self.__next_id += 1
        print(f"Usuario {nombre} registrado con éxito.")
        return usuario

    def iniciar_sesion(self, email, contrasena):
        for usuario in self.__usuarios:
            if usuario.get_email() == email and usuario.verificar_contrasena(contrasena):
                print(f"¡Inicio de sesión exitoso! Bienvenido/a {usuario.get_nombre()}")
                return usuario
        print("Email o contraseña incorrectos.")
        return None

    def listar_usuarios(self):
        if not self.__usuarios:
            print("No hay usuarios registrados.")
            return
        print("\nLista de usuarios:")
        for u in self.__usuarios:
            print(u)

    def editar_rol_usuario(self, email, nuevo_rol):
        for usuario in self.__usuarios:
            if usuario.get_email() == email:
                usuario.set_rol(nuevo_rol)
                print(f"Rol de {usuario.get_nombre()} actualizado a {nuevo_rol}.")
                return usuario
        print("Usuario no encontrado.")