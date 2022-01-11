import math
import pickle
import os.path


class Point:
    def __init__(self, cx, cy, desc='p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc


def display(puntos):
    for i in puntos:
        print(to_string(i))


def deserial(puntos):
    m = open("D:\\Proyectos Python\\Desafío4\\puntos.df4", "rb")
    t = os.path.getsize("D:\\Proyectos Python\\Desafío4\\puntos.df4")

    while t > m.tell():
        pun = pickle.load(m)
        puntos.append(pun)

    m.close()


def to_string(point):
    r = str(point.descripcion) + '(' + str(point.x) + ', ' + str(point.y) + ')'
    return r


def distance_between(p1, p2):
    # calcular "delta y" y "delta x"
    dy = p2.y - p1.y
    dx = p2.x - p1.x

    # Distancia entre ellos... Pitágoras...
    return math.sqrt(pow(dx, 2) + pow(dy, 2))


def menor(puntos):
    dmax = 0
    dmin = distance_between(puntos[0], puntos[1])
    n = len(puntos)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            d = distance_between(puntos[i], puntos[j])
            if d < dmin:
                dmin = d
            if d > dmax:
                dmax = d

    print('Distancia mínima: ', dmin)
    print('Distancia máxima: ', dmax)


def principal():
    puntos = []
    deserial(puntos)
    menor(puntos)


if __name__ == '__main__':
    principal()
