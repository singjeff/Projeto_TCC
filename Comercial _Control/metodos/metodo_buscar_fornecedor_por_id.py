QUERY = 'SELECT a.inscricao, a.nome, b.cep, b.endereco, b.numero_endereco, '
QUERY += 'b.complemento, b.cidade, b.uf, c.nome_contato, c.email,c.telefone, c.celular '
QUERY += 'FROM Pessoa A '
QUERY += 'INNER JOIN Endereco_Pessoa B '
QUERY += 'ON B.id_pessoa= A.id_pessoa '
QUERY += 'INNER JOIN  Contato_Pessoa C  '
QUERY += 'ON C.id_pessoa= A.id_pessoa '
QUERY += 'where A.id_pessoa = ? '

class busca_fornecedor_por_id:
    def __init__(self, db):
        self.__db = db

    def listar(self, id):
            cursor = self.__db.connection.cursor()
            cursor.execute(QUERY, id)
         
            dados = []

            for row in cursor:
                dados.append(row)

            return dados
            

