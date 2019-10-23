from models import  Usuario

SQL_DELETA_JOGO = 'delete from jogo where id = ?'
SQL_JOGO_POR_ID = 'SELECT id, nome, categoria, console from jogo where id = ?'
SQL_USUARIO_POR_ID = 'SELECT * from Usuario where email_usuario = ?'
SQL_ATUALIZA_USUARIO = 'UPDATE Usuario SET  senha_aplicacao=?  where cod_usuario = ?'
SQL_BUSCA_JOGOS = 'SELECT id, nome, categoria, console from jogo'


'''
class cadas_att:
    def __init__(self, db):
        self.__db = db

    def atualiza(self, usuario):
        cursor = self.__db
        cursor.execute(SQL_ATUALIZA_USUARIO, (usuario.senha_aplicacao, usuario.cod_usuario))
        self.__db.connection.commit()
        return usuario
    
    

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_JOGOS)
        jogos = traduz_jogos(cursor.fetchall())
        return jogos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_JOGO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_JOGO, (id, ))
        self.__db.connection.commit()

'''
class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_login(dados) if dados else None
        return usuario

'''
def traduz_jogos(jogos):
    def cria_jogo_com_tupla(tupla):
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_jogo_com_tupla, jogos))
'''

def traduz_login(tupla):
    return Usuario(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], tupla[10], tupla[11], tupla[0])
