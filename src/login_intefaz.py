import tkinter as tk
from tkinter import ttk, messagebox
import sys 
sys.path.insert(0,'../src')
from gui import ComponentesVentana
from login_funcion import Login



class VentanaLogin:
    def __init__(self, master):
        self.master = master
        self.master.geometry('300x130')
        self.master.title('Login')
        self.master.resizable(False, False)

        self.login_boton = None
        self.password_entrada = None
        self.password_etiqueta = None
        self.usuario_entrada = None
        self.usuario_etiqueta = None

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=3)

        self.crear_interfaz()

    def crear_interfaz(self):
        # Usuario
        self.usuario_etiqueta = ttk.Label(self.master, text='Usuario:')
        self.usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = ttk.Entry(self.master)
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # Contraseña
        self.password_etiqueta = ttk.Label(self.master, text='Password:')
        self.password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.password_entrada = ttk.Entry(self.master, show='*')
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Botón Login
        self.login_boton = ttk.Button(self.master, text='Login', command=self.login)
        self.login_boton.grid(row=3, column=0, columnspan=2)

    def login(self):
        usuario = self.usuario_entrada.get()
        contra = self.password_entrada.get()
        if usuario == "" or contra == "":
            messagebox.showinfo("Error", "No se insertaron datos")
        else:
            login_conexion = Login(usuario, contra)
            login_conexion.conexion_base()
            if login_conexion.verificar_usuario():
                gui = ComponentesVentana()
                gui.mainloop()
            else:
                messagebox.showinfo("Error", "Usuario o contraseña invalidos")
            login_conexion.cerrar_conexion()


if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaLogin(root)
    root.mainloop()


