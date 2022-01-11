# 14. Modelo Parcial 2019
# Una compañía de servicios de limpieza desea un programa para procesar
# los datos de los trabajos ofrecidos. Por cada trabajo se tienen los
# siguientes datos:

# el número de identificación del trabajo,
# o nombre del mismo,
# el tipo de trabajo
# (un valor de 0 a 3, 0:interior, 1:exterior, 2:piletas, 3:tapizados),

# el importe a cobrar por ese trabajo y la cantidad de personal
# afectado para prestar ese servicio. Se desea almacenar la
# información referida a los n trabajos en un arreglo de
# registros de trabajos (definir el Trabajo y cargar n por teclado).

# Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
# 1- Cargar el arreglo pedido con los datos de los n trabajos.
# Valide que el número identificador del trabajo sea positivo
# y que el importe a cobrar sea mayor a cero. Puede hacer la carga
# en forma manual, o puede generar los datos en forma automática (con valores aleatorios)
# o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

# 2- Mostrar todos los datos de todos los trabajos,
# en un listado ordenado de mayor a menor según los importes a cobrar.

# 3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de
# personal afectado (no importa si hay varios trabajos con la misma cantidad
# máxima de personal: se pide mostrar uno y sólo uno cuya cantidad de personal sea máxima).

# 4- Determinar si existe un trabajo cuya descripción sea igual a d,
# siendo d un valor que se carga por teclado. Si existe, mostrar sus datos.
# Si no existe, informar con un mensaje. Si existe más de un registro que
# coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.

# 5- Determinar y mostrar la cantidad de trabajos por tipo.
#
from random import *


class Trabajo:
	def __init__(self, ident, nombre, tipo_t, monto, personal_afectado):
		self.ident = ident
		self.nombre = nombre
		self.tipo_t = tipo_t
		self.monto = monto
		self.personal_afectado = personal_afectado


def random_name():
	nombre = (
		"Alexander", "Bianca", "Jeremias", "Bruno", "Juan", "Mateo", "Matias",
		"Marcos",
		"Lucas", "Melisa", "Anilem", "Valentino", "Uriel", "Brian", "Kevin",
		"Erick", "Lara", "Lucia", "Maximo", "Vladimir", "Jorge", 'Exequiel',
		'Felipe', 'Andrea'
		, 'Alan', 'Lautaro', 'Benjamin', 'Alex', 'Nadya', 'Juan Cruz', 'Karen',
		'Ulises', 'Osvaldo'
		, 'Thiago', 'Gael', 'Pablo', 'Hugo', 'Adrian', 'Martin', 'Alvaro',
		'Daniel', 'Javier', 'Ada',
		'Lia', 'Gimena', 'Jimena', 'Lola', 'Julia', 'Cloe', 'Maria', 'Amalia',
		'Paula', 'Pablo', 'Sofia', 'Catalina', 'Benjamin', 'Isabella',
		'Martina', 'Catalina', 'Bautista', 'Sofia', 'Olivia', 'Felipe',
		'Emma', 'Valentino', 'Benicio', 'Joaquín', 'Delfina', 'Lorenzo',
		'Francesca', 'Valentina', 'Emilia',
		'Mateo', 'Santino', 'Tomás', 'Francisco', 'Juana', 'Josefina',
		'Santiago', 'Simon', 'Guillermina',
		'Ignacio', 'Victoria', 'Guadalupe', 'Agustin', 'Julieta', 'Pedro',
		'Renata', 'Alma', 'Jazmin', 'Ciro',
		'Thiago', 'Lola', 'Pilar', 'Lucia', 'Lautaro', 'Bruno', 'Malena',
		'Julia', 'Dante', 'Valentin', 'Salvador',
		'Nicolas', 'Maximo', 'Mia', 'Tiziano', 'León', 'Camila', 'Clara',
		'Bianca', 'Milo', 'Facundo', 'Vicente',
		'Helena', 'Zoe', 'Agustina', 'Ambar', 'Ramiro', 'Manuel', 'Nina',
		'Julián', 'Bastian', 'María Paz',
		'Paulina', 'Mora', 'Jeremías', 'Amparo', 'Morena', 'Franco', 'Matias',
		'Felicitas', 'Luca', 'Genaro',
		'Lucas', 'Augusto', 'Mia Jazmin', 'Fausto', 'Camilo', 'Vera', 'Elena',
		'Giovanni', 'Lucio', 'Juliana',
		'Antonella', 'Antonia', 'Agostina', 'Matilda', 'Martin', 'Constanza',
		'Alejo', 'Paloma', 'Ian', 'Gael',
		'Lara', 'Luciano', 'Federico', 'Milagros', 'Lisandro', 'Pía',
		'Francesco', 'Lourdes', 'Noah', 'Sara',
		'Alfonsina', 'Lupe', 'Sebastián', 'Candelaria', 'Octavio', 'Jonás',
		'Geronimo', 'Teo', 'Abril', 'Tobias',
		'Gino')

	apellido = (
	'	González', 'Rodríguez', 'Gómez', '	Fernández', 'López', 'Díaz',
	'Martínez', 'Pérez',
	'García', 'Sánchez', 'Romero', 'Sosa', 'Torres', 'Álvarez', 'Ruiz',
	'Ramírez', 'Flores', 'Benítez',
	'	Acosta', 'Medina', 'Herrera', 'Suárez', 'Aguirre', 'Giménez',
	'Gutiérrez', 'Pereyra', 'Rojas', 'Molina', 'Castro', 'Ortiz', 'Silva',
	'Kibysz', 'González', 'Rodríguez', 'Gómez', 'Fernández', 'López', 'Díaz',
	'Martínez', 'Pérez', 'García', 'Sánchez', 'Romero',
	'Sosa', 'Torres', 'Álvarez', 'Ruiz', 'Ramírez', 'Flores', 'Benítez',
	'Acosta', 'Medina', 'Herrera', 'Suárez',
	'Aguirre', 'Giménez', 'Gutiérrez', 'Pereyra', 'Rojas', 'Molina', 'Castro',
	'Ortiz', 'Silva', 'Núñez', 'Luna',
	'Juárez', 'Cabrera', 'Ríos', 'Morales', 'Godoy', 'Moreno', 'Ferreyra',
	'Domínguez', 'Carrizo', 'Peralta',
	'Castillo', 'Ledesma', 'Quiroga', 'Vega', 'Vera', 'Muñoz', 'Ojeda', 'Ponce',
	'Villalba', 'Cardozo', 'Navarro',
	'Coronel', 'Vázquez', 'Ramos', 'Vargas', 'Cáceres', 'Arias', 'Figueroa',
	'Córdoba', 'Correa', 'Maldonado', 'Paz',
	'Rivero', 'Miranda', 'Mansilla', 'Farias', 'Roldán', 'Méndez', 'Guzmán',
	'Agüero', 'Hernández', 'Lucero', 'Cruz',
	'Páez', 'Escobar', 'Mendoza', 'Barrios', 'Bustos', 'Ávila', 'Ayala',
	'Blanco', 'Soria', 'Maidana', 'Acuña', 'Leiva',
	'Duarte', 'Moyano', 'Campos', 'Soto', 'Martín', 'Valdez', 'Bravo', 'Chávez',
	'Velázquez', 'Olivera', 'Toledo')
	nombre1 = choice(nombre)
	apellido1 = choice(apellido)
	completo = (nombre1 + apellido1)
	return completo


def generar_ident():
	x = -1
	while x < 0:
		x = randint(-10000, 10000)
	return x


def carga(v):
	for i in range(len(v)):
		identificador = generar_ident()
		nombre = random_name()
		tipo_t = randint(0, 3)
		monto = randint(1000, 1000000)
		personal_requerido = randint(0, 50)
		v[i] = Trabajo(identificador, nombre, tipo_t, monto, personal_requerido)


def write(v, list=True):
	if list:
		print('')
		print('=' * 60)
		print('{0:^10}{1:^16}{2:^10}{3:^10}{4:^10}'.format('identificador',
														   'nombre',
														   'tipo trabajo',
														   'monto',
														   'personal afectado'))
		for i in range(len(v)):
			print('{0:^10}{1:^16}{2:^10}{3:^10}{4:^10}'.format(v[i].ident,
															   v[i].nombre,
															   v[i].tipo_t,
															   v[i].monto, v[
																   i].personal_afectado))
		print('=' * 60)
	else:
		print('=' * 60)
		print('{0:^10}{1:^16}{2:^10}{3:^10}{4:^10}'.format('identificador',
														   'nombre',
														   'tipo trabajo',
														   'monto',
														   'personal afectado'))
		print('{0:^10}{1:^16}{2:^10}{3:^10}{4:^10}'.format(v.ident, v.nombre,
														   v.tipo_t,
														   v.monto,
														   v.personal_afectado))
		print('=' * 60)


def ordenar(v):
	n = len(v)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if v[i].monto < v[j].monto:
				v[i], v[j] = v[j], v[i]
	return v


def mayor_personal_pos(v):
	mayor = 0
	indice = None
	for i in range(len(v)):
		if v[i].personal_afectado > mayor:
			mayor = v[i].personal_afectado
			indice = i
	return indice


def busqueda_descr(v, desc):
	for i in range(len(v)):
		if v[i].nombre == desc:
			write(v[i], False)


def cant_trabajo_tipo(v):
	v2 = [0] * 4
	for i in range(len(v)):
		if v[i].tipo_t != None:
			x = v[i].tipo_t
			v2[x] += 1
	return v2


def menu(v):
	opcion = 1
	b = True
	while opcion >= 0:
		print(
			'Menu\n1. Cargar el arreglo pedido con los datos de los n trabajos\n'
			'2. Mostrar todos los datos de todos los trabajos\n 3.Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de '
			'personal afectado\n4. Determinar si existe un trabajo cuya descripción sea igual a d \n 5. eterminar y mostrar la cantidad de trabajos por tipo.'
			'\n0. SALIR')
		opcion = int(input('ingrese su seleccion: '))
		if opcion == 1:
			carga(v)
			b = False
		if opcion == 2:
			if b:
				print('por favor cargue datos')
				continue
			else:
				v = ordenar(v)
				write(v)
		if opcion == 3:
			if b:
				print('por favor cargue datos')
				continue
			else:

				i = mayor_personal_pos(v)
				write(v[i], False)
		if opcion == 4:
			if b:
				print('por favor cargue datos')
				continue
			else:

				desc = input('ingrese la descripcion que quiera buscar: ')
				busqueda_descr(v, desc)
		if opcion == 5:
			if b:
				print('por favor cargue datos')
				continue
			else:
				v2 = cant_trabajo_tipo(v)
				for i in range(len(v2)):
					print(i, '--->', v2[i])
		if opcion == 0:
			break


def principal():
	n = int(input('ingrese valor de registros que quiera generar: '))
	v = [None] * n
	menu(v)


if __name__ == '__main__':
	principal()
