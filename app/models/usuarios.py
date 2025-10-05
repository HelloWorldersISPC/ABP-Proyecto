class Usuario:
    def __init__(self, id_usuario, email, nombre, contrasena, rol="invitado"):
        self.__id_usuario = id_usuario
        self.__email = email
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__rol = rol

    def get_id_usuario(self):
        return self.__id_usuario

    def get_email(self):
        return self.__email

    def get_nombre(self):
        return self.__nombre

    def get_rol(self):
        return self.__rol

    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre.strip():
            self.__nombre = nuevo_nombre

    def set_rol(self, nuevo_rol):
        if nuevo_rol in ["administrador", "invitado"]:
            self.__rol = nuevo_rol

    def verificar_contrasena(self, contrasena):
        return self.__contrasena == contrasena

    def cambiar_contrasena(self, actual, nueva):
        if self.verificar_contrasena(actual):
            self.__contrasena = nueva
            return True
        return False

    def __str__(self):
        return (f"ID: {self.__id_usuario}, "
                f"Email: {self.__email}, "
                f"Nombre: {self.__nombre}, "
                f"Rol: {self.__rol}")



