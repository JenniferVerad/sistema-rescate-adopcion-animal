import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from rescate.modelo import Estado, ExpedienteGato, ExpedienteFaunaSilvestre, fabrica_para
from rescate.notificaciones import Voluntario
from rescate.servicio import GestorCasos


class TestPatrones(unittest.TestCase):
    def setUp(self):
        GestorCasos.reiniciar()

    def test_singleton(self):
        self.assertIs(GestorCasos(), GestorCasos())

    def test_factory(self):
        self.assertIsInstance(fabrica_para("gato").crear_expediente(1, "Misi", "X"), ExpedienteGato)
        self.assertIsInstance(fabrica_para("Fauna Silvestre").crear_expediente(2, "M", "Y"), ExpedienteFaunaSilvestre)
        with self.assertRaises(ValueError):
            fabrica_para("dragon")

    def test_observer(self):
        g, v = GestorCasos(), Voluntario("Ana")
        g.suscribir(v)
        g.registrar_rescate("perro", "Rocky", "Pedernales")
        self.assertEqual(len(v.bandeja), 1)

    def test_estados(self):
        g = GestorCasos()
        e = g.registrar_rescate("gato", "Misi", "Cojimíes")
        g.cambiar_estado(e.id_caso, Estado.ADOPCION)
        self.assertEqual(len(g.listar(Estado.ADOPCION)), 1)


if __name__ == "__main__":
    unittest.main()
