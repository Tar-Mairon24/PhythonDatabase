import cx_Oracle

try:
    connection = cx_Oracle.connect(
        user='proyectotbd',
        password='proyecto',
        dsn='localhost:1521/xe',
        encoding='UTF-8'
    )
    print(connection.version)
except Exception as ex:
    print(ex)
