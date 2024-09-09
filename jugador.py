class Jugador:
    def __init__(self, nombre, fichas= 5):
        self.nombre = nombre
        self.fichas = fichas
    def __repr__(self):
        return f"{self.nombre}, {self.fichas} fichas"
    def darFicha(self,cuantas_fichas=1):
        self.fichas += cuantas_fichas
    def sacarFicha(self, cuantas_fichas=1):
            if cuantas_fichas > self.fichas:
             raise ValueError("No hay suficientes fichas para quitar")
            self.fichas -= cuantas_fichas
    def tieneFicha(self, cuantas_fichas=1):
        return self.fichas >= cuantas_fichas
    def sinFichas(self):
        return self.fichas == 0