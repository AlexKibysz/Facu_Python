import os.path
import pickle


def separar():
    print(100 * "-")


def bidimensional():
    print("Los arreglos Bi-dimensionales, en pocas palabras, son matrices. Estas mismas "
          "estan compuestas por filas y columnas.")
    print("Para crear un arreglo Bi-dimensional debemos utilizar la siguiente funcion: "
          "matriz = [[0] * m for filas in range(n) ]")
    n = 3
    m = 4
    matriz = [[0] * m for filas in range(n)]
    print("Matriz de prueba: ", matriz)
    print("Dado este caso, creamos una matriz pero cuando la printeamos se muestra toda en una"
          " sola linea, mas adelante veremos como se debe hacer para mostrarse como una matriz.")
    print("Pero por el momento, podemos observar que 'm' es la cantidad de columnas y 'n' la "
          "cantidad de filas, el cual a estos datos si queremos se los podemos pedir al usuario, "
          "\nutilizando el int(input()).")


def pasos_mostrar():
    print("Para mostrar una matriz de manera simple y que se muestr tal como tal, debemos "
          "utilizar un for, en el cual iteraremos en un rango de (len(matriz)).")
    print("Para esto, debemos pasarle la matriz al for y el len de la matriz para saber con "
          "exactitud cuantas veces debe iterar. \nEn len(matriz) nos dira cuantas filas tiene "
          "la matriz y dependiendo de cuantas filas tenga, las mostrara.\n")


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def recorrer_filas(matriz):
    print("Para recorrer por filas, debemos efectuar la siguiente iteracion: ")
    print("Datos de la fila 1:")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print("Fila: ", i, "Columna:", j)


def recorrer_columna(matriz):
    print("Para recorrer por columnas, debemos efectuar la siguiente iteracion: ")
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            print("Columna: ", j, "Fila: ", i)


def cargar_matriz():
    print("Si deseamos cargar una matriz, debemos primero crear la misma: ")
    n = int(input("Cntidad de filas: "))
    m = int(input("Cantidad de columnas: "))
    print("\nMatriz creada: \n")
    matriz = [[0] * m for filas in range(n)]
    mostrar_matriz(matriz)
    print("Como vemos, creamos una matriz de", n, "filas y", m, "columnas:")
    print("Ahora, si deseamos cargar la matriz, podemos usar el recorrido por filas o columnas.")
    print("En este caso, usaremos el recorrido por filas: \n")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = int(input("[" + str(i) + "]" + "[" + str(j) + "]" + "Ingrese un valor: "))
    print("\nAhora veremos la matriz cargada: \n")
    mostrar_matriz(matriz)


def tema_archivos():
    print("Para empezar el tema, los archivos se dividen en archivos Binario y de Texto. ")
    print("Los archivos de texto son archivos en el cual todos los bytes del mismo son \n"
          "interpretados como caracteres, por ejemplo en caracteres como ASCII.")
    print("Normalmente en estos tipos de archivos cuando los abrimos sin ningun programa \n"
          "o con algun editor de texto, se pueden leer o ver los datos.")
    print("\n\nLuego, siguiendo con la linea de aprendizaje, estan los archivos Binarios.\n"
          "Estos archivos como bien dice el nombre, pueden llegar a representar cualquier \n"
          "tipo de dato, desde numeros binarios, hasta valores booleanos.")
    print("En los archivos binarios no se sabe que tipo de archivo hay dentro, solo el \n"
          "programador distinguira que tipo de datos tiene dando la forma en la cual se \n"
          "tenga que interpretar el archivo. Tengamos en cuenta que si intentamos abrir un \n"
          "archivo binario sin algun interprete o programa no podremos ver los datos del mismo, \n"
          "ya que los datos estarian en lenguaje de maquina. ")
    print("\nA todo esto, cabe aclarar que los archivos de texto tambien estan escritos en \n"
          "lenguaje de maquina pero en la practca se utiliza el termino texto o binario para \n"
          "distinguir valores donde se encuentren caracteres o informacion.\n")
    print("Para abrir un archivo, debemos efectuar lo siguiente:  ")
    print('m = open("nombreDelArchivo.dat", "w")\n')
    m = open("nombreDelArchivo.dat", "w")
    print("Y despues de usar el archivo debemos cerrarlo, MUY IMPORTANTE.")
    print("Lo cerramos: 'm.close()'")
    m.close()


def cargar_archivos():
    print("Algo que hay que tener muy en cuenta es que cada vez que vayamos a usar \n"
          "archivos, tenemos que importar os.path y pickle.")
    print("\nEl os.path es el encargado de traer funciones y comandos del S.O"
          "\ny pickle, PICKLE RICKKKK - Famosa frase de Rick and Morty, es el encargado de trare funciones y comandos para \n"
          "cargar archivos o guardarlos.")
    print("\nGrabaremos numeros en un archivo:")
    m = open("prueba.num", "wb")
    x = 10
    y = 20
    z = 30
    pickle.dump(x, m)
    pickle.dump(y, m)
    m.close()

    print("Una vez cargados los datos com 'pickle.dump(contenido, donde lo cargamos)', tenemos que\n"
          "cerrar el archivo con m.close (luego de abrirlo y accionar en el).")


def mostrar_archivo():
    print("Para mostrar los datos de un archivo, debemos primero cargarlo, mostrar y luego cerrarlo.")
    m = open("prueba.num", "rb")
    a = pickle.load(m)
    b = pickle.load(m)
    print("Datos recuperados del archivo:", a, "-", b)
    m.close()


opc = -1
while opc != 0:
    n = 3
    m = 4
    matriz = [[0] * m for filas in range(n)]
    separar()
    print("\t\t\t\tTodo el temario de Matrices, se encuentra en la ficha 16")
    separar()
    print("\t\t\t\tTodo el temario de Archivos, se encuentra en la ficha 22")
    separar()
    print("1 - Arreglos Bi-Dimensionales (Matrices)")
    print("2 - Mostrar matriz")
    print("3 - Recorrido por filas (Orden creciente)")
    print("4 - Recorrido por columnas (Orden creciente)")
    print("5 - Cargar una matriz")
    print("6 - Archivos")
    print("7 - Modos de apertura de un archivo en Python")
    print("8 - Cargar archivos")
    print("9 - Mostrar datos del archivo")
    print("0 - Salir")
    opc = int(input("Ingrese a donde desee ir: "))
    separar()

    if opc == 1:
        bidimensional()
        separar()
    elif opc == 2:
        pasos_mostrar()
        mostrar_matriz(matriz)
        separar()
    elif opc == 3:
        recorrer_filas(matriz)
        separar()
    elif opc == 4:
        recorrer_columna(matriz)
        separar()
    elif opc == 5:
        cargar_matriz()
        separar()
    elif opc == 6:
        tema_archivos()
        separar()
    elif opc == 7:
        print("Mirar Ficha 22 - Pagina 443")
    elif opc == 8:
        cargar_archivos()
        separar()
    elif opc == 9:
        mostrar_archivo()
        separar()
    elif opc == 0:
        print("\n+Fin del programa")
    else:
        print("Error")
        separar()
