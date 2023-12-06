import cx_Oracle

<<<<<<< HEAD

=======
>>>>>>> origin/main
class Conexion:
    def __init__(self):
        self.connection = None
        self.cursor = None

<<<<<<< HEAD
        self.isbn = None
        self.titulo = None
        self.nombre_ed = None
        self.anio_l = None
        self.nombre_aut = None

    def conexion_base(self):
        try:
            self.connection = cx_Oracle.connect(
                user='proyectotaller',
                password='proyecto',
                dsn='localhost:1521/XE',
                encoding='UTF-8'
=======
    def conexion_base(self):
        try:
            self.connection = cx_Oracle.connect(
                user = 'proyectotbd',
                password = 'proyecto',
                dsn = 'localhost:1521/XE',
                encoding = 'UTF-8'
>>>>>>> origin/main
            )
            print(self.connection.version)
            self.cursor = self.connection.cursor()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Conexion con base de datos erronea:", error)

    def cerrar_conexion(self):
        if self.connection:
            self.connection.close()
            print("Conexion cerrada")
        else:
            print("ERROR: conexion a la base de datos inexistente")

<<<<<<< HEAD
    # cursor = connection.cursor()

    # Consulta tabla en bd
    # isbn = input("Dame el isbn del libro a buscar")

    def buscar_libro_por_isbn(self, isbn):
        sql = '''
=======
   # cursor = connection.cursor()

    #Consulta tabla en bd 
    #isbn = input("Dame el isbn del libro a buscar")

    def buscar_libro_por_isbn(self,isbn):
        SQL = '''
>>>>>>> origin/main
        SELECT l.isbn, l.titulo, e.nombre, l.anio, a.nombre
        FROM libros l, editoriales e, autores a
        WHERE a.id_autor = l.id_autor and 
        e.id_editorial = l.id_editorial and
        l.isbn = :isbn
        '''
<<<<<<< HEAD
        valores_select = {'isbn': isbn}
        self.cursor.execute(sql, valores_select)
        records = self.cursor.fetchall()
        for rows in records:
            # print(x)
            self.isbn = rows[0]
            self.titulo = rows[1]
            self.nombre_ed = rows[2]
            self.anio_l = rows[3]
            self.nombre_aut = rows[4]
        print(str(isbn) + ' ' + self.titulo + ' ' + self.nombre_ed + ' ' + str(self.anio_l) + ' ' + self.nombre_aut)

    # Insertar registros en BD

    # Insertar libro
=======
        valores_select = {'isbn':isbn}
        self.cursor.execute(SQL,valores_select)
        records = self.cursor.fetchall()
        for rows in records:
            #print(x)
            isbn = rows[0]
            titulo = rows[1]
            nombre_ed = rows[2]
            anio_l = rows[3]
            nombre_aut = rows[4]
        print(str(isbn) +' '+ titulo +' '+ nombre_ed+' '+str(anio_l)+' '+nombre_aut)

    #Insertar registros en BD

    #Insertar libro
>>>>>>> origin/main

    """ isbn = input("Insertar isbn ")
    titulo = input("Insertar titulo ")
    nombre_editorial = input("Insertar nombre editorial ")
    anio_libro = input("Insertar año ")
<<<<<<< HEAD
    nombre_autor = input("Insertar nombre autor ") """

    def insertar_libro(self, isbn, titulo, nombre_editorial, anio_libro, nombre_autor):
=======
    nombre_autor = input("Insertar nombre autor ")
    fecha_ini = input("Insertar fecha inicial ") 
    fecha_fin = input("Insertar fecha final ")
       """

    def insertar_libro(self,isbn,titulo,nombre_editorial,anio_libro,nombre_autor,fecha_ini,fecha_fin):
>>>>>>> origin/main
        # Obtener el próximo valor de la secuencia para el ID_autor
        self.cursor.execute("SELECT MAX(id_autor) + 1 FROM autores")
        id_autor = self.cursor.fetchone()[0]
        # Si no hay registros en autores, establecer el ID en 1
        if id_autor is None:
            id_autor = 1

        # Obtener el valor siguiente de la secuencia para el ID_editorial
        self.cursor.execute("SELECT MAX(id_editorial) + 1 FROM editoriales")
        id_editorial = self.cursor.fetchone()[0]
        # Si no hay registros en editoriales, establecer el ID en 1
        if id_editorial is None:
            id_editorial = 1

        # Verificar si el ISBN ya existe en la tabla libros
        self.cursor.execute("SELECT COUNT(*) FROM libros WHERE ISBN = :isbn", {'isbn': isbn})
        existe_isbn = self.cursor.fetchone()[0]
        if existe_isbn > 0:
            print(f"El libro con ISBN {isbn} ya existe. No se puede insertar.")
        else:
<<<<<<< HEAD
            # Insertar en autores
            insert_autores = '''
            insert into autores(ID_AUTOR,NOMBRE) VALUES (:id_autor,:nombre_autor)
            '''
            valores_autores = {'id_autor': id_autor, 'nombre_autor': nombre_autor}
            self.cursor.execute(insert_autores, valores_autores)

            # Insertar en editoriales
            insert_editoriales = '''
            insert into editoriales(ID_EDITORIAL, NOMBRE) VALUES (:id_editorial,:nombre_editorial)
            '''
            valores_editoriales = {'id_editorial': id_editorial, 'nombre_editorial': nombre_editorial}
            self.cursor.execute(insert_editoriales, valores_editoriales)

            # Insertar libro
            insert_libros = '''
            insert into libros (ISBN,ID_EDITORIAL,ID_AUTOR,ID_USER,TITULO,ANIO) VALUES(:isbn,:id_editorial,:id_autor,1,:
            titulo,:anio)
            '''
            valores_libros = {'isbn': isbn, 'id_editorial': id_editorial, 'id_autor': id_autor, 'titulo': titulo,
                              'anio': anio_libro}
            self.cursor.execute(insert_libros, valores_libros)
            self.connection.commit()

    """ nombre_libro = input("titulo a actualizar ")
    buscar_isbn = input("buscar isbn ") """

    def actualizar_titulo(self, nombre_libro, buscar_isbn):
        # Actualizar registros en la BD
        update_libro = '''
        update libros SET titulo =:nombre_libro where ISBN =:buscar_isbn
        '''
        valores_update = {'nombre_libro': nombre_libro, 'buscar_isbn': buscar_isbn}
        try:
            self.cursor.execute(update_libro, valores_update)
=======
            #Insertar en autores
            insert_autores = '''
            insert into autores(ID_AUTOR,NOMBRE) VALUES (:id_autor,:nombre_autor)
            '''
            valores_autores = {'id_autor':id_autor,'nombre_autor':nombre_autor}
            self.cursor.execute(insert_autores,valores_autores)

            #Insertar en editoriales
            insert_editoriales = '''
            insert into editoriales(ID_EDITORIAL, NOMBRE) VALUES (:id_editorial,:nombre_editorial)
            '''
            valores_editoriales = {'id_editorial':id_editorial,'nombre_editorial':nombre_editorial}
            self.cursor.execute(insert_editoriales,valores_editoriales)

            #Insertar libro
            insert_libros = '''
            insert into libros (ISBN,ID_EDITORIAL,ID_AUTOR,ID_USER,TITULO,ANIO,FECHA_INI,FECHA_FIN) VALUES(:isbn,:id_editorial,:id_autor,1,:titulo,:anio,:fecha_ini,:fecha_fin)
            '''
            valores_libros = {'isbn':isbn,'id_editorial':id_editorial,'id_autor':id_autor,'titulo':titulo,'anio':anio_libro, 'fecha_ini':fecha_ini,'fecha_fin': fecha_fin}
            self.cursor.execute(insert_libros,valores_libros)
            self.connection.commit()


    """ nombre_libro = input("titulo a actualizar ")
    buscar_isbn = input("buscar isbn ") """
    
    def actualizar_titulo(self,nombre_libro,buscar_isbn):
        #Actualizar registros en la BD
        update_libro = '''
        update libros SET titulo =:nombre_libro where ISBN =:buscar_isbn
        '''
        valores_update = {'nombre_libro':nombre_libro,'buscar_isbn':buscar_isbn}
        try:
            self.cursor.execute(update_libro,valores_update)
>>>>>>> origin/main
            self.connection.commit()
            print("Actualizacion")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error de base de datos:", error)

<<<<<<< HEAD
    # Eliminar registros en la BD
    def eliminar_libro(self, eliminar_libro):
        delete_libro = '''
        DELETE from libros where isbn =:eliminar_libro 
        '''
        valores_delete = {'eliminar_libro': eliminar_libro}
        try:
            self.cursor.execute(delete_libro, valores_delete)
=======
    #Eliminar registros en la BD
    def eliminar_libro(self,eliminar_libro):
        delete_libro = '''
        DELETE from libros where isbn =:eliminar_libro 
        '''
        valores_delete = {'eliminar_libro':eliminar_libro}
        try:
            self.cursor.execute(delete_libro,valores_delete)
>>>>>>> origin/main
            self.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error de base de datos:", error)
