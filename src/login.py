import tkinter
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("default")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Registro de Libros")
root.iconbitmap('../assets/icono_libro.ico')
root.geometry("800x600")

# imagenes
icono_usuario = ImageTk.PhotoImage(Image.open("../assets/usuario.png").resize((20, 20)))
icono_crear_usuario = ImageTk.PhotoImage(Image.open("../assets/agregar-contacto.png").resize((20, 20)))

# botones
boton_usuario = customtkinter.CTkButton(master=root, image=icono_usuario, text="Iniciar Sesion", width=240, height=80,
                                        compound="left")
boton_usuario.pack(pady=20, padx=20)
boton_crear_usuario = customtkinter.CTkButton(master=root, image=icono_crear_usuario, text="Crear Usuario", width=240,
                                              height=80, compound="left", fg_color="#D35B58", hover_color="#C77C78")
boton_crear_usuario.pack(pady=20, padx=20)

root.mainloop()
