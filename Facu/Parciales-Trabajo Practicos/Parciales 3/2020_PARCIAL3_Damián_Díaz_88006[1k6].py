#Parcial 3 (05 de septiembre de 2020)
# Una empresa de recursos humanos desea un programa para procesar los datos de los postulantes que se han presentado a la convocatoria.
# Para cada postulante se tienen los siguientes datos: número de identificación del postulante, apellido del postulante, puntaje obtenido en la entrevista
# y código del área al que se postula el postulante (valor entero entre 0 y 12, por ejemplo: 0: Administración 1: Recursos Humanos, etc.).
# Se desea almacenar información referida a los n postulantes que se presentaron en la empresa de recursos humanos en un arreglo de registros de tipo
# Postulante (definir el tipo Postulante y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones,  que permita gestionar las siguientes tareas:
#
# 1. Cargar el arreglo pedido con los datos de los n postulantes. Valide que el número identificador del postulante sea positivo y que el código de área a
# la que se postula sea mayor o igual a cero y menor o igual que 12. Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios)
# o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
# 2. Mostrar todos los datos de los postulantes cuyo puntaje obtenido este comprendido entre un valor x y otro valor y, siendo x e y valores que se cargan por teclado,
# en un listado ordenado de mayor a menor según los apellidos de los participantes.
# 3. Determinar y mostrar la cantidad de postulantes por cada código de área posible. En total, 13 contadores usando un vector de conteo. Mostrar solo
# los valores del vector que sean distintos de cero.
# 4. Mostrar los datos de todos los postulantes que hayan obtenido un puntaje mayor al promedio de todos los puntajes del vector. Al final del listado,
# mostrar la cantidad de postulantes que se incluyeron en el listado.
# 5. Determinar si existe un postulante cuyo número identificador sea igual a c, siendo c un valor que se carga por teclado. Si existe, mostrar sus datos.
# Si no existe, informar con un mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.

class Postulante:
    def __init__(self, identificacion, apellido, puntaje, codigo):
        self.identificacion = identificacion
        self.apellido = apellido
        self.puntaje = puntaje
        self.codigo = codigo

def validar_numero_positivo(mensaje_de_carga):
    n = int(input(mensaje_de_carga))
    while n <= 0:
        print("El número ingresado debe ser positivo...")
        n = int(input("Ingrese de nuevo: "))
    return n

def validar_codigo():
    codigo = int(input("Ingrese el código de área a la que se postula (un número entre 0 y 12): "))
    while codigo < 0 or codigo > 12:
        print("El código de área ingresado no corresponde a ninguna...")
        codigo = int(input("Ingrese de nuevo: "))
    return codigo

def cargar_vector():
    identificacion =validar_numero_positivo("Ingrese el número de identificación del postulante: ")
    apellido = input("Ingrese el apellido: ")
    puntaje = validar_numero_positivo("Ingrese el puntaje obtenido en la entrevista: ")
    codigo = validar_codigo()
    return Postulante(identificacion, apellido, puntaje, codigo)

def generar_vector(n):
    vec_postulantes = []
    for i in range(n):
        vec_postulantes.append(cargar_vector())
    return vec_postulantes

def ordenar(vec_postulantes):
    n = len(vec_postulantes)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vec_postulantes[i].apellido < vec_postulantes[j].apellido:
                vec_postulantes[i], vec_postulantes[j] = vec_postulantes[j], vec_postulantes[i]

def mostrar_un_postulante(un_postulante):
    return "Postulante N°: " + str(un_postulante.identificacion) + \
        " | Apellido: " + un_postulante.apellido + \
        " | Puntaje: " + str(un_postulante.puntaje) + \
        " | Código del área a la que se postula: " + str(un_postulante.codigo)

def mostrar_postulantes_entre_dos_valores(vec_postulantes, x, y):
    print("Los postulantes que obtuvieron un puntaje entre ", x, "y ", y, "son:")
    for i in range(len(vec_postulantes)):
        if vec_postulantes[i].puntaje >= x and vec_postulantes[i].puntaje <= y:
            print(mostrar_un_postulante(vec_postulantes[i]))

def conteo_area(vec_postulantes):
    vec_areas = [0] * 13
    for i in range(len(vec_postulantes)):
        vec_areas[vec_postulantes[i].codigo] += 1
    return vec_areas

def mostrar_postulantes_por_area(vec_areas):
    for i in range(len(vec_areas)):
        if vec_areas[i] != 0:
            print("Cantidad de postulantes en el área ", i, ": ", vec_areas[i])

def puntaje_promedio(vec_postulantes):
    puntaje_promedio = 0
    postulantes = 0
    for i in range(len(vec_postulantes)):
        puntaje_promedio = puntaje_promedio + vec_postulantes[i].puntaje
        postulantes += 1
    puntaje_promedio_final = puntaje_promedio / postulantes
    return puntaje_promedio_final

def posicion_postulantes_puntaje_mayor_al_promedio(vec_postulantes, promedio):
    posiciones = []
    cant_postulantes_promedio = 0
    for i in range(len(vec_postulantes)):
        if vec_postulantes[i].puntaje > promedio:
            posiciones.append(i)
            cant_postulantes_promedio += 1
    return posiciones, cant_postulantes_promedio

def mostrar_postulantes_puntaje_mayor_al_promedio(vec_postulantes, posiciones, cantidad):
    if cantidad > 0:
        print("Los postulantes que obtuvieron un puntaje mayor al puntaje promedio son:")
        for i in range(len(posiciones)):
            print(mostrar_un_postulante(vec_postulantes[i]))
    else:
        print("Ningún postulante obtuvo un puntaje mayor al promedio.")

def buscar_postulante_por_identificacion(vec_postulantes, c):
    s = 0
    for i in range(len(vec_postulantes)):
        if vec_postulantes[i].identificacion == c:
            postulante_buscado = i
            s += 1
        if s == 1:
            break
    if s == 0:
        postulante_buscado = -1
    return postulante_buscado

def programa_principal():
    opcion = -1
    vec_postulantes = []
    while opcion != 0:
        print("Opción 1: Cargar el vector de los postulantes.")
        print("Opción 2: Buscar los postulantes que hayan obtenido un puntaje entre x e y (siendo estos 2 valores cargados por usted).")
        print("Opción 3: Mostrar la cantidad de postulantes por área.")
        print("Opción 4: Mostrar los postulantes que obtuvieron un puntaje mayor al puntaje promedio")
        print("Opción 5: Buscar un postulante a partir del número de identificación")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            cantidad = validar_numero_positivo("Ingrese la cantidad de postulantes a cargar: ")
            vec_postulantes = generar_vector(cantidad)
            input("Presione ENTER para continuar...")
        if opcion == 2:
            if vec_postulantes != []:
                x = validar_numero_positivo("Ingrese el límite inferior del puntaje: ")
                y = validar_numero_positivo("Ingrese el límite superior del puntaje: ")
                ordenar(vec_postulantes)
                mostrar_postulantes_entre_dos_valores(vec_postulantes, x, y)
                input("Presione ENTER para continuar...")
            else:
                print("El vector de los postulantes está vacío. Por favor, cárguelo...")
                input("Presione ENTER para continuar...")
        if opcion == 3:
            if vec_postulantes != []:
                vec_postulantes_por_area = conteo_area(vec_postulantes)
                mostrar_postulantes_por_area(vec_postulantes_por_area)
                input("Presione ENTER para continuar...")
            else:
                print("El vector de los postulantes está vacío. Por favor, cárguelo...")
                input("Presione ENTER para continuar...")
        if opcion == 4:
            if vec_postulantes != []:
                promedio = puntaje_promedio(vec_postulantes)
                vec_postulantes_puntaje_promedio, cant_postulantes_puntaje_promedio = posicion_postulantes_puntaje_mayor_al_promedio(vec_postulantes, promedio)
                mostrar_postulantes_puntaje_mayor_al_promedio(vec_postulantes, vec_postulantes_puntaje_promedio, cant_postulantes_puntaje_promedio)
                print("La cantidad de postulantes que obtuvieron un puntaje mayor al puntaje promedio son: ", cant_postulantes_puntaje_promedio)
                input("Presione ENTER para continuar...")
            else:
                print("El vector de los postulantes está vacío. Por favor, cárguelo...")
                input("Presione ENTER para continuar...")
        if opcion == 5:
            if vec_postulantes != []:
                nro_id_a_buscar = validar_numero_positivo("Ingrese el número de identificación que desea buscar: ")
                posicion_nro_id_buscada = int(buscar_postulante_por_identificacion(vec_postulantes, nro_id_a_buscar))
                if posicion_nro_id_buscada != -1:
                    print("El postulante que tiene el número de identificación buscado es: ")
                    print(mostrar_un_postulante(vec_postulantes[posicion_nro_id_buscada]))
                    input("Presione ENTER para continuar...")
                else:
                    print("No se ha encontrado ningún postulante con el número de identificación buscado...")
                    input("Presione ENTER para continuar...")
            else:
                input("Presione ENTER para continuar...")

if __name__== '__main__':
    programa_principal()



