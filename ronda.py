class Ronda:
    def __init__(self):
        self.jugadores = []

    def __str__(self):
        return '\n'.join(str(jugador) for jugador in self.jugadores)

    def agregarJugador(self, jugador):
        if not jugador.tiene_fichas():
            raise ValueError(f"El jugador {jugador.nombre} no tiene fichas.")
        self.jugadores.append(jugador)

    def sacarJugadoresSinFichas(self):
        self.jugadores = [jugador for jugador in self.jugadores if jugador.tiene_fichas()]

    def jugadorEnTurno(self):
        if not self.jugadores:
            raise IndexError("No hay jugadores en la ronda.")
        return self.jugadores[0]

    def pasarTurno(self):
        if not self.jugadores:
            raise IndexError("No hay jugadores en la ronda.")
        jugador = self.jugadores.pop(0)
        self.jugadores.append(jugador)

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1