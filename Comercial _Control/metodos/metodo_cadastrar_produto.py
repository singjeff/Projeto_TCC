from models import Produto, Item, Compra, Categoria_Produto, Marca_Produto

SQL_CADASTRAR_PRODUTO = 'insert into Produto(codigo_produto, id_categoria, descricao, id_marca, valor_venda) values (?, ?, ?, ?, ?)'

SQL_CADASTRAR_ITEM = 'insert into Item(id_item, codigo_produto, quantidade) values (?, ?, ?)'
SQL_CADASTRAR_COMPRA = 'insert into Compra(id_compra, id_item, id_fornecedor, id_funcionario, data_compra, num_notafiscal) values (?, ? ,? ,? ,? ,?) '

class cadastrar_produto:
    def __init__(self, db):
        self.__db = db
    

    def salvar_produto(self,Produto):
        cursor= self.__db
        cursor.execute(SQL_CADASTRAR_PRODUTO, (Produto.codigo_produto, Produto.id_categoria, Produto.descricao, Produto.id_marca, Produto.valor_venda))
        
        #cursor.execute(SQL_CADASTRAR_ITEM, (Item.id_item, Item.codigo_produto, Item.quantidade))
        #cursor.execute(SQL_CADASTRAR_COMPRA, (Compra.id_item, Compra.id_item, Compra.id_fornecedor, Compra.id_funcionario, Compra.data_compra, Compra.num_notafiscal))
        self.__db.connection.commit()
        return Produto


    
