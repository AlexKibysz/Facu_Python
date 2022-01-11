# 1. Triatlon
# El Comité Argentnio de Atletismo llevo a cabo una prueba atletica de Triatlón,
# nos solicito un programa que valide lo anotado por los jueces del evento,
# para dicho propósito se deben cargar los datos de los tres atletas con
# mejor promedio. De cada atleta se conocen Nombre, Tiempo Natacion,
# Tiempo Ciclismo, Tiempo Corriendo (todo en minutos para simplificar los calculos).

# Usted debe:

# Informar tiempo promedio de cada competidor
# Determinar el podio, indicando el nombre del
# primer, segundo y tercer mejor promedio


class Atleta:
	def __init__(self, nombre, tiempo_n, tiempo_c, tiempo_r, prom):
		self.nombre = nombre
		self.tiempo_n = tiempo_n
		self.tiempo_c = tiempo_c
		self.tiempo_r = tiempo_r
		self.prom = prom


def carga(v):
	for i in range(len(v)):
		nombre = input('ingrese nombre: ')
		tiempo_natacion = int(input('ingrese tiempo de natacion: '))
		tiempo_ciclismo = int(input('tiempo de ciclismo: '))
		tiempo_corriendo = int(input('ingrese tiempo corriendo: '))
		v[i] = Atleta(nombre, tiempo_natacion, tiempo_ciclismo,
					  tiempo_corriendo, 0)


def promedio(v):
	for i in range(len(v)):
		prome = (v[i].tiempo_n + v[i].tiempo_c + v[i].tiempo_r) // 3
		v[i].prom = prome


def write(v):
	for i in range(len(v)):
		print(v[i].nombre, '\n', v[i].tiempo_n, '\n', v[i].tiempo_c, '\n',
			  v[i].tiempo_r, '\n', v[i].prom)


def mostrar_prom(v):
	for i in range(len(v)):
		print(f'el promedio del atleta {v[i].nombre} es : {v[i].prom}')


def principal():
	x = int(input('igrese cuantos jugadores va ingresar: '))
	v = [None] * x
	carga(v)
	promedio(v)
	write(v)
	mostrar_prom(v)
	show_order(v)


def ordenar(v):
	n = len(v)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if v[i].prom < v[j].prom:
				v[i], v[j] = v[j], v[i]



def show_order(v):
	ordenar(v)
	for i in range(len(v)):
		print(f'{i+1}. Puesto: ' ,v[i].nombre)



if __name__ == '__main__':
	principal()
