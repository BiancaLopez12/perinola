import unittest
from apuesta import Apuesta

class TestApuesta(unittest.TestCase):

    def setUp(self):
        """Preparar el entorno para las pruebas."""
        self.apuesta = Apuesta()

    def test_inicializacion(self):
        """Probar la inicialización de la apuesta."""
        self.assertEqual(self.apuesta.fichas, 0)

    def test_ponerFicha(self):
        """Probar el método ponerFicha."""
        self.apuesta.ponerFicha(5)
        self.assertEqual(self.apuesta.fichas, 5)
        self.apuesta.ponerFicha()
        self.assertEqual(self.apuesta.fichas, 6)

    def test_tomarFicha(self):
        """Probar el método tomarFicha."""
        self.apuesta.ponerFicha(10)
        self.apuesta.tomarFicha(3)
        self.assertEqual(self.apuesta.fichas, 7)
        self.apuesta.tomarFicha()
        self.assertEqual(self.apuesta.fichas, 6)
        
        with self.assertRaises(ValueError):
            self.apuesta.tomarFicha(10)

    def test_tomarTodas(self):
        """Probar el método tomarTodas."""
        self.apuesta.ponerFicha(5)
        todas = self.apuesta.tomarTodas()
        self.assertEqual(todas, 5)
        self.assertEqual(self.apuesta.fichas, 0)

    def test_tieneFicha(self):
        """Probar el método tieneFicha."""
        self.apuesta.ponerFicha(3)
        self.assertTrue(self.apuesta.tieneFicha(2))
        self.assertFalse(self.apuesta.tieneFicha(4))

    def test_estaVacia(self):
        """Probar el método estaVacia."""
        self.assertTrue(self.apuesta.estaVacia())
        self.apuesta.ponerFicha(1)
        self.assertFalse(self.apuesta.estaVacia())
        self.apuesta.tomarTodas()
        self.assertTrue(self.apuesta.estaVacia())

    def tearDown(self):
        """Limpiar después de las pruebas (opcional en este caso)."""
        del self.apuesta

if __name__ == "__main__":
    unittest.main()