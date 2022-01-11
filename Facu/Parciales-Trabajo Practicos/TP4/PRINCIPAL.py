import random
import pickle
import os


class Archivo:
	def __init__(self, nombre, puntos, wins):
		self.nombre = nombre
		self.puntos = puntos
		self.wins = wins

	def __str__(self):
		linea = 'Nombre: {:<31} | Puntos: {:<6} | Campeonatos Ganados: {}'
		return linea.format(self.nombre, self.puntos, self.wins)


class Equipo:
	def __init__(self, confederacion, nombre, puntos, wins):
		self.confederacion = confederacion
		self.nombre = nombre
		self.puntos = puntos
		self.wins = wins

	def __str__(self):
		linea = 'Confederacion: {:<10} | Nombre: {:<31} | Puntos: {:<6} | Campeonatos Ganados: {}'
		return linea.format(codificacion_numerica(self.confederacion),
							self.nombre, self.puntos, self.wins)


def codificacion_numerica(valor):
	confederacion = ['UEFA', 'CONMEBOL', 'CONCACAF', 'CAF', 'AFC', 'OFC']
	return confederacion[valor]


def intervalo(a, b, msg):
	n = int(input(msg))
	while a > n or b < n:
		print('\033[1;31m❌❌❌ (mayor o igual a', str(a),
			  'y menor a ' + str(b + 1) + ')\033[0m')
		n = int(input(msg))
	return n


def mayor_que(num, msg):
	n = int(input(msg))
	while n <= num:
		print('\033[1;31m❌❌❌ (mayor a ' + str(num) + ')\033[0m')
		n = int(input(msg))
	return n


# CARGAR A VECTOR
def add_in_order(v, reg):  # Sin repetidos
	n = len(v)
	pos = n
	izq, der = 0, n - 1
	while izq <= der:
		c = (izq + der) // 2
		if v[c].puntos == reg.puntos:
			pos = c
			break
		elif reg.puntos < v[c].puntos:
			der = c - 1
		else:
			izq = c + 1
	if izq > der:
		pos = izq
	v[pos:pos] = [reg]


def importarArchivo(fd):
	vector = []
	if os.path.exists(fd):
		data = open(fd, 'rt')
		for linea in data:
			dato = linea.split(',')
			confederacion = int(dato[0])
			nombre = dato[1]
			puntos = int(dato[2])
			wins = int(dato[3])
			registro = Equipo(confederacion, nombre, puntos, wins)
			add_in_order(vector, registro)

		data.close()
	else:
		print('No hay archivo con ese nombre...')
	return vector


# OPCION 1
def mostrar_vector(vec):
	n = len(vec)
	print('=' * 40)
	for i in range(n):
		print('{:>3}'.format(i + 1) + ') ', vec[i])
	print('=' * 40)


# OPCION 2 -> chequear editando .csv
def mayor_cant_campeonatos(vec):
	campeones = []
	n = len(vec)
	may = 0
	for i in range(n):  # range(1,n)
		if vec[i].wins > vec[may].wins:
			may = i
			campeones = []
			campeones.append(may)
		elif vec[i].wins == vec[may].wins:
			campeones.append(i)

	return campeones


def mostrar_may_cant_campeonatos(campeones, vec):
	if len(campeones) != 1:
		print('\nLos paises con mayor cantidad de campeonatos ganados fueron: ')
		for i in campeones:
			print('- ', vec[i].nombre)
	else:
		print('El pais con mayor cantidad de campeonatos ganados fue: ')
		print('- ', vec[0].nombre)


# OPCION 3 -> chequear
def ganadores_por_pais(vec, confederacion, ganadores):
	n = len(vec)
	for i in range(n):
		if vec[i].wins != 0 and confederacion == vec[i].confederacion:
			ganadores[confederacion] += 1


def campeones_por_confederacion(vec):
	ganadores = [0] * 6
	n = len(vec)
	for confederacion in range(6):
		ganadores_por_pais(vec, confederacion, ganadores)
		print('Confederacion: ', confederacion + 1, '- Cantidad de ganadores: ',
			  ganadores[confederacion])


# OPCION 4 -> chequear
def vector_a_vector(dato):
	nombre = dato.nombre
	puntos = dato.puntos
	wins = dato.wins
	return Archivo(nombre, puntos, wins)


def ordenar_por(vec):
	n = len(vec)
	for i in range(n - 1):
		for f in range(i + 1, n):
			if vec[i].puntos < vec[f].puntos:
				vec[i].puntos, vec[f].puntos = vec[f].puntos, vec[i].puntos


def new_vector_confX(vec, x):
	new_vec = []
	for dato in vec:
		if dato.confederacion == x:
			new_vec.append(vector_a_vector(dato))

	ordenar_por(new_vec)

	fd = 'Clasificacion' + str(x) + '.dat'
	data = open(fd, 'wb')
	large = len(new_vec)
	for i in range(large):
		pickle.dump(new_vec[i], data)
	data.close()

	print('Se creó el archivo "' + fd + '"con', large, 'cantidad de datos.')


def opcion4(vec):
	print('0: UFA |1: CONMEBOL |2: CONCACAF |3: CAF |4: AFC |5: OFC')
	x = intervalo(0, 5, 'Ingrese codigo de confederacion: ')
	new_vector_confX(vec, x)


# OPCION 5
def archivo_de_clasificacion(n, vec):
	fd = 'Clasificacion' + str(n) + '.dat'

	if not os.path.exists(fd):
		print('El archivo no existe. Redireccionando ')
		new_vector_confX(vec, n)

	t = os.path.getsize(fd)
	data = open(fd, 'rb')
	while data.tell() < t:
		linea = pickle.load(data)
		print(linea)
	data.close()


# OPCION 6
#   PUNTO A

def crear_matriz():
	matriz = [[None] * 8 for i in range(4)]
	return matriz


# llenar lider
def llenar_matriz(matriz, vec):
	matriz[0][0] = validar_pais_in_vec('Ingrese pais organizador del fixture: ',
									   vec)
	# hacer los otros componentes de la matriz


def validar_pais_in_vec(msg, vec):
	pais = input(msg)
	loop = True
	while loop:
		for linea in vec:
			if pais == linea.nombre:
				return pais
		pais = input(msg)


#   PUNTO B
# llenar fila 0
def llenar_cabeceras(matriz, vec):
	x = len(vec)
	incluidos = [matriz[0][0]]
	columna = len(matriz[0])
	for cabecera in range(1, columna):
		x -= 1
		matriz[0][cabecera] = vec[x].nombre
		if matriz[0][cabecera] in incluidos:
			x -= 1
			matriz[0][cabecera] = vec[x].nombre
		incluidos.append(matriz[0][cabecera])
	return incluidos


# [NOMBRE , NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE]
# [NOMBRE , NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE]
# [NOMBRE , NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE]
# [NOMBRE , NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE, NOMBRE]
#         if matriz[0][c] != None:
#           incluidos.append(matriz[0][c])
#           continue


#   PUNTO C
# llenar restantes
def completar_paises(matriz, vec, incluidos):
	for grupo in range(len(matriz[0])):
		matriz[1][grupo] = validar_pais_random(random.randint(1, 201),
											   incluidos, vec)
		matriz[2][grupo] = validar_pais_random(random.randint(1, 201),
											   incluidos, vec)
		matriz[3][grupo] = validar_pais_random(random.randint(1, 201),
											   incluidos, vec)


def validar_pais_random(num_pais, incluidos, vec):
	for usado in incluidos:
		while usado == vec[num_pais - 1].nombre:
			num_pais = random.randint(1, 201)
	incluidos.append(vec[num_pais - 1].nombre)
	return vec[num_pais - 1].nombre


def mostrar_matriz(matriz):
	filas = len(matriz)
	colum = len(matriz[0])

	# print 4 grupos
	print('\033[47m\t', end='')
	for i in range(colum // 2):
		print('\tGRUPO {:<21}'.format(chr(i + 65)), end='\t')
	print('\033[0m')

	for f in range(filas):
		print('\t', end='')
		for c in range(colum // 2):
			print('▶{:<31}'.format(matriz[f][c]), end='')
		print()

	# print otros 4 grupos abajo
	print('\033[47m\t', end='')
	for i in range(4, colum):
		print('\tGRUPO {:<21}'.format(chr(i + 65)), end='\t')
	print('\033[0m')

	for f in range(filas):
		print('\t', end='')
		for c in range(4, colum):
			print('▶{:<31}'.format(matriz[f][c]), end='')
		print()


# OPCION 7
def validar_pais_in_mat(mat, msg):
	pais = input(msg)
	filas, columnas = len(mat), len(mat[0])
	loop = True
	while loop:
		for f in range(filas):
			for c in range(columnas):
				if mat[f][c] == pais:
					return f, c
		print('Este pais no esta incluido en el fixture')
		pais = input(msg)


def mostrar_grupo(matriz, fila, columna):
	print('\t\t\t', '\033[0;34;47m',
		  '{0:^11}'.format('GRUPO ' + chr(columna + 65)), '\033[0m')
	for f in range(4):
		if f != fila:
			print('\t\t\t ', '{0:>1}{1:^10}'.format('▶', matriz[f][columna]))
		else:
			print('\t\t\t', '\033[0;37;44m',
				  '{0:>1}{1:^10}'.format('▶', matriz[fila][columna]), '\033[0m')


# MENU
def menu():
	print('MENU')
	print('1. Mostrar listado completo.')
	print('2. Informar pais con mayor cantidad de campeonatos ganados.')
	print('3. Cuantos paises ganaron algun campeonato.')
	print('4. Nuevo archivo de X Confederacion.')
	print('5. Abrir Clasificacion')
	print('6. Preparar Fixture para el proximo mundial.')
	print('7. Mostrar Fixture.')
	print('')
	opcion = intervalo(0, 7, 'Ingrese una opcion: ')
	return opcion


def ppal(op=-1):
	incluidos = []
	fd = 'paises.csv'
	vec = importarArchivo(fd)
	while op != 0:
		op = menu()

		if op == 1:
			mostrar_vector(vec)

		elif op == 2:
			campeones = mayor_cant_campeonatos(vec)
			mostrar_may_cant_campeonatos(campeones, vec)

		elif op == 3:
			campeones_por_confederacion(vec)

		elif op == 4:
			opcion4(vec)

		elif op == 5:
			print('0: UFA |1: CONMEBOL |2: CONCACAF |3: CAF |4: AFC |5: OFC')
			n = intervalo(0, 5, 'Ingrese codigo de confederacion: ')
			archivo_de_clasificacion(n, vec)

		elif op == 6:
			matriz = crear_matriz()

			# PUNTO A
			llenar_matriz(matriz, vec)
			# PUNTO B
			incluidos = llenar_cabeceras(matriz, vec)
			# PUNTO C
			completar_paises(matriz, vec, incluidos)
			# PUNTO D
			mostrar_matriz(matriz)

		elif op == 7:
			print()
			if len(incluidos) != 0:
				fila, columna = validar_pais_in_mat(matriz,
													'Ingrese un pais incluido en el Fixture: ')
				if fila != None:
					mostrar_grupo(matriz, fila, columna)
			else:
				print(
					'No se puede procesar esta solicitud, debe crear primero el Fixture.')
			print()


if __name__ == '__main__':
	ppal()
