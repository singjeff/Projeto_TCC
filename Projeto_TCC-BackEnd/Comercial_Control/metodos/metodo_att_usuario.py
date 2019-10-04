from models import  Usuario

SQL_ATUALIZA_USUARIO = 'UPDATE Usuario SET  senha_aplicacao=?  where cod_usuario = ?'


class atualiza_usuario:
    def __init__(self, db):
        self.__db = db

    def atualiza(self, usuario):
        cursor = self.__db
        cursor.execute(SQL_ATUALIZA_USUARIO, (usuario.senha_aplicacao, usuario.cod_usuario))
        self.__db.connection.commit()
        return usuario