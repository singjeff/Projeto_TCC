QUERY = 'SELECT a.cnpj, a.data_compra, a.num_notafiscal, b.codigo_produto, b.descricao, b.valor_venda, '
QUERY += 'c.quantidade, b.id_marca, b.id_categoria, a.valor_total '

QUERY += 'FROM Produto B '
QUERY += 'INNER JOIN Compra A  '
QUERY += 'ON A.codigo_produto= B.codigo_produto '
QUERY += 'INNER JOIN  Item C '
QUERY += 'ON C.codigo_produto = B.codigo_produto  '
QUERY += 'WHERE B.codigo_produto = ? '

class busca_produto_por_id:
    def __init__(self, db):
        self.__db = db

    def listar(self, id):
            cursor = self.__db.connection.cursor()
            cursor.execute(QUERY, id)
         
            dados = []

            for row in cursor:
                dados.append(row)

            return dados
            