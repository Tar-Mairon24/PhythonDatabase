from conexion import Conexion

def main():
    conn = Conexion()
    try:
        conn.conexion_base()
        #Ejecutar buscar
        isbn_buscar = input("Dame el isbn del libro a buscar")
        conn.buscar_libro_por_isbn(isbn_buscar)

        # Ejecutar insertar
        isbn = input("Insertar isbn ")
        titulo = input("Insertar titulo ")
        nombre_editorial = input("Insertar nombre editorial ")
        anio_libro = input("Insertar año ")
        nombre_autor = input("Insertar nombre autor ")

        conn.insertar_libro(isbn,titulo,nombre_editorial,anio_libro,nombre_autor)

        #Ejecutar actualizar
        nombre_libro = input("titulo a actualizar ")
        buscar_isbn = input("buscar isbn ")    
        conn.actualizar_titulo(nombre_libro,buscar_isbn)    

        #Ejecutar eliminar
        eliminar_libro = input("ISBN a eliminar ")
        conn.eliminar_libro(eliminar_libro)
        
    except  Exception as e:
        print(f"Error de base de datos: {e}")
    finally:
        conn.cerrar_conexion()

if __name__ == "__main__":
    main()
