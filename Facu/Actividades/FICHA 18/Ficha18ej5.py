# 5. Guerra de Cartas
# Desarrollar un programa para implementar un juego de cartas de la baraja española.
# Es una competencia de 3 rondas entre 2 jugadores.
# En cada ronda, cada jugador recibe una carta
# (cuyo número y palo el programa deberá generar de forma aleatoria)
# y se define la ronda de la siguiente manera:
# El jugador que tenga la carta de mayor valor, se lleva ambas.
# Si las cartas son del mismo valor, se las lleva quien tenga una carta de oro.
# Si ninguno tiene oro, cada jugador recupera su carta.
# Los puntos de cada jugador se determinan sumando los valores de todas
# las cartas que ganó. Será triunfador el que tenga mayor puntaje total.
from random import *


class color:
	PURPLE = '\033[1;35;48m'
	CYAN = '\033[1;36;48m'
	BOLD = '\033[1;37;48m'
	BLUE = '\033[1;34;48m'
	GREEN = '\033[1;32;48m'
	YELLOW = '\033[1;33;48m'
	RED = '\033[1;31;48m'
	BLACK = '\033[1;30;48m'
	UNDERLINE = '\033[4;37;48m'
	END = '\033[1;37;0m'


class Datos:
	def __init__(self, jugador, cartas, baraja):
		self.jugador = jugador
		self.cartas = cartas
		self.baraja = baraja


def cartas_aleatorias():
	cartas1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	cartas = choice(cartas1)
	return cartas


def baraja_aleatoria():
	baraja1 = ['oro', 'basto', 'espada', 'copa']
	baraja = choice(baraja1)
	return baraja


def carga(v):
	for i in range(len(v)):
		jugador = f'jugador {i+1}'
		cartas = cartas_aleatorias()
		baraja = baraja_aleatoria()
		v[i] = Datos(jugador, cartas, baraja)


def enfrentamiento(v):
	if v[0].cartas < v[1].cartas:
		v[1].cartas += v[0].cartas
		v[0].cartas = 0
	elif v[0].cartas > v[1].cartas:
			v[0].cartas += v[1].cartas
			v[1].cartas = 0
	else:
		if v[1].baraja == 'oro' and v[0] != 'oro':
			v[1].cartas += v[0].cartas
			v[0].cartas = 0
		elif v[0].baraja == 'oro' and v[1] != 'oro':
			v[0].cartas += v[1].cartas
	return v[0].cartas, v[1].cartas


def write(v):
	for i in range(len(v)):
		print(color.PURPLE + '■■' * 20 + color.END)
		r = ''
		r += "{:20}".format('jugador: ' + str(v[i].jugador))
		r += "{:10}".format('Carta: ' + str(v[i].cartas))
		r += "{:1}".format('Baraja: ' + str(v[i].baraja))
		print(r)
	print(color.PURPLE + '■■' * 20 + color.END)


def principal():
	v = [None] * 2
	cont1 = cont2 = 0
	for i in range(3):
		carga(v)
		write(v)
		enfrentamiento(v)
		cont1 += v[0].cartas
		cont2 += v[1].cartas
	print('/=*'*20,'\n resultados finales: ')
	if cont1>cont2:
		print(f'el ganador es {v[0].jugador} con la sumatoria de: {cont1}')
	elif cont1<cont2:
		print(f'el ganador es {v[1].jugador} con la sumatoria de: {cont2}')
	else:
		print('se obtuvo un empate')

if __name__ == '__main__':
	principal()
