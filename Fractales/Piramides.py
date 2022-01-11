from tkinter import *

__author__ = 'Cátedra de AED'


def pyramid(canvas, x, y, r):
    if r > 0:
        # dibujar recursivamente el soporte inferior izquierdo...
        pyramid(canvas, x - r, y + r, r // 2)
        # dibujar recursivamente el soporte inferior derecho...
        pyramid(canvas, x + r, y + r, r // 2)
        # dibujar recursivamente el soporte superior izquierdo...
        pyramid(canvas, x - r, y - r, r // 2)
        # dibujar recursivamente el soporte superior derecho...
        pyramid(canvas, x + r, y - r, r // 2)
        # dibujar en (post-orden) la tapa o cima de la pirámide...
    square(canvas, x, y, r)


def square(canvas, x, y, r):
    left = x - r
    top = y - r
    right = x + r
    down = y + r
    canvas.create_rectangle((left, top, right, down), outline='yellow', fill='blue')


def render():
    # configuracion inicial de la ventana principal...
    root = Tk()
    root.title("Piramide Fractal")
    # calculo de resolucion en pixels de la pantalla...
    maxw = root.winfo_screenwidth()
    maxh = root.winfo_screenheight()
    # ajustar dimensiones y coordenadas de arranque de la ventana...
    root.geometry("%dx%d+%d+%d" % (maxw, maxh, 0, 0))
    # un lienzo de dibujo dentro de la ventana...
    canvas = Canvas(root, width=maxw, height=maxh)
    canvas.grid(column=0, row=0)
    # sea valor inicial de r igual a un duodécimo del ancho de la pantalla...
    r = 100
    # coordenadas del centro de la pantalla...
    cx = maxw // 2
    cy = maxh // 2
    # dibujar piramide centrada en (cx, cy) y el cuadrado mayor con lado = 2r.
    pyramid(canvas, cx, cy, r)
    # lanzar el ciclo principal de control de eventos de la ventana...
    root.mainloop()


if __name__ == '__main__':
    render()
