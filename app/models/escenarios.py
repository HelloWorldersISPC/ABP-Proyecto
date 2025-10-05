class Escenario:
    def __init__(self, id_escenario, nombre, descripcion="", acciones=None):
        self.__id_escenario = id_escenario
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__acciones = acciones if acciones is not None else []

    def get_id_escenario(self):
        return self.__id_escenario

    def get_nombre(self):
        return self.__nombre

    def get_descripcion(self):
        return self.__descripcion

    def get_acciones(self):
        return self.__acciones

    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre.strip():
            self.__nombre = nuevo_nombre

    def set_descripcion(self, nueva_descripcion):
        self.__descripcion = nueva_descripcion

    def set_acciones(self, nuevas_acciones):
        if isinstance(nuevas_acciones, list):
            self.__acciones = nuevas_acciones

    def agregar_accion(self, accion):
        self.__acciones.append(accion)

    def ejecutar(self, dispositivos):
        for accion in self.__acciones:
            accion(dispositivos)

    def __str__(self):
        return (f"ID Escenario: {self.__id_escenario}, "
                f"Nombre: {self.__nombre}, "
                f"Descripción: {self.__descripcion}, "
                f"Acciones: {len(self.__acciones)}")