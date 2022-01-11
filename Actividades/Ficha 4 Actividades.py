'''1. Generador de Dirección de Mail
Se desea un programa que: solicite al usuario un nombre, un apellido y
el dominio y luego, proponga una dirección de mail para el nombre y
apellido ingresado de acuerdo a las siguientes reglas:
Componer la dirección de correo de la siguiente manera:
<primera letra del nombre><apellido>@<dominio>
Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= frc.utn.edu.ar la dirección de mail sería:
fsteffolani@frc.utn.edu.ar
Pero si la primera letra del nombre y la primera letra del apellido son la misma entonces utilizar:
<nombre>.<apellido>@<dominio>
Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:
soledad.steffolani@colegiorosarito.edu.ar'''

# resultados: Mail completo

# Datos: 1.nombre 2.apellido 3.dominio 4.direccion

# procesos: if primeraletranombre!=primeraletraapellido mail de forma AKibysz@gmail.com bla bla bla
#          else primeraletranombre==primeraletraapellido mail de forma Alexander.ASTHETIC@gmail.com
nombre = input('ingrese nombre')
apellido = input('ingrese apellido')
dominio = input('ingrese dominio web')
direccion = input('ingrese su direccion mail(''gmail, hotmail, etc'')')
if nombre[0] != apellido[0]:
    print(nombre[0] + apellido + dominio + '@' + direccion + '.com')
else:
    print(nombre + '.' + apellido + dominio + '@' + direccion + '.com')

'''2. Suma - División - Potencia
Se necesita desarrollar un programa que
permita calcular la suma de tres números.
Si el resultado es mayor a 10 dividir por 2
(mostrar su resultado sin decimales),
en caso contrario elevar el resultado al cubo.'''
a = int(input('pon tu primer numero'))
b = int(input('pon tu segundo numero'))
c = int(input('pon tu tercer numero'))
suma = a + b + c
if suma > 10:
    print(int(suma / 2))
else:
    print(suma ** 3)
'''3. Impuesto Automotor
Crear un programa que permita calcular los impuestos que 
debe pagar un auto, conociendo su modelo (año de fabricación) y tipo 
(P: Particular/T: Taxi/R: Remis). Para calcular los impuestos, tener en cuenta que:

a. Los autos particulares de menos de 10 años de antigüedad pagan $200, entre 10 y 20 años pagan $150 y 
no pagan impuestos los que tienen más de 20 años.

b. Los taxis pagan impuestos como auto particular, más $150 por la licencia de taxi.

c. Los remises pagan $100 por cada año de antigüedad de su vehículo.'''
# resultado:
# datos:
# procesos:
vehiculo = input('ingrese tipo de vehiculo T/P/R')
anos = int(input('ingrese anios del vehiculo'))
r = anos * 100
taxI = anos + 150
# Particular
if vehiculo == ('p' or 'P') or vehiculo == ('t' or 'T'):
    if vehiculo == 'p' or vehiculo == 'P':
        print('tienes un auto particular')
        if anos < 10:
            print('tu impuesto es de 200$')
        else:
            if 20 > anos >= 10:
                print('tu impuesto es de 150$')
            else:
                print('tu impuesto es de 0$')
                # TAXI
    else:
        print('tienes un taxi tu impuesto es de: ', taxI, '$')
        # Remis
else:
    print('tienes un Remis y tu impuesto es:', r, '$')
'''4. Calculo de Regularidad
La facultad pide un simple programa que pida las
tres notas de un alumno en cualquier materia y
mostrar si el alumno esta libre, regular o promocionado.
Las tres notas son los dos parciales mas la nota de prácticos
y las condiciones de regularidad están descriptas a continuacón:

El promedio menor a 4 el alumno esta libre.
El promedio comprendido entre 4 y 8 el alumno esta regular.
El promedio mayor a 8 el alumno está promocionado.'''
n1 = float(input('ingrese nota parcial 1'))
n2 = float(input('ingrese nota parcial 2'))
n3 = float(input('ingrese nota trabajos practicos'))
prom = (n1 + n2 + n3) / 3
if prom > 8:
    print('alumno promocionado promedio de: ', prom)
else:
    if prom < 4:
        print('alumno libre promedio de :', prom)
    else:
        print('alumno regular promedio de: ', prom)
'''
5. Punto en el plano
Se pide realizar un programa que ingresando el valor x e y de un punto determine a que cuadrante pertenece en el sistemas de coordenadas.
'''
x = float(input('pon x'))
y = float(input('pon tu y'))
if x > 0 and y > 0:
    print('estas en el 1er cuadrante capo')
else:
    if x > 0 and y < 0:
        print('estas en el cuarto cuadrante master')
    else:
        if x < 0 and y < 0:
            print('tas en el tercer cuadrante mi rey/na')
        else:
            print('estas en el 2 cuadrante campeon')
'''6. Se tienen los datos de tres postulantes a un empleo a los que se les realizó un test de capacitación.
Por cada postulante se tiene la siguiente información:
nombre del postulante, cantidad total de preguntas que se le realizaron y cantidad de preguntas que contestó correctamente.

Se pide confeccionar un programa que lea los datos de los tres postulantes, informe el nivel de cada uno según los
criterios de aprobación que se indican mas abajo, e indique finalmente el nombre del postulante que ganó el puesto.
Los criterios de aprobación son los siguientes, en función del porcentaje de respuestas correctas sobre el total de
preguntas realizadas a cada postulante:

     Nivel Superior:       Porcentaje >= 90%
     Nivel Medio:          75% <= Porcentaje < 90%
     Nivel Regular:        50% <= Porcentaje < 75%
     Fuera de Nivel:       Porcentaje < 50%'''
'''6. Postulantes a un empleo
Se tienen los datos de tres postulantes a un empleo a los que se les
realizó un test de capacitación. Por cada postulante se tiene la siguiente
 información:
 datos:
 #nombre del postulante,
 #cantidad total de preguntas que se le realizaron y
 #cantidad de preguntas que contestó correctamente.

Se pide confeccionar un programa que lea los datos de los tres postulantes,
informe el nivel de cada uno según los criterios de aprobación que se indican mas
abajo, e indique finalmente el nombre del postulante que ganó el puesto. Los criterios
de aprobación son los siguientes, en función del porcentaje de respuestas correctas sobre
el total de preguntas realizadas a cada postulante:
* Nivel Superior:       Porcentaje >= 90%
* Nivel Medio:          75% <= Porcentaje < 90%
* Nivel Regular:        50% <= Porcentaje < 75%
* Fuera de Nivel:       Porcentaje < 50%'''
postulantes = ('postulante 1. Alexander Kibysz', 'postulante 2. Jeremie De Philipis', 'postulante 3. Bianca Cano')
cantpreguntas = int(input('cantidad de preguntas realizadas al candidato 1')), int(
    input('cantidad de preguntas realizadas al candidato 2')), int(
    input('cantidad de preguntas realizadas al candidato 3'))
cantpregrespondidas = int(input('cantidad de preguntas respondidas del candidato 1')), int(
    input('cantidad de preguntas respondidas del candidato 2')), int(
    input('cantidad de preguntas respondidas del candidato 3'))
porcentajes = (cantpreguntas[0] * cantpregrespondidas[0]) / 10, (cantpreguntas[1] * cantpregrespondidas[1]) / 10, (
            cantpreguntas[2] * cantpregrespondidas[2]) / 10
total = (postulantes[0], porcentajes[0]), (postulantes[1], porcentajes[1]), (postulantes[2], porcentajes[2])
print('/' * 100)
# Nivel 1\\\\\\
if porcentajes[0] > 9:
    print('nivel superior:', total[0])
else:
    if porcentajes[0] >= 7.5:
        print('nivel medio: ', total[0])
    else:
        if 5 <= porcentajes[0]:
            print('nivel regular: ', total[0])
        else:
            print('fuera de nivel: ', total[0])
print('/' * 100)
# nivel 2//////////////
if porcentajes[1] > 9:
    print('nivel superior:', total[1])
else:
    if porcentajes[1] >= 7.5:
        print('nivel medio: ', total[1])
    else:
        if 5 <= porcentajes[1]:
            print('nivel regular: ', total[1])
        else:
            print('fuera de nivel: ', total[1])
# nivel 3
print('/' * 100)
if porcentajes[2] > 9:
    print('nivel superior:', total[2])
else:
    if porcentajes[2] >= 7.5:
        print('nivel medio: ', total[2])
    else:
        if 5 <= porcentajes[2]:
            print('nivel regular: ', total[2])
        else:
            print('fuera de nivel: ', total[2])
print('/' * 100)
# ganador
if porcentajes[0] > porcentajes[1] > porcentajes[2]:
    print('el ganador es: ' + total[0])
else:
    if porcentajes[0] < porcentajes[1] < porcentajes[2]:
        print('el ganador es: ', total[2])
    else:
        if porcentajes[0] < porcentajes[1] > porcentajes[2]:
            print('el ganador es: ', total[1])
'''Se necesita desarrollar un programa
para el área de recursos humanos de una
empresa que permita informar el jornal
de un determinado operario. Usted deberá
cargar por teclado el código de turno que
el operario trabajó ese día
(1- representa Diurno y 2- representa Nocturno)
 y la cantidad de horas trabajadas.

La política de trabajo en la empresa es que los
operarios de la misma pueden trabajar en
el turno diurno o nocturno. Si un operario trabaja
 en el turno nocturno el pago es 40.60 pesos la hora,
  si lo hace en el turno diurno cobra 35.50 pesos la hora.'''
horario = int(input('ingrese numero de seleccion\n1-Diurno y 2-Nocturno: '))
hora = int(input('ingrese horas trabajadas'))
jornalnocturno = 40.69 * hora
jornaldiurno = 35.50 * hora
if horario == 1:
    print(jornaldiurno)
else:
    print(jornalnocturno)
'''8. Comercio
Un comerciante tiene a la venta 3 tipos de artículos principales.
Conociendo la cantidad vendida de cada artículo y el precio unitario de cada artículo
, hacer un programa que determine cuál fue el producto que
realizó el mayor aporte en los ingresos y el porcentaje que
dicho aporte significa en el ingreso absoluto de los 3 artículos sumados.
Ese porcentaje se calcula así:
Absoluto    ____________  100%
Mayor aporte   _________     x %
Por lo tanto:    x = mayor aporte  *  100 / absoluto'''
articulos = 'Huevo de Dinosaurio', 'Panqueque Original de Stranger Things', 'Cafe de Cafeina'
articulosprec = 350, 300, 200
print('1.350 2.300 1.200')
vendidos = float(input('cuantas unidades del articulo 1 se vendieron?')), float(
    input('cuantas unidades del articulo 2 se vendieron?')), float(
    input('cuantas unidades del articulo 3 se vendieron?'))
venta = (articulosprec[0] * vendidos[0], articulosprec[1] * vendidos[1], articulosprec[2] * vendidos[2])
absoluto = venta[0] + venta[1] + venta[2]
mayorparte = max(venta[0], venta[1], venta[2])
porcentajemax = (mayorparte * 100) / absoluto
mostrar = (articulos[0], articulosprec[0], venta[0]), (articulos[1], articulosprec[1], venta[1]), (
    articulos[2], articulosprec[2], venta[2])
print('/' * 200)
print('/' * 200)
print('/' * 200)
print('/' * 200)
print('ganancia total de: ', absoluto)
# 1,2,3 PUESTO
if venta[0] > venta[1] > venta[2]:
    print('en primer puesto: ' + articulos[0], 'su ganancia fue de: ', venta[0],
          '\n',
          'en segundo puesto: ',
          articulos[1], 'su ganancia fue de: ', venta[1],
          '\n',
          'en tercer puesto: ', articulos[2], 'su ganancia fue de: ', venta[2])
else:
    if venta[0] > venta[2] > venta[1]:
        print('en primer puesto: ' + articulos[0], 'su ganancia fue de: ', venta[0],
              '\n',
              'en segundo puesto: ',
              articulos[2], 'su ganancia fue de: ', venta[2],
              '\n',
              'en tercer puesto: ', articulos[1], 'su ganancia fue de: ', venta[1])
    else:
        if venta[1] > venta[2] > venta[0]:
            print('en primer puesto: ' + articulos[1], 'su ganancia fue de: ', venta[1],
                  '\n',
                  'en segundo puesto: ',
                  articulos[2], 'su ganancia fue de: ', venta[2],
                  '\n',
                  'en tercer puesto: ', articulos[0], 'su ganancia fue de: ', venta[0])
        else:
            if venta[1] > venta[0] > venta[2]:
                print('en primer puesto: ' + articulos[1], 'su ganancia fue de: ', venta[1],
                      '\n',
                      'en segundo puesto: ',
                      articulos[0], 'su ganancia fue de: ', venta[0],
                      '\n',
                      'en tercer puesto: ', articulos[2], 'su ganancia fue de: ', venta[2])
            else:
                if venta[2] > venta[0] > venta[1]:
                    print('en primer puesto: ' + articulos[2], 'su ganancia fue de: ', venta[2],
                          '\n',
                          'en segundo puesto: ',
                          articulos[0], 'su ganancia fue de: ', venta[0],
                          '\n',
                          'en tercer puesto: ', articulos[1], 'su ganancia fue de: ', venta[1])
                else:
                    if venta[2] > venta[1] > venta[0]:
                        print('en primer puesto: ' + articulos[2], 'su ganancia fue de: ', venta[2],
                              '\n',
                              'en segundo puesto: ',
                              articulos[1], 'su ganancia fue de: ', venta[1],
                              '\n',
                              'en tercer puesto: ', articulos[0], 'su ganancia fue de: ', venta[0])
                    else:
                        print('ERRRRRRRRORRRRRRRRRRRRRRRRRR')
'''9. Pago a un Proveedor
Un comercio necesita informar el importe final
a pagar a un determinado proveedor.

Para ello debe ingresar la categoría
(que puede ser categoría 'A' o 'B')

y el importe original a abonar.

Considerar las siguientes condiciones para el cálculo del importe final a pagar:

Si el cliente es categoría A y el monto a pagar supera a los 1000 pesos debe aplicarse un descuento del 5%.
Si el cliente es categoría B y el importe a pagar oscila entre 1500 y 2500 pesos debe aplicarse un descuento del 2%.
Para ambas categorías en caso de no cumplirse las condiciones especificadas no se aplicará ningún tipo de descuento
sobre el importe que se le debe abonar.'''

print('Una Facturita A o B masters!')
Factura=input('A o B')
importe=float(input('monto a pagar'))
descuentoA=importe-(importe*0.05)
descuentoB=importe-(importe*0.02)
if Factura=='A' or Factura=='a':
    print('Factura A chosen perdone el frances')
    if importe>1000:
        print('tenes un descuentazo del %5 mastercard te quedaria en: ', descuentoA)
    else:
        print('el monto a pagar es importe jeje', importe)
else:
    if 1500<importe<2500:
        print('tenes alto decuento campeon de %2 te quedaria en : ', descuentoB)
    else:
        print('el monto a pagar es de: ', importe)
'''
10. Galería de Arte
Una galería de arte desea preparar un catálogo de sus cuadros más famosos. 
Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. 
El programa deberá:
Verificar si todos los cuadros son anteriores al siglo XX 
(El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000).
Determinar cuántos tienen antigüedad inferior a 10 años. 
Si no hay ninguno, imprimir el mensaje "Renovar stock”.
'''
cuadros = 'la banana y la cinta', 'el bulto de un griego', 'una pelota pinchada'
anios = int(input('ingrese anio del cuadro 1')), int(input('ingrese anio del cuadro 2')), int(input('ingrese anio del cuadro 3'))
tot0 = cuadros[0], anios[0]
tot1 = cuadros[1], anios[1]
tot2 = cuadros[2], anios[2]

antiguedad= (2020-anios[0]), (2020-anios[1]), (2020-anios[2])
if 1901 > anios[0] and 1901 > anios[1] and 1901 > anios[2]:
    print('Todos tus cuadros son anteriores al siglo XX'
          '\n', tot0,
          '\n', tot1,
          '\n', tot2)
else:
    if 1901 <anios[0]<2000 and 1901<anios[1]<2000 and 1901<anios[2]<2000:
        print('todos tus cuadros son del siglo XX')
if antiguedad[0]<10:
    print('Tu primer cuadro tiene menos de 10 anios')
else:
    if antiguedad[1]<10:
     print('tu segundo cuadro tiene menos de 10 anios')
    else:
        if antiguedad[2]<10:
            print('tu cuadro tiene menos de 10 anios')
if antiguedad[0]<10 and antiguedad[1]<10 and antiguedad[2]<10:
    print('Renovar Stock todos tus cuadros tienen menos de 10 anios')
'''11. Temperatura diaria
Se solicita realizar un programa que
permita generar tres temperaturas en
forma aleatoria
(correspondientes a diferentes momentos de un día) y determinar:

Cual es el promedio de las temperaturas.
Si existe alguna temperatura que sea mayor al promedio.'''
import random
# número aleatorio entero y tal que 2 <= y < 10
t1 = random.randrange(20, 42)
t2= random.randrange(20, 42)
t3=random.randrange(20, 42)
print('temperatura 1: ', t1)
print('temperatura 2: ', t2)
print('temperatura 3: ', t3)
prom=(t1+t2+t3)/3
print('promedio de temperaturas',prom)
if prom<t1:
    print('la temperatura 1 es mayor al promedio')
else:
    if prom<t2:
        print('la temperatura 2 es mayor al promedio')
    else:
        if prom<t3:
            print('la temperatura 3 es mayor al promedio')
'''13. Analisis de palabra
Se pide un programa que le solicite al usuario
que ingrese una palabra. Con esa palabra calcular
 los siguientes puntos:

Determinar la cantidad de letras que tiene  la palabra.
Mostrar un mensaje que informe si la palabra termina en vocal.'''
palabra = input('ingrese palabra')
canpal = len(palabra)
ultimaletra = palabra[-1]
print('la cantidad de letras son de: ', canpal)
if ultimaletra=='A' or 'E' or 'I' or 'O' or 'U' or 'a' or 'e' or 'i' or 'o' or 'u':
    print('tu palabra termina con vocal', ultimaletra)
'''14. ¿Piedra, Papel o Tijera?
Desarrollar un programa que permita al 
usuario jugar contra la computadora el clásico 
“Piedra, Papel o Tijera” y determine cuál de ellos es el ganador.

Las reglas son:

La piedra aplasta (o rompe) la tijera. (Gana la piedra).
La tijera corta el papel. (Gana la tijera).
El papel envuelve la piedra. (Gana el papel)
Si los dos jugadores eligen el mismo elemento, empatan.'''
print('quieres jugar piedra papel o tijera con tu computadora, te sientes solo?')
x='Piedra', 'Papel', 'Tijera'
Humano=input('Piedra, Papel o Tijera')
PC=random.choice(x)
print(PC)
