import cx_Oracle


class Login:
    def __init__(self, usuario, contra):
        self.conexion = None
        self.usuario = usuario
        self.contra = contra

    def conexion_base(self):
        try:
            self.conexion = cx_Oracle.connect(
                user='proyectotbd',
                password='proyecto',
                dsn='localhost:1521/xe',
                encoding='UTF-8'
            )
            print(self.conexion.version)
            return self.conexion
        except Exception as ex:
            print(ex)
            return None

    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
            print("Conexion cerrada")
        else:
            print("ERR: conexion a la base de datos inexistente")

    def verificar_usuario(self):
        if self.conexion:
            cursor = self.conexion.cursor()
            buscar_usuario = self.usuario
            buscar_contra = self.contra
            sql = "SELECT * FROM USUARIOS WHERE NOM_USUARIO = :usuario and CONTRASENIA = :contra"
            cursor.execute(sql, usuario=buscar_usuario, contra=buscar_contra)
            rows = cursor.fetchone()
            if rows is None:
                return False
            else:
                return True
