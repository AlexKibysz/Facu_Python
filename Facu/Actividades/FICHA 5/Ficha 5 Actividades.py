import random

'''1. Operaciones de orden con 3 nros.
Realizar un programa que tome tres números, 
los ordene de mayor a menor, y diga si el tercero es el resto de la división de los dos primeros. '''
numero1 = float(input('Ingrese 1er numero'))
numero2 = float(input('Ingrese 2er numero'))
numero3 = float(input('Ingrese 3er numero'))
mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)
if numero1 == numero2 == numero3:
    print('todos los numeros son iguales')
elif mayor > numero1 > menor:
    mayor, medio, menor = mayor, numero1, menor
elif mayor > numero2 > menor:
    mayor, medio, menor = mayor, numero2, menor
elif mayor > numero3 > menor:
    mayor, medio, menor = mayor, numero3, menor
print('primero(', mayor, ')segundo(', medio, ')tercero(', menor, ')')
resto = numero1 % numero2
if resto == numero3:
    print('Tu Tercer numero(', numero3, ') Es el resto de los dos primeros')
else:
    print('Tu Tercer numero(', numero3, ') NO es el resto de los dos primeros')
'''1. Operaciones de orden con 3 nros.
Realizar un programa que tome tres números, 
los ordene de mayor a menor, y diga si el tercero es el resto de la división de los dos primeros. '''
nro1 = float(input('Ingrese 1er numero'))
nro2 = float(input('Ingrese 2er numero'))
nro3 = float(input('Ingrese 3er numero'))
if nro1 > nro2:
    may, men = nro1, nro2
else:
    may, men = nro2, nro1
if nro3 > may:
    med, may = may, nro3
else:
    if nro3 < men:
        med, men = men, nro3
print('primero(', may, ')segundo(', med, ')tercero(', men, ')')
resto = nro1 % nro2
if resto == numero3:
    print('Tu Tercer numero(', numero3, ') Es el resto de los dos primeros')
else:
    print('Tu Tercer numero(', numero3, ') NO es el resto de los dos primeros')
'''2. Elecciones Presidenciales
Según la Ley Electoral de la República Argentina, el Presidente y
el Vicepresidente se eligen de acuerdo a las siguientes reglas:

Artículo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %)
de los votos afirmativos válidamente emitidos;

en su defecto, aquella que hubiere obtenido el cuarenta por ciento (40 %)
por lo menos de los votos afirmativos válidamente emitidos y, además, existiere
una diferencia mayor de diez puntos porcentuales respecto del total de
 los votos afirmativos válidamente emitidos, sobre la fórmula que le sigue en número de votos.

Artículo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escrutinio ejecutado por las
Juntas Electorales, y cuyo resultado único para toda la Nación será anunciado por
la Asamblea Legislativa atento lo dispuesto por el artículo 120 de la presente ley,
se realizará una segunda vuelta dentro de los treinta (30) días.

Artículo 151. — En la segunda vuelta participarán solamente las dos fórmulas más votadas en la primera,
 resultando electa la que obtenga mayor número de votos afirmativos válidamente emitidos.

Desarrollar un programa que permita ingresar,
para los 3 partidos más votados: fórmula (presidente + vice) y cantidad de votos obtenidos.

Luego determinar:

Qué fórmula obtuvo el mayor porcentaje.
Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso,
indicar también quienes participan de la segunda vuelta.'''
formula_1 = input('Presidente y Vice:')
votos_1 = int(input('Ingrese la cantidad de votos de la F1:'))
formula_2 = input('Presidente y Vice:')
votos_2 = int(input('Ingrese la cantidad de votos de la F2:'))
formula_3 = input('Presidente y Vice:')
votos_3 = int(input('Ingrese la cantidad de votos de la F3:'))

tot = votos_1 + votos_2 + votos_3
prom1 = votos_1 * 100 / tot
prom2 = votos_2 * 100 / tot
prom3 = votos_3 * 100 / tot
el_cuarenta5 = 45 * 100 / tot
el_cuarenta = 40 * 100 / tot
el_diez = 10 * 100 / tot

if prom1 > prom2:
    may, men = prom1, prom2
    mayn, menn = formula_1, formula_2
else:
    may, men = prom2, prom1
    mayn, menn = formula_2, formula_1

if prom3 > may:
    med, may = may, prom3
    medn, menn = mayn, formula_3
else:
    if prom3 < men:
        med, men = men, prom3
        medn, menn = menn, formula_3
    else:
        med = prom3
        medn = formula_3

dif = False
if may > el_cuarenta or may - med > el_diez:
    dif = True

if may > el_cuarenta5 and dif:
    print('La formula elegida es:', mayn)

else:
    print('Ninguna formula ha superado las condiciones. \nSegunda vuelta:', '\nParticipantes:', mayn, 'y:', medn)
'''3. Mantenimiento Informático
El Área de Mantenimiento de un laboratorio informático nos ha solicitado el desarrollo de
un programa que facilite la gestión de las tareas realizadas en el día.

El usuario debe ingresar de tres equipos informáticos (PC) los siguientes datos: número de identificación de la PC,
tiempo de reparación (expresado en minutos) y la causa de mantenimiento (1- Problema de Hardware 2-Problema de Software)

Los requerimientos funcionales son:

a)  ¿Cuál es el tiempo total de las tareas de mantenimiento?

b)  ¿Cuál es la PC (Número de identificación) que tuvo mayor tiempo en tareas de mantenimiento?

c)  Tiempo promedio de tareas de mantenimiento.

d)  Informar con un mensaje si todas las PC (Número de identificación)
que se les ha realizado mantenimiento tuvieron problemas de Hardware.'''

Equipo1 = input('numero de identificacion de la 1er computadora: '), float(input('ingrese minutos: ')), \
          int(input('Seleccione\n1- Problema de Hardware 2-Problema de Software: '))
Equipo2 = input('numero de identificacion de la 2da computadora: '), float(input('ingrese minutos: ')), \
          int(input('Seleccione\n1- Problema de Hardware 2-Problema de Software: '))
Equipo3 = input('numero de identificacion de la 3er computadora: '), float(input('ingrese minutos: ')), \
          int(input('Seleccione\n1- Problema de Hardware 2-Problema de Software: '))
print('/*' * 100)
# a
totaltiempo = Equipo1[1] + Equipo2[1] + Equipo3[1]
# b
pcmaxtime = max(Equipo1[1], Equipo2[1], Equipo3[1])
if pcmaxtime == Equipo1[1]:
    print('la computadora que mas tardo fue la: ', Equipo1[0])
else:
    if pcmaxtime == Equipo2[1]:
        print('la computadora que mas tardo fue la: ', Equipo2[0])
    else:
        print('la computadora que mas tardo fue la: ', Equipo3[0])
# c
prom = (Equipo1[1] + Equipo2[1] + Equipo3[1]) / 3
promedio = round(prom, 2)
# d
print('el tiempo total fue de(', totaltiempo, ') minutos', sep='')
print('el promedio de tiempo de arreglo por cada computadora es de(', promedio, ') minutos', sep='')
if Equipo1[2] == 1 and Equipo2[2] == 1 and Equipo3[2] == 1:
    print('Todas las computadoras fueron arregladas fueron por problema de hardware')
'''4. Observatorio meteorológico
Un observatorio meteorológico ha tomado el registro de temperaturas en distintos momentos del día.
Se solicita el desarrollo de un programa que facilite información estadísticas de ellas.

El usuario debe ingresar cuatro valores de temperatura (considerar que son valores enteros).

Los requerimientos funcionales son:

a) Promedio de temperatura diaria.

b) Temperatura máxima.

c) Temperatura mínima.

d) Informar con un mensaje si algunas de las temperaturas supera a la temperatura promedio.'''
v1 = int(input('ingrese valor 1: '))
v2 = int(input('ingrese valor 2: '))
v3 = int(input('ingrese valor 3: '))
v4 = int(input('ingrese valor 4: '))
# a prom
print('=*' * 100)
prom = (v1 + v2 + v3 + v4) / 4
print('el promedio fue de: ', prom)
# b Temperatura Maxima
tmpmax = max(v1, v2, v3, v4)
print('la temperatura mas alta fue: ', tmpmax)
# c Temperatura Minima
tmpmin = min(v1, v2, v3, v4)
print('la temperatura mas baja fue: ', tmpmin)
# D
if v1 > prom:
    print('temperatura 1 es mas alta que el promedio con: ', v1, 'grados')
else:
    if v2 > prom:
        print('la temperatura 2 es mas alta que el promedio con: ', v2, 'grados')
    elif v3 > prom:
        print('la temperatura 3 es mas alta que el promedio con: ', v3, 'grados')
    elif v4 > prom:
        print('la temperatura 4 es mas alta que el promedio con: ', v4, 'grados')
'''5. Menú de Opciones Básico
Diseñar un programa que según la opción ingresada por el usuario permita realizar las siguientes operaciones:

Si la opción es 1 mostrar la superficie de un triángulo.
Si la opción ingresada es 2 mostrar el perímetro del triángulo.
Si la opción ingresada es 3 informar la longitud del lado menor.
Si la opción ingresada no fue ni 1, 2 o 3 informar un mensaje de error.
Para ello usted deberá ingresar por teclado el número de opción y el valor de los tres lados del triángulo.

 '''
opcion = int(input('Marque segun lo que quiera\n1. mostrar la superficie de un triángulo\n'
                   '2 mostrar el perímetro del triángulo\n3 informar la longitud del lado menor'))
if opcion != 1 and opcion != 2 and opcion != 3:
    print('Error Ingrese un Numero valido')
else:
    lado_1 = float(input('ingrese lado 1'))
    lado_2 = float(input('ingrese lado 2'))
    lado_3 = float(input('ingrese lado 3'))
    print('/=' * 100)
    if opcion == 1:
        print('ha elegido mostrar la superficie de un tirangulo')
        superficie = lado_1 * lado_2 * lado_3
        print('la superficie es de: ', superficie)
    elif opcion == 2:
        print('ha elegido la opcion 2 mostrar el perimetro de un triangulo')
        perimetro = lado_1 + lado_2 + lado_3
        print('el perimetro es de: ', perimetro)
    elif opcion == 3:
        print('ha elegido la opcion 3 longitud del lado menor')
        lado_menor = min(lado_1, lado_2, lado_3)
        print('el lado menor es de: ', lado_menor)
'''6. Institución Educativa
Una institución educativa necesita un programa que facilite la gestión de cupos de los cursos de primer grado.
Ingresar tres grados.

 De cada grado se ingresa el código de identificación (Ejemplo 1A, 1B, ...) y
la cantidad de niños y de niñas y cupo máximo (que es el mismo para los tres cursos).

Los requerimientos funcionales son:

a)  Código de identificación del curso que tenga menos alumnos inscriptos.

b)  Porcentaje de niñas de cada curso.

c)  Porcentaje de niños de cada curso.

d)  Promedio general de alumnos.

e) Si algunos de los tres grados supera el cupo máximo informar un mensaje la necesidad de
apertura de una nueva división.'''

print('ingrese codigo de identificacion de curso en formato [1A, 1B, ...]')
nombre_curso_1 = input('')
nombre_curso_2 = input('')
nombre_curso_3 = input('')
cant_alumnos_1 = int(input('ingrese cantidad de alumnos aula 1'))
cant_alumnas_1 = int(input('ingrese cantidad de alumnas aula 1'))
cant_alumnos_2 = int(input('ingrese cantidad de alumnos aula 2'))
cant_alumnas_2 = int(input('ingrese cantidad de alumnas aula 2'))
cant_alumnos_3 = int(input('ingrese cantidad de alumnos aula 3'))
cant_alumnas_3 = int(input('ingrese cantidad de alumnas aula 3'))
cupo = int(input('ingrese cupos de curso o cantidad maxima'))
total_alumnos_1 = cant_alumnos_1 + cant_alumnas_1
total_alumnos_2 = cant_alumnos_2 + cant_alumnas_2
total_alumnos_3 = cant_alumnos_3 + cant_alumnas_3
porc_alumnas_1 = (cant_alumnas_1 * 100) / cupo
porc_alumnas_2 = (cant_alumnas_2 * 100) / cupo
porc_alumnas_3 = (cant_alumnas_3 * 100) / cupo
porc_alumnos_1 = (cant_alumnos_1 * 100) / cupo
porc_alumnos_2 = (cant_alumnos_2 * 100) / cupo
porc_alumnos_3 = (cant_alumnos_3 * 100) / cupo
cant_estudiantes_1 = (cant_alumnos_1 + cant_alumnas_1)
cant_estudiantes_2 = (cant_alumnos_2 + cant_alumnas_2)
cant_estudiantes_3 = (cant_alumnos_3 + cant_alumnas_3)
prom_general = cant_estudiantes_1 + cant_estudiantes_2 + cant_estudiantes_3
# Código de identificación del curso que tenga menos alumnos inscriptos.
if total_alumnos_1 < cupo:
    print('curso', nombre_curso_1, 'pocos alumnos (', cant_estudiantes_1, ') alumnos en el curso')
if total_alumnos_2 < cupo:
    print('curso', nombre_curso_2, 'pocos alumnos (', cant_estudiantes_2, ') alumnos en el curso')
if total_alumnos_3 < cupo:
    print('curso', nombre_curso_3, 'pocos alumnos (', cant_estudiantes_3, ') alumnos en el curso')
if total_alumnos_1 > cupo:
    print('curso', nombre_curso_1, 'demasiados alumnos (', cant_estudiantes_1,
          ') alumnos en el curso abrir nueva division')
if total_alumnos_2 > cupo:
    print('curso', nombre_curso_2, 'demasiados alumnos (', cant_estudiantes_2,
          ') alumnos en el curso abrir nueva division')
if total_alumnos_3 > cupo:
    print('curso', nombre_curso_3, 'demasiados alumnos (', cant_estudiantes_3,
          ') alumnos en el curso abrir nueva division')
else:
    print('error')
'''7. Virus Pantevil
Son muchas las concesionarias que en el último tiempo se han visto afectados por el poderoso virus PANTEVIL que ataca los registros de automóviles, alterando el identificador de la patente de los mismos. Sabemos que el identificador de patente de un automóvil está compuesto por 3 letras en mayúsculas y 3 números, por ejemplo AED335.
Luego de un exhaustivo análisis de los registros infectados, se logró decodificar cómo funciona el virus. Vamos a separar en letras y números para explicar cómo codifica el virus:
Letras:
El virus transforma cada carácter en el entero Unicode al que representa.
Luego chequea si esos tres números son iguales, en caso afirmativo reemplaza los valores del primer y último número por valores
aleatorios generados entre 65 y 90.
Una vez que tiene esos números, los convierte a cadena de caracteres y los concatena, anteponiendo:
Un signo @ en caso que los tres números hayan sido iguales o
Un signo & en caso contrario.
Números:
Para codificar los números el virus utiliza una cadena con 5 caracteres
El primer carácter codifica:
Un signo + si los 3 números eran pares y les suma 1 a cada número.
Un signo - si los 3 números no son pares.
En el segundo carácter el virus pone:
Un signo # en caso que el primer número y el segundo son iguales,| y cambia el valor de segundo numero por el tercero.
Un signo $ en caso que el primer número y el tercero son iguales, |y cambia el valor de tercer numero por el segundo.
Un signo * en caso que el segundo número y el tercero son iguales,| y cambia el valor de tercer numero por el primero.
Un signo ! en caso que los 3 números sean diferentes.
En el tercero, cuarto y quinto carácter el virus simplemente concatena los números resultantes.
Finalmente y como si fuera poco, una vez codificados, el virus invierte el orden de los números y letras.
Esto es primero coloca los números codificados y luego las letras codificadas. Veamos algunos ejemplos:
Patente sin Virus                   Patente con Virus

AED335                                   -#355&656968

PEP456                                    -!456&806980

RRR682                                   +!793@898280
Debido a la gravedad del caso, las concesionarias afectadas no pueden realizar ninguna venta hasta que no se reparen
los archivos dañados,
es que nos han solicitado con urgencia un reparador para el virus PANTEVIL. '''
print('Desencriptador PANTEVIL a sus servicios')
pantevil_code = input('ingrese patente codificada: ')
primernumero = int(pantevil_code[2])
segundonumero = int(pantevil_code[3])
tercernumero = int(pantevil_code[4])
pantevil_primeraletra = int(pantevil_code[6] + pantevil_code[7])
pantevil_segundaletra = int(pantevil_code[8] + pantevil_code[9])
pantevil_terceraletra = int(pantevil_code[10] + pantevil_code[11])
# letras decodificadas
primer_letra = chr(pantevil_primeraletra)
segunda_letra = chr(pantevil_segundaletra)
tercer_letra = chr(pantevil_terceraletra)
# Un signo + si los 3 números eran pares y les suma 1 a cada número.
# Un signo - si los 3 números no son pares.
# primer digito
if pantevil_code[0] == '+':
    primernumero = primernumero - 1
    segundonumero = segundonumero - 1
    tercernumero = tercernumero - 1
else:
    primernumero % 2 != 0 and segundonumero % 2 != 0 and tercernumero % 2 != 0
    # segundo digito
'''Un signo # en caso que el primer número y el segundo son iguales, y cambia el valor de segundo numero por el tercero.
   Un signo $ en caso que el primer número y el tercero son iguales, y cambia el valor de tercer numero por el segundo.
   Un signo * en caso que el segundo número y el tercero son iguales, y cambia el valor de tercer numero por el primero.
   Un signo ! en caso que los 3 números sean diferentes.'''
if pantevil_code[1] == '!':
    print('')
elif pantevil_code[1] == '#':
    segundonumero = primernumero
    primernumero = segundonumero
elif pantevil_code[1] == '$':
    primernumero = tercernumero
    tercernumero = primernumero
elif pantevil_code[1] == '*':
    segundonumero = tercernumero
    tercernumero = segundonumero
'''Luego chequea si esos tres números son iguales, en caso afirmativo reemplaza los valores del primer y último número por valores
aleatorios generados entre 65 y 90.
Una vez que tiene esos números, los convierte a cadena de caracteres y los concatena, anteponiendo:
Un signo @ en caso que los tres números hayan sido iguales o
Un signo & en caso contrario.'''
if pantevil_code[5] == '@':
    primer_letra = segunda_letra
    tercer_letra = segunda_letra
print('/=' * 55)
print('tu patente es: ')
print(primer_letra, segunda_letra, tercer_letra, primernumero, segundonumero, tercernumero, sep='')
input('')
'''8. Juego de Dados: Pares e Impares
Desarrollar un programa para simular un juego de dados con las siguientes reglas:

Participan 2 jugadores
En cada ronda se lanzan 2 dados. Si la suma de ambos es impar, gana el jugador 1; si no, gana el jugador 2.
Primera ronda: el ganador obtiene tantos puntos como indica la suma de los dados
Segunda ronda: a los puntos de la primera ronda, el ganador suma tantos puntos como
indique el dado de mayor valor, y al perdedor se le restan tantos puntos como indique el dado de menor valor
Se pide:'''

'''Mostrar en cada ronda el valor de los dados y los puntajes de cada jugador.
Determinar quién fue el ganador por mayor cantidad de puntos (puede haber un empate).
Al terminar, informar si en alguna de las rondas se obtuvo el mismo valor en ambos dados.'''
rondas_ganadas_1 = 0
rondas_ganadas_2 = 0
puntos_ganados_1 = 0
puntos_ganados_2 = 0
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dados = dado1 + dado2
dadogrande = max(dado1, dado2)
dadochico = min(dado1, dado2)
print('tus dados dan: ', dado1, dado2)
if dados % 2 != 0:
    print('ganador numero 1')
    print('tus dados son: ', dado1, dado2)
    rondas_ganadas_1 += 1
    puntos_ganados_1 += dados
    print('el jugador 1 obtuvo', puntos_ganados_1, 'puntos')
    print('Ronda 2')
    print('Dado grande: ', dadogrande, 'Dado chico: ', dadochico)
    puntos_ganados_1 += dadogrande
    puntos_ganados_2 -= dadochico
    print('Los puntos del ganador son: ', puntos_ganados_1,'y los puntos del perdedor son: ', puntos_ganados_2)
else:
    print('ganador numero 2')
    print('tus dados son: ', dado1, dado2)
    rondas_ganadas_2 += 1
    puntos_ganados_2 += dados
    print('el jugador 2 obtuvo', puntos_ganados_2)
    print('Ronda 2')
    print('Dado grande: ', dadogrande, 'Dado chico: ', dadochico)
    puntos_ganados_2 += dadogrande
    puntos_ganados_1 -= dadochico
    print('Los puntos del ganador son: ', puntos_ganados_2,'y los puntos del perdedor son: ', puntos_ganados_1)
''''cree un programa que ingresando 4 numeros los ordene de mayor a menor y
viceversa, dceterminar si la suma de los dos primeros es un numero par, y
determinar si la suma de los dos ultimos son numero impar. no usar max() ni
min()'''
numero_1 = int(input('ingrese primer valor'))
numero_2 = int(input('ingrese segundo valor'))
numero_3 = int(input('ingrese tercer valor'))
numero_4 = int(input('ingrese cuarto valor'))
if numero_1 > numero_2:
    orden1, orden4 = numero_1, numero_2
else:
    orden1, orden4 = numero_2, numero_1
if numero_3 > orden1 > orden4:
    orden1, orden2, orden3 = numero_3, orden1, orden4
elif orden1 > numero_3 > orden4:
    orden1, orden2, orden3 = orden1, numero_3, orden4
elif orden1 > orden4 > numero_3:
    orden1, orden2, orden3 = orden1, orden4, numero_3
if numero_4 > orden1 > orden2 > orden3:
    orden1, orden2, orden3, orden4 = numero_4, orden1, orden2, orden3
elif orden1 > numero_4 > orden2 > orden3:
    orden1, orden2, orden3, orden4 = orden1, numero_4, orden2, orden3
elif orden1 > orden2 > numero_4 > orden3:
    orden1, orden2, orden3, orden4 = orden1, orden2, numero_4, orden3
elif orden1 > orden2 > orden3 > numero_4:
    orden1, orden2, orden3, orden4 = orden1, orden2, orden3, numero_4
print('primer numero: ', orden1, ' segundo numero: ', orden2, ' tercer numero:'
                        '', orden3,'cuarto numero: ', orden4)
print('/'*70)
print('la suma de los dos primeros numeros: ',(orden1+orden2),
         'la suma de tus ultimos dos numeros: ', (orden3+orden4))
if (orden1+orden2)%2==0:
    print('la suma de tus dos primeros numeros son pares')
if (orden3+orden4)%2!=0:
    print('la suma de tus ultimos dos numeros es impar')
else:
    print('la suma de tus dos ultimos numeros es par')
