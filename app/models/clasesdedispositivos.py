class Dispositivo:
    def __init__(self, tipo, ubicacion, nombre, estado=True):
        self._tipo = tipo
        self._ubicacion = ubicacion
        self._nombre = nombre
        self._estado = estado
        
    def get_tipo(self):
        return self._tipo

    def get_ubicacion(self):
        return self._ubicacion

    def get_nombre(self):
        return self._nombre

    def get_estado(self):
        return self._estado


    def set_estado(self, nuevo_estado):
        if isinstance(nuevo_estado, bool):
            self._estado = nuevo_estado
        else:
            print("Error: El estado debe ser un valor booleano (Encendido/Apagar).")
