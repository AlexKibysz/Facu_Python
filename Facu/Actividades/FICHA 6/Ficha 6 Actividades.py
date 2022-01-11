'''1. Complejo de cines
Desarrollar un programa que permita procesar funciones de un complejo de cines.
 Por cada función se conoce: cantidad de espectadores y descuento (S/N).
 La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).

El programa deberá:

a) Calcular la recaudación total del complejo, considerando que el valor de
la entrada es de $50 en los días con descuento y $75 en los días sin descuento.

b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje
representan sobre el total de funciones.'''
espectadores = int(input('ingrese espectadores: '))
descuento = int(input('ingrese 1 si y 2 no'))
ventas = 0
print('*' * 100)
print('espectadores: ', espectadores)
while espectadores != 0:
    if descuento == 1:
        ventas += 50
        espectadores -= 1
    else:
        espectadores -= 1
        ventas += 75
print(' las ventas totales fueron de: ', ventas)
''''2. Ventas por sucursal
Ingresar una serie de números por teclado que representan la cantidad de 
ventas realizadas en las diferentes sucursales de un país de una determinada 
empresa.

Los requerimientos funcionales del programa son:

a) Informar la cantidad de ventas ingresadas.

b) Total de ventas.

c) Cantidad de ventas cuyo valor este comprendido entre 100 y 300 unidades.

d) Cantidad de ventas con 400, 500 y 600 unidades.

e) Indicar si hubo una cantidad de ventas inferior a 50 unidades.

Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor 
negativo.'''

Ventas_tipo_1 = 0
Ventas_tipo_2 = 0
Ventas_tipo_3 = 0
print('*' * 100)
ventas = 0
cant_ventas = 0
print('con un numero negativo se cierra el programa')
while ventas >= 0:
    ventas = int(input('ingresar ventas: '))
    cant_ventas += 1
    if 0 < ventas < 50:
        Ventas_tipo_3 += 1
    elif 600 >= ventas >= 400:
        Ventas_tipo_2 += 1
    elif 300 >= ventas >= 100:
        Ventas_tipo_1 += 1
    ventas -= 1
print('Ventas total: ', cant_ventas)
print('entre 100 y 300 ventas: ', Ventas_tipo_1)
print('400, 500 y 600 ventas: ', Ventas_tipo_2)
print('ventas inferior a 50 unidades: ', Ventas_tipo_3)
'''3. Promedio de números aleatorios
Realice un programa que permita calcular el promedio de 1000 números aleatorios 
generados en el rango de [0, 100000]'''
import random

num = 1000
cant_den = 0
cant_num = 0
while num != 0:
    aleatorio = random.randint(0, 100000)
    num -= 1
    cant_den += 1
    cant_num += aleatorio
print(cant_num, '/', cant_den)
promedio = cant_num / cant_den
print('Tu promedio es de: ', promedio)
'''4. Busqueda de mayor
Realizar un programa que permita buscar el mayor de 10.000 números aleatorios
 generados en el rango de [0, 100.000].'''
import random

num = 0
cont_ran = 0
maxi = 0
while num <= 10000:
    num += 1
    aleatorio = random.randint(0, 100000)
    if aleatorio > maxi:
        maxi = aleatorio
print('el maximo en los 10mil randoms es: ', maxi)
'''5. Menores y pomedio
Realizar un programa que genere 5000 numeros aleatorios en el rango de
[0, 100000] y que permita:

Determinar el menor de los numeros generados en forma aleatoria
Calcular el valor promedio de los números menores a 10.000.'''
import random

maximo, minimo = 0, 5000
num = 0
cont_men_10m = 0
while num <= 5000:

    num += 1
    aleatorio = random.randint(0, 100000)
    if aleatorio < minimo:
        minimo = aleatorio
    if aleatorio < 10.000:
        cont_men_10m += 1
promedio = cont_men_10m / 5000

print('El menor numero generado entre es: ', minimo)
print('numeros menores a 10mil: ', cont_men_10m)
print('el promedio de numeros menores a 10mil es de: ', promedio)
'''6. Números pares e impares
Se pide desarrollar un programa que permita leer una serie de números.
La finalización de carga de datos se presenta cuando el usuario ingrese un
número negativo.

Los requerimientos funcionales del programa son:

a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.

b) Cantidad de valores pares ingresados.

c) Cantidad de valores impares ingresados.

d) Informar si en la carga de números se ingreso al menos un número 0.

e) Informar si la serie contiene solo números pares e impares alternados'''
num = int(input('ingrese numero (si es negativo se cierra el programa): '))
contador_a = 0
contador_b = 0
contador_c = 0
alerta_0 = False
alternados = True
paridad_anterior = None
while num >= 0:
    num = int(input('ingrese numero (si es negativo se cierra el programa): '))
    if 100 >= num >= 50:
        contador_a += num
    paridad = num % 2
    if paridad == 0 and num >= 0:
        contador_b += 1
    elif paridad != 0 and num >= 0:
        contador_c += 1
    if num == 0:
        alerta_0 = True
    if paridad_anterior == paridad:
        alternados = False
    paridad_anterior = paridad

print('La sumatoria de solo los números que estén comprendidos entre 50 y 100'
      ' es: ', contador_a)
print('Cantidad de valores pares ingresados es: ', contador_b)
print('Cantidad de valores impares ingresados es: ', contador_c)
if alerta_0 == True:
    print('se ingreso un valor 0')
if not alternados:
    print('los numeros no estan alternados')
else:
    print('los numeros alternan')
'''7. Censo
Desarrollar un programa que permita procesar los datos del último censo de
una pequeña población.

Por cada habitante se ingresa: sexo (M/F) y edad. La carga de datos finaliza
al ingresar cualquier otro valor para sexo.

El programa debe informar:

a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que
puede ser igual)

b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)

c) Si hay algún varón que supere los 80 años de edad'''
cont_m = 0
cont_f = 0
edad_escolar = 0
edad_anciano = 0
cant_p = 0
sexo = input('sexo (M/F) el programa cierra con otro valor: ')
if sexo == 'M':
    cont_m += 1
    cant_p += 1
elif sexo == 'F':
    cont_f += 1
    cant_p += 1
else:
    print('ingrese valor valido')
while sexo == 'M' or sexo == 'F':
    edad = int(input('Ingrese edad: '))
    sexo = input('sexo (M/F) el programa cierra con otro valor: ')
    if sexo == 'F':
        cont_f += 1
        cant_p += 1
        if 18 >= edad and edad >= 4:
            edad_escolar += 1
    if sexo == 'M':
        cont_m += 1
        cant_p += 1
        if 80 < edad:
            edad_anciano += 1
print('*' * 100)
print('cantidad de hombres: ', cont_m)
print('cantidad de hombres: ', cont_f)
print('cantidad de hombres y mujeres: ', cant_p)
if cont_f > cont_m:
    print('hay mas mujeres que hombres')
elif cont_f < cont_m:
    print('hay mas hombres que mujeres')
elif cont_f == cont_m:
    print('hay la misma cantidad de mujeres y hombres')
print('mujeres en edad escolar: ', edad_escolar)
print('hombres +80: ', edad_anciano)
'''8. Mayor numero en orden par
Ingresar de a uno una serie de números. Encontrar e imprimir el mayor de todos
los números pares cuyo número de orden sea par, el proceso terminará cuando
el número leído sea igual a cero'''
num = int(input('ingrese un numero con (0) se cierra el programa'))
may = 0
while num > 0:
    num = int(input('ingrese un numero con (0) se cierra el programa'))
    if num % 2 == 0:
        if may < num:
            may = num
print('el mayor valor de los numeros pares es: ', may)
'''9. Comisión de Vendedores
Una empresa debe calcular el total de comisiones que debe abonar por
ventas realizadas por sus vendedores, para ello le solicita un sistemita
que le permita calcular dicho montos.

Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores
 (1 a 4). Usted debe solicitar el ingreso de la categoría del vendedor y
 el total de la venta (el proceso termina cuando se ingrese una categoría
 igual a cero) y acumular las comisiones de las ventas rendidas por los
 vendedores de diferentes en base a los siguientes cálculos:

a) Categoría 1: cobra una comisión de 10%
b) Categoría 2: cobra una comisión de 25%
c) Categoría 3: cobra una comisión de 30%
d) Categoría 4: cobra una comisión de 40%

Una vez procesadas todas las ventas mostrar el total de comisiones a
pagar por cada categoría de vendedores que tiene la empresa junto con el
total general'''

categoria = int(input('categorías de vendedores(1 a 4) con 0 cierra programa'))
venta = int(input('ingrese venta realizada'))
categoria1_porc = venta * 10 / 100
categoria2_porc = venta * 25 / 100
categoria3_porc = venta * 30 / 100
categoria4_porc = venta * 40 / 100
cat1_sumatoria = 0
cat2_sumatoria = 0
cat3_sumatoria = 0
cat4_sumatoria = 0
if categoria == 1:
    categoria1_porc = venta * 10 / 100
    cat1_sumatoria += categoria1_porc
elif categoria == 2:
    categoria2_porc = venta * 25 / 100
    cat2_sumatoria += categoria2_porc
elif categoria == 3:
    categoria3_porc = venta * 30 / 100
    cat3_sumatoria += categoria3_porc
elif categoria == 4:
    categoria4_porc = venta * 40 / 100
    cat4_sumatoria += categoria4_porc
else:
    print('ingrese valor valido')
while categoria != 0:
    categoria = int(input('categorías de vendedores(1 a 4) con 0 cierra '
                          'programa'))
    venta = int(input('ingrese venta realizada'))
    if categoria == 1:
        categoria1_porc = venta * 10 / 100
        cat1_sumatoria += categoria1_porc

    elif categoria == 2:
        categoria2_porc = venta * 25 / 100
        cat2_sumatoria += categoria2_porc

    elif categoria == 3:
        categoria3_porc = venta * 30 / 100
        cat3_sumatoria += categoria3_porc

    elif categoria == 4:
        categoria4_porc = venta * 40 / 100
        cat4_sumatoria += categoria4_porc

print('Comisiones Categoria 1: ', cat1_sumatoria)
print('Comisiones Categoria 2: ', cat2_sumatoria)
print('Comisiones Categoria 3: ', cat3_sumatoria)
print('Comisiones Categoria 4: ', cat4_sumatoria)
total = cat1_sumatoria + cat2_sumatoria + cat3_sumatoria + cat4_sumatoria
print('Total de comisiones: ', total)
'''10. Proceso de Discriminantes
Un matemático desea un simple programa que le permita cargar una serie de
números que representan los discriminantes de diferentes ecuaciones de segundo
 grado, el proceso de la secuencia finaliza cuando el matemático no desea
 seguir cargando discriminantes. Usted debe:


a) Determinar la cantidad de discriminantes que darán 2 raíces
b) Determinar la cantidad de discriminantes que darán una única raíz
c) Determinar la cantidad de discriminantes que daran raíces en el campo de
 los números imaginarios
d) Indicar el porcentaje que representa el punto c sobre el total de
discriminantes procesados por el matemático'''
