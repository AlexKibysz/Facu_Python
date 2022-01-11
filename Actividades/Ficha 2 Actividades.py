# 1. Cuadrados y cubos
# Leer dos números y calcular:
# La suma de sus cuadrados.
# El promedio de sus cubos.
import math

a = float(input('ingrese su numero a'))
b = float(input('ingrese su numero b'))
sumadecuadrados = (a ** 2) + (b ** 2)
print('tu suma de cuadrados da: ', sumadecuadrados)
# promedio de cubos
cubos = (a ** 3) + (b ** 3)
prom = cubos / 2
print('el promedio de tus cubos da: ')
print(cubos)
print('-' * 100)
# 2. Descuento en medicinas
# Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
# (cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos
# tienen un descuento del 35%. Mostrar el precio actual,
# el monto del descuento y el monto final a pagar.
precio = float(input('precio del medicamento'))
descuento = (precio * 35) / 100
descuentoprecio = precio - descuento
preciofinal = descuento
print('Precio de medicamento: ', precio)
print('Precio con descuento: ', descuentoprecio)
print('descuento de: ', preciofinal)
# 3. Ecuación de Einstein
# La famosa ecuación de Einstein para conversión de una masa m en energía viene dada por la fórmula:
# E = mc2
# Donde c es la velocidad de la luz cuyo valor es c = 299792.458 km/seg.
# Desarrolle un programa que lea el valor una masa m en kilogramos y
# obtenga la cantidad de energía E producida en la conversión.
c = 299792.458
m = float(input('pon tu masa en km: '))
E = m * c ** 2
print('la energia obtenida es de: ', E)
# 4. Polinomio de segundo grado
# Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado
# , y calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado). Además,
# para el mismo polinomio, calcule y
# muestre el valor del discriminante de la fórmula para el cálculo de las raíces de la ecuación.
# RESULTADOS: 1.VALOR X 2. DISCRIMINANTE
#
#
a = float(input('\033[0;36m''Primer valor(A) '))
b = float(input('Segundo valor(B) '))
c = float(input('Tercer valor(C) ' + '\033[0;m'))

xf = (b ** 2) - 4 * a * c
if xf < 0:

    print('Valor irreal menor a 0')
elif xf >= 0:
    x1 = (-b + math.sqrt(xf)) / (2 * a)
    x2 = (-b - math.sqrt(xf)) / (2 * a)
    y1 = (-b / 2 * a)
    y2 = (-b / 2 * a)
    print('Tu valor de x1 es ={0} Tu valor de y1 es ={1}'.format(x1, y1))
    print('Tu valor de x2 es ={0} Tu valor de y2 es ={1}'.format(x2, y2))
    discriminante = (b ** 2) - (4 * a * c)
    print('tu discrimante es:', discriminante)
# 5. Cálculo de ángulos
# Se sabe que la suma de dos ángulos desconocidos (alfa + beta) es igual a cierto valor x
# que se carga por teclado. Además se sabe que la diferencia entre esos mismos dos ángulos
# (alfa - beta) es igual a otro valor y que también se carga por teclado.
# Desarrolle un programa que dados los valores x e y, determine el valor de los dos
# ángulos alfa y beta. No es necesario convertir a grados, minutos y segundos el valor de cada ángulo:
# expréselos como números reales, tal cual hayan sido obtenidos.
#
# Resultados: diferencia de angulos y suma de angulos
#
# datos: (alfa+beta)=x        (alfa-beta)=y
#
# procesos:
#
x = float(input('pon tu x'))
y = float(input('pon tu y'))
alpha = ((y + x) / 2)
beta = ((x - y) / 2)
print('tu alpha da: ', alpha)
print('tu beta da: ', beta)
print()
print('/' * 200)
''' 6. Precio de venta
Conociendo el precio de lista de un artículo, determinar:

Precio de venta al contado (10% de descuento) 
Precio de venta con tarjeta (5% de recargo)'''

articuloprecio = float(input('pon el precio del articulo'))
print('en contado tenes un 10% de descuento\n en tarjeta tenes un 5% de recargo')
preciocont = (articuloprecio * 10) / 100
recargo = (articuloprecio * 5) / 100
print('precio de contado con 10% de descuento')
print(articuloprecio - preciocont)
print('precio total tarjeta')
print(recargo + articuloprecio)

'''7. Votación en el Congreso
En el Congreso se vota la sanción de una ley muy importante. 
Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra, 
e informe el porcentaje obtenido en cada caso.'''

vfavor = int(input('votos a favor'))
vcontra = int(input('votos en contra'))
porcentaje = (vfavor * 100) // vcontra

print(porcentaje)

'''8. Rinde de un Campo Agricola
Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela. 
Se pide ingresar el largo y el ancho en metros de la parcela y determinar el rinde sabiendo que en 10 m2 
se obtienen 2 quintales.'''
largo = float(input('ingrese metros de largo'))
ancho = float(input('ingrese metros de ancho'))
metros = largo * ancho
quintales = (metros / 5)
print('vas a tener : ', quintales, 'quintales')
'''9. Datos de un rectángulo
Hacer un programa que tome como entrada el ancho y el alto de un rectángulo 
y determine el perímetro y la superficie del mismo.
'''
ancho = float(input('ingrese ancho'))
alto = float(input('ingrese alto'))
perimetro = alto + ancho
superficie = alto * ancho
print('tu perimetro es de:', perimetro)
print('tu superficie es de: ', superficie)
