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
#insert_autores = '''
#insert into autores values(2,'MEMO','ORTIZ','AGUILAR')
#'''
nombre_autor = input()
paterno_autor = input()
materno_autor = input()

# Obtener el próximo valor de la secuencia para el ID
cursor.execute("SELECT autoincremento.NEXTVAL FROM dual")
id_autor = cursor.fetchone()[0]

insert_autores = '''
insert into autores(ID_AUTOR,NOMBRE,PATERNO,MATERNO) VALUES (:id_autor,:nombre_autor,:paterno_autor,:materno_autor)
'''
valores = {'id_autor':id_autor,'nombre_autor':nombre_autor,'paterno_autor':paterno_autor,'materno_autor':materno_autor}
cursor.execute(insert_autores,valores)
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