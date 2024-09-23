import unittest
from jugador import Jugador  # Asegúrate de que la clase Jugador esté importada correctamente
from ronda import Ronda

class TestRonda(unittest.TestCase):

    def setUp(self):
        """Configura el entorno para cada test."""
        self.ronda = Ronda()
        self.jugador1 = Jugador("Tomas", 3)
        self.jugador2 = Jugador("Ana", 0)  # Sin fichas
        self.jugador3 = Jugador("Luis", 5)

    def test_agregar_jugador_con_fichas(self):
        self.ronda.agregarJugador(self.jugador1)
        self.assertEqual(str(self.ronda), "Tomas, 3 fichas")

    def test_agregar_jugador_sin_fichas(self):
        with self.assertRaises(ValueError) as context:
            self.ronda.agregarJugador(self.jugador2)
        self.assertEqual(str(context.exception), "El jugador Ana no tiene fichas.")

    def test_listar_jugadores(self):
        self.ronda.agregarJugador(self.jugador1)
        self.ronda.agregarJugador(self.jugador3)
        self.assertEqual(str(self.ronda), "Tomas, 3 fichas\nLuis, 5 fichas")

    def test_jugador_en_turno(self):
        self.ronda.agregarJugador(self.jugador1)
        self.assertEqual(self.ronda.jugadorEnTurno(), self.jugador1)

    def test_pasar_turno(self):
        self.ronda.agregarJugador(self.jugador1)
        self.ronda.agregarJugador(self.jugador3)
        self.ronda.pasarTurno()
        self.assertEqual(self.ronda.jugadorEnTurno(), self.jugador3)

    def test_queda_un_solo_jugador(self):
        self.ronda.agregarJugador(self.jugador1)
        self.ronda.agregarJugador(self.jugador3)
        self.assertFalse(self.ronda.quedaUnSoloJugador())
        self.ronda.sacarJugadoresSinFichas()
        self.ronda.jugador1.sacarFicha(3)  # Ahora Tomas se queda sin fichas
        self.ronda.sacarJugadoresSinFichas()
        self.assertTrue(self.ronda.quedaUnSoloJugador())

    def test_sacar_jugadores_sin_fichas(self):
        self.ronda.agregarJugador(self.jugador1)
        self.ronda.agregarJugador(self.jugador2)
        self.ronda.agregarJugador(self.jugador3)
        self.ronda.sacarJugadoresSinFichas()
        self.assertEqual(str(self.ronda), "Tomas, 3 fichas\nLuis, 5 fichas")

    def test_jugador_en_turno_sin_jugadores(self):
        with self.assertRaises(IndexError) as context:
            self.ronda.jugadorEnTurno()
        self.assertEqual(str(context.exception), "No hay jugadores en la ronda.")

    def test_pasar_turno_sin_jugadores(self):
        with self.assertRaises(IndexError) as context:
            self.ronda.pasarTurno()
        self.assertEqual(str(context.exception), "No hay jugadores en la ronda.")

if __name__ == "__main__":
    unittest.main()
