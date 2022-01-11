# FACTORIAL
x = int(input('escribe un numero'))
f = 1
for i in range(1, x + 1):
    f = f * i
print('tu numero es: ', f)
# Multiplo de un numero
x = int(input('escribe un numero'))
m = int(input('ingrese multiplo'))
for i in range(0, (x + 1), m):
    print('tu numero es: ', i)
'''1. Ciclistas
La final de una carrera de ciclistas tiene n competidores
(n se ingresa por teclado).

Desarrollar un programa que permita cargar, por cada competidor,
nombre y tiempo de carrera. Luego se pide:

a) Determinar y mostrar el nombre del ganador de la carrera.

b) Ingresar por teclado el tiempo record registrado para dicha carrera.
Determinar si el tiempo del ganador es menor al tiempo record, mostrar un
mensaje.

c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.'''

n = int(input('ingrese competidores'))
tiempototal = 0
for i in range(0, n):
    nombre = input('ingrese nombre: ')
    tiempo = int(input('ingrese el tiempo: '))
    tiempototal += tiempo
    promedio = (tiempototal / n)
    if i == 0:
        tiempomax = tiempo
        nombre_ganador = nombre

    if tiempo > tiempomax:
        tiempomax = tiempo
        nombre_ganador = nombre

print('ganador', nombre_ganador, 'tiempo ganador', tiempomax)
print('Promedio', promedio)
'''2. Secuencia de impares
Cargar por teclado dos números, e imprimir los números impares que 
se encuentran comprendidos entre ellos, en forma ascendente y descendente.'''
n1 = int(input('ingrese numero 1: '))
n2 = int(input('ingrese numero 2: '))
if n1 > n2:
    may, men = n1, n2
else:
    may, men = n2, n1
if men % 2 == 0:
    men += 1
if may % 2 == 0:
    may -= 1
ascendente = range(men, may + 1, 2)
for i in ascendente:
    print(i)
print('*' * 100)
descendente = range(may, men - 1, -2)
for e in descendente:
    print(e)
'''3. Ingresar por teclado los sueldos de un vendedor, correspondientes al
primer semestre del año y luego:

a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto
del período. nice

b) Determinar en qué mes recibió el sueldo más bajo del período.

c) Informar el sueldo promedio del semestre.'''
semestre = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio')
primero = True
total = 0
for i in semestre:
    sueldo = int(input('Ingrese su sueldo de ' + str(i) + ': '))
    if primero:
        may = sueldo
        men = sueldo, i
        primero = False
        total += sueldo
    else:
        total += sueldo
        if may < sueldo:
            may = sueldo
        if sueldo < men[0]:
            men = sueldo

aguinaldo = may / 2
print('[]' * 100)
print('su aguinaldo es de: ', aguinaldo)
print('su sueldo mas bajo fue en ' + men[1] + ' con ' + str(men[0]))
print('y el total del semestre es de: ', total)
'''4. Decimal a Hexadecimal

Generar n numeros aleatorios entre el rango de 5000 y 450000, por cada 
uno de ellos mostrar y generar el numero hexadecimal'''
'''5. Analisis de Texto

El usuario ingresa una frase al comenzar el programa, la misma no puede tener
 longitud cero. La frase finaliza con un punto, 
 y las palabras están separadas por espacios únicamente.
Se debe mostrar:

a) Ver el porcentaje de vocales respecto del total de letras de la frase.

b) La longitud promedio de las palabras

c) La longitud de la palabra mas larga del texto

c) Cantidad de palabras que comienzan con "ta"'''
tiene_t = False
tiene_ta = 0
palabras = 0
letras = 0
cant_vocales = 0
texto = input('ingrese texto')
long_text = len(texto)
for letras in texto:
    if letras == 'a' or letras == 'e' or letras == 'i' or letras == 'u':
        cant_vocales += 1
        letras += 1
    if letras == ' ':
        palabras += 1

    if letras == 't':
        tiene_t = True
        letras += 1
    if letras == 'a' and tiene_t:
        tiene_t = False
        tiene_ta += 1
        letras += 1
'''6. Números Enteros
Escribir un programa que permita leer la cantidad de números enteros ingresados
 por el usuario y calcular lo siguiente:

a) El segundo menor

b) El promedio de los números positivos.

c) El mayor de los números negativos.'''


def segundo_menor(men, seg_men, i, n):
    if i == 0:
        men = n
    elif i == 1:
        if men > n:
            men = n
            seg_men = men
    elif men < n:
        seg_men = n
    else:
        if n < men:
            men, seg_men = n, men
        elif n < seg_men:
            seg_men = n
    return seg_men, men


def promedio(x, y):
    if y != 0:
        prom = x / y
    return prom


# mayor negativo
carga = int(input('ingrese numeros a cargar'))
mayor = menor = mayor_negativo = contador_positivo = contador_negativo = 0
sumatoria_positiva = 0
for i in range(carga):
    print('ingrese numero ', i + 1)
    numero = int(input())
    if numero > 0:
        contador_positivo += 1
        sumatoria_positiva += numero
    if i == 0:
        menor = numero
    if i >= 1:
        if numero > menor:
            mayor = numero
            menor = menor

        else:
            mayor = menor
            menor = mayor
    if 0 > mayor > menor:
        mayor_negativo = mayor
    elif 0 > menor > mayor:
        mayor_negativo = menor
print('el mayor negativo es: ', mayor_negativo)
if contador_positivo != 0:
    print('el proemdio de positivos es: ',
          promedio(sumatoria_positiva, contador_positivo))
'''7 Cargar por teclado una frase, pero a razón de un caracter por 
vez en una variable. La frase debe terminar con un punto 
(al aparecer el punto, la carga debe finalizar). El programa debe informar:

a) Promedio de letras por palabra.

b) Cantidad de palabras que terminan con la letra 's' (minúscula).

c) Cantidad de palabras que contienen a la sílaba 'sa' (minúscula).'''
texto = input('ingrese texto a analizar: ')
anterior = None
termina_con_s = 0
palabras = 0
tiene_sa = 0
letras = 0
for caracter in texto:
    if (caracter == '.' or caracter == ' '):
        palabras += 1
        if (caracter == '.' or caracter == ' ') and anterior == 's':
            termina_con_s += 1
    else:
        letras += 1
    if anterior == 's' and caracter == 'a':
        tiene_sa += 1
    elif caracter == '.' and anterior != None:
        break
    anterior = caracter


def prom(x, y):
    if y != 0:
        promedio = x / y
    else:
        promedio = 0
    return promedio


print(letras)
print(palabras)
print('Promedio de letras por palabra ', prom(letras, palabras))
print('Cantidad de palabras que terminan con la letra s (minúscula): ',
      termina_con_s)
print('Cantidad de palabras que contienen a la sílaba sa (minúscula): ',
      tiene_sa)
'''8. Puntos en un plano
Desarrollar un programa que permita ingresar las coordenadas de n puntos
en el plano, e informe:

a) En qué cuadrante se encuentra cada uno.

b) Determinar cuántos puntos se encuentran en el primer o tercer cuadrante.

c) Determinar cuál de todos los puntos cargados se encuentra a mayor distancia
del origen de coordenadas.'''
import math
def cuadrantes(x, y):
    if x < 0 and y < 0:
        pos = print('pertenece al tercer cuadrante')
    elif x > 0 and y < 0:

        pos = print('pertenece al cuarto cuadrante')
    elif x > 0 and y > 0:
        pos = print('pertenece al primer cuadrante')
    else:
        pos = print('pertenece al segundo cuadrante')
    return (pos)

n = int(input('ingrese cuantas coordenadas quiere analizar: '))
cant_en_primer_tercer = mayor = 0
mayor=0

for i in range(n):
    x = float(input('ingrese punto x: '))
    y = float(input('ingrese punto y: '))
    cuadrantes(x, y)
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        cant_en_primer_tercer += 1
        print('+1')
    # mayor
        modulo = math.sqrt((x ** 2) + (y ** 2))
        if modulo>mayor:
            mayor=modulo
        print('modulo de: ', (x, y),'es: ', modulo)
print('la mayor distancia desde el punto de origen es: ', mayor)
print('hay ',cant_en_primer_tercer, 'puntos en los cuadrantes 1 y 3')
'''9. Números: Mayor y Menor
Cargar por teclado n números enteros positivos, uno a uno.
Se deberá establecer qué número es el mayor de los números pares y
el menor de los números impares.

Por ejemplo, en una secuencia de números: 8, 15, 9, 2, 27, 18, 0; el
mayor de los pares sería el número 18 y el menor de los impares el número 9.'''
cant_numeros=int(input('ingrese cuantos numeros quiere procesar'))
inpar=0
for num in range(cant_numeros):
    print('ingrese numero ', num+1)
    numeros=int(input())
    if numeros%2==0:
        if num==0:
            mayor= numeros
        elif mayor<numeros:
            mayor=numeros
    elif numeros%2!=0 and numeros!=0:
        inpar+=1
        if inpar==1:
            menor=numeros
        if menor>numeros:
            menor=numeros
print('el mayor de los números pares', mayor)
print('el menor de los números inpares', menor)
'''10. Caracteres: Promedio de Letras.
Cargar por teclado una frase (de a un caracter por vez). La carga solo debe
terminar cuando se ingrese un punto (el cual no forma parte de la frase a
procesar). Se debe informar la cantidad de palabras de la frase y cantidad
 promedio de letras por palabra. Por ejemplo, la frase “Este es un ejercicio
  muy sencillo.” tiene 6 palabras y la cantidad promedio de letras por palabra
  es de 4,66 ([4+2+2+9+3+8]/6).'''
palabra = 0
letras=0
anterior = None
texto=input('ingrese texto (con . termina)')
for carac in texto:
    if carac==' ' or carac=='.':
        palabra+=1
        if anterior!=None and carac=='.':
            break
    else:
        letras+=1
print('promedio de letras por texto: ', letras/palabra)
'''11. Caracteres: Sílaba 'ci'
Cargar por teclado una frase, cada palabra separada unicamente por espacio y
el texto terminar cuando se ingrese un punto
(el cual no forma parte de la frase a procesar).
Se debe obtener la cantidad de palabras que poseen al menos una vez la sílaba
“ci”. Por ejemplo, la frase “Este es un ejercicio moderado.” tiene 1 palabra
que posee la sílaba “ci” (“ejercicio”).'''
__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Tratamiento de Caracteres, lectura caracter por caracter')
print('-' * 90)

hay_c = False
hay_ci = False
cantidad_palabras_ci = palabra  =0

texto = input('Ingrese el texto a procesar: ')
texto = texto.upper()

print('Tratamiento de Caracteres, lectura caracter por caracter')
print('-' * 90)

hay_c = False
hay_ci = False
cantidad_palabras_ci = 0

texto = input('Ingrese el texto a procesar: ')
texto = texto.upper()

for car in texto:
    if car != ' ' and car != '.':
        if car == 'C':
            hay_c = True
        else:
            if car == 'I' and hay_c:
                hay_ci = True
            hay_c = False
    else:
        if hay_ci:
            cantidad_palabras_ci += 1
        hay_ci = False

print('La cantidad de palabras que tienen ci son', cantidad_palabras_ci)
