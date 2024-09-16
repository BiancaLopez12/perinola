import unittest
from jugador import Jugador

class TestJugador(unittest.TestCase):

    def setUp(self):
        """Preparar el entorno para las pruebas."""
        self.jugador = Jugador("Tomas", 5)

    def test_inicializacion(self):
        """Probar la inicialización del jugador."""
        self.assertEqual(self.jugador.nombre, "Tomas")
        self.assertEqual(self.jugador.fichas, 5)

    def test_darFicha(self):
        """Probar el método darFicha."""
        self.jugador.darFicha(3)
        self.assertEqual(self.jugador.fichas, 8)
        self.jugador.darFicha()
        self.assertEqual(self.jugador.fichas, 9)

    def test_sacarFicha(self):
        """Probar el método sacarFicha."""
        self.jugador.sacarFicha(2)
        self.assertEqual(self.jugador.fichas, 3)
        self.jugador.sacarFicha()
        self.assertEqual(self.jugador.fichas, 2)
        
        with self.assertRaises(ValueError):
            self.jugador.sacarFicha(3)

    def test_tieneFicha(self):
        """Probar el método tieneFicha."""
        self.assertTrue(self.jugador.tieneFicha(2))
        self.assertFalse(self.jugador.tieneFicha(6))

    def test_sinFichas(self):
        """Probar el método sinFichas."""
        self.assertFalse(self.jugador.sinFichas())
        self.jugador.sacarFicha(5)
        self.assertTrue(self.jugador.sinFichas())

    def tearDown(self):
        """Limpiar después de las pruebas (opcional en este caso)."""
        del self.jugador

if __name__ == "__main__":
    unittest.mai