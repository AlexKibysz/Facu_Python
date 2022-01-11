"""
2. Analizando Temperaturas

El Servicio Metereológico Nacional solicitó un programa que mediante un menu de opciones,
permita analizar las amplitudes térmicas desde diferentes puntos de vista,
para ello las opciones a las que el programa debe responder son:

    Cargar n analisis térmicos (n ingresado por el usuario), cuyos datos son:
    región, mes (numero del 1 al 12), temperatura máxima, temperatura mínima.

    Permitir informar la temperatura máxima promedio en el primer semestre

    Permitir informar la región y el mes en que se registró la temperatura mínima del año

    Salir
"""


class Clima:
    def __init__(self, region, mes, t_max, t_min):
        self.region = region
        self.mes = mes
        self.t_max = t_max
        self.t_min = t_min


def cargar(v):
    print('■' * 25)
    for i in range(len(v)):
        region = input('Region de su zona: ').upper()
        mes = int(input('Del mes: '))
        while mes < 1 or mes > 12:
            print('\033[1;31mERROR Entre(1 y 12)\033[0m')
            mes = int(input('Del mes: '))
        tempmax = float(input('Ingrese la temperatura máxima: '))
        tempmin = float(input('Ingrese la temperatura mínima: '))
        v[i] = Clima(region, mes, tempmax, tempmin)
        print('■' * 25)


def showmax(v):
    maxm = 0
    for i in range(len(v)):
        if v[i].mes < 7:
            if v[i].t_max > maxm:
                maxm = v[i].t_max
    print('La temp máxima del primer semestre: ',maxm)


def showmin(v):
    men = 0
    n = len(v)
    for i in range(n):
        if v[i].t_min < v[men].t_min:
            men = i
    print('Region mas fria', v[men].region, '→Con', v[men].t_min)


def ppal():
    v = None
    opcion = 5
    while opcion != 0:
        print('■' * 25)
        print(
            '0. Salir.\n'
            '1. Cargar analisis térmicos.\n'
            '2. Mostrar la temp máxima del 1er semestre.\n'
            '3. Mostrar la region y mes con temp mínima.'
        )
        opcion = int(input('Opcion:'))
        print('■' * 25)
        if opcion == 1:
            n = int(input('Cuantos analisis térmicos desea ingresar: '))
            v = [None] * n
            cargar(v)
        elif opcion == 2:
            if v is not None:
                showmax(v)
            else:
                print('No estan cargados los datos!')
        elif opcion == 3:
            if v is not None:
                showmin(v)
            else:
                print('No estan cargados los datos!')
        elif opcion == 0:
            print('Ninos!')
        else:
            print('Le pifiaste al numero.')


if __name__ == '__main__':
    ppal()
