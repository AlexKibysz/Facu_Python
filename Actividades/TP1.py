#       TRABAJO PRACTICO AED 01
_author_ = 'De Philippis Jérémie, Cano Bianca, Kibysz Alexander'
# TP1-G040
# Legajo: 85421, 86809, 85698
# Curso: 1K02
# -----Carga de Datos------
print('\t\t\033[1;32m' + '=' * 40)
print('\t\t|           𝕋𝔼𝕊𝕋 ℂ𝕆𝕍𝕀𝔻 𝟙𝟡           |')
print('\t\t' + '=' * 40, '\033[0;0m')
# Punto 1
nombre = input('\nBienvenido, Ingrese su nombre: ')
edad = int(input('-' + nombre + ' ingrese su edad: '))
temperatura = float(input('-Ingrese su temperatura corporal: '))
neumonia = int(input(nombre + ' responda con:\n1 = Si\n2 = No\n'
                              '¿Usted tuvo neumonía previamente?: '))
caso_sospechoso = 0
# =================================Bandera=========================================+
grupo_de_riesgo = False
if edad > 60:
    grupo_de_riesgo = True
# =================================Bandera=========================================+
if neumonia == 1:
    caso_sospechoso = True
    mensaje = "\033[1;31m--CASO SOSPECHOSO--\n \033[0;0m Padece de Neumonia."
elif neumonia == 2 and temperatura < 38:
    caso_sospechoso = False
# Punto 2
elif neumonia == 2 and temperatura > 37:
    print('/' * 100)
    print('\n', nombre, 'Responda utilizando \033[1;32m(1 = Si / 2 = No)\033[0m segun corresponda\n')
    tos, odinofagia, dif_respi = int(input('-¿Padece de tos?: ')), \
                                 int(input('-¿Padece de dolor de garganta?: ')), \
                                 int(input('-¿Posee alguna otra dificultad respiratoria?: '))
    # Contador de problemas respiratorios
    problemas_respiratorios = 0
    if tos == 1:
        problemas_respiratorios += 1
    if odinofagia == 1:
        problemas_respiratorios += 1
    if dif_respi == 1:
        problemas_respiratorios += 1
    else:
        ''
    # Punto 3
    if temperatura > 37 and problemas_respiratorios > 0:
        print('/' * 100)
        print('Sr/Sra.' + nombre, '\nresponda utilizando \033[1;32m(1 = Si / 2 = No)\033[0m segun corresponda\n')
        print('Si dentro de los ultimos \033[31m14\033[0m dias usted..')
        personal_de_salud = int(input('-¿Estuvo activo como personal de salud?: '))
        contacto = int(input('-¿Estuvo en contacto con casos confirmados?: '))
        exterior = int(input('-¿Ha viajado al exterior?: '))
        local = int(input('-¿Estuvo en zonas nacionales con casos de transmisión local confirmados?: '))
        # =================================Bandera=========================================+
        sospechoso_exterior = False
        if personal_de_salud == 1 or contacto == 1 or exterior == 1:
            sospechoso_exterior = True
        # =================================Bandera=========================================+
        sospechoso_autoctono = False
        if local == 1:
            sospechoso_autoctono = True
        # =================================Bandera=========================================+
        if sospechoso_exterior or sospechoso_autoctono:
            caso_sospechoso = True
        else:
            caso_sospechoso = False
        if caso_sospechoso and sospechoso_autoctono and not sospechoso_exterior and problemas_respiratorios > 1:
            mensaje = '\033[1;31m--CASO SOSPECHOSO AUTOCTONO--\033[0;0m'
            mensaje += '\nNo tuvo contacto con casos confirmados ni ha viajado fuera del país,' \
                       'pero estuvo en zonas de transmisión local.'
            mensaje += '\nPosee, ademas, mas de un problema respiratorio.'
        elif caso_sospechoso or sospechoso_exterior:
            mensaje = '\033[1;31m--CASO SOSPECHOSO--\033[0;0m\nSe piensa que el contagio podria ser \
importado del extranjero.'
if not caso_sospechoso and grupo_de_riesgo:
    mensaje = '\033[1;34m--CASO NO SOSPECHOSO--\033[0;0m\nPero pertenece al grupo de riesgo.\nQUEDESE EN CASA.'
elif not caso_sospechoso and not grupo_de_riesgo:
    mensaje = '\033[1;34m--CASO NO SOSPECHOSO--\033[0;0m \nNo pertenece al grupo de riesgo.\nCuidese de todas formas.'
print('/' * 100)
print('\nSe ha diagnosticado al paciente ' + nombre + ' de edad', edad, 'como:\n', mensaje)
print('\n', '/' * 41, 'FIN DE PROGRAMA', '/' * 41)
# El siguiente input es para evitar que se cierre el programa :D
input()
