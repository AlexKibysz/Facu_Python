# 4. Usuarios (sin repetir!)
# Desarrollar un programa que permita gestionar la creación de n nuevos usuarios
# de un sistema (n se ingresa por teclado).

# Se deben cargar los nombres de usuario uno a uno y guardarlos en un vector.
# El programa no debe permitir que se ingrese un nombre repetido.


def linear_search(v, x):
	n = len(v)
	for i in range(n):
		if x == v[i]:
			return True
	return False


def test():
	n = int(input('ingrese cant de usuarios que quiere generar: '))
	v = []
	for i in range(n):
		nombre = input(f'ingrese del {i} nombre de usuario')
		while linear_search(v, nombre) != False:
			nombre = input('Ya existe! Ingrese otro: ')
		v.append(nombre)
	print('usuarios', v)


if __name__ == '__main__':
	test()
