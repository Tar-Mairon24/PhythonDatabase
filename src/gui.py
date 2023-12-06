import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep
from datetime import datetime, timedelta


class ComponentesVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('450x400+100+100')
        self.title('Libreria')

        self.titulo = None
        self.isbn = None
        self.editorial = None
        self.anio = None
        self.autor = None

        self.conexion = Conexion()

        self._crear_tabs()

    def tabulador1(self, tabulador):
        # etiqueta y un componente de entrada

        etiqueta1 = ttk.Label(tabulador, text='ISBN:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)
        self.isbn = entrada1.get()

        etiqueta2 = ttk.Label(tabulador, text='Titulo:')
        etiqueta2.grid(row=1, column=0, sticky=tk.E)
        entrada2 = ttk.Entry(tabulador, width=30)
        entrada2.grid(row=1, column=1, padx=5, pady=5)
        self.titulo = entrada2.get()

        etiqueta3 = ttk.Label(tabulador, text='Editorial:')
        etiqueta3.grid(row=2, column=0, sticky=tk.E)
        entrada3 = ttk.Entry(tabulador, width=30)
        entrada3.grid(row=2, column=1, padx=5, pady=5)
        self.editorial = entrada3.get()

        etiqueta4 = ttk.Label(tabulador, text='Año:')
        etiqueta4.grid(row=3, column=0, sticky=tk.E)
        entrada4 = ttk.Entry(tabulador, width=30)
        entrada4.grid(row=3, column=1, padx=5, pady=5)
        self.anio = entrada4.get()

        etiqueta5 = ttk.Label(tabulador, text='Autor:')
        etiqueta5.grid(row=4, column=0, sticky=tk.E)
        entrada5 = ttk.Entry(tabulador, width=30)
        entrada5.grid(row=4, column=1, padx=5, pady=5)
        self.autor = entrada5.get()

        # botón para registrar
        def enviar():
            self.conexion.insertar_libro(self.isbn, self.titulo, self.editorial, self.anio,
                                         self.autor)
            messagebox.showinfo("")

        boton1 = ttk.Button(tabulador, text='OK', command=enviar)
        boton1.grid(row=5, column=0, columnspan=2)

    def tabulador2(self, tabulador):
        etiqueta1 = ttk.Label(tabulador, text='ISBN:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        # lista de fechas datetime
        etiqueta2 = ttk.Label(tabulador, text='Fecha de inicio:')
        etiqueta2.grid(row=1, column=0, sticky=tk.E)
        fecha_actual = datetime.now()
        fecha_Ini = [fecha_actual - timedelta(days=x) for x in range(10)]
        fecha_Ini_str = [fecha.strftime("%Y-%m-%d") for fecha in fecha_Ini]

        etiqueta3 = ttk.Label(tabulador, text='Fecha de fin:')
        etiqueta3.grid(row=2, column=0, sticky=tk.E)
        fecha_actual = datetime.now()
        fecha_Fin = [fecha_actual - timedelta(days=x) for x in range(10)]
        fecha_Fin_str = [fecha.strftime("%Y-%m-%d") for fecha in fecha_Fin]

        # Combobox con las fechas
        combobox = ttk.Combobox(tabulador, width=30, values=fecha_Ini_str)
        combobox.grid(row=1, column=1, padx=5, pady=5)

        combobox = ttk.Combobox(tabulador, width=30, values=fecha_Fin_str)
        combobox.grid(row=2, column=1, padx=5, pady=5)

        # Seleccionamos la primera fecha pasada como predeterminada
        combobox.current(0)

        # botón para mostrar la fecha seleccionada
        def mostrar_valor():
            messagebox.showinfo('Memo Joto', 'Registro completado')

        boton_mostrar = ttk.Button(tabulador, text='OK', command=mostrar_valor)
        boton_mostrar.grid(row=3, column=1)

    def tabulador3(self, tabulador):
        etiqueta1 = ttk.Label(tabulador, text='ISBN:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        # botón para mostrar la fecha seleccionada
        def mostrar_valor():
            messagebox.showinfo('Memo Joto', 'Registro completado')

        boton_mostrar = ttk.Button(tabulador, text='OK', command=mostrar_valor)
        boton_mostrar.grid(row=3, column=1)

    def tabulador4(self, tabulador):
        etiqueta1 = ttk.Label(tabulador, text='ISBN:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        # botón para mostrar la fecha seleccionada
        def mostrar_valor():
            messagebox.showinfo('Memo Joto', 'Registro completado')

        boton_mostrar = ttk.Button(tabulador, text='OK', command=mostrar_valor)
        boton_mostrar.grid(row=3, column=1)

    def _crear_tabs(self):
        # Creamos un tab control, para ello usamos la clase Notebook
        control_tabulador = ttk.Notebook(self)
        # Agregamos un marco (frame) para agregar dentrol del tab y organizar elementos
        tabulador1 = ttk.Frame(control_tabulador)
        # Agregamos el tabulador al control de tabuladores
        control_tabulador.add(tabulador1, text='Ingresar Libro')
        # Mostramos el tabulador
        control_tabulador.pack(fill='both')
        # Creamos los componentes del tabulador1
        self.tabulador1(tabulador1)

        tabulador2 = ttk.LabelFrame(control_tabulador, text='Busqueda de libro')
        control_tabulador.add(tabulador2, text='Busqueda de libro')
        self.tabulador2(tabulador2)

        # tabulador 3
        # Update, con el titulo actualizar

        tabulador3 = ttk.LabelFrame(control_tabulador, text='Actualizar')
        control_tabulador.add(tabulador3, text='ISBN a actualizar')
        self.tabulador3(tabulador3)

        # tabulador 5
        # borrar, con el ISBN
        tabulador4 = ttk.LabelFrame(control_tabulador, text='Borrar')
        control_tabulador.add(tabulador4, text='Borrar')
        self.tabulador4(tabulador4)


if __name__ == '__main__':
    # Creamos un objeto de nuestra clase
    componentes_ventana = ComponentesVentana()
    componentes_ventana.mainloop()
