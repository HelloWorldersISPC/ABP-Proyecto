import unittest
from usuarios import Usuario
from sistemausuarios import SistemaUsuarios
import io
import sys

class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.user = Usuario(1, "test@test.com", "Gastón", "1234")

    def test_creacion_usuario(self):
        self.assertEqual(self.user.get_email(), "test@test.com")
        self.assertEqual(self.user.get_nombre(), "Gastón")
        self.assertEqual(self.user.get_rol(), "invitado")

    def test_verificar_contrasena_correcta(self):
        self.assertTrue(self.user.verificar_contrasena("1234"))

    def test_verificar_contrasena_incorrecta(self):
        self.assertFalse(self.user.verificar_contrasena("wrong"))

    def test_cambiar_contrasena_correcta(self):
        resultado = self.user.cambiar_contrasena("1234", "nueva")
        self.assertTrue(resultado)
        self.assertTrue(self.user.verificar_contrasena("nueva"))

    def test_cambiar_contrasena_incorrecta(self):
        resultado = self.user.cambiar_contrasena("mala", "nueva")
        self.assertFalse(resultado)
        self.assertTrue(self.user.verificar_contrasena("1234"))

    def test_cambiar_nombre_valido(self):
        self.user.set_nombre("Gastón O.")
        self.assertEqual(self.user.get_nombre(), "Gastón O.")

    def test_cambiar_nombre_invalido(self):
        self.user.set_nombre("   ")
        self.assertEqual(self.user.get_nombre(), "Gastón")


class TestSistemaUsuarios(unittest.TestCase):

    def setUp(self):
        self.sistema = SistemaUsuarios()

    

    def test_admin_por_defecto(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output   
        self.sistema.listar_usuarios()
        sys.stdout = sys.__stdout__  

        salida = captured_output.getvalue()
        self.assertIn("admin@smarthome.com", salida)
        self.assertIn("Administrador", salida)


    def test_registro_usuario_valido(self):
        usuario = self.sistema.registrar_usuario("test@test.com", "Gastón", "1234")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.get_email(), "test@test.com")

    def test_registro_email_duplicado(self):
        self.sistema.registrar_usuario("test@test.com", "Gastón", "1234")
        usuario2 = self.sistema.registrar_usuario("test@test.com", "Otro", "1234")
        self.assertIsNone(usuario2)

    def test_registro_email_invalido(self):
        usuario = self.sistema.registrar_usuario("mal-correo", "Gastón", "1234")
        self.assertIsNone(usuario)

    def test_login_correcto(self):
        self.sistema.registrar_usuario("test@test.com", "Gastón", "1234")
        usuario = self.sistema.iniciar_sesion("test@test.com", "1234")
        self.assertIsNotNone(usuario)

    def test_login_incorrecto(self):
        self.sistema.registrar_usuario("test@test.com", "Gastón", "1234")
        usuario = self.sistema.iniciar_sesion("test@test.com", "wrong")
        self.assertIsNone(usuario)

    def test_editar_rol_existente(self):
        usuario = self.sistema.registrar_usuario("test@test.com", "Gastón", "1234")
        print("Usuario creado:", usuario)  
        actualizado = self.sistema.editar_rol_usuario("test@test.com", "administrador")
        print("Usuario actualizado:", actualizado)  #
        self.assertIsNotNone(actualizado)
        self.assertEqual(actualizado.get_rol(), "administrador")

    def test_editar_rol_inexistente(self):
        actualizado = self.sistema.editar_rol_usuario("noexiste@test.com", "administrador")
        self.assertIsNone(actualizado)


if __name__ == "__main__":
    unittest.main()


