from models import Categoria_Produto


SQL_CADASTRAR_CATEGORIA = 'insert into Categoria_Produto(id_categoria, descricao) values (?, ?)'
SQL_BUSCAR_CATEGORIA = 'select * from Categoria_Produto'



class cadastrar_categoria:
    def __init__(self, db):
        self.__db = db
    

    def salvar_categoria(self,Categoria_Produto):
        cursor= self.__db
        cursor.execute(SQL_CADASTRAR_CATEGORIA, (Categoria_Produto.id_categoria, Categoria_Produto.descricao))
        Categoria_Produto.id_categoria = cursor.execute('SELECT @@IDENTITY AS id_categoria;')
        self.__db.connection.commit()
        return Categoria_Produto
    
    def exibe_categoria(self):
            cursor = self.__db.connection.cursor()
            cursor.execute(SQL_BUSCAR_CATEGORIA)
            categoria = traduz_categoria(cursor.fetchall())
            return categoria



def traduz_categoria(lista_categoria):
    def cria_categoria_com_tupla(tupla):
        return Categoria_Produto(tupla[0], tupla[1])
    return list(map(cria_categoria_com_tupla, lista_categoria))