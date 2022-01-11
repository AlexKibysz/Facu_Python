# 1. Cuadrados y cubos
# Leer dos números y calcular:
# La suma de sus cuadrados.
# El promedio de sus cubos.
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
