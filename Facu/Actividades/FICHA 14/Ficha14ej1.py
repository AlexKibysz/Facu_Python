# Se pide un programa que:

# Ingrese n muestras de temperatura, donde cada muestra contiene la
# temperatura registrada, la región donde se registró la misma (1-20),
# y el día del mes en el que se registró la temperatura

# Determinar el promedio general de temperatura

# Dada una región, mostrar las temperaturas de la misma, ordenadas por dia,
# de menor a mayor

# Dada una región, determinar si la temperatura de alguna muestra superó el
# valor x, ingresado por teclado.

# Determinar la cantidad de muestras por region (20 contadores)

def carga(x):
	temperaturas = [] * x
	region = [] * x
	dia = [] * x
	for i in range(x):
		temperaturas[i] = int(input('ingrese temperatura'))
		region[i] = int(input('ingrese region (1 al 20)'))
		dia[i] = int(input('ingrese dia en el que se registro'))
	return dia, region, temperaturas


def promedio(lista):
	n = len(lista)
	sumatoria = 0
	for i in range(n):
		sumatoria += lista[i]
	return (sumatoria // n)


def ordenar_vec_paralelos(temperatura, region, dia):
	n = len(temperatura)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if dia[i] > dia[j]:
				temperatura[i], temperatura[j] = temperatura[j], temperatura[i]
				region[i], region[j] = region[j], region[i]
				dia[i], region[j] = region[j], region[i]
	return temperatura, region, dia


def search_in_vec_parall(temperatura, region, x):
	n = len(temperatura)
	for i in range(n):
		if region[i] == region:
			if x > temperatura:
				return True
	return False


def menu():
	print("1 _ Cargar datos")
	print("2 _ Promedio de temperaturas")
	print("3 _ Mostrar temperatura de una región")
	print("4 _ Buscar temperaturas mayores a x")
	print("5 _ Salir")
	return int(input("Ingrese opción: "))


def mostrar_temperaturas(dias, regiones, temperaturas, reg):
	print("Dia \t\t Temperatura")
	for i in range(len(regiones)):
		if regiones[i] == reg:
			print(dias[i], "\t\t\t", temperaturas[i])


def main():
	op = 0
	n = int(input('ingrese cuantos datos quiere cargar: '))
	while op != 5:
		op = menu()
		if op == 1:
			dias, regiones, temperaturas = carga(n)
		elif op == 2:
			promedio = promedio(temperaturas)
			print("El promedio de temperaturas fue de: ", promedio)
		elif op == 3:
			ordenar_vec_paralelos(temperaturas, regiones, dias)
			reg = int(input("Ingrese región a analizar: "))
			mostrar_temperaturas(dias, regiones, temperaturas, reg)
		elif op == 4:
			reg = int(input("Ingrese región a analizar: "))
			x = int(input("Ingrese temperatura a controlar: "))
			existe = search_in_vec_parall(temperaturas, regiones, x)
			if existe:
				resultado = "Hay al menos una temperatura menor a"
			else:
				resultado = "No hay temperaturas menores a"
			print(resultado, x, "en la región analizada")
		elif op == 5:
			print("Hasta luego.")
		else:
			print("Error, opción errónea")


if __name__ == "__main__":
	main()
