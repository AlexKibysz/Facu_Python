# operaciones matematicas

# Autor Alexander Kibysz (Mr.Fox)
# Autor Jérémie De Philippis

import math

restart = 'no'
while restart == 'no':
    print('\nHola soy el FoxMath Sistema para Tus calculos')
    print("\n\033[1;33m" + "Seleccione una opcion" + '\033[0;m')
    print('1.Suma y Resta')
    print('2.Binomio Cuadrado Perfecto')
    print('3.Trinomio Cubico Perfecto')
    print('4.Potencias')
    print('5.Raices')
    print('6.Multiplos de un numero')
    print('7.Bhaskara')
    print('8.Pitagoras')
    print('9.Logaritmo')
    print('10.Conversion de Tiempo')
    print('11.Teorema del Resto')
    

    opcion = int(input('\nElija una opcion: '))
    print()
    # 1.Suma
    if opcion == 1:
        sr = print(input('Suma o Resta'))
        print('Cuantas variables quieres?')
        print('A.2 variables')
        print('B.3 variables')
        print('C.4 variables')
        print('D.Elegir Variables')

        os = str(input())
        # 1.opcion A 2 digits
        if os == 'A' or os == 'a':
            # 1.vs1/vs2/vs3/vs4=variable
            print('Dame tu primer Digito')
            vs1 = float(input())
            print('Dame tu segundo Digito')
            vs2 = float(input())
            if sr == 'suma' or sr == 'SUMA' or sr == 'Suma':
                print('tu suma es: ', vs1 + vs2)
            elif sr == 'resta' or sr == 'RESTA' or sr == 'Resta':
                print('tu resta es: ', vs1 - vs2)

        # 1.opcion B 3 digits
        if os == 'B' or os == 'b':
            print('Dame tu primer Digito')
            vs1 = float(input())
            print('Dame tu segundo Digito')
            vs2 = float(input())
            print('Dame tu tercer Digito')
            vs3 = float(input())
            print('tu suma es:', vs1 + vs2 + vs3)
        # 1.opcion C 4 digits
        if os == 'C' or os == 'c':
            print('Dame tu primer Digito')
            vs1 = float(input())
            print('Dame tu segundo Digito')
            vs2 = float(input())
            print('Dame tu tercer Digito')
            vs3 = float(input())
            print('Dame tu cuarto Digito')
            vs4 = float(input())

            print('tu suma es:', vs1 + vs2 + vs3 + vs4)

        # 1.opcion D ingresar digitos a eleccion
        if os == '4':

            def resta(args):  # todos los valores que ingreses en la funcion te lo devuelve en forma de tupla, osea un solo valor
                x = max(args)
                var1 = sum(args) - x

                return (x - var1)


            g = int(input('Cuantos digitos querés ingresar?'))
            lista = []
            for i in range(g):
                lista.append(float(input('{} Digito'.format(i + 1))))
            if suma_resta == '1':
                print(sum(lista))
            if suma_resta == '2':
                print(resta(lista))

    # 2.Binomio Cuadrado perfecto

    elif opcion == 2:

        a = float(input('pon tu A'))
        b = float(input('pon tu B'))
        bcp = a ** 2 + 2 * a * b + b ** 2

        print('Tu binomio cuadrado perfecto da:', bcp)

    # 3. Trinomio Cubo Perfecto

    elif opcion == 3:

        a = float(input('pon tu A'))
        b = float(input('pon tu B'))
        tcp = (a ** 3) + (3 * (a ** 2) * b) + (3 * a * (b ** 2)) + (b ** 3)

        print('Tu trinomio cubo perfecto da:', tcp)

    # 4.Potenciacion

    elif opcion == 4:

        a = float(input('pon tu Base'))
        b = float(input('pon tu Exponente'))
        pot = a ** b

        print('Tu potenciacion da:', pot)

    # 5.Raices

    elif opcion == 5:

        a = float(input('pon tu radicando'))
        b = float(input('pon tu indice'))
        rad = a ** (1 / b)

        print('tu Raiz da:', rad)

    # 6.Multiplos de X

    elif opcion == 6:

        n = float(input("\033[3;34m"'valor numerico: '))
        m = int(input('cantidad de multiplos: ' + '\033[0;m'))

        print('='*20)
        for r in range(1, m + 1):
            print("\033[3;33m" + str(r), '°', "multiplo= " + '\033[0;m' + str(r * n))
        else:
            print('='*20)

    # 7.Bhaskara

    elif opcion == 7:

        while True:
            try:
                a = float(input('Primer valor(A) '))
                b = float(input('Segundo valor(B) '))
                c = float(input('Tercer valor(C) '))
                break
            except ValueError:
                print('\033[0;31m'+'Solo números'+'\033[0m')
                continue

        xf = (b ** 2) - 4 * a * c

        try:
            x1 = (-b + math.sqrt(xf)) / (2 * a)
            x2 = (-b - math.sqrt(xf)) / (2 * a)
        except ValueError:
            print('Valor imaginario')
            x1, x2 = 'un valor imaginario','un valor imaginario'
        xdelV = (-b / (2 * a))
        ydelV = (a * (xdelV ** 2) + (b * xdelV) + c)
        print('Tu valor de x1 es =', x1,
        '\nTu valor de x2 es =', x2,
        '\nTu valor X del vertice es =', xdelV,
        '\nTu valor Y del vertice es =', ydelV)

    # 8. Pitagoras

    elif opcion == 8:
        print('Que quieres calcular?')
        print('A.Hipotenusa')
        print('B.Cateto Faltante')
        print(0)
        Cp = input()
        if Cp == ('a') or Cp == ('A'):
            a = float(input('\033[0;36m''Cateto valor(A) '))
            b = float(input('Cateto valor(B) ' + '\033[0;m'))
            # h = float(input('Hipotenusa valor(C) ' + '\033[0;m'))
            rph = ((a ** 2) + (b ** 2)) ** (1 / 2)
            print('tu hipotenusa da: ', rph)
        elif Cp == ('b') or Cp == ('B'):
            a = float(input('\033[0;36m''Cateto valor(A o B): '))
            h = float(input('Hipotenusa(H): ' + '\033[0;m'))
            rpc = ((h ** 2) - (a ** 2)) ** (1 / 2)
            print('Tu cateto desconocido da: ', rpc)

    # 9. Logaritmo
    elif opcion == 9:
        # x= exponente
        # base=base lo que cuelga
        # r resultado logaritmo

        # Printing the log base 5 of 14
        base = float(input('Inserte la base: '))
        exponente = float(input('Inserte el exponente: '))
        print("El logaritmo da  ")
        print(math.log(exponente, base))

    #10. De segundos a horas y minutos
    while True:
        try:
            segs = int(input('íngrese segundos= '))
            break
        except ValueError:
            print('\033[0;31m'+'--------------\n'
                'Solo numeros enteros!\n'
                '--------------\n\033[0m')
            continue
    if segs >=60:
        minutos = segs//60
        segs %= 60
        if minutos >= 60:
            horas = minutos//60
            minutos %=60
            print('Hrs: ', horas, 'Mintuos:', minutos,'Segundos: ', segs)
        else:
            print('Mintuos:', minutos,'Segundos: ', segs)
    else:
        print('Sgs: ',segs)

# Auto Observacion: falta usar el else para ampliar la capacidades de problemas es decir poder usar suma o resta
# dividir o multiplicar, o mixtos
restart = input('Finalizar Programa?')
