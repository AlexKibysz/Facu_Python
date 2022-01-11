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
