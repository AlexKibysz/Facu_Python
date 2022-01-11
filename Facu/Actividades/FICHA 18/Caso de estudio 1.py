# Programador   (legajo, nombre, piso(1,2), sueldo,categoria(1al3))

# 1 n programadores cargar
# 2mostrar vector
# 3. mostrar porcentaje de los que trabajan en planta baja
# 4. mostrar los que trabajan en el subsuelo
# 5. acumulador de sueldos por categoria
# 6. busqueda secuencial de quien gana mas

from random import *


class Programador:
	def __init__(self, legajo, nombre, piso, sueldo, categoria):
		self.legajo = legajo
		self.nombre = nombre
		self.piso = piso
		self.sueldo = sueldo
		self.categoria = categoria


def name_selector():
	Nm1 = ['rosa', 'armando', 'Alan', 'Alba', 'Naruto', 'Tobi', 'Pepe',
		   'Monica', 'Susana', 'Chicken', 'Hamburgeso']
	Nm2 = ['melano', 'Britos', 'Paredes', 'Sura', 'Torio', 'Inca', 'kentuky',
		   'King', 'Lopez', 'Correa']
	nombre = choice(Nm1).upper() + ' ' + choice(Nm2).upper()
	return nombre


def carga(v):
	for i in range(len(v)):
		legajo = randint(10000, 99999)
		nombre = name_selector()
		piso = randint(1, 2)
		sueldo = randint(1000, 200000)
		categoria = randint(1, 3)
		v[i] = Programador(legajo, nombre, piso, sueldo, categoria)


def write(v, Lista=True):
	if Lista:
		print('{0:^10}{1:^20}{2:^3}{3:^10}{4:^2}'.format('legajo', 'nombre',
														 'piso',
														 'sueldo', 'categoria'))
		for i in range(len(v)):
			print('{0:^10}{1:^20}{2:^6}{3:^10}{4:^2}'.format(v[i].legajo,
															 v[i].nombre,
															 v[i].piso,
															 v[i].sueldo,
															 v[i].categoria))
	else:
		print('{0:5}{1:20}{2:6}{3:10}{4:2}'.format(v.legajo, v.nombre, v.piso,
												   v.sueldo, v.categoria))


def mostrar_planta_baja(v):
	cont = 0
	for i in range(len(v)):
		if v[i].piso == 1:
			cont += 1
	operacion = (cont * 100 / len(v))
	return print(
		f'la cantidad de empleados en la planta baja es de {operacion}')


def mostrar_planta_alta(v):
	cont = 0
	for i in range(len(v)):
		if v[i].piso == 2:
			cont += 1
	operacion = (cont * 100 / len(v))
	return print(
		f'la cantidad de empleados en la planta alta es de {operacion}')


def sueldos_cat(v):
	v2 = [0] * 3
	for i in range(len(v)):
		if v[i].categoria != None:
			x = v[i].categoria
			v2[x - 1] += v[i].sueldo
	return v2


def menu(v):
	opcion = 1
	while opcion > 0:
		print('Menu\n1.n programadores cargar\2.mostrar vector\n'
			  '3.mostrar porcentaje de los que trabajan en planta baja'
			  '\n4.  mostrar los que trabajan en el subsuelo'
			  '\n5. acumulador de sueldos por categoria'
			  '\n6. busqueda secuencial de quien gana mas \n0. SALIR	')
		opcion = int(input('ingerese su seleccion: '))
		if opcion == 1:
			carga(v)
		if opcion == 2:
			write(v)
		if opcion == 3:
			mostrar_planta_baja(v)
		if opcion == 4:
			mostrar_planta_alta(v)
		if opcion == 5:
			v2 = sueldos_cat(v)
			for i in range(len(v2)):
				print(i, '--->', v2[i])
		if opcion == 6:
			el_mas_pijudo(v)
		if opcion == 0:
			break


def el_mas_pijudo(v):
	mayor = 0
	pos = None
	for i in range(len(v)):
		if v[i].sueldo > mayor:
			mayor = v[i].sueldo
			pos = i
	return print(f'el que gana mas es {v[pos].nombre}')


def principal():
	n = int(input('ingrese cantidad de n registros: '))
	v = [None] * n
	menu(v)


if __name__ == '__main__':
	principal()
