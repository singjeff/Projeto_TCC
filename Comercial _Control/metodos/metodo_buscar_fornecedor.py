

BUSCAR_FORNECEDOR = 'SELECT nome FROM Pessoa p INNER JOIN Fornecedor f ON p.id_pessoa = f.id_pessoa WHERE p.inscricao = ? ' 


class busca_fornecedor:
    def __init__(self, db):
        self.__db = db

    def listar(self, cnpj):
            cursor = self.__db.connection.cursor()
            cursor.execute(BUSCAR_FORNECEDOR, cnpj)
         
            nome_fornecedor = ""

            for row in cursor:
                nome_fornecedor = row[0]

            return nome_fornecedor
            


