  
from models import  Fornecedor, Pessoa, Endereco_Pessoa, Fornecedor, ContatoPessoa, exibe_fornecedor

SQL_CADASTRAR_FORNECEDOR = 'insert into Fornecedor(id_pessoa) values (?)'
SQL_CADASTRAR_PESSOA = 'insert into Pessoa(id_pessoa, id_tipo_pessoa, nome, inscricao, data_cadastro, ind_funcionario, ind_fornecedor) values (?, ?, ?, ?, ?, ?, ?)'
SQL_CADASTRAR_ENDERECO = 'insert into Endereco_Pessoa(id_pessoa, cep, endereco, numero_endereco, complemento ,cidade, uf) values (?,?, ?, ?, ?, ?, ?)'
SQL_CADASTRAR_CONTATO = 'insert into Contato_Pessoa(id_pessoa, celular, telefone, email, nome_contato) values (?, ?, ?, ?, ?)'
SQL_ID_FORNECEDOR = 'select max(id_pessoa) as id_pessoa from Pessoa'

SQL_EXIBE_FORNECEDOR = "SELECT a.id_pessoa, a.nome, a.inscricao, b.endereco, b.uf, c.celular, c.telefone, c.nome_contato\
          FROM Pessoa A INNER JOIN Endereco_Pessoa B ON B.id_pessoa = A.id_pessoa\
          INNER JOIN  Contato_Pessoa C ON C.id_pessoa = A.id_pessoa where id_tipo_pessoa ='3'"

class cadastrar_fornecedor:
    def __init__(self, db):
        self.__db = db
    

    def cadastra_fornecedor(self, Pessoa,Endereco_Pessoa,ContatoPessoa,Fornecedor):
        cursor= self.__db

        cursor.execute(SQL_CADASTRAR_PESSOA, (Pessoa.id_pessoa, Pessoa.id_tipo_pessoa, Pessoa.nome, Pessoa.inscricao, Pessoa.data_cadastro, Pessoa.ind_funcionario, Pessoa.ind_fornecedor))
        cursor.execute(SQL_CADASTRAR_ENDERECO, (Endereco_Pessoa.id_pessoa, Endereco_Pessoa.cep, Endereco_Pessoa.endereco, Endereco_Pessoa.num_endereco, Endereco_Pessoa.complemento, Endereco_Pessoa.cidade, Endereco_Pessoa.uf))
        cursor.execute(SQL_CADASTRAR_CONTATO, (ContatoPessoa.id_pessoa, ContatoPessoa.celular, ContatoPessoa.telefone, ContatoPessoa.email, ContatoPessoa.nome_contato))
        cursor.execute(SQL_CADASTRAR_FORNECEDOR, (Fornecedor.id_pessoa))
        self.__db.connection.commit()
    
    def exibe_fornecedor(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_EXIBE_FORNECEDOR)
        fornecedor = traduz_fornecedor(cursor.fetchall())
        return fornecedor
    
    def id_fornecedor(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ID_FORNECEDOR)
        dados = cursor.fetchone()
        idpessoa = int(dados[0])
        return idpessoa


def traduz_fornecedor(lista_fornecedor):
    def cria_fornecedor_com_tupla(tupla):
        return exibe_fornecedor(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[0])
    return list(map(cria_fornecedor_com_tupla, lista_fornecedor))