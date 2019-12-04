from models import Produto, Item, Compra, Categoria_Produto, Marca_Produto, Exibe_Produto

SQL_CADASTRAR_PRODUTO = 'insert into Produto(codigo_produto, id_categoria, descricao, id_marca, valor_venda) values (?, ?, ?, ?, ?)'
SQL_ID_ITEM = 'select max(id_item) as Item from Item'
SQL_CADASTRAR_ITEM = 'insert into Item(id_item, codigo_produto, quantidade) values (?, ?, ?)'
SQL_CADASTRAR_COMPRA = 'insert into Compra(id_item, codigo_produto, id_fornecedor, cnpj, id_funcionario, data_compra, num_notafiscal, valor_total) values (?, ?, ?, ? ,? ,? ,?, ?) '


SQL_EXIBE_PRODUTO = "SELECT a.codigo_produto, a.descricao, b.descricao, c.descricao, a.valor_venda, e.quantidade, d.valor_total, d.cnpj, d.num_notafiscal, d.data_compra\
      FROM Produto A INNER JOIN Marca_Produto B ON B.id_marca= A.id_marca\
          INNER JOIN  Categoria_Produto C ON C.id_categoria= A.id_categoria\
		  INNER JOIN Compra D on D.codigo_produto = A.codigo_produto\
          INNER JOIN Item E on E.codigo_produto = A.codigo_produto"



class cadastrar_produto:
    def __init__(self, db):
        self.__db = db
    

    def salvar_produto(self,Produto, Item, Compra):
        cursor= self.__db
        cursor.execute(SQL_CADASTRAR_PRODUTO, (Produto.codigo_produto, Produto.id_categoria, Produto.descricao, Produto.id_marca, Produto.valor_venda))
        
        cursor.execute(SQL_CADASTRAR_ITEM, (Item.id_item, Item.codigo_produto, Item.quantidade))
        cursor.execute(SQL_CADASTRAR_COMPRA, (Compra.id_item, Compra.codigo_produto, Compra.id_fornecedor, Compra.cnpj, Compra.id_funcionario, Compra.data_compra, Compra.num_notafiscal, Compra.valor_total))
        self.__db.connection.commit()
        return Produto


    def item_id(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ID_ITEM)
        dados = cursor.fetchone()
        itemid = int(dados[0])
        return itemid

    
        
    def exibe_produto(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_EXIBE_PRODUTO)
        produto = traduz_produto(cursor.fetchall())
        print(produto)
        return produto
        




def traduz_produto(Lista_Produto):
    def cria_produto_com_tupla(tupla):
        return Exibe_Produto(tupla[0],tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9])
    return list(map(cria_produto_com_tupla, Lista_Produto))
