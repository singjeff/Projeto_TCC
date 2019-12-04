from models import Pessoa, Endereco_Pessoa, ContatoPessoa


SQL_PROCEDURE_UPDATE_FORNECEDOR = "{CALL sp_update_fornecedor (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}"
SQL_PESSOA_POR_ID = 'SELECT * from Pessoa where inscricao = ?'

class atualiza_fornecedor:
    def __init__(self, db):
        self.__db = db

    def att_fornecedor(self, Pessoa, Endereco_Pessoa, ContatoPessoa):
        cursor = self.__db

        values = (
            Pessoa.nome, Endereco_Pessoa.cep,  Endereco_Pessoa.cidade, Endereco_Pessoa.uf, Endereco_Pessoa.endereco, Endereco_Pessoa.num_endereco,  
            Endereco_Pessoa.complemento, ContatoPessoa.nome_contato, ContatoPessoa.email,ContatoPessoa.telefone, ContatoPessoa.celular, Pessoa.inscricao
          
        )
        cursor.execute(SQL_PROCEDURE_UPDATE_FORNECEDOR, values)

        self.__db.connection.commit()
        return Pessoa


    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PESSOA_POR_ID, (id,))
        dados = cursor.fetchone()
        pessoa = traduz_pessoa(dados) if dados else None
        return pessoa


def traduz_pessoa(tupla):
    return Pessoa(tupla[0],tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7])
