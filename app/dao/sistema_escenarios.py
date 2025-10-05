from escenarios import Escenario

class SistemaEscenarios:
    def __init__(self):
        self.__escenarios = []
        self.__next_id = 1

    def agregar_escenario(self, nombre, descripcion="", acciones=None):
        escenario = Escenario(
            id_escenario=self.__next_id,
            nombre=nombre,
            descripcion=descripcion,
            acciones=acciones
        )
        self.__escenarios.append(escenario)
        self.__next_id += 1
        print(f"Escenario '{nombre}' creado con éxito.")
        return escenario

    def listar_escenarios(self):
        if not self.__escenarios:
            print("No hay escenarios disponibles.")
            return
        print("\nEscenarios disponibles:")
        for i, esc in enumerate(self.__escenarios, 1):
            print(f"{i}. {esc.get_nombre()}")

    def usar_escenario(self, index, dispositivos):
        if index < 1 or index > len(self.__escenarios):
            print("Opción inválida.")
            return
        escenario = self.__escenarios[index - 1]
        escenario.ejecutar(dispositivos)
        print(f"Escenario '{escenario.get_nombre()}' aplicado.")

    def obtener_escenario_por_id(self, id_escenario):
        for esc in self.__escenarios:
            if esc.get_id_escenario() == id_escenario:
                return esc
        return None

    def eliminar_escenario(self, id_escenario):
        escenario = self.obtener_escenario_por_id(id_escenario)
        if escenario:
            self.__escenarios.remove(escenario)
            print(f"Escenario '{escenario.get_nombre()}' eliminado.")
            return True
        print("Escenario no encontrado.")
        return False