# Este es el modulo en el que se definiran algunas de las funciones a utilizar en el archivo principal
from time import sleep as delay


class Participante:
    # método constructor para el registro de participantes
    def __init__(self, nom, cont, rank, puntaje=None):
        self.nombre = nom
        self.continente = cont
        self.ranking = rank

    def __str__(self):
        cad = 'Nombre: {:<15} - Continente: {:<10} - Ranking: {:>4}'
        return cad.format(self.nombre, continentes(self.continente),
                          self.ranking)



def continentes(n):
    cont = ['América', 'Europa', 'Asia', 'África', 'Oceanía']
    return cont[n]


# Se inician todos los participantes con un puntaje nulo que luego sera reemplazado en cada partido
# >> Desde un inicio se sabe que cada participante jugara al menos una vez

class Enfrentamiento:
    def __init__(self, jug1=None, jug2=None, puntaje1=None, puntaje2=None, ganador=None):
        self.jugador1 = jug1
        self.jugador2 = jug2
        self.puntaje1 = puntaje1
        self.puntaje2 = puntaje2
        self.ganador = ganador

    def __str__(self):
        separar()
        cad = '¡Felicidades! => Nombre:{:<10}'
        return cad.format(self.ganador)


def validar_mayor_que(num, inf):
    val = num - 1
    while val <= num:
        val = int(input(inf))
        if val <= num:
            print('\033[31mERROR: Porfavor elija un valor mayor a', num,
                  '\033[0m')
    return val


def validar_intervalo(n1, n2, mensaje='\033[33m=>Ingrese una opcion: \033[0m'):
    num = n1 - 1
    while num < n1 or num > n2:
        num = int(input(mensaje))
        if num < n1 or num > n2:
            print('\033[1;31mERROR: Porfavor elija un valor entre:', n1,
                  'y', n2, '\033[0m')
    return num


def validar_opcion(opcion, op1, op2, op3, op4):
    val = False
    if opcion == 0:
        print('Fin de programa.')
    elif opcion != 1 and not op1:
        print('\033[31mERROR: primero cargue valores\033[0m')
    elif opcion == 3 and not op2:
        print('\033[31mERROR: primero juegue OCTAVOS\033[0m')
    elif opcion == 4 and not op3:
        print('\033[31mERROR: primero juegue CUARTOS\033[0m')
    elif opcion == 5 and not op4:
        print('\033[31mERROR: primero juegue la SEMIFINAL\033[0m')
    else:
        val = True
    return val


def texto_lindo(inf):
    for i in inf:
        print(i, end='')
        delay(0.07)


def separar():
    print('=' * 70)


# Funcion de ordenamiento para el ranking.
def ordenar_ranking(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].ranking < v[j].ranking:
                v[i], v[j] = v[j], v[i]


def promedio(v):
    s = 0
    n = len(v)
    for i in range(n):
        s += v[i].puntaje1 + v[i].puntaje2
    p = s / (n * 2)
    return p


def contador(vec, n):
    nw = [0] * n
    for i in range(len(vec)):
        nw[vec[i].continente] += 1
    return nw


# Funcion que se llamara para mostrar el vector de los participantes en formato matriz
# Los vectores se crearon para ahorrar el trabajo de utilizar condicionales


def nombre_random(val):
    choic = ['ONIX', 'RAICHU', 'VULPIX', 'MEW', 'SNORLAX',
             'DITO', 'JYNX', 'MAGIKARP', 'MACHOTE', 'HYPNO', 'GOLEM',
             'DIGLET', 'GOLDUCK', 'DODO', 'PIKACHU', 'STARYU']
    return choic[val]
