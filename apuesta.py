class Apuesta:
 
 
    def __init__(self):
        self.fichas = 0
    def __repr__(self):
        return f"Apuesta: {self.fichas} fichas"
    def ponerFicha(self, cuantas_fichas=1):
        self.fichas += cuantas_fichas
    def tomarFicha(self,cuantas_fichas=1 ):
        if cuantas_fichas > self.fichas:
            raise ValueError("No hay suficientes fichas para quitar")
        self.fichas -= cuantas_fichas
    def tomarTodas(self):
        todas = self.fichas
        self.fichas = 0
        return todas
    def tieneFicha(self, cuantas_fichas=1):
        return self.fichas >= cuantas_fichas
    def estaVacia(self):
        return self.fichas == 0