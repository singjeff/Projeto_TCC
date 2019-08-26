from models import jogo, Usuario

SQL_DELETA_JOGO = 'delete from jogo where id = ?'
SQL_JOGO_POR_ID = 'SELECT id, nome, categoria, console from jogo where id = ?'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = ?'
SQL_ATUALIZA_JOGO = 'UPDATE jogo SET nome=?, categoria=?, console=? where id = ?'
SQL_BUSCA_JOGOS = 'SELECT id, nome, categoria, console from jogo'
SQL_CRIA_JOGO = 'INSERT into jogo (nome, categoria, console) values (?, ?, ?)'


class JogoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, jogo):
        cursor = self.__db.connection.cursor()

        if (jogo.id):
            cursor.execute(SQL_ATUALIZA_JOGO, (jogo.nome, jogo.categoria, jogo.console, jogo.id))
        else:
            cursor.execute(SQL_CRIA_JOGO, (jogo.nome, jogo.categoria, jogo.console))
            jogo.id = cursor.lastrowid
        self.__db.connection.commit()
        return jogo

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_JOGOS)
        jogos = traduz_jogos(cursor.fetchall())
        return jogos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_JOGO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_JOGO, (id, ))
        self.__db.connection.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return Usuario


def traduz_jogos(jogos):
    def cria_jogo_com_tupla(tupla):
        return jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_jogo_com_tupla, jogos))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
