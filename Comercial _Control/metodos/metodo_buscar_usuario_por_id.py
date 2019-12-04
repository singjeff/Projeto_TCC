QUERY = 'SELECT u.nome_usuario, e.cep, e.cidade, e.uf, e.endereco, '
QUERY += 'e.numero_endereco, c.telefone, c.celular, f.cargo, '
QUERY += 'u.email_usuario, u.id_tipopessoa '
QUERY += 'FROM USUARIO u '
QUERY += 'INNER JOIN FUNCIONARIO f '
QUERY += 'ON u.id_funcionario = f.id_funcionario '
QUERY += 'INNER JOIN CONTATO_PESSOA c '
QUERY += 'ON u.id_contato_pessoa = c.id_contato_pessoa '
QUERY += 'INNER JOIN ENDERECO_PESSOA e '
QUERY += 'ON u.id_endereco_pessoa = e.id_endereco_pessoa '
QUERY += 'WHERE u.cod_usuario = ? '

class busca_usuario_por_id:
    def __init__(self, db):
        self.__db = db

    def listar(self, id):
            cursor = self.__db.connection.cursor()
            cursor.execute(QUERY, id)
         
            dados = []

            for row in cursor:
                dados.append(row)

            return dados
            


