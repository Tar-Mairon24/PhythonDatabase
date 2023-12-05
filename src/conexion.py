import cx_Oracle

#try:
connection = cx_Oracle.connect(
        user = 'proyectotaller',
        password = 'proyecto',
        dsn = 'localhost:1521/XE',
        encoding = 'UTF-8'
    )
print(connection.version)

cursor = connection.cursor()
#Consulta tabla en bd 
isbn = input("Dame el isbn del libro a buscar")
SQL = '''
SELECT l.isbn, l.titulo, e.nombre, l.anio, a.nombre
FROM libros l, editoriales e, autores a
WHERE a.id_autor = l.id_autor and 
e.id_editorial = l.id_editorial and
l.isbn = :isbn
'''
valores_select = {'isbn':isbn}
cursor.execute(SQL,valores_select)
records = cursor.fetchall()
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
isbn = input("Insertar isbn ")
titulo = input("Insertar titulo ")
nombre_editorial = input("Insertar nombre editorial ")
anio_libro = input("Insertar año ")
nombre_autor = input("Insertar nombre autor ")

# Obtener el próximo valor de la secuencia para el ID_autor
cursor.execute("SELECT MAX(id_autor) + 1 FROM autores")
id_autor = cursor.fetchone()[0]
# Si no hay registros en autores, establecer el ID en 1
if id_autor is None:
    id_autor = 1

# Obtener el valor siguiente de la secuencia para el ID_editorial
cursor.execute("SELECT MAX(id_editorial) + 1 FROM editoriales")
id_editorial = cursor.fetchone()[0]
# Si no hay registros en editoriales, establecer el ID en 1
if id_editorial is None:
    id_editorial = 1

# Verificar si el ISBN ya existe en la tabla libros
cursor.execute("SELECT COUNT(*) FROM libros WHERE ISBN = :isbn", {'isbn': isbn})
existe_isbn = cursor.fetchone()[0]
if existe_isbn > 0:
    print(f"El libro con ISBN {isbn} ya existe. No se puede insertar.")
else:
    #Insertar en autores
    insert_autores = '''
    insert into autores(ID_AUTOR,NOMBRE) VALUES (:id_autor,:nombre_autor)
    '''
    valores_autores = {'id_autor':id_autor,'nombre_autor':nombre_autor}
    cursor.execute(insert_autores,valores_autores)

    #Insertar en editoriales
    insert_editoriales = '''
    insert into editoriales(ID_EDITORIAL, NOMBRE) VALUES (:id_editorial,:nombre_editorial)
    '''
    valores_editoriales = {'id_editorial':id_editorial,'nombre_editorial':nombre_editorial}
    cursor.execute(insert_editoriales,valores_editoriales)

    #Insertar libro
    insert_libros = '''
    insert into libros (ISBN,ID_EDITORIAL,ID_AUTOR,ID_USER,TITULO,ANIO) VALUES(:isbn,:id_editorial,:id_autor,1,:titulo,:anio)
    '''
    valores_libros = {'isbn':isbn,'id_editorial':id_editorial,'id_autor':id_autor,'titulo':titulo,'anio':anio_libro}
    cursor.execute(insert_libros,valores_libros)
    connection.commit()


#Actualizar registros en la BD

#update_autor = '''
#update autores SET nombre = 'Guillermo' where ID_AUTOR = 2
#'''
nombre_libro = input("titulo a actualizar ")
buscar_isbn = input("buscar isbn ")
update_libro = '''
update libros SET titulo =:nombre_libro where ISBN =:buscar_isbn
'''
valores_update = {'nombre_libro':nombre_libro,'buscar_isbn':buscar_isbn}
try:
    cursor.execute(update_libro,valores_update)
    connection.commit()
    print("Actualizacion")
except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("Error de base de datos:", error)


#Eliminar registros en la BD
eliminar_libro = input("ISBN a eliminar ")
delete_libro = '''
DELETE from libros where isbn =:eliminar_libro ;
'''
valores_delete = {'delete_libro':delete_libro}
try:
    cursor.execute(delete_libro,valores_delete)
    connection.commit()
except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("Error de base de datos:", error)







#cursor.execute(update_libro)
#connection.commit()

#cursor.execute("SELECT * FROM LIBROS")
    #rows = cursor.fetchall()
    #for row in rows:
     #   print(row)
#except Exception as ex:
#   print(ex)    

#finally:
#    connection.close()
#    print('Conexion finalizada')