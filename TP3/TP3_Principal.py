from TP3_AED_Mod import *
from random import *

#       TRABAJO PRACTICO AED - 3
_author_ = 'De Philippis Jérémie, Cano Bianca, Kibysz Alexander'


# TP3-G166
# Legajo: 85421, 86809, 85698
# Curso: 1K02


# =============================CARGA DEL VECTOR================================

# Se realiza la carga ingresando los valores por teclado.
def carga_manual(v):
    name_usados = []
    for i in range(len(v)):
        print('>> Participante Nro => [', i + 1, ']. <<')
        nombre = validar_nombre(name_usados)
        name_usados.append(nombre)
        continente = validar_intervalo(0, 4, '+ Continente: ')

        # Se considera que si puede existir ranking 0 pero no negativo
        rank = validar_mayor_que(-1, '+ Ranking Mundial: ')
        v[i] = Participante(nombre, continente, rank)
        print('=' * 70)


# Se cargan los 16 participantes de manera aleatoria.
def carga_aleatoria(v):
    n = len(v)
    for i in range(n):
        nombre = nombre_random(i)
        continente = randint(0, 4)
        ranking = randint(0, 1000)
        v[i] = Participante(nombre, continente, ranking)


# Se realiza la validacion para evitar que se repita el nombre.
def validar_nombre(nombres_usados):
    nombre = input('+ Nombre: ').upper()
    while nombre in nombres_usados:
        print('\033[31mValueError: name entered already exists.\033[0m')
        nombre = input('+ Nombre: ').upper()
    return nombre


# =============================== PUNTAJE =====================================

# ===> Se realiza la carga mientras se asegura que no se produzca ningun empate

def no_empate_manual(i, c, vec):
    p2 = p1 = 0
    while p1 == p2:
        p1 = validar_mayor_que(1, '▶ Jugador Nro [' + str(
            i + 1) + '] => Puntaje: ')
        p2 = validar_mayor_que(1, '▶ Jugador Nro [' + str(
            c + len(vec) + 1) + '] => Puntaje: ')
        if p1 == p2:
            print(
                '\033[31m¡Oh! ha habido un ¿¿Empate??... Juegan de nuevo.\033[0m')
    return p1, p2


# ===> Se asegura que no se produzca ningun empate en el aleatorio

def no_empate_aleatorio(val):
    p1 = p2 = 0
    while p1 == p2:
        p1 = randint(1, val)
        p2 = randint(1, val)
    return p1, p2


# ========================= Print de la partida ===============================

# Funcion que mostrara los enfrentamientos y definira el ganador segun los puntajes

def print_de_puntajes(vec):
    for i in range(len(vec)):
        separar()
        print('\033[1;33mJugador Nro [' + str(i + 1) + '] "', vec[i].jugador1,
              '" => Puntos:',
              vec[i].puntaje1, '\033[0m')
        print('\t\t\033[33mVS\033[0m')
        print('\033[1;33mJugador Nro [' + str((len(vec) * 2) - i) + ']"',
              vec[i].jugador2,
              '" => Puntos:',
              vec[i].puntaje2, '\033[0m')
        separar()

        if vec[i].puntaje1 > vec[i].puntaje2:
            vec[i].ganador = vec[i].jugador1
        elif vec[i].puntaje2 > vec[i].puntaje1:
            vec[i].ganador = vec[i].jugador2
        print('\t\t\033[1;33;7mGANADOR:', vec[i].ganador, '\033[0m')


# =================================OPCION 1====================================
def mostrar_vector(v):
    for i in range(len(v)):
        print('=>>\033[1;33m🔰 JUGADOR [' + str(i + 1) + ']🏁\033[0m')
        print((v[i]))
        separar()


def opcion1(cntints):
    jugadores = manual_or_random()
    ordenar_ranking(jugadores)
    mostrar_vector(jugadores)
    cont_continente = contador(jugadores, len(cntints))
    return jugadores, cont_continente


def manual_or_random():
    print('¿Desea cargar los participantes manual o automaticamente? '
          '\n\t\t(Manual = 1 / Aleatorio = 2)')
    op = validar_intervalo(1, 2, 'Ingrese su opcion =>: ')
    vec = [0] * 16
    if op == 1:
        print('\033[33;3mRecuerde que para los continentes:'
              '\n\t(0: América, 1: Europa, 2: Asia, 3: África, 4: Oceanía) :)\033[0m')
        carga_manual(vec)
    else:
        carga_aleatoria(vec)
    return vec


# Segun con que valor ingrese val se ejecutara la validacion de no repeticion correspondiente

def crear_enfrentamiento(jugadores, val, primera_carga=False):
    c = 0
    new_vect = list()
    maxm = 0
    if val == 2:
        maxm = validar_mayor_que(1, 'Nro maximo de puntos en la ronda: ')
    for i in range(len(jugadores) // 2):
        c -= 1
        if primera_carga:
            jug1 = jugadores[i].nombre
            jug2 = jugadores[c].nombre
        else:
            jug1 = jugadores[i].ganador
            jug2 = jugadores[c].ganador
        if val == 1:
            p1, p2 = no_empate_manual(i, c, jugadores)
        else:
            p1, p2 = no_empate_aleatorio(maxm)
        new_vect.append(Enfrentamiento(jug1, jug2, p1, p2))
    return new_vect


# =================================OPCION 2====================================
# SE JUEGA OCTAVOS


def opcion2(jugadores):
    separar()
    op = preguntar_manual_random()
    octavos = crear_enfrentamiento(jugadores, op, True)
    print_de_puntajes(octavos)
    print('\n\n\t\t\t🏆 JUGADORES QUE PASARON A CUARTOS 🏆')
    mostrar_vector(octavos)
    prom = promedio(octavos)
    return prom, octavos


# =================================OPCION 3====================================
def opcion3(octavos):
    separar()
    op = preguntar_manual_random()
    cuartos = crear_enfrentamiento(octavos, op)
    print_de_puntajes(cuartos)
    prom = promedio(cuartos)
    print('\n\n\t\t\t🏆 JUGADORES QUE PASARON A LA SEMIFINAL 🏆')
    mostrar_vector(cuartos)
    return prom, cuartos


# =================================OPCION 4====================================
def opcion4(cuartos):
    separar()
    op = preguntar_manual_random()
    semifinal = crear_enfrentamiento(cuartos, op)
    print_de_puntajes(semifinal)
    prom = promedio(semifinal)
    print('\n\n\t\t\t🏆 JUGADORES QUE PASARON A LA FINAL 🏆')
    mostrar_vector(semifinal)
    return prom, semifinal


def preguntar_manual_random():
    print('¿Desea cargar los puntajes manual o automaticamente? '
          '\n\t\t(Manual = 1 / Aleatorio = 2)')
    op = validar_intervalo(1, 2)
    return op


# =================================OPCION 5====================================
# En la opcion 5 se realiza tanto el partido para definir el 3er puesto como la final

def opcion5(finalistas, cuartos, jugadores):
    tercer_p = perdedor(cuartos, finalistas)
    separar()
    print(
        '\n\t\t\033[3;33m>> Primero se jugara por el TERCER PUESTO <<\033[0m\n')

    op = preguntar_manual_random()
    tercer_puesto = crear_enfrentamiento(tercer_p, op)
    print_de_puntajes(tercer_puesto)

    print('\n\t\t\033[3;33m>> Ahora... LA FINAL <<\033[0m\n')
    op = preguntar_manual_random()
    jugar_final = crear_enfrentamiento(finalistas, op)
    texto_lindo('\n\t\tE L   G A N A D O R   E S . . .\n')
    print_de_puntajes(jugar_final)
    print('\n\t\033[1;33;7m¡¡¡¡¡¡¡WINNER WINNER CHICKEN DINNER!!!!!!! =>',
          jugar_final[0].ganador, '\033[0m\n')

    if jugar_final[0].ganador != jugar_final[0].jugador1:
        segundo = jugar_final[0].jugador1
    else:
        segundo = jugar_final[0].jugador2

    podio = [jugar_final[0].ganador, segundo, tercer_puesto[0].ganador]
    puntajes(podio, jugadores)

    # se ordena el ranking para en estadisticas msotrarlo tood ya procesado
    ordenar_ranking(jugadores)
    return podio


def perdedor(cuartos, semifinal):
    create = list()
    for i in range(len(cuartos)):
        if cuartos[i].ganador not in (
                semifinal[0].ganador, semifinal[1].ganador):
            create.append(cuartos[i])
    return create


# Funcion para asignar los puntajes correspondientes a los 3 primeros puestos
def puntajes(podio, jugadores):
    for i in range(len(jugadores)):
        if podio[0] == jugadores[i].nombre:
            jugadores[i].ranking += 25
        elif podio[1] == jugadores[i].nombre:
            jugadores[i].ranking += 15
        elif podio[2] == jugadores[i].nombre:
            jugadores[i].ranking += 5


# ==========================ESTADISTICAS EN GENERAL================================
# Todas las funciones se encargan SOLAMENTE de mostrar las estadisticas,
# sus valores ya han sido procesados.


# Se muestra el contador de participantes por continente
def estadistica_1(cont_v, conts):
    print('\t\033[3;33m>> Cantidad de participantes por continente <<\033[0m')
    show_cant_continentes(cont_v, conts)
    separar()


def show_cant_continentes(cont_v, continent):
    for i in range(len(continent)):
        if cont_v[i] != 0:
            print('🔰 Continente: ', continent[i],
                  '\n\t -> Cantidad de Participantes: ', cont_v[i])
        else:
            print('\033[31mNo hay participantes provenientes de:',
                  continent[i],
                  ' :(\033[0m')


# Estadistica general que muestra los promedios de cada enfrentamiento
def estadistica_prom(prom, inf):
    print('\t\033[3;33m>> Puntaje promedio por participante en ', inf,
          ' <<\033[0m')
    print('\t\t\t\t[', prom, ']')
    separar()


# Mostrar podio y el vector de los 16 participantes con los rankings ya aumentados
def estadistica_5(podio, jugadores):
    mostrar_podio(podio)
    separar()
    print(
        '\n\t>> Se mostraran los 16 participantes originales con su nuevo ranking!!')
    separar()
    mostrar_vector(jugadores)


def mostrar_podio(podio):
    c = 0
    print('\033[3mPodio:\033[0m\n')
    for i in range(len(podio)):
        c += 2
        print('\t' * c, '\033[1;33m', i + 1, '°', podio[i], '\033[0m')


# ================================MINI MENUS===================================

def mini_menu(n, inf):
    print('>> MENU DE LA OPCION [', n, ']. <<')
    print('\n1.', inf,
          '\n2. Mostrar estadisticas. '
          '\n3. Volver al menu principal.')
    op = validar_intervalo(1, 3)
    separar()
    return op


def menu():
    separar()
    print('{:^50}'.format('\033[7;1;33m 🏁 MENU PRINCIPAL 🏁 \033[0m\n'),
          '\n1. Cargar Datos     - Mostrar 1ra estadistica.'
          '\n2. Jugar  OCTAVOS   - Mostrar 2da estadisitca.'
          '\n3. Jugar  CUARTOS   - Mostrar 3ra estadistica.'
          '\n4. Jugar  SEMIFINAL - Mostrar 4ta estadistica.'
          '\n5. Jugar  FINAL     - Mostrar podio y resultados finales.'
          '\n0. Salir.')
    op = validar_intervalo(0, 5)
    return op


# ==============================SCRIPT PRINCIPAL=================================
def principal():
    print('- Sea usted bienvenido a la...'
          '\n\n\t\t>> ADMINISTRACION GENERAL DE COMPETENCIAS <<\n')
    print('\033[3m Dieciseis participantes... un ganador.. '
          '¿Quien sera el vencedor de este inolvidable torneo?'
          '\n\t¡Adentrate en nuestro menu para descubrirlo! \033[0m')

    continent = ['América', 'Europa', 'Asia', 'África', 'Oceanía']
    jugadores = []
    opcion = -1
    op1 = op2 = op3 = op4 = op5 = False
    prom_oct = cont_cntes = prom_cuart = pasan_a_cuartos = pasan_a_semi = pasan_a_final = prom_sem = podio = 0
    while opcion != 0:
        opcion = menu()
        separar()
        valido = validar_opcion(opcion, op1, op2, op3, op4)

        if valido:
            print('\n\t\t\033[1;33m 🥇\033[36m OPCION', opcion,
                  '\033[33m🥇\033[0m')

            # Vec del que se definira que se dira en cada una de las ejecuciones ❤
            msg = ['Cargar datos.', 'Jugar partidos de los OCTAVOS.',
                   'Jugar partidos de los CUARTOS.', 'Jugar la SEMIFINAL.',
                   'Jugar por el 3er puesto y LA FINAL.']
            op = -1
            while op != 3:
                op = mini_menu(opcion, msg[opcion - 1])

                if op == 1:
                    if opcion == 1:
                        jugadores, cont_cntes = opcion1(continent)
                        op1 = True
                    elif opcion == 2 and op1:
                        prom_oct, pasan_a_cuartos = opcion2(jugadores)
                        op2 = True
                    elif opcion == 3 and op2:
                        prom_cuart, pasan_a_semi = opcion3(pasan_a_cuartos)
                        op3 = True
                    elif opcion == 4 and op3:
                        prom_sem, pasan_a_final = opcion4(pasan_a_semi)
                        op4 = True
                    elif opcion == 5 and op4:
                        podio = opcion5(pasan_a_final, pasan_a_semi, jugadores)
                        op5 = True

                elif op == 2:
                    if opcion == 1 and op1:
                        estadistica_1(cont_cntes, continent)
                    elif opcion == 2 and op2:
                        estadistica_prom(prom_oct, 'OCTAVOS')
                    elif opcion == 3 and op3:
                        estadistica_prom(prom_cuart, 'CUARTOS')
                    elif opcion == 4 and op4:
                        estadistica_prom(prom_sem, 'SEMIFINAL')
                    elif opcion == 5 and op5:
                        estadistica_5(podio, jugadores)
                    else:
                        print('\033[31mAun no cargo valores...\033[0m')
                        separar()
                elif op == 3:
                    print('Volviendo al menu...')


if __name__ == '__main__':
    principal()
