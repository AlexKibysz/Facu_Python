"""
5. Guerra de Cartas

Desarrollar un programa para implementar un juego de cartas de la baraja española.

Es una competencia de 3 rondas entre 2 jugadores.

En cada ronda, cada jugador recibe una carta (cuyo número y palo el programa deberá generar de forma aleatoria)
y se define la ronda de la siguiente manera:

    El jugador que tenga la carta de mayor valor, se lleva ambas.
    Si las cartas son del mismo valor, se las lleva quien tenga una carta de oro.
    Si ninguno tiene oro, cada jugador recupera su carta.

Los puntos de cada jugador se determinan sumando los valores de todas las cartas que ganó.
Será triunfador el que tenga mayor puntaje total.
"""
import random


class Cartas:
    def __init__(self, palos, valor):
        self.palo = palos
        self.valor = valor


def write(card, pl):
    if card.palo == 'Oro':
        color = '\033[0;33m'
    elif card.palo == 'Basto':
        color = '\033[0;36m'
    elif card.palo == 'Espada':
        color = '\033[0;34m'
    elif card.palo == 'Copa':
        color = '\033[0;31m'
    print(color + '■' * 25, '\033[0m')
    print('La carta del', pl,
          '\n-', card.palo,
          '\n-', card.valor)
    print(color + '■' * 25, '\033[0m')


def cargar(v):
    for i in range(2):
        palo = random.choice(['Copa', 'Basto', 'Espada', 'Oro'])
        valor = random.randint(1, 4)
        v[i] = Cartas(palo, valor)


def mayor(v):
    pl1 = pl2 = False
    if v[0].valor < v[1].valor:
        pl2 = True
    elif v[0].valor > v[1].valor:
        pl1 = True
    else:
        pl1, pl2 = empate_valor(v)
    return pl1, pl2


def empate_valor(v):
    pl1 = pl2 = False
    if v[0].palo == 'Oro' and not v[1].palo == 'Oro':
        pl1 = True
    elif v[1].palo == 'Oro' and not v[0].palo == 'Oro':
        pl2 = True
    return pl1, pl2


def wwcd(pl1, pl2):
    print('\033[6;30;47m=' * 10, 'Results', '=' * 10 + '\033[0m')
    if pl1 > pl2:
        print('\t\033[6;30;47mGanó el jugador 1\033[0m')
    elif pl2 > pl1:
        print('\t\033[6;30;47mGanó el jugador 2\033[0m')
    else:
        print('\t\033[6;30;47mHubo un EMPATE\033[0m')


def ppal():
    v = [None] * 2
    pts_pl_1 = pts_pl_2 = 0
    for i in range(3):
        print('\033[6;30;47m=' * 10, 'Ronda', i, '=' * 10 + '\033[0m')
        cargar(v)
        write(v[0], 'Jugador 1')
        write(v[1], 'Jugador 2')
        pl1, pl2 = mayor(v)
        if pl1:
            pts_pl_1 += v[0].valor + v[1].valor
        elif pl2:
            pts_pl_2 += v[0].valor + v[1].valor
    wwcd(pts_pl_1, pts_pl_2)


if __name__ == '__main__':
    ppal()
