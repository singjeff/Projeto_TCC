from models import  exibe_usuario

BUSCAR_USUARIO_ID = 'SELECT cod_usuario, id_tipopessoa, email_usuario, nome_usuario, dt_cadastro  FROM Usuario'


class busca_usuario:
    def __init__(self, db):
        self.__db = db

    def listar(self):
            cursor = self.__db.connection.cursor()
            cursor.execute(BUSCAR_USUARIO_ID)
            usuario = traduz_usuario(cursor.fetchall())
            return usuario



def traduz_usuario(lista_usuario):
    def cria_usuario_com_tupla(tupla):
        return exibe_usuario(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
    return list(map(cria_usuario_com_tupla, lista_usuario))