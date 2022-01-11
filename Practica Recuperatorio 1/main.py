from registro import *
from arch import *


def porcentaje_total_voc(texto):
	vocales=['a','e','i','o','u']
	no_letras=[' ','.',',']
	cont_voc=0
	cont_letras=0
	texto=texto.lower()
	for c in texto:
		if c in vocales:
			cont_voc+=1
		if c not in no_letras:
			cont_letras+=1
	promedio= cont_voc*100/cont_letras
	print(f'El Promedio de vocales en el texto es de: {promedio} %')



def principal(fd):
	n = int(input('Ingrese cantidad de obras que quiera generar'))
	v = carga(n)
	ordenar_dni(v)
	crear_arch(fd,v)
	print('Los datos del archivo generado son: ')
	leer_archivo(fd)
	param = input('Ingrese el nombre que desea buscar: ')
	busqueda_reg(v,param)
	v_cont(v)
	texto=input('Ingrese texto que quiera analizar: ')
	porcentaje_total_voc(texto)
if __name__ == '__main__':
	fd='Restauracion de Obras'
	principal(fd)



