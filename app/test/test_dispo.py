import unittest 
from clasesdedispositivos import Dispositivo
from sistemas_disposi import SistemaDispositivos
import io
import sys

class Testdispositivo(unittest.TestCase):
  def setUp(self):
        self.dispo = Dispositivo("tipo1", "ubicacion1", "nombre1", True)

def test_creacion_dispositivo(self):
        self.assertEqual(self.dispo.get_tipo, "tipo1")
        self.assertEqual(self.dispo.get_ubicacion, "ubicacion1")
        self.assertEqual(self.dispo.get_nombre, "nombre1")
        self.assertEqual(self.dispo.get_estado, True)

class TestSistemaDispositivos(unittest.TestCase):

    def setUp(self):
        self.sistema = SistemaDispositivos()

    def test_agregar_dispositivo(self):
        dispositivo = self.sistema.agregar_dispositivo("Dispositivo1", "Test", [])
        self.assertIsNotNone(dispositivo)
        self.assertEqual(dispositivo.get_nombre(), "Dispositivo 1")

    def test_listar_dispositivos(self):
        self.sistema.agregar_dispositivo("Dispositivo 1", "Test", [])
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.sistema.listar_dispositivo()
        sys.stdout = sys.__stdout__
        salida = captured_output.getvalue()
        self.assertIn("Dispositivo1", salida)

    def test_eliminar_dispositivo(self):
        dispositivo = self.sistema.agregar_dispositivo("Eliminar", "", [])
        result = self.sistema.eliminar_dispositivo(dispositivo.get_nombre())
        self.assertTrue(result)
        self.assertIsNone(self.sistema.obtener_dispositivo_por_nombre(dispositivo.get_nombre()))



if __name__ == "__main__":
    unittest.main()