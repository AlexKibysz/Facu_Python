import math

compuesto = []
primo = []


def Num_Primo(Numero):
	if Numero > 1:
		if Numero == 2:
			return True
		else:
			if Numero % 2 == 0:
				return False
			else:
				Factorial = 1
				Indicador = Numero
				while Indicador > 1:
					Factorial = (Indicador - 1) * Factorial
					Indicador = Indicador - 1
				'''
				Inicia el Teorema de Wilson.
				'''
				if (Factorial + 1) % Numero == 0:
					return True
				else:
					return False
				'''
				Termina el Teorema de Wilson.
				'''
	else:
		print("El número que ingresas no es primo.")
		return False


for i in range(100):
	if Num_Primo(i):
		primo.append(i)
	else:
		compuesto.append(i)

print('Numeros Compuestos: ', compuesto)
print('Numeros Primos: ', primo)

x = int(input('Es Primo: '))
print(Num_Primo(x))

numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
				  59, 61, 67, 71, 73, 79, 83, 89, 97]


def algoritmo_primalidad(x, numeros_primos):
	Noprimo= False
	raiz = math.sqrt(x)
	raiz = int(raiz)
	for i in numeros_primos:
		if i < raiz:
			op = x % i
			print(f'{x} mod {i} = {op}')
			if op == 0:
				Noprimo=True
				print('No es Primo')
	if not Noprimo:
		print('Es primo')


x = int(
	input('Ingrese el numero que quiere analizar con algoritmo de primalidad'))
algoritmo_primalidad(x, numeros_primos)
