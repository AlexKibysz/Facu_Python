# numero de socio
# deporte ((0: Natacion/1: Basquet/2: Karate/3: Futbol/ 4: Patin))
# día del mes en que pagó
# valor de la cuota
# Si el socio aún no abonó
# el día del mes debe ser 0
from ej6file import *


class Asosiados:
	def __init__(self,ind, id, deporte, dia, cuota, pago) -> object:
		self.ind=ind
		self.id = id
		self.deporte = deporte
		self.dia = dia
		self.cuota = cuota
		self.pago = pago


def to_string(a):
	p = '{0:<10}{1:<10}'.format('index: ', a.ind)
	p += '{0:<10}{1:<10}'.format('ID socio: ', a.id)
	p += '{0:<10}{1:<15}'.format('Deporte: ', a.deporte)
	p += '{0:<10}{1:<15}'.format('Dia de pago: ', a.dia)
	p += '{0:<10}{1:<15}'.format('Cuota: ', a.cuota)
	p += '{0:<10}{1:<15}'.format('Pago: ', a.pago)
	print(p)


def totales_y_partic(v):
	v_cont = [0] * 5
	v_cont_2 = [0] * 5
	mayor = 0
	for i in range(len(v)):
		v_cont[v[i].deporte] += v[i].pago
		v_cont_2[v[i].deporte] += 1
	for j in range(len(v_cont)):
		p = '{0:<10}{1:<20}'.format(deporte_conv(v[j].deporte),
									v_cont[v[j].deporte])
		print(p)
		if v_cont_2[j] > mayor:
			mayor = v_cont_2[j]
		print(
			f'El deporte con mas cantidad de socios es: {deporte_conv(v_cont_2[v[j].deporte])}')
