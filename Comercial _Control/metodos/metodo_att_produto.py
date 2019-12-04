from models import Produto, Item, Compra


SQL_PROCEDURE_UPDATE_PRODUTO = "{CALL sp_update_produto (?, ?, ?, ?, ?, ?, ?, ?, ?)}"
SQL_PRODUTO_POR_ID = 'SELECT * from Produto where codigo_produto = ?'
SQL_COMPRA_POR_ID = 'SELECT * from Compra where codigo_produto = ?'

class atualiza_produto:
    def __init__(self, db):
        self.__db = db

    def att_produto(self, Compra, Item, Produto):
        cursor = self.__db

        values = (
            Compra.data_compra, Compra.num_notafiscal,  Produto.descricao, Produto.valor_venda, Item.quantidade, Produto.id_marca,  
            Produto.id_categoria, Compra.valor_total, Produto.codigo_produto
          
        )
        cursor.execute(SQL_PROCEDURE_UPDATE_PRODUTO, values)

        self.__db.connection.commit()
        return Compra


    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PRODUTO_POR_ID, (id,))
        dados = cursor.fetchone()
        produto = traduz_produto(dados) if dados else None
        return produto

    def tb_compra_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_COMPRA_POR_ID, (id,))
        dados = cursor.fetchone()
        compra = traduz_tb_compra(dados) if dados else None
        return compra

def traduz_produto(tupla):
    return Produto(tupla[0],tupla[1], tupla[2], tupla[3], tupla[4])


def traduz_tb_compra(tupla):
    return Compra(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8], None)