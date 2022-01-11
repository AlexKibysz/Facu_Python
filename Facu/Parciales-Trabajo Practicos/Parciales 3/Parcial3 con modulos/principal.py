"""
Una empresa de seguros pide un programa para procesar los datos de las Pólizas que están siendo administradas.
Por cada Póliza se conoce su número de identificación, el nombre del cliente, el tipo de póliza
(un valor del 0 al 19, por ejemplo: 0: Terceros, 1: Terceros Transportados, 2: Total, etc.)
y el costo mensual de dicha poliza. Se desea almacenar la información referida a los n pólizas en un
 arreglo de registros de tipo Poliza (definir el tipo Poliza y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones,  que permita gestionar las siguientes tareas:

1- Cargar el arreglo con los datos de las n pólizas. Valide que el costo mensual de la póliza sea mayor a cero y
que el tipo de póliza esté en el rango especificado. Puede hacer la carga en forma manual, o puede generar los datos
en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2- Mostrar todos los datos de todas las pólizas, en un listado ordenado de mayor a menor según el nombre de los clientes.

3- Determinar la cantidad total por cada tipo de póliza que se carga en el puerto, 20 contadores en total en un vector de conteo.

4- Determinar el costo mensual promedio entre todas las pólizas del vector que sean tipo 2, 5, o 9.
Muestre además los datos de todas las pólizas de esos tres tipos, cuyo costo mensual sea menor al promedio que acaba de calcular.

5- Determinar si existe una póliza cuya número sea igual x y tal que su costo mensual sea mayor a un valor c,
siendo x y c dos valores que se carga por teclado. Si existe, mostrar sus datos.
Si no existe, informar con un mensaje.
Si existe mas de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
"""
from funciones import *
from time import sleep


# Script principal
def principal():
    # Título
    print('PARCIAL 3 DE AED')
    print('-' * 100)

    # Generación del vector, y bandera
    vector_polizas = []
    cargado = False

    # Menú de opciones
    op = -1
    while op != 6:
        print()
        print('=' * 100)
        print('1 --> Cargar pólizas')
        print('2 --> Mostrar todas las pólizas, ordenadas por nombre del cliente')
        print('3 --> Mostrar cantidad total de cada tipo de póliza')
        print('4 --> Costo mensual promedio entre las pólizas de tipo 2, 5, 9')
        print('5 --> Buscar por número de identificacion y costo')
        print('6 --> Salir')
        print('=' * 100)

        # Ingreso de opcion
        op = int(input('-Ingrese una opción: '))
        print()

        # Opcion 1
        if op == 1:
            if not cargado:
                n = validar_carga('-Ingrese la cantidad de pólizas: ', 1)

                # Carga...
                crear_vector(vector_polizas, n)
                cargado = True
                print('\n>>> El vector fue cargado con éxito!')
            else:
                print('>>> El vector ya fue cargado antes!!')

            sleep(1.5)

        # Opcion 2
        elif op == 2:
            if cargado:
                ordenar_por_nombres(vector_polizas)
                mostrar_vector(vector_polizas)
            else:
                print('>>> El vector no fue cargado!!')

            sleep(2)

        # Opcion 3
        elif op == 3:
            if cargado:
                # Se realiza el conteo
                conteo = contar_tipo(vector_polizas)

                # Se muestra...
                print('> Cantidad de polizas de cada tipo: \n')
                mostrar_conteo(conteo)
            else:
                print('>>> El vector no fue cargado!!!')

            sleep(2)

        # Opcion 4
        elif op == 4:
            if cargado:
                punto_4(vector_polizas)
            else:
                print('>>> El vector no fue cargado!!')

            sleep(2)

        # Opcion 5
        elif op == 5:
            if cargado:
                x = validar_carga('-Ingrese el número de identificación a buscar: ', 1)
                c = validar_carga('-Ingrese el costo mensual a buscar: ', 1)

                # Se realiza la busqueda...
                buscar = buscar_por_numero_costo(vector_polizas, x, c)

                # Se muestra según resultado...
                if buscar is not None:
                    print('\n> Se encontró un resultado para esta búsqueda:\n')
                    print(to_string(buscar))
                else:
                    print('\n> No se encontró ningún resultado para esta búsqueda...')
            else:
                print('>>> El vector no fue cargado!!')

            sleep(2)

        # Salida
        elif op == 6:
            print('>>> Chauuuu!')
            sleep(1)

        # Si no se elige ninguna opcion correcta...
        else:
            print('>>> No elegiste ninguna opción correcta, intentalo de vuelta!')
            sleep(1)


# Prueba del programa
if __name__ == '__main__':
    principal()
