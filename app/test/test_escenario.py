import unittest
from escenarios import Escenario
from sistema_escenarios import SistemaEscenarios
import io
import sys

class TestEscenario(unittest.TestCase):

    def setUp(self):
        def apagar_todo(dispositivos):
            for d in dispositivos:
                d["estado"] = False

        self.accion_apagar = apagar_todo
        self.escenario = Escenario(1, "Apagar todo", "Apaga todos los dispositivos", [self.accion_apagar])

    def test_creacion_escenario(self):
        self.assertEqual(self.escenario.get_id_escenario(), 1)
        self.assertEqual(self.escenario.get_nombre(), "Apagar todo")
        self.assertEqual(self.escenario.get_descripcion(), "Apaga todos los dispositivos")
        self.assertEqual(len(self.escenario.get_acciones()), 1)

    def test_agregar_accion(self):
        def encender_todo(dispositivos):
            for d in dispositivos:
                d["estado"] = True
        self.escenario.agregar_accion(encender_todo)
        self.assertEqual(len(self.escenario.get_acciones()), 2)

    def test_ejecutar_accion(self):
        dispositivos = [{"nombre": "Luz 1", "estado": True}]
        self.escenario.ejecutar(dispositivos)
        self.assertFalse(dispositivos[0]["estado"])


class TestSistemaEscenarios(unittest.TestCase):

    def setUp(self):
        self.sistema = SistemaEscenarios()

    def test_agregar_escenario(self):
        escenario = self.sistema.agregar_escenario("Escenario 1", "Test", [])
        self.assertIsNotNone(escenario)
        self.assertEqual(escenario.get_nombre(), "Escenario 1")

    def test_listar_escenarios(self):
        self.sistema.agregar_escenario("Escenario 1", "Test", [])
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.sistema.listar_escenarios()
        sys.stdout = sys.__stdout__
        salida = captured_output.getvalue()
        self.assertIn("Escenario 1", salida)

    def test_usar_escenario(self):
        def apagar(dispositivos):
            for d in dispositivos:
                d["estado"] = False
        escenario = self.sistema.agregar_escenario("Apagar", "", [apagar])
        dispositivos = [{"nombre": "Luz", "estado": True}]
        self.sistema.usar_escenario(1, dispositivos)
        self.assertFalse(dispositivos[0]["estado"])

    def test_eliminar_escenario(self):
        escenario = self.sistema.agregar_escenario("Eliminar", "", [])
        result = self.sistema.eliminar_escenario(escenario.get_id_escenario())
        self.assertTrue(result)
        self.assertIsNone(self.sistema.obtener_escenario_por_id(escenario.get_id_escenario()))

    def test_eliminar_escenario_inexistente(self):
        result = self.sistema.eliminar_escenario(999)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()