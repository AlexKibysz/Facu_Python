# 3. Trafico de Red
# Un cyber nos solicitó un programa que permita realizar un análisis del tráfico


# registro
# de la red, para ello debemos procesar n registros

# que contengan la dirección ip de la máquina que envía,
# dirección ip de la máquina que recibe  la info y
# el tamaño en bytes enviados.

# En base a esto usted debe, mediante un menú de opciones, darle la oportunidad
# al usuario de:

# 1. Saber la cantidad total de bytes enviados por una dirección ip ingresada por
# el usuario

# 2. Mostrar los datos del registro que tengan la menor información enviada

# 3. Saber para una ip destino, la cantidad  y el porcentaje de veces que recibio
# informacion sobre el total del trafico de la red
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


class Trafico:
	def __init__(self, ip_salida, ip_entrada, size):
		self.ip_salida = ip_salida
		self.ip_entrada = ip_entrada
		self.size = size


# Trafico(ip_salida, ip_entrada, size)


def carga(v, aleatorio=True):
	for i in range(len(v)):
		if aleatorio == True:
			ip_salida = randint(1, 100000010)
			ip_entrada = randint(1, 100000010)
			size = randint(10, 100000)
			v[i] = Trafico(ip_salida, ip_entrada, size)
		else:
			ip_salida = int(input('ingrese ip de salida: '))
			ip_entrada = int(input('ingrese ip de entrada: '))
			size = int(input('ingrese tamaño de datos: '))
			v[i] = Trafico(ip_salida, ip_entrada, size)


def write(v):
	print(color.PURPLE + '▧', 'ip salida', '▧' * 5, 'ip entrada', '▧' * 5,
		  'size', '▧' + color.END)
	for i in range(len(v)):
		print(color.PURPLE + '▧' + color.END, v[i].ip_salida,
			  color.PURPLE + '▧' * 5 + color.END,
			  v[i].ip_entrada, color.PURPLE + '▧' * 5 + color.END,
			  v[i].size, color.PURPLE + '▧' + color.END)
	print(color.PURPLE + '▧' * 33 + color.END,'\n\n')


def menor_peso(v):
	for i in range(len(v) - 1):
		for j in range(i + 1, len(v)):
			if v[i].size > v[j].size:
				v[i].size, v[j].size = v[j].size, v[i].size
	print(
		color.GREEN + 'El registro con menor cantidad de datos enviados es: ' + color.END,
		f' \npeso: {v[0].size} \nip de salida: {v[0].ip_salida} \nip de entrada: {v[0].ip_entrada}')


def verificacion_bytes(v):
	ip = int(input('Ingrese la ip que quiera buscar: '))
	flag = False
	for i in range(len(v)):
		if ip == v[i].ip_salida:
			print(f'la {ip} de salida envio {v[i].size} bytes...')
			flag = True

	if flag == False:
		print(
			color.PURPLE + f'No se encontro la ip: {ip} en los registros de salida' + color.END)


def total_in_traffic(v, x):
	cont_ip_recibida = 0
	for i in range((len(v))):
		if x == v[i].ip_entrada:
			cont_ip_recibida += 1
	return cont_ip_recibida


def porcentaje(x, v):
	if v != 0:
		porcentaje = (x * 100) / v
		return porcentaje
	else:
		porcentaje = 0
		return porcentaje


def info_traffic(v):
	print(color.CYAN + '▢' * 10 + color.END)
	x = int(input('ingrese la ip que quiera analizar: '))
	veces_recibida = total_in_traffic(v, x)
	print(
		f'las veces que la data es enviada a la ip:{x} es de {veces_recibida}')
	print('el porcentaje del total usado del trafico de red es: '
		  ,porcentaje(veces_recibida, len(v)))


def principal():
	print('Analizador de Trafico de RED')
	n = int(input('ingrese numero de registros: '))
	v = [None] * n
	carga(v)
	write(v)
	menu(v)


def validar_intervalo(n1, n2, mensaje='Ingrese seleccion: '):
	num = n1 - 1
	while num < n1 or num > n2:
		num = int(input(mensaje))
		if num < n1 or num > n2:
			print('Porfavor elija un valor entre:', n1,
				  'y', n2)
	return num


def menu(v):
	x = 1
	while x != 0:
		print('Analizador de Trafico de red\n Menu:\n'

			  '1.♦Saber la cantidad total de bytes enviados por una dirección ip'
			  ' ingresada por el usuario'
			  '\n2.♦ Mostrar los datos del registro que tengan la menor información'
			  ' enviada'
			  '\n3.♦ Saber para una ip destino, la cantidad  y el porcentaje '
			  'de veces que recibio informacion sobre el total del trafico de '
			  'la red '
			  '\n0.♦ salir'
			  )
		x = validar_intervalo(0, 3)
		if x == 1:
			verificacion_bytes(v)
		if x == 2:
			menor_peso(v)
		if x == 3:
			info_traffic(v)
		if x == 0:
			exit

if __name__ == '__main__':
	principal()
