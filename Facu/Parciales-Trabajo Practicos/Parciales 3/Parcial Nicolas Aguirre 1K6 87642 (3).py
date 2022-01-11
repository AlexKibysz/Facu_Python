#Una empresa de recursos humanos desea un programa para procesar los datos de los postulantes que se han presentado
#a la convocatoria. Para cada postulante se tienen los siguientes datos: número de identificación del postulante,
#apellido del postulante, puntaje obtenido en la entrevista y código del área al que se postula el postulante
#(valor entero entre 0 y 12, por ejemplo: 0: Administración 1: Recursos Humanos, etc.).
#Se desea almacenar información referida a los n postulantes que se presentaron en la empresa de recursos humanos
#en un arreglo de registros de tipo Postulante (definir el tipo Postulante y cargar n por teclado).

#Se pide desarrollar un programa en Python controlado por un menú de opciones,  que permita gestionar las siguientes tareas:

#Cargar el arreglo pedido con los datos de los n postulantes. Valide que el número identificador del
#postulante sea positivo y que el código de área a la que se postula sea mayor o igual a cero y
#menor o igual que 12. Puede hacer la carga en forma manual, o puede generar los datos en forma
#automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
#Mostrar todos los datos de los postulantes cuyo puntaje obtenido este comprendido entre un valor x y otro valor y,
#siendo x e y valores que se cargan por teclado, en un listado ordenado de mayor a menor según los apellidos de los participantes.
#Determinar y mostrar la cantidad de postulantes por  cada tipo de localidad de origen posible. En total, 13
#contadores usando un vector de conteo. Mostrar solo los valores del vector que sean distintos de cero.
#Mostrar los datos de todos los postulantes que hayan obtenido un puntaje mayor al promedio de todos los puntajes
#del vector. Al final del listado, mostrar la cantidad de postulantes que se incluyeron en el listado.
#Determinar si existe un postulante cuyo número identificador sea igual a c, siendo c un valor que se carga por
#teclado. Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida
#con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
import random
class Postulante:
    def __init__(self,nro,apellido,puntaje,codigo):
        self.numero = nro
        self.apellido = apellido
        self.puntaje = puntaje
        self.codigo = codigo

def validate(n):
    while n<0:
        print("Error, debe introducir un valor superior a cero (0)")
        n = int(input("Ingrese el valor nuevamente: "))
    return n

def cargar_vector(vec):
    for i in range(len(vec)):
        apellidos ="Bernasconi", "Facciuto", "Hernandez", "Serra", "Fritelli", "Martinez", "Nicolli", "Lennon", \
        "McCartney", "Alvarez", "Starr","Soltermann"
        numero = random.randint(1,100)
        apellido = random.choice(apellidos)
        puntaje = random.randint(1,10)
        codigo = random.randint(0,12)
        vec[i] = Postulante(numero,apellido,puntaje,codigo)

def write(vec):
    print("El numero identificador del postulante es:", vec.numero)
    print("El apellido  del postulante es:", vec.apellido)
    print("El puntaje del postulante es:", vec.puntaje)
    print("El codigo de area del postulante es:", vec.codigo)

def mostrar_vector(vec):
    for i in range(len(vec)):
        print("")
        write(vec[i])
        print("")

def ordenar(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i +1,n):
            if vec[i].apellido < vec[j].apellido:
                vec[i] , vec[j] = vec[j], vec[i]


def busqueda(x,y,vec):
    vector = []
    for i in range(len(vec)):
        if vec[i].puntaje >= x and (vec[i].puntaje) <= y:
            vector.append(vec[i])
    if len(vector) == 0:
        print("No se encontro lo solicitado")
    else:
        return vector

def vector_conteo(vec):
    acumuladores = [0] * 13
    for i in range(len(vec)):
        acumuladores[vec[i].codigo] +=1
    return acumuladores

def promedio(vec):
    sumatorio = 0
    for i in range(len(vec)):
        sumatorio+= vec[i].puntaje
    promedio = sumatorio / len(vec)
    return promedio

def mayores(vec,promedio):
    contador = 0
    bandera = False
    for i in range(len(vec)):
        if vec[i].puntaje > promedio:
            print("")
            write(vec[i])
            print("")
            contador+=1
            bandera = True
    if bandera == False:
        print("No hubo ningun postulante que supere el promedio")
    else:
        return contador

def linear_search(c,vec):
    bandera = False
    for i in range(len(vec)):
        if vec[i].numero == c:
            print("")
            write(vec[i])
            print("")
            bandera = True
            break
    if bandera == False:
        print("No hubo un postulante con dicho numero de identificacion")

def menu():
    vec = []
    print("\033[1;30;44m" + "Autor: Nicolás Aguirre Bruno", "\tCurso 1K6" + '\033[0;m')
    print("Bienvenido al menú de opciones:")
    print('=' * 1000)
    print("\n Opcion 1: Cargar el arreglo pedido"
          "\n Opcion 2: Mostrar todos los datos de los postulantes cuyo puntaje "
          "obtenido este comprendido entre un valor x y otro valor y, siendo x e y valores que se cargan por teclado"
          ", en un listado ordenado de mayor a menor según los apellidos de los participantes."
          "\n Opcion 3: Determinar y mostrar la cantidad de postulantes por  "
          "cada tipo de localidad de origen posible."
          "\n Opcion 4: Mostrar los datos de todos los postulantes que hayan obtenido un puntaje mayor al "
          "promedio de todos los puntajes del vector."
          "\n Opcion 5: Determinar si existe un postulante cuyo número identificador sea igual a c, siendo c un valor "
          "que se carga por teclado."
          "\n Opcion 6: Salir")
    print('=' * 1000)
    opcion = int(input("\nIngrese la opcion que desea ejecutar: "))

    while opcion !=6:
        if opcion ==1:
            n = int(input("Ingrese la cantidad de vueltas que tendrá el registro: "))
            validador_n = validate(n)
            vec = [None] * validador_n
            cargar_vector(vec)
        elif len(vec) == 0:
            print("Error, debe pasar por la opcion 1 primero")
        elif opcion == 2:
            x = int(input("Ingrese el limite izquierdo para buscar: "))
            y = int(input("Ingrese el limite derecho para buscar: "))
            validar_x = validate(x)
            validar_y = validate(y)
            punto2 = busqueda(validar_x,validar_y,vec)
            if punto2 is not None:
                ordenar(punto2)
                mostrar_vector(punto2)
        elif opcion == 3:
            conteo  = vector_conteo(vec)
            for i in range(len(conteo)):
                if conteo[i] >0:
                    print("La cantidad de personas que hubo en el area",i,"fue de: ",conteo[i])
        elif opcion ==4:
            average = promedio(vec)
            cant_mayores = mayores(vec,average)
            if cant_mayores >0:
                print("Los postulantes que superaron al puntaje promedio fueron: ",cant_mayores)
        elif opcion ==5:
            c = int(input("Ingrese el numero identificador que desea buscar: "))
            validar_c = validate(c)
            linear_search(validar_c,vec)





        opcion = int(input("\nIngrese la opcion que desea ejecutar: "))

if __name__ == "__main__":
    menu()

