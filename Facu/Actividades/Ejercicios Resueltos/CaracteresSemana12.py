
from BasicosAED import *

# Ejemplo: Tratamiento de Caracteres
#
# Desarrollar un programa en Python que permita cargar por teclado un texto completo.
# Siempre se supone que el usuario cargará un punto para indicar el final del texto,
# y que cada palabra de ese texto está separada de las demás por un espacio en blanco.
# El programa debe (Con Módulos):
# 1: Determinar la cantidad de palabras que comienzan con la primer letra del texto.
# 2: Determinar la cantidad de palabras con igual cantidad de vocales y consonantes.
# 3: Calcular el promedio de letras por palabra en las palabras que cumplen con el punto 2.
# 4: Calcular el promedio de letras por palabra en el texto.

def test():

    texto = input('Ingrese texto: ')

    cp_item1 = 0
    cl = 0
    cp = 0
    primer_letra_texto = None
    c_voc, c_conso, cp_item2 = 0, 0, 0
    cl_total, cl_item2 = 0, 0
    for car in texto:

        if car == ' ' or car == '.':
            # fin de palabra
            cp += 1

            # PUNTO 2 y 3
            if c_voc == c_conso:
                cp_item2 += 1
                cl_item2 += cl

            # PUNTO 4
            cl_total += cl

            # inicializaciones
            cl = 0
            c_voc = c_conso = 0

        else:
            # no es ' '  ni '.'
            cl += 1

            # PUNTO 1
            if primer_letra_texto == None:
                primer_letra_texto = car  # l
            else:
                if cl == 1 and car == primer_letra_texto:
                    cp_item1 += 1

            # PUNTO 2
            if esVocal(car):
                c_voc += 1
            else:
                if esConsonante(car):
                    c_conso += 1

    print('PUNTO 1-Palabras que comienzan con la primer letra del texto: ', cp_item1)
    print('PUNTO 2-Palabras que tienen igual cantidad de vocales y consonantes: ', cp_item2)
    print('PUNTO 3-Promedio de letras por palabras de las palabras del Punto 2: ', promedio(cl_item2, cp_item2))
    print('PUNTO 4-Promedio de letras por palabras de todas las palabras del texto: ', promedio(cl_total, cp))


if __name__ == '__main__':
    test()
