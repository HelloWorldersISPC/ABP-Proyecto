from clasesdedispositivos import Dispositivo

class SistemaDispositivos:
    def __init__(self):
        self.__dispositivo = []


    def agregar_dispositivo(self,tipo, ubicacion="",nombre="" , estado=None):
        dispositivo = Dispositivo(
            tipo=tipo,
            ubicacion=ubicacion,
            nombre=nombre,
            estado=estado
        
        )
        self.__dispositivo.append(dispositivo)
        print(f"dispositivo '{nombre}' creado con éxito.")
        return dispositivo

    def listar_dispositivo(self):
        if not self.__dispositivo:
            print("No hay dispositivo disponibles.")
            return
        print("\ndispositivos disponibles:")
        for i, esc in enumerate(self.__dispositivo, 1):
            print(f"{i}. {esc.get_nombre()}")

    def obtener_dispositivo_por_nombre(self, nombre):
        for esc in self.__dispositivo:
            if esc.get_nombre() == nombre:
                return esc
        return None

    def eliminar_dispositivo(self, nombre):
        dispositivo = self.obtener_dispositivo_por_nombre(nombre)
        if dispositivo:
            self.__dispositivo.remove(dispositivo)
            print(f"Dispositivo '{dispositivo.get_nombre()}' eliminado.")
            return True
        print("Dispositivo  no encontrado.")
        return False




