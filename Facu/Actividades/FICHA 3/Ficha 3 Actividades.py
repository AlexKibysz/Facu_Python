'''1. Plazo fijo
Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo por un cliente de un
banco y calcular el saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que el interés pactado era de
2.3% y que el banco cobra una tasa fija de gastos por servicios financieros igual $20 por cuenta.'''
deposito = float(input('ingrese dinero a depositar: '))
ganancia = deposito * 0.023
plazofijo = (deposito + ganancia) - 20
print('dinero total: ', plazofijo)
''' 2. Fecha como cadena
Desarrollar un programa que cargue por teclado 
una cadena de caracteres que se supone representa 
una fecha en formato 'dd/mm/aaaa', y muestre por separado el 
día, el mes y el año. Ejemplo: si la cadena ingresada es '16/03/2016' 
el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'''

'''fechas = input('ingrese dd/mm/aaaa')
print(fechas, ano)'''
'''3. Importe como cadena
Desarrollar un programa que cargue por teclado un importe 
(cantidad de dinero) expresado como número en coma flotante y 
muestre un mensaje con esa cantidad pero en dos formatos:
en uno debe aparecer precedida por el signo '$' y en el otro debe aparecer precedida 
por la palabra "pesos".'''
plata = float(input('ingrese dinero'))
print(plata, '$')
print(plata, 'pesos')
'''4. Duración de un vuelo
Desarrollar un programa que, 
conociendo el horario de partida y llegada de un vuelo (hora y minutos), 
determine cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más 
para ir del aeropuerto al hotel que ha reservado, ¿a qué hora llegara al mismo?'''

print('ingrese su hora y minuto de partida')
partidah, partidam = float(input('hora de partida')), float(
    input('minuto de partida'))
print('ingrese su hora y minuto de llegada')
llegadah, llegadam = float(input('hora de llegada')), float(
    input('minuto de llegada'))
viaje = ((llegadah * 60) + llegadam) - ((partidah * 60) + partidam)
viajetotal = viaje + 45
print('vas a llegar a las: ', viajetotal, 'min')
print('vas a llegar en: ', ((viaje / 60) + 0.45), 'hs')

'''5. Control electoral
Desarrollar un programa de control electoral en un centro vecinal, 
en el que se ingresen, para cierto candidato: apellido, 
nombre y cantidad de votos. Luego presentar en pantalla un resumen que muestre: 
iniciales del candidato, cantidad de votos entre paréntesis, y debajo una línea con tantas 
 "x" como votos obtenidos (por ejemplo, el candidato obtuvo 4 votos, deberá aparecer una línea
  como esta:  "xxxx"  con cuatro letras "x") (Asumimos que en el centro vecinal no hay demasiados electores, 
  de forma que podamos estar seguros que no habrá miles o millones de votos... sólo unos pocos para darle sentido 
  al enunciado).'''
votos = int(input('ingrese cantidad de votos'))
nombre = 'Alexander Kibysz'
print(nombre, votos)
inicialn, iniciala = nombre[0], nombre[10]
x = (votos * 'x')
votosfinales = print(inicialn, iniciala, '(', votos, ')')
print(x)
'''6. Cálculo de sueldo
Se conoce el monto del salario actual de un empleado, el nombre del empleado
y el área funcional al cual pertenece.

Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento del 8% sobre su
salario actual
y un descuento de 2.5% por servicios, informando los resultados con el formato que se especifica a continuación:
Nombre Empleado:  xxxxxxxxx
Nuevo Salario: $ xxx
Área Funcional:  xxxxxxxxxxxx
Salario Actual: $ xxxx'''
# +5.5%
Empleado = 'Alexander Kibysz'
Salario = float(input('ingrese salario'))
Areaf = 'Ingeniero'
salarioaumento = (Salario * 0.055) + Salario
print('Nombre Empleado: ', Empleado)
print('Nuevo Salario: ', Salario)
print('Area Funcional: ', Areaf)
print('Salario Actual: ', salarioaumento)

'''7. Cálculo presupuestario
En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología. El presupuesto anual del hospital se reparte de la siguiente manera:
Urgencias=37%
Pediatria=42%
Traumatologia=21%
Cargar por teclado el monto del presupuesto 
total del hospital, y calcular y 
mostrar el monto que recibirá cada área.
'''
ingresostotales = float(input('ingresos del hospital'))
poru = (ingresostotales * 3.7) / 10
porp = (ingresostotales * 4.2) / 10
port = (ingresostotales * 2.1) / 10
print('ingresos totales', ingresostotales,
      '\nporcentaje urgencias', poru,
      '\nporcentaje pediatria', porp,
      '\nporcentaje trauma', port)
'''8. Calculo Distancia de Viaje
Un persona cautivada por los paisajes argentinos
se le ocurrió la loca idea de unir los puntos
mas extremos (Ushuahia y La Quiaca) en bicicleta,
es decir se propuso hacer 3641.3 Km en bicicleta.
Nuestro aventurero efectivamente inició
la travesía pero se accidentó y sólo recorrió x metros
 según su GPS.
Usted debe solicitar ese valor x e informar cuántos kilómetros y metros
recorrió nuestro aventurero y qué porcentaje represento lo recorrido del total de kms
 a recorrer de Ushuahia a La Quiaca (para el porcentaje usted deberá realizar los calculos en metros).'''
kilometros = 3641.3
accidente = float(input('km en el que se accidento'))
gpsubi = kilometros - accidente
gpsum = (gpsubi / 1000)
print('ustede esta en el metro', gpsum, 'usted esta en el km', gpsubi)
porcentaje = (gpsubi * gpsum) / 100
print('ustede esta alejado un %', porcentaje)
'''
9. Costos del Proyecto
Una pequeña empresa de informática tiene que
desarrollar un sistema de información y para ello
 tiene un presupuesto de x pesos para cubrir los
 costos de crear el sistema. Sabiendo que tiene pensado
 ganar al menos 17% por el proyecto, determine cuál es el
 valor máximo que pueden alcanzar los costos del proyecto.
'''
presupuesto = float(input('presupuesto'))
ganancia = presupuesto * 1.7
print(ganancia)
'''10. Tiempos de Triatlon
Un triatlón es una competición deportiva en que los participantes realizan tres carreras:

una de natación, una ciclista y una pedestre.

Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos)
logrados en cada etapa por uno de los deportistas participantes.
Con esos datos determinar:
    *Tiempo total de la prueba (en formato hh:mm:ss)
    *Tiempo máximo y mínimo (en segundos)
    *Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)
Consejo: convertir a segundos los horarios ingresados, para facilitar las operaciones'''

tiempom = float(input('ingrese tiempo transcurrido en minutos '))
tiempos = float(input('ingrese tiempo transcurrido en segundos'))
tiempos1 = (tiempom * 60)
tiempototal1 = tiempos1 + tiempos
primeraetapa = tiempototal1
print('tardo', tiempototal1, 's en la primera etapa')
# 2 etapa
print('/' * 200)
tiempom2 = float(input('ingrese tiempo transcurrido en minutos 2da etapa'))
tiempos2 = float(input('ingrese tiempo transcurrido en segundos 2da etapa'))
tiempos2 = (tiempom2 * 60)
tiempototal2 = tiempos2 + tiempos2
segundaetapa = tiempototal2
print('tardo', tiempototal2, 's en la segunda etapa')
print('/' * 200)
# 3 etapa
tiempom3 = float(input('ingrese tiempo transcurrido en minutos 3ra etapa'))
tiempos3 = float(input('ingrese tiempo transcurrido en segundos 3ra etapa'))
tiempos3 = (tiempom3 * 60)
tiempototal3 = tiempos3 + tiempos3
terceraetapa = tiempototal3
print('tardo', tiempototal3, 's en la tercera etapa')
print('/' * 200)
# Tiempo total de la prueba (en formato hh:mm:ss)
tiempofinalhoras = (tiempototal1 + tiempototal2 + tiempototal3) / 3600
tiempofinalminutos = (tiempototal1 + tiempototal2 + tiempototal3) / 60
tiempototlasegundos = (tiempototal1 + tiempototal2 + tiempototal3)
tiempototalprueba = (
tiempofinalhoras, 'hs', tiempofinalminutos, 'min', tiempototlasegundos, 's')
print(tiempototalprueba)
# Tiempo máximo y mínimo (en segundos)
print('/' * 200)
maximo = max(tiempototal1, tiempototal2, tiempototal3)
print('el maximo es ', maximo, 's')
minimo = min(tiempototal1, tiempototal2, tiempototal3)
print('tu tiempo minimo fue', minimo, 's')
# Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)
print('/' * 200)
final = primeraetapa + segundaetapa + terceraetapa
redondeadofinal = round(final, 2)
print('el tiempo total es de: ')
print(redondeadofinal, 's')
'''11. Palabra enmascarada
Desarrollar un programa que permita ingresar
una palabra por teclado y la devuelva enmascarada,
mostrando la primer letra y la última, pero reemplazando
los caracteres intermedios por asteriscos.
Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.'''
palabra = input('pon tu palabra')
numeros = len(palabra)
print(numeros)
x = numeros
print(x)
mascara = palabra[0] + '*' * (x - 2) + palabra[(x - 1)]
print(mascara)
