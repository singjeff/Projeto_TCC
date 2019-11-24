from models import Marca_Produto


SQL_CADASTRAR_MARCA = 'insert into Marca_Produto(id_marca, descricao) values (?, ?)'
SQL_BUSCAR_MARCA = 'select * from Marca_Produto'



class cadastrar_categoria:
    def __init__(self, db):
        self.__db = db
    

    def salvar_marca(self,Marca_Produto):
        cursor= self.__db
        cursor.execute(SQL_CADASTRAR_MARCA, (Marca_Produto.id_marca, Marca_Produto.descricao))
        self.__db.connection.commit()
        return Marca_Produto
    
    def exibe_marca(self):
            cursor = self.__db.connection.cursor()
            cursor.execute(SQL_BUSCAR_MARCA)
            marca = traduz_marca(cursor.fetchall())
            return marca



def traduz_marca(lista_marca):
    def cria_marca_com_tupla(tupla):
        return Marca_Produto(tupla[0], tupla[1])
    return list(map(cria_marca_com_tupla, lista_marca))