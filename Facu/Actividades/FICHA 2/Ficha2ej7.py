'''7. Votación en el Congreso
En el Congreso se vota la sanción de una ley muy importante.
Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra,
e informe el porcentaje obtenido en cada caso.'''

vfavor = int(input('votos a favor'))
vcontra = int(input('votos en contra'))
porcentaje = (vfavor * 100) // vcontra

print(porcentaje)
