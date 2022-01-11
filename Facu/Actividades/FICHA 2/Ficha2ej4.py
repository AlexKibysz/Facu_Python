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
