from models import  exibe_usuario

SQL_DELETA_USUARIO = 'delete from Usuario where cod_usuario = ?'
SQL_DELETA_ENDERECO = 'delete from Endereco_Pessoa where id_pessoa= ?'
SQL_DELETA_CONTATO='delete from Contato_Pessoa where id_pessoa = ?'
SQL_DELETA_PESSOA='delete from Pessoa where id_pessoa = ?'



class deletar:
    def __init__(self, db):
        self.__db = db
    

    def deletar_usuario(self, cod_usuario):
        self.__db.connection.cursor().execute(SQL_DELETA_USUARIO, (cod_usuario, ))
        self.__db.connection.commit()
    
    def deletar_fornecedor(self, id_pessoa,):
        self.__db.connection.cursor().execute(SQL_DELETA_ENDERECO, (id_pessoa, ))
        self.__db.connection.cursor().execute(SQL_DELETA_CONTATO, (id_pessoa, ))
        self.__db.connection.cursor().execute(SQL_DELETA_PESSOA, (id_pessoa, ))
        self.__db.connection.commit()