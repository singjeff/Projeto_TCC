from models import  exibe_usuario

SQL_DELETA_USUARIO = 'delete from Usuario where cod_usuario = ?'
SQL_DELETA_FORNECEDOR = 'delete from Fornecedor where id_pessoa = ?'
SQL_DELETA_ENDERECO = 'delete from Endereco_Pessoa where id_pessoa= ?'
SQL_DELETA_CONTATO='delete from Contato_Pessoa where id_pessoa = ?'
SQL_DELETA_PESSOA='delete from Pessoa where id_pessoa = ?'

SQL_DELETA_COMPRA='delete from Compra where codigo_produto= ?'
SQL_DELETA_ITEM='delete from Item where codigo_produto= ?'
SQL_DELETA_PRODUTO='delete from Produto where codigo_produto= ?'



class deletar:
    def __init__(self, db):
        self.__db = db
    

    def deletar_usuario(self, cod_usuario):
        self.__db.connection.cursor().execute(SQL_DELETA_USUARIO, (cod_usuario, ))
        self.__db.connection.commit()
    
    def deletar_fornecedor(self, id_pessoa,):
        self.__db.connection.cursor().execute(SQL_DELETA_ENDERECO, (id_pessoa, ))
        self.__db.connection.cursor().execute(SQL_DELETA_CONTATO, (id_pessoa, ))
        self.__db.connection.cursor().execute(SQL_DELETA_FORNECEDOR, (id_pessoa, ))
        self.__db.connection.cursor().execute(SQL_DELETA_PESSOA, (id_pessoa, ))
        self.__db.connection.commit()
     
    def deletar_produto(self, codigo_produto,):
        self.__db.connection.cursor().execute(SQL_DELETA_COMPRA,(codigo_produto,))
        self.__db.connection.cursor().execute(SQL_DELETA_ITEM,(codigo_produto,))
        self.__db.connection.cursor().execute(SQL_DELETA_PRODUTO,(codigo_produto,))
        self.__db.connection.commit()