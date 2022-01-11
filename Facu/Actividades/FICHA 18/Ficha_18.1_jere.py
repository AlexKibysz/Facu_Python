"""
1. Triatlon

El Comité Argentnio de Atletismo llevo a cabo una prueba atletica de Triatlón, nos solicito un programa que valide lo
anotado por los jueces del evento,
-para dicho propósito se deben cargar los datos de los tres atletas con mejor promedio.
De cada atleta se conocen
    Nombre
    Tiempo Natacion
    Tiempo Ciclismo
    Tiempo Corriendo
(todo en minutos para simplificar los calculos).

Usted debe:

    -Informar tiempo promedio de cada competidor
    -Determinar el podio, indicando el nombre del primer, segundo y tercer mejor promedio
"""
import random


class Atletas:
    def __init__(self, nom, t_swing, t_bike, t_run, promedio):
        self.nombre = nom
        self.natacion = t_swing
        self.ciclismo = t_bike
        self.correr = t_run
        self.prom = promedio


def cargar(v):
    for i in range(len(v)):
        print('Para el', str(i + 1), 'sujeto:')
        nombre = input('Nombre del sujeto: ').upper()
        nat = random.randrange(10)  # int(input('Tiempo en natacion: '))
        bike = random.randrange(10)  # int(input('Tiempo en ciclismo: '))
        run = random.randrange(10)  # int(input('Tiempo en correr: '))
        v[i] = Atletas(nombre, nat, bike, run, 0)


def prom_t_total(v):
    for i in range(len(v)):
        v[i].prom = round((v[i].natacion + v[i].ciclismo + v[i].correr) / len(v), 2)


def escribir(texto, v):
    print('=' * 30)
    for i in range(len(v)):
        print(v[i].nombre, texto, v[i].prom)
    print('=' * 30)


def mejor_prom(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].prom > v[j].prom:
                v[i], v[j] = v[j], v[i]


def podio(v):
    maxm = 0
    for i in range(len(v)):
        if len(v[i].nombre) > maxm:
            maxm = len(v[i].nombre)
    primer = len(v[0].nombre)  # 5
    sencon = len(v[1].nombre)  # 3
    tercer = len(v[2].nombre)  # 7
    if v[0].prom == v[1].prom:
        print(v[0].nombre, v[1].nombre, ' ' * (maxm * 2 - primer - sencon) + '🏁 Ⅰ')
        print(v[2].nombre, ' ' * (maxm * 2 - sencon), '🏁 Ⅱ')
    elif v[0].prom == v[2].prom:
        print(v[0].nombre, v[2].nombre, ' ' * (maxm * 2 - primer - tercer) + '🏁 Ⅰ')
        print(v[1].nombre, ' ' * (maxm * 2 - sencon), '🏁 Ⅱ')
    elif v[1].prom == v[2].prom:
        print(v[0].nombre, ' ' * (maxm * 2 - primer), '🏁 Ⅰ')
        print(v[1].nombre, v[2].nombre, ' ' * (maxm * 2 - sencon - tercer) + '🏁 Ⅱ')
    else:
        print(v[0].nombre, ' ' * (maxm - primer), '🏁 Ⅰ')
        print(v[1].nombre, ' ' * (maxm - sencon), '🏁 Ⅱ')
        print(v[2].nombre, ' ' * (maxm - tercer), '🏁 Ⅲ')

def ppal():
    v = [None] * 3
    cargar(v)
    prom_t_total(v)
    escribir('tiene un tiempo de: ', v)
    mejor_prom(v)
    podio(v)


if __name__ == '__main__':
    ppal()
