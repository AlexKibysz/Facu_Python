
'''a. Enunciado y Consignas.[1]

Programa para Programa para Generación de Estadísticas de COVID-19
(Coronavirus)

En el contexto de la pandemia de COVID-19, se solicita desarrollar un
programa que permita generar estadísticas sobre pacientes sospechosos,
a los cuales se les ha realizado el test (o hisopado) de COVID-19 y a
partir del mismo se genera información de utilidad para la toma de decisiones
en nuestra Provincia.

En primer lugar, el sistema debe solicitar la cuenta de usuario de la
 persona que generará el reporte. La cuenta debe ingresarse con formato
 nombre@dominio y el programa validará que cumpla con las siguientes reglas:

    Tener un sólo caracter @ en una posición intermedia de la cadena
    (ni la primera ni la última letra)
    No contener dos puntos seguidos (uno a continuación del otro)
    No empezar ni terminar con un punto

Si la cuenta ingresada es inválida, se debe permitir el reingreso de la misma.
 Luego de tres intentos incorrectos, el programa debe detener la ejecución.

Luego de confirmar que la cuenta es válida, solicitar al usuario que ingrese
 la cantidad de pacientes a procesar. Y a continuación, por cada paciente
 sospechoso, generar de manera aleatoria los siguientes datos:

    Edad
    Resultado del test (Positivo/Negativo)
    Región (Capital, Gran Córdoba, Norte y Sur)
    Si tuvo contacto con casos confirmados
    Si es personal de salud
    Si viajo al exterior

El programa automáticamente determinará si se considera un caso autóctono.
 Se considera un caso autóctono si el resultado del test fue positivo y NO
  estuvo en contacto con casos confirmados, NO es personal de salud y NO viajó
   al exterior.

Una vez cargados y procesados los datos de los n pacientes, mediante un menú
 de opciones, informar:

    Cantidad de casos confirmados (test positivo) y porcentaje sobre el
    total de casos.
    Edad promedio de los pacientes que pertenecen a grupo de riesgo
    (para pertenecer al grupo de riesgo el test debe ser negativo y
    tener más de 60 años).
    Cantidad y porcentaje que el personal de salud representa sobre el
     total de casos.
    Edad promedio entre los casos confirmados.
    Menor edad entre los casos autóctonos.
    Cantidad de casos confirmados por región y porcentaje que representa
     cada uno sobre el total de casos.
    Cantidad de casos confirmados con viaje al exterior.
    Cantidad de casos sospechosos en contacto con casos confirmados.
    Las regiones sin casos confirmados.
    Porcentaje de casos positivos autóctonos sobre el total de positivos.'''

'''  Tener un sólo caracter @ en una posición intermedia de la cadena 
    (ni la primera ni la última letra)
    No contener dos puntos seguidos (uno a continuación del otro)
    No empezar ni terminar con un punto

Si la cuenta ingresada es inválida, se debe permitir el reingreso de la misma.
 Luego de tres intentos incorrectos, el programa debe detener la ejecución.'''


import random
# @hola.com
# hola.com@
# .hola.com.
# @hola.com@
# .hola.com
# hola.com.
# hola@hotmail.com correcto
# ejrea@
# =================================
def validar_cuenta(cuenta):
    arroba = 0
    anterior = ''
    dos_puntos = validacion = False
    no_valido = '.@'

    for caracter in cuenta:
        if caracter == '@':
            arroba += 1
        elif caracter == '.' and anterior == '.':
            dos_puntos = True
        anterior = caracter
    if arroba == 1 and not dos_puntos and cuenta[0] not in no_valido and \
            cuenta[-1] not in no_valido:
        validacion = True
    return validacion


def aleatorios():
    edad = random.randint(1, 100)
    test = random.randint(1, 2)
    region = random.randint(1, 4)
    contacto_confirmados = random.randint(1, 2)
    personal_salud = random.randint(1, 2)
    viaje_exterior = random.randint(1, 2)
    return edad, test, region, contacto_confirmados, personal_salud, viaje_exterior

def porcentaje(tot, can):
    if tot != 0:
        p = round((can * 100) / tot, 2)
    else:
        p = 0
    return p

def promedio(tot, can):
    if tot != 0:
        prom = round((can / tot), 2)
    else:
        prom = 0
    return prom

def opciones(pacientes):
    cont_edad = cant_test_positivo = cant_test_negativo = cant_pacientes_grup_riesgo \
        = cant_personal_salud = autoctono = edad_positiv = cant_viaje_exterior = ccc = men_edad = 0

    # contador por regiones.
    capital = gran_cordoba = sur = norte = 0

    for i in range(pacientes):

        # funcion aleatorios
        edad, test, region, contacto_confirmados, personal_salud, viaje_exterior = aleatorios()
        # Borrar
        print('Edad:', str(edad), 'Test:', str(test), 'Region', str(region),
              'contacto_confirmados', str(contacto_confirmados),
              'personal_salud', str(personal_salud), 'viaje_exterior',
              str(viaje_exterior))

        neg = False

        if test == 1:
            cant_test_positivo += 1
            edad_positiv += edad
        else:
            cant_test_negativo += 1
            neg = True

        if edad > 60 and neg:
            cont_edad += edad
            cant_pacientes_grup_riesgo += 1

        if personal_salud == 1:
            cant_personal_salud += 1

        if contacto_confirmados == 1:
            ccc += 1  # contacto con confirmados

        if viaje_exterior == 1:
            cant_viaje_exterior += 1

        if test == 1 and personal_salud == 2 and contacto_confirmados == 2 and viaje_exterior == 2:
            autoctono += 1
            if autoctono == 1:
                men_edad = edad
            elif int(edad) < men_edad:
                men_edad = edad

        # 1 = Capital
        # 2 = Gran Cordoba
        # 3 = Norte
        # 4 = Sur
        if test == 1:
            if region == 1:
                capital += 1
            elif region == 2:
                gran_cordoba += 1
            elif region == 3:
                norte += 1
            else:
                sur += 1



    # >>OPCIONES A ACCIONAR<<
    # =========================================OPCION-1=================================================
    opcion1 = cant_test_positivo, porcentaje(pacientes, cant_test_positivo)
    # =========================================OPCION-2=================================================
    opcion2 = promedio(cant_pacientes_grup_riesgo, cont_edad)
    # =========================================OPCION-3=================================================
    opcion3 = cant_personal_salud, porcentaje(pacientes, cant_personal_salud)
    # =========================================OPCION-4=================================================
    opcion4 = promedio(cant_test_positivo, edad_positiv)
    # =========================================OPCION-5=================================================
    opcion5 = autoctono, men_edad
    # =========================================OPCION_6=================================================
    capital_info = porcentaje(pacientes, capital)
    gran_cordoba_info = porcentaje(pacientes, gran_cordoba)
    norte_info = porcentaje(pacientes, norte)
    sur_info = porcentaje(pacientes, sur)
    opcion6 = capital, capital_info, gran_cordoba, gran_cordoba_info, norte, norte_info, sur, sur_info
    # =========================================OPCION-7=================================================
    if cant_viaje_exterior > 0:
        opcion7 = cant_viaje_exterior
    else:
        opcion7 = 0
    # =========================================OPCION-8=================================================
    opcion8 = pacientes, ccc
    # =========================================OPCION-9===============================================
    opcion9 = ''
    if capital == 0:
        opcion9 += '➜Capital'
    elif gran_cordoba == 0:
        opcion9 += '➜Gran cordoba'
    elif norte == 0:
        opcion9 += '➜Norte'
    elif sur == 0:
        opcion9 += '➜Sur'
    # =========================================OPCION-10==============================================
        # Porcentaje de casos positivos autóctonos sobre el total de positivos.
    opcion10 = promedio(cant_test_positivo, autoctono)
    return opcion1, opcion2, opcion3, opcion4, opcion5, opcion6, opcion7, opcion8, opcion9, opcion10


def validacion():
    opcion = -1
    while opcion not in range(0, 10):

        opcion = int(input('\033[1;39m➥ Ingrese su opcion 🔎: \033[0m'))
        if opcion not in range(0, 10):
            print(
                '\033[1;31mERROR: Porfavor seleccione una opcion valida.\033[0m')
    return opcion


def menu(opcion1, opcion2, opcion3, opcion4, opcion5, opcion6, opcion7, opcion8, opcion9, opcion10):
    continuar = True
    print('\n\t\t\t\033[7;1;33m>>📈 MENU DE ESTADISTICAS 📈<<\033[0m'
        '\n\nSeleccione la opcion de su preferencia para mostrar los datos procesados.\033[0m'
        '\n\033[7;1;33m[1].\033[0;3;33m Porcentaje de casos confirmados sobre el total.'
        '\n\033[7;1;33m[2].\033[0;3;33m Edad promedio de los pacientes dentro del grupo de riesgo. '
        '\n\033[7;1;33m[3].\033[0;3;33m Porcentaje de personas que son personal de salud. '
        '\n\033[7;1;33m[4].\033[0;3;33m Edad promedio de pacientes que dieron POSITIVO. '
        '\n\033[7;1;33m[5].\033[0;3;33m Edad del menor paciente autoctono.'
        '\n\033[7;1;33m[6].\033[0;3;33m Cantidad de casos confirmados por region y su porcentaje sobre el total.'
        '\n\033[7;1;33m[7].\033[0;3;33m Cantidad de casos confirmados que viajaron al exterior.'
        '\n\033[7;1;33m[8].\033[0;3;33m Cantidad de casos sospechosos en contacto con casos confirmados.'
        '\n\033[7;1;33m[9].\033[0;3;33m Regiones sin casos confirmados.'
        '\n\033[7;1;33m[10]\033[0;3;33m. Porcentaje de casos positivos autóctonos sobre el total de positivos'
        '\n\033[3;1;31m[0]. => SALIR \033[0m')
    opcion = validacion()
    print('\n\t\t\t\033[1;33m ⇲OPCION-'+str(opcion)+'⇱\033[0m')
    if opcion == 1:# Cantidad de casos confirmados (test positivo) y porcentaje sobre el total

        print('➥ Cantidad de casos confirmados:', opcion1[0])
        print(
            'La cantidad de casos cofirmados sobre el total de pacientes es: %',
            opcion1[1], sep='')

    elif opcion == 2:  # Edad promedio de los pacientes que pertenecen a grupo de riesgo
        if opcion2 != 0:
            print('La edad promedio de los pacientes que pertenecen al grupo de riesgo es de: %',
                opcion2, sep='')
        else:
            print('No hubo ningun paciente dentro del grupo de riesgo.')

    elif opcion == 3:  # Cantidad y porcentaje que el personal de salud representa sobre el total de casos.
        print('La cantidad de personas que son parte del personal de salud es: ',
            opcion3[0])
        print('El porcentaje que hay entre el personal y los casos totales es de: %',
            opcion3[1], sep='')

    elif opcion == 4: # Edad promedio entre los CASOS CONFIRMADOS.
        if opcion4 != 0:
            print('La edad promedio entre los casos confirmados es de: ',
                  opcion4)
        else:
            print('No hay casos confirmados... ¡Que suerte!')


    elif opcion == 5: # Menor edad entre los casos autóctonos.
        if opcion5[0]:
            print('Sobre los ', opcion5[0], ' casos autoctonos, el paciente de ', opcion5[1], ' años es el más joven.',
                  sep='')
        else:
            print('No hay casos autoctonos.')

    elif opcion == 6: # Cantidad de casos confirmados por región y porcentaje sobre el total

        print('\033[7;33mCasos confirmados por regiones:\033[0m\n'
              '\n\t\t\t\t\033[1;33m CANTIDAD\t\tPORCENTAJE\033[0m'
              '\n-CAPITAL:\t\t\t', opcion6[0], '\t\t\t\t%' + str(opcion6[1]),
              '\n-GRAN CORDOBA:\t\t', opcion6[2],
              '\t\t\t\t%' + str(opcion6[3]),
              '\n-NORTE:\t\t\t\t', opcion6[4], '\t\t\t\t%' + str(opcion6[5]),
              '\n-SUR:\t\t\t\t', opcion6[6], '\t\t\t\t%' + str(opcion6[7]))

    elif opcion == 7: # Cantidad de casos confirmados con viaje al exterior.
        if opcion7 != 0:
            print('La cantidad de casos confirmados que viajaron al exterior es de:', opcion7)
        else:
            print('No hubo casos confirmados que viajaron al exterior.')

    elif opcion == 8: # Cantidad de casos sospechosos en contacto con casos confirmados.
        if opcion8[1] != 0:
            print('De los', opcion8[0], 'casos sospechosos,', opcion8[1], 'estuvieron en contacto con ya casos confirmados')
        else:
            print('No hubo ningun caso sospechoso en contaco con algun caso confirmado.')
    elif opcion == 9: # Las regiones sin casos confirmados.
        if opcion9 != '':
            print('La regiones SIN NINGUN caso confirmado son:', opcion9)
        else:
            print('Todas las regiones a analizar poseen al menos un caso confirmado.')
    elif opcion == 10: # Porcentaje de casos positivos autóctonos sobre el total de positivos.
        if opcion10 != 0:
            print('El Porcentaje de casos positivos autóctonos sobre el total de positivos: ', opcion10)
        else:
            print('No hubo casos positivos autoctonos sobre el total de positivos')
    if opcion == 0:
        continuar = False
    else:
        input('\n\033[7;33m¿Desea continuar? = ENTER.\033[0m')
    return continuar


def carga():
    print('\t\033[1;33m' + '=' * 70)
    print(
        '\t\033[1;30;43m\t\t💉¡BIENVENIDO A LA INTERFAZ DE ESTADISTICAS COVID 19!💉\t\t \033[0m')
    print('\t\033[1;33m' + '=' * 70 + '\033[0m')
    print(
        '\nPara garantizar la seguridad de la informacion provista, necesitamos confirmar su identidad .')
    cta = 0
    valido = False
    while cta != 3 and not valido:
        cuenta = input('\033[3;33m ➜ Ingrese su cuenta, porfavor: \033[0m')
        valido = validar_cuenta(cuenta)
        cta += 1
        if valido:
            print('\n¡Bienvenido! la cuenta ingresada ha sido valida.')
        else:
            if cta < 3:
                print(
                    '\033[3;31mERROR: Cuenta invalida, intentelo de nuevo:\033[0m')
    if not valido:
        print(
            '\033[7;3;31mERROR: Lo siento se le acabaron los intentos. :(\033[0m')
        print('\n---Fin de programa.---')
        return

    pacientes = int(input('\n\033[3;33m➜ ¿Cuantos pacientes desea procesar?: \033[0m'))
    opcion1, opcion2, opcion3, opcion4, opcion5, opcion6, opcion7, opcion8, opcion9, opcion10 = opciones(pacientes)
    continuar = 1
    while continuar:
        continuar = menu(opcion1, opcion2, opcion3, opcion4, opcion5, opcion6, opcion7, opcion8, opcion9, opcion10)
    else:
        print(
            '\n\033[3;33m➥¡Gracias por usar nuestro servicio de estadisticas COVID19!\033[0m')
        print('\n\033[33m' + '=' * 70)
        print('FIN DE PROGRAMA.\033[0m')


carga()
