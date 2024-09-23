from apuesta import Apuesta
from perinola import Perinola
from jugador import Jugador
from ronda import Ronda

ronda = Ronda()
nombres = ("j1", "j2", "j3", "j4")
for n in nombres:
    j = Jugador(n)
    ronda.agregarJugador(j)
apuesta = Apuesta()
perinola = Perinola()

def ponerTodos():
    print("Ponen todos")
    for j in ronda.jugadores:
        j.sacarFicha()
        apuesta.ponerFicha()    

ponerTodos()

while not ronda.quedaUnSoloJugador():
    print(ronda)
    print(apuesta)

    if apuesta.estaVacia():
        ponerTodos()
    ronda.sacarJugadoresSinFichas()

    if ronda.quedaUnSoloJugador():
        break

    jt = ronda.jugadorEnTurno()
    print("le toca a: ", end="")
    print(jt)

    p = perinola.tirar()
    print(p)

    if p == "Pon 1":
        jt.sacarFicha()
        apuesta.ponerFicha()
    elif p == "Pon 2":
        if jt.fichas == 1:
            jt.sacarFicha()
            apuesta.ponerFicha()
        else:
            jt.sacarFicha(2)
            apuesta.ponerFicha(2)
    elif p == "Toma 1":
        apuesta.tomarFicha()
        jt.darFicha()
    elif p == "Toma 2":
        if apuesta.fichas == 1:
            apuesta.tomarFicha()
            jt.darFicha()
        else:
            apuesta.tomarFicha(2)
            jt.darFicha(2)
    elif p == "Toma Todo":
        fichas = apuesta.tomarTodas()
        jt.darFicha(fichas)
    elif p == "Todos Ponen":
        ponerTodos()

    else:
        raise ValueError("Valor inesperado")



    print(apuesta)
    print(ronda)
    ronda.sacarJugadoresSinFichas()
    ronda.pasarTurno()
    print()

if ronda.quedaUnSoloJugador():
    print(f"Terminó el jugo, ganó: {ronda.jugadorEnTurno}")
else: 
    print(f"Terminó el juego, perdieron todos")