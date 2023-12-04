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
SQL = '''
SELECT * FROM libros
'''
cursor.execute(SQL)
records = cursor.fetchall()
for x in records:
    #print(x)
    isbn = x[0]
    id_ed = x[1]
    id_aut = x[2]
    titulo = x[4]
    print(str(isbn) +' '+ titulo)

#Insertar registros en BD

#autores
nombre_autor = input()
paterno_autor = input()
materno_autor = input()

# Obtener el próximo valor de la secuencia para el ID
cursor.execute("SELECT MAX(id_autor) + 1 FROM autores")
id_autor = cursor.fetchone()[0]
# Si no hay registros en la tabla, establecer el ID en 1
if id_autor is None:
    id_autor = 1

insert_autores = '''
insert into autores(ID_AUTOR,NOMBRE,PATERNO,MATERNO) VALUES (:id_autor,:nombre_autor,:paterno_autor,:materno_autor)
'''
valores_autores = {'id_autor':id_autor,'nombre_autor':nombre_autor,'paterno_autor':paterno_autor,'materno_autor':materno_autor}
cursor.execute(insert_autores,valores_autores)
connection.commit()

#Insertar en editoriales
#Ingresar
nombre_editorial = input()
# Obtener el valor siguiente de la secuencia para el ID
cursor.execute("SELECT MAX(id_editorial) + 1 FROM editoriales")
id_editorial = cursor.fetchone()[0]
# Si no hay registros en la tabla, establecer el ID en 1
if id_editorial is None:
    id_editorial = 1

insert_editoriales = '''
insert into editoriales(ID_EDITORIAL, NOMBRE) VALUES (:id_editorial,:nombre_editorial)
'''
valores_editoriales = {'id_editorial':id_editorial,'nombre_editorial':nombre_editorial}
cursor.execute(insert_editoriales,valores_editoriales)
connection.commit()

#Insertar libro
isbn = input()
titulo = input()

insert_libros = '''
insert into libros (ISBN,ID_EDITORIAL,ID_AUTOR,ID_USER,TITULO) VALUES(:isbn,:id_editorial,:id_autor,1,:titulo)
'''
valores_libros = {'isbn':isbn,'id_editorial':id_editorial,'id_autor':id_autor,'titulo':titulo}
cursor.execute(insert_libros,valores_libros)
connection.commit()


#Actualizar registros en la BD

#update_autor = '''
#update autores SET nombre = 'Guillermo' where ID_AUTOR = 2
#'''
#cursor.execute(update_autor)
#connection.commit()

#update_libro = '''
#update libros SET titulo = 'LIBRO' where ISBN = 1;
#'''

#Eliminar registros en la BD
#delete_autor = '''
#DELETE from autores where id_autor = 2;
#'''
#cursor.execute(delete_autor)
#connection.commit()








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