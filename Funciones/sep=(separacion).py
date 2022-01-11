#sin sep
print('SIN SEP')
numero1= float(input('Ingrese 1er numero'))
numero2= float(input('Ingrese 2er numero'))
numero3= float(input('Ingrese 3er numero'))
mayor= max(numero1, numero2, numero3)
menor= min(numero1, numero2, numero3)
if numero1==numero2==numero3:
   print('todos los numeros son iguales')
elif mayor>numero1>menor:
    mayor, medio, menor= mayor, numero1, menor
elif mayor>numero2>menor:
   mayor, medio, menor= mayor, numero2, menor
elif mayor>numero3>menor:
   mayor, medio, menor= mayor, numero3, menor
print('primero(',mayor ,')segundo(',medio,')tercero(',menor,')')
resto= numero1%numero2
if resto==numero3:
    print('Tu Tercer numero(',numero3,') Es el resto de los dos primeros')
else:
    print('Tu Tercer numero(',numero3,') NO es el resto de los dos primeros')
#con sep
print('CON SEP')
numero1= float(input('Ingrese 1er numero'))
numero2= float(input('Ingrese 2er numero'))
numero3= float(input('Ingrese 3er numero'))
mayor= max(numero1, numero2, numero3)
menor= min(numero1, numero2, numero3)
if numero1==numero2==numero3:
   print('todos los numeros son iguales')
elif mayor>numero1>menor:
    mayor, medio, menor= mayor, numero1, menor
elif mayor>numero2>menor:
   mayor, medio, menor= mayor, numero2, menor
elif mayor>numero3>menor:
   mayor, medio, menor= mayor, numero3, menor
print('primero(',mayor ,')segundo(',medio,')tercero(',menor,')', sep='')
resto= numero1%numero2
if resto==numero3:
    print('Tu Tercer numero(',numero3,') Es el resto de los dos primeros',sep='')
else:
    print('Tu Tercer numero(',numero3,') NO es el resto de los dos primeros',sep='' )
