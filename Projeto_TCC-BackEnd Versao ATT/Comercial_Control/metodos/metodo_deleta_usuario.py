from models import  exibe_usuario

SQL_DELETA_USUARIO = 'delete from Usuario where cod_usuario = ?'



class deleta_usuario:
    def __init__(self, db):
        self.__db = db
    

    def deletar(self, cod_usuario):
        self.__db.connection.cursor().execute(SQL_DELETA_USUARIO, (cod_usuario, ))
        self.__db.connection.commit()