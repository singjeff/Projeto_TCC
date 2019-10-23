from models import  Fornecedor, Pessoa, Endereco_Pessoa, ContatoPessoa, exibe_fornecedor

SQL_CADASTRAR_FORNECEDOR = 'insert into Fornecedor(id_fornecedor, id_pessoa) values (?, ?)'
SQL_CADASTRAR_PESSOA = 'insert into Pessoa(id_pessoa, id_tipo_pessoa, nome, inscricao, data_cadastro, ind_funcionario, ind_fornecedor) values (?, ?, ?, ?, ?, ?, ?)'
SQL_CADASTRAR_ENDERECO = 'insert into Endereco_Pessoa(id_pessoa, endereco, complemento, cidade, uf ,cep) values (?, ?, ?, ?, ?, ?)'
SQL_CADASTRAR_CONTATO = 'insert into Contato_Pessoa(id_pessoa, celular, telefone, email, nome_contato) values (?, ?, ?, ?, ?)'



SQL_SELECT_PESSOA= 'Select * from Pessoa'
SQL_SELECT_ENDERECO_PESSOA = 'Select * From Endereco_Pessoa'
SQL_SELECT_CONTATO_PESSOA = 'Select * from Contato_Pessoa'

SQL_EXIBE_FORNECEDOR = 'SELECT a.id_pessoa, a.nome, a.inscricao, b.endereco, c.celular\
      FROM Pessoa A INNER JOIN Endereco_Pessoa B ON B.id_pessoa = A.id_pessoa\
          INNER JOIN  Contato_Pessoa C ON C.id_pessoa = A.id_pessoa'

class cadastrar_fornecedor:
    def __init__(self, db):
        self.__db = db
    

    def cadastra_fornecedor(self, Pessoa,Endereco_Pessoa,ContatoPessoa):
        cursor= self.__db

        cursor.execute(SQL_CADASTRAR_PESSOA, (Pessoa.id_pessoa, Pessoa.id_tipo_pessoa, Pessoa.nome, Pessoa.inscricao, Pessoa.data_cadastro, Pessoa.ind_funcionario, Pessoa.ind_fornecedor))
        cursor.execute(SQL_CADASTRAR_ENDERECO, (Endereco_Pessoa.id_pessoa, Endereco_Pessoa.endereco, Endereco_Pessoa.complemento, Endereco_Pessoa.cidade, Endereco_Pessoa.uf, Endereco_Pessoa.cep))
        cursor.execute(SQL_CADASTRAR_CONTATO, (ContatoPessoa.id_pessoa, ContatoPessoa.celular, ContatoPessoa.telefone, ContatoPessoa.email, ContatoPessoa.nome_contato))
        
        self.__db.connection.commit()
    
    def exibe_fornecedor(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_EXIBE_FORNECEDOR)
        fornecedor = traduz_fornecedor(cursor.fetchall())
        return fornecedor



def traduz_fornecedor(lista_fornecedor):
    def cria_fornecedor_com_tupla(tupla):
        return exibe_fornecedor(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
    return list(map(cria_fornecedor_com_tupla, lista_fornecedor))