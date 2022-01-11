from tkinter import *

# crear ventana
ventana = Tk()
# establecemos el tamanio de la ventana
ventana.geometry('300x300')

etiqueta = Label(ventana, text='Hola mundo', bg='purple')
# side
# bottom #left #right


etiqueta.pack(fill=constants.X, expand=True)


# etiqueta.pack() es la forma mas facil de empaquetar los widgets al programa


# widget boton
def saludo(Nombre='Elpepe'):
    print('Hola ' + Nombre)


boton = Button(ventana, text='Presiona', padx=30, pady=30, command=lambda: textodelacaja())
boton.pack()

cajatexto = Entry(ventana, font='helvetica 30')
cajatexto.pack()


def textodelacaja():
    t = cajatexto.get()
    print(t)


# mainloop mantiene todos lo que esta sucediendo en la ventana
ventana.mainloop()
